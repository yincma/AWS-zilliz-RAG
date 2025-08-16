r'''
# Amazon GameLift Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_gamelift as gamelift
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for GameLift construct libraries](https://constructs.dev/search?q=gamelift)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::GameLift resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GameLift.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-gamelift-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::GameLift](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GameLift.html).

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
class CfnAlias(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnAlias",
):
    '''The ``AWS::GameLift::Alias`` resource creates an alias for an Amazon GameLift (GameLift) fleet destination.

    There are two types of routing strategies for aliases: simple and terminal. A simple alias points to an active fleet. A terminal alias displays a message instead of routing players to an active fleet. For example, a terminal alias might display a URL link that directs players to an upgrade site. You can use aliases to define destinations in a game session queue or when requesting new game sessions.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html
    :cloudformationResource: AWS::GameLift::Alias
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_alias = gamelift.CfnAlias(self, "MyCfnAlias",
            name="name",
            routing_strategy=gamelift.CfnAlias.RoutingStrategyProperty(
                type="type",
        
                # the properties below are optional
                fleet_id="fleetId",
                message="message"
            ),
        
            # the properties below are optional
            description="description",
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
        routing_strategy: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlias.RoutingStrategyProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A descriptive label that is associated with an alias. Alias names do not need to be unique.
        :param routing_strategy: The routing configuration, including routing type and fleet target, for the alias.
        :param description: A human-readable description of the alias.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a91f3a4a7dfbcf1655ec6812682d7a8824bfb46a9ce2a65e3c859108e3633c8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAliasProps(
            name=name,
            routing_strategy=routing_strategy,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6c7223e714d0339897da2cbb4b67d9e03a5022aa12f568680b86e828460d501)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a1fbbe6ec42c9ed6d59226c8fe9df0391ca1a181a605b688f9e6267ea6f2a055)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAliasArn")
    def attr_alias_arn(self) -> builtins.str:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to a Amazon GameLift Servers alias resource and uniquely identifies it. ARNs are unique across all Regions. Format is ``arn:aws:gamelift:<region>::alias/alias-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`` . In a GameLift alias ARN, the resource ID matches the alias ID value.

        :cloudformationAttribute: AliasArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAliasArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAliasId")
    def attr_alias_id(self) -> builtins.str:
        '''A unique identifier for the alias. For example, ``arn:aws:gamelift:us-west-1::alias/alias-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912``.

        Alias IDs are unique within a Region.

        :cloudformationAttribute: AliasId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAliasId"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A descriptive label that is associated with an alias.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8666b32153f5438f8d6ea2d03ad01cbf8c67bad1071d8e1cdc42963a8912ad3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="routingStrategy")
    def routing_strategy(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAlias.RoutingStrategyProperty"]:
        '''The routing configuration, including routing type and fleet target, for the alias.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAlias.RoutingStrategyProperty"], jsii.get(self, "routingStrategy"))

    @routing_strategy.setter
    def routing_strategy(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAlias.RoutingStrategyProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__529d8fec4c06eafb4c38da47298670dd8132ede4d21975eafb43f51a366a3d82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routingStrategy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description of the alias.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98d25b43c56fe6060dfb6e36792550c92a6a537d6d2e31b8c97947858787f55a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc43df2fa439cbdde0361a6e15a7a3a916a006856add3cb38bca18959f9c8775)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnAlias.RoutingStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "fleet_id": "fleetId", "message": "message"},
    )
    class RoutingStrategyProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            fleet_id: typing.Optional[builtins.str] = None,
            message: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The routing configuration for a fleet alias.

            :param type: A type of routing strategy. Possible routing types include the following: - *SIMPLE* - The alias resolves to one specific fleet. Use this type when routing to active fleets. - *TERMINAL* - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a ``TerminalRoutingStrategyException`` with the message that you specified in the ``Message`` property.
            :param fleet_id: A unique identifier for a fleet that the alias points to. If you specify ``SIMPLE`` for the ``Type`` property, you must specify this property.
            :param message: The message text to be used with a terminal routing strategy. If you specify ``TERMINAL`` for the ``Type`` property, you must specify this property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                routing_strategy_property = gamelift.CfnAlias.RoutingStrategyProperty(
                    type="type",
                
                    # the properties below are optional
                    fleet_id="fleetId",
                    message="message"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4057d890d9c2fba51db14d6885375c0c7263cd6b07fb4401e3fb51d7676734f9)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument fleet_id", value=fleet_id, expected_type=type_hints["fleet_id"])
                check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if fleet_id is not None:
                self._values["fleet_id"] = fleet_id
            if message is not None:
                self._values["message"] = message

        @builtins.property
        def type(self) -> builtins.str:
            '''A type of routing strategy.

            Possible routing types include the following:

            - *SIMPLE* - The alias resolves to one specific fleet. Use this type when routing to active fleets.
            - *TERMINAL* - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a ``TerminalRoutingStrategyException`` with the message that you specified in the ``Message`` property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html#cfn-gamelift-alias-routingstrategy-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def fleet_id(self) -> typing.Optional[builtins.str]:
            '''A unique identifier for a fleet that the alias points to.

            If you specify ``SIMPLE`` for the ``Type`` property, you must specify this property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html#cfn-gamelift-alias-routingstrategy-fleetid
            '''
            result = self._values.get("fleet_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def message(self) -> typing.Optional[builtins.str]:
            '''The message text to be used with a terminal routing strategy.

            If you specify ``TERMINAL`` for the ``Type`` property, you must specify this property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html#cfn-gamelift-alias-routingstrategy-message
            '''
            result = self._values.get("message")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RoutingStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnAliasProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "routing_strategy": "routingStrategy",
        "description": "description",
        "tags": "tags",
    },
)
class CfnAliasProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        routing_strategy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlias.RoutingStrategyProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAlias``.

        :param name: A descriptive label that is associated with an alias. Alias names do not need to be unique.
        :param routing_strategy: The routing configuration, including routing type and fleet target, for the alias.
        :param description: A human-readable description of the alias.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_alias_props = gamelift.CfnAliasProps(
                name="name",
                routing_strategy=gamelift.CfnAlias.RoutingStrategyProperty(
                    type="type",
            
                    # the properties below are optional
                    fleet_id="fleetId",
                    message="message"
                ),
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e74c18c4446e0f846baf63e2e707aa2ba663f37170623164846853f1176d7891)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument routing_strategy", value=routing_strategy, expected_type=type_hints["routing_strategy"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "routing_strategy": routing_strategy,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A descriptive label that is associated with an alias.

        Alias names do not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html#cfn-gamelift-alias-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def routing_strategy(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAlias.RoutingStrategyProperty]:
        '''The routing configuration, including routing type and fleet target, for the alias.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html#cfn-gamelift-alias-routingstrategy
        '''
        result = self._values.get("routing_strategy")
        assert result is not None, "Required property 'routing_strategy' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAlias.RoutingStrategyProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description of the alias.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html#cfn-gamelift-alias-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html#cfn-gamelift-alias-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAliasProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnBuild(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnBuild",
):
    '''The ``AWS::GameLift::Build`` resource creates a game server build that is installed and run on instances in an Amazon GameLift fleet.

    This resource points to an Amazon S3 location that contains a zip file with all of the components of the game server build.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html
    :cloudformationResource: AWS::GameLift::Build
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_build = gamelift.CfnBuild(self, "MyCfnBuild",
            name="name",
            operating_system="operatingSystem",
            server_sdk_version="serverSdkVersion",
            storage_location=gamelift.CfnBuild.StorageLocationProperty(
                bucket="bucket",
                key="key",
                role_arn="roleArn",
        
                # the properties below are optional
                object_version="objectVersion"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            version="version"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: typing.Optional[builtins.str] = None,
        operating_system: typing.Optional[builtins.str] = None,
        server_sdk_version: typing.Optional[builtins.str] = None,
        storage_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBuild.StorageLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A descriptive label that is associated with a build. Build names do not need to be unique.
        :param operating_system: The operating system that your game server binaries run on. This value determines the type of fleet resources that you use for this build. If your game build contains multiple executables, they all must run on the same operating system. You must specify a valid operating system in this request. There is no default value. You can't change a build's operating system later. .. epigraph:: Amazon Linux 2 (AL2) will reach end of support on 6/30/2025. See more details in the `Amazon Linux 2 FAQs <https://docs.aws.amazon.com/amazon-linux-2/faqs/>`_ . For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See `Migrate to server SDK version 5. <https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html>`_
        :param server_sdk_version: A server SDK version you used when integrating your game server build with Amazon GameLift Servers. For more information see `Integrate games with custom game servers <https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-custom-intro.html>`_ . By default Amazon GameLift Servers sets this value to ``4.0.2`` .
        :param storage_location: Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift Servers to access your Amazon S3 bucket. The S3 bucket and your new build must be in the same Region. If a ``StorageLocation`` is specified, the size of your file can be found in your Amazon S3 bucket. Amazon GameLift Servers will report a ``SizeOnDisk`` of 0.
        :param tags: An array of key-value pairs to apply to this resource.
        :param version: Version information that is associated with this build. Version strings do not need to be unique.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2f3884df6574dd3d4e76d857acf05a15fdc616d818da1cebcfcce4084ca8ddc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBuildProps(
            name=name,
            operating_system=operating_system,
            server_sdk_version=server_sdk_version,
            storage_location=storage_location,
            tags=tags,
            version=version,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dabd8e19951007a8e9f2bcb21f9e872c9fc5b6a638701939005bc4d813c12a3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__52be0a2eff399965a7232bfe5d136a98b17426adc22dd0fe1be4ebd8de6c3b47)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBuildArn")
    def attr_build_arn(self) -> builtins.str:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to a Amazon GameLift Servers build resource and uniquely identifies it. ARNs are unique across all Regions. Format is ``arn:aws:gamelift:<region>::build/build-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`` . In a GameLift build ARN, the resource ID matches the *BuildId* value.

        :cloudformationAttribute: BuildArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBuildArn"))

    @builtins.property
    @jsii.member(jsii_name="attrBuildId")
    def attr_build_id(self) -> builtins.str:
        '''A unique identifier for the build.

        :cloudformationAttribute: BuildId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBuildId"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A descriptive label that is associated with a build.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a86d40dd79232f1b81dd44ba375e9a9432429c05c3444beaf1128ab336d19dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="operatingSystem")
    def operating_system(self) -> typing.Optional[builtins.str]:
        '''The operating system that your game server binaries run on.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatingSystem"))

    @operating_system.setter
    def operating_system(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__086f4a5a0a253ca19c97937d0f25a8ade9bb623ef1c01cacdc76233a24f4ef0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operatingSystem", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serverSdkVersion")
    def server_sdk_version(self) -> typing.Optional[builtins.str]:
        '''A server SDK version you used when integrating your game server build with Amazon GameLift Servers.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverSdkVersion"))

    @server_sdk_version.setter
    def server_sdk_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb7f1e9548565a4821c004b0e86bae438a45b45de61043075555fb43127d349d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSdkVersion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="storageLocation")
    def storage_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBuild.StorageLocationProperty"]]:
        '''Information indicating where your game build files are stored.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBuild.StorageLocationProperty"]], jsii.get(self, "storageLocation"))

    @storage_location.setter
    def storage_location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBuild.StorageLocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdd3e9ea10aa8547b05a398258efac5d3e786e68d7875c76104c89d2a3178e02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageLocation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61f5c317acb9e4d0abf34641df15710032d796e858c0b0962748ce1d84bf6d9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[builtins.str]:
        '''Version information that is associated with this build.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "version"))

    @version.setter
    def version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f69e6e764a220fcdeac2ac30cce1d3fbf57e0ef02b497976b1bb0e8162a6a67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnBuild.StorageLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "key": "key",
            "role_arn": "roleArn",
            "object_version": "objectVersion",
        },
    )
    class StorageLocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: builtins.str,
            role_arn: builtins.str,
            object_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The location in Amazon S3 where build or script files are stored for access by Amazon GameLift.

            :param bucket: An Amazon S3 bucket identifier. The name of the S3 bucket. .. epigraph:: Amazon GameLift doesn't support uploading from Amazon S3 buckets with names that contain a dot (.).
            :param key: The name of the zip file that contains the build files or script files.
            :param role_arn: The ARNfor an IAM role that allows Amazon GameLift to access the S3 bucket.
            :param object_version: A version of a stored file to retrieve, if the object versioning feature is turned on for the S3 bucket. Use this parameter to specify a specific version. If this parameter isn't set, Amazon GameLift Servers retrieves the latest version of the file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                storage_location_property = gamelift.CfnBuild.StorageLocationProperty(
                    bucket="bucket",
                    key="key",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    object_version="objectVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6d6726269ab0714348382710795aeac31efd3f1d29c3bac05a4aefa5c90bcba4)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
                "role_arn": role_arn,
            }
            if object_version is not None:
                self._values["object_version"] = object_version

        @builtins.property
        def bucket(self) -> builtins.str:
            '''An Amazon S3 bucket identifier. The name of the S3 bucket.

            .. epigraph::

               Amazon GameLift doesn't support uploading from Amazon S3 buckets with names that contain a dot (.).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-storagelocation-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''The name of the zip file that contains the build files or script files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-storagelocation-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARNfor an IAM role that allows Amazon GameLift to access the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-storagelocation-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_version(self) -> typing.Optional[builtins.str]:
            '''A version of a stored file to retrieve, if the object versioning feature is turned on for the S3 bucket.

            Use this parameter to specify a specific version. If this parameter isn't set, Amazon GameLift Servers retrieves the latest version of the file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-storagelocation-objectversion
            '''
            result = self._values.get("object_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StorageLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnBuildProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "operating_system": "operatingSystem",
        "server_sdk_version": "serverSdkVersion",
        "storage_location": "storageLocation",
        "tags": "tags",
        "version": "version",
    },
)
class CfnBuildProps:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        operating_system: typing.Optional[builtins.str] = None,
        server_sdk_version: typing.Optional[builtins.str] = None,
        storage_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBuild.StorageLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnBuild``.

        :param name: A descriptive label that is associated with a build. Build names do not need to be unique.
        :param operating_system: The operating system that your game server binaries run on. This value determines the type of fleet resources that you use for this build. If your game build contains multiple executables, they all must run on the same operating system. You must specify a valid operating system in this request. There is no default value. You can't change a build's operating system later. .. epigraph:: Amazon Linux 2 (AL2) will reach end of support on 6/30/2025. See more details in the `Amazon Linux 2 FAQs <https://docs.aws.amazon.com/amazon-linux-2/faqs/>`_ . For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See `Migrate to server SDK version 5. <https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html>`_
        :param server_sdk_version: A server SDK version you used when integrating your game server build with Amazon GameLift Servers. For more information see `Integrate games with custom game servers <https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-custom-intro.html>`_ . By default Amazon GameLift Servers sets this value to ``4.0.2`` .
        :param storage_location: Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift Servers to access your Amazon S3 bucket. The S3 bucket and your new build must be in the same Region. If a ``StorageLocation`` is specified, the size of your file can be found in your Amazon S3 bucket. Amazon GameLift Servers will report a ``SizeOnDisk`` of 0.
        :param tags: An array of key-value pairs to apply to this resource.
        :param version: Version information that is associated with this build. Version strings do not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_build_props = gamelift.CfnBuildProps(
                name="name",
                operating_system="operatingSystem",
                server_sdk_version="serverSdkVersion",
                storage_location=gamelift.CfnBuild.StorageLocationProperty(
                    bucket="bucket",
                    key="key",
                    role_arn="roleArn",
            
                    # the properties below are optional
                    object_version="objectVersion"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                version="version"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ea486b468f726c96f63f78347aac31445ce3b0bd1ea282f6fce30ca4e8642d7)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument operating_system", value=operating_system, expected_type=type_hints["operating_system"])
            check_type(argname="argument server_sdk_version", value=server_sdk_version, expected_type=type_hints["server_sdk_version"])
            check_type(argname="argument storage_location", value=storage_location, expected_type=type_hints["storage_location"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if operating_system is not None:
            self._values["operating_system"] = operating_system
        if server_sdk_version is not None:
            self._values["server_sdk_version"] = server_sdk_version
        if storage_location is not None:
            self._values["storage_location"] = storage_location
        if tags is not None:
            self._values["tags"] = tags
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A descriptive label that is associated with a build.

        Build names do not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operating_system(self) -> typing.Optional[builtins.str]:
        '''The operating system that your game server binaries run on.

        This value determines the type of fleet resources that you use for this build. If your game build contains multiple executables, they all must run on the same operating system. You must specify a valid operating system in this request. There is no default value. You can't change a build's operating system later.
        .. epigraph::

           Amazon Linux 2 (AL2) will reach end of support on 6/30/2025. See more details in the `Amazon Linux 2 FAQs <https://docs.aws.amazon.com/amazon-linux-2/faqs/>`_ . For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See `Migrate to server SDK version 5. <https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-operatingsystem
        '''
        result = self._values.get("operating_system")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_sdk_version(self) -> typing.Optional[builtins.str]:
        '''A server SDK version you used when integrating your game server build with Amazon GameLift Servers.

        For more information see `Integrate games with custom game servers <https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-custom-intro.html>`_ . By default Amazon GameLift Servers sets this value to ``4.0.2`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-serversdkversion
        '''
        result = self._values.get("server_sdk_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBuild.StorageLocationProperty]]:
        '''Information indicating where your game build files are stored.

        Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift Servers to access your Amazon S3 bucket. The S3 bucket and your new build must be in the same Region.

        If a ``StorageLocation`` is specified, the size of your file can be found in your Amazon S3 bucket. Amazon GameLift Servers will report a ``SizeOnDisk`` of 0.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-storagelocation
        '''
        result = self._values.get("storage_location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBuild.StorageLocationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Version information that is associated with this build.

        Version strings do not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBuildProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnContainerFleet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerFleet",
):
    '''Describes an Amazon GameLift Servers managed container fleet.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html
    :cloudformationResource: AWS::GameLift::ContainerFleet
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_container_fleet = gamelift.CfnContainerFleet(self, "MyCfnContainerFleet",
            fleet_role_arn="fleetRoleArn",
        
            # the properties below are optional
            billing_type="billingType",
            deployment_configuration=gamelift.CfnContainerFleet.DeploymentConfigurationProperty(
                impairment_strategy="impairmentStrategy",
                minimum_healthy_percentage=123,
                protection_strategy="protectionStrategy"
            ),
            description="description",
            game_server_container_group_definition_name="gameServerContainerGroupDefinitionName",
            game_server_container_groups_per_instance=123,
            game_session_creation_limit_policy=gamelift.CfnContainerFleet.GameSessionCreationLimitPolicyProperty(
                new_game_sessions_per_creator=123,
                policy_period_in_minutes=123
            ),
            instance_connection_port_range=gamelift.CfnContainerFleet.ConnectionPortRangeProperty(
                from_port=123,
                to_port=123
            ),
            instance_inbound_permissions=[gamelift.CfnContainerFleet.IpPermissionProperty(
                from_port=123,
                ip_range="ipRange",
                protocol="protocol",
                to_port=123
            )],
            instance_type="instanceType",
            locations=[gamelift.CfnContainerFleet.LocationConfigurationProperty(
                location="location",
        
                # the properties below are optional
                location_capacity=gamelift.CfnContainerFleet.LocationCapacityProperty(
                    desired_ec2_instances=123,
                    max_size=123,
                    min_size=123
                ),
                stopped_actions=["stoppedActions"]
            )],
            log_configuration=gamelift.CfnContainerFleet.LogConfigurationProperty(
                log_destination="logDestination",
                log_group_arn="logGroupArn",
                s3_bucket_name="s3BucketName"
            ),
            metric_groups=["metricGroups"],
            new_game_session_protection_policy="newGameSessionProtectionPolicy",
            per_instance_container_group_definition_name="perInstanceContainerGroupDefinitionName",
            scaling_policies=[gamelift.CfnContainerFleet.ScalingPolicyProperty(
                metric_name="metricName",
                name="name",
        
                # the properties below are optional
                comparison_operator="comparisonOperator",
                evaluation_periods=123,
                policy_type="policyType",
                scaling_adjustment=123,
                scaling_adjustment_type="scalingAdjustmentType",
                target_configuration=gamelift.CfnContainerFleet.TargetConfigurationProperty(
                    target_value=123
                ),
                threshold=123
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
        fleet_role_arn: builtins.str,
        billing_type: typing.Optional[builtins.str] = None,
        deployment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerFleet.DeploymentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        game_server_container_group_definition_name: typing.Optional[builtins.str] = None,
        game_server_container_groups_per_instance: typing.Optional[jsii.Number] = None,
        game_session_creation_limit_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerFleet.GameSessionCreationLimitPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        instance_connection_port_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerFleet.ConnectionPortRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        instance_inbound_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerFleet.IpPermissionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        instance_type: typing.Optional[builtins.str] = None,
        locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerFleet.LocationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        log_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerFleet.LogConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        metric_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        new_game_session_protection_policy: typing.Optional[builtins.str] = None,
        per_instance_container_group_definition_name: typing.Optional[builtins.str] = None,
        scaling_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerFleet.ScalingPolicyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param fleet_role_arn: The unique identifier for an AWS Identity and Access Management (IAM) role with permissions to run your containers on resources that are managed by Amazon GameLift Servers. See `Set up an IAM service role <https://docs.aws.amazon.com/gamelift/latest/developerguide/setting-up-role.html>`_ . This fleet property can't be changed.
        :param billing_type: Indicates whether the fleet uses On-Demand or Spot instances for this fleet. Learn more about when to use `On-Demand versus Spot Instances <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot>`_ . You can't update this fleet property. By default, this property is set to ``ON_DEMAND`` .
        :param deployment_configuration: Set of rules for processing a deployment for a container fleet update.
        :param description: A meaningful description of the container fleet.
        :param game_server_container_group_definition_name: The name of the fleet's game server container group definition, which describes how to deploy containers with your game server build and support software onto each fleet instance.
        :param game_server_container_groups_per_instance: The number of times to replicate the game server container group on each fleet instance.
        :param game_session_creation_limit_policy: A policy that limits the number of game sessions that each individual player can create on instances in this fleet. The limit applies for a specified span of time.
        :param instance_connection_port_range: The set of port numbers to open on each instance in a container fleet. Connection ports are used by inbound traffic to connect with processes that are running in containers on the fleet.
        :param instance_inbound_permissions: The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet.
        :param instance_type: The Amazon EC2 instance type to use for all instances in the fleet. Instance type determines the computing resources and processing power that's available to host your game servers. This includes including CPU, memory, storage, and networking capacity. You can't update this fleet property.
        :param locations: 
        :param log_configuration: The method that is used to collect container logs for the fleet. Amazon GameLift Servers saves all standard output for each container in logs, including game session logs. - ``CLOUDWATCH`` -- Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group. - ``S3`` -- Store logs in an Amazon S3 bucket that you define. - ``NONE`` -- Don't collect container logs.
        :param metric_groups: The name of an AWS CloudWatch metric group to add this fleet to. Metric groups aggregate metrics for multiple fleets.
        :param new_game_session_protection_policy: Determines whether Amazon GameLift Servers can shut down game sessions on the fleet that are actively running and hosting players. Amazon GameLift Servers might prompt an instance shutdown when scaling down fleet capacity or when retiring unhealthy instances. You can also set game session protection for individual game sessions using `UpdateGameSession <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameSession.html>`_ . - *NoProtection* -- Game sessions can be shut down during active gameplay. - *FullProtection* -- Game sessions in ``ACTIVE`` status can't be shut down.
        :param per_instance_container_group_definition_name: The name of the fleet's per-instance container group definition.
        :param scaling_policies: A list of rules that control how a fleet is scaled.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d30a780826320cc5d36af5934da7151d1abdd72973e8cb82c8f063951d6fe96d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnContainerFleetProps(
            fleet_role_arn=fleet_role_arn,
            billing_type=billing_type,
            deployment_configuration=deployment_configuration,
            description=description,
            game_server_container_group_definition_name=game_server_container_group_definition_name,
            game_server_container_groups_per_instance=game_server_container_groups_per_instance,
            game_session_creation_limit_policy=game_session_creation_limit_policy,
            instance_connection_port_range=instance_connection_port_range,
            instance_inbound_permissions=instance_inbound_permissions,
            instance_type=instance_type,
            locations=locations,
            log_configuration=log_configuration,
            metric_groups=metric_groups,
            new_game_session_protection_policy=new_game_session_protection_policy,
            per_instance_container_group_definition_name=per_instance_container_group_definition_name,
            scaling_policies=scaling_policies,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8beb89172335ad10958d248c189bbeedc924ed5525d311d2bf335e603ec0616c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f53d6bba4bd4d54dbd42a8199fcf6ff8c140c57e7fdcf6ef20d3b79946767cd0)
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
        '''A time stamp indicating when this data object was created.

        Format is a number expressed in Unix time as milliseconds (for example ``"1469498468.057"`` ).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrDeploymentDetails")
    def attr_deployment_details(self) -> _IResolvable_da3f097b:
        '''Provides information about the last deployment ID and its status.

        :cloudformationAttribute: DeploymentDetails
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrDeploymentDetails"))

    @builtins.property
    @jsii.member(jsii_name="attrFleetArn")
    def attr_fleet_arn(self) -> builtins.str:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is ``arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`` . In a GameLift fleet ARN, the resource ID matches the ``FleetId`` value.

        :cloudformationAttribute: FleetArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFleetArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFleetId")
    def attr_fleet_id(self) -> builtins.str:
        '''A unique identifier for the container fleet to retrieve.

        :cloudformationAttribute: FleetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFleetId"))

    @builtins.property
    @jsii.member(jsii_name="attrGameServerContainerGroupDefinitionArn")
    def attr_game_server_container_group_definition_arn(self) -> builtins.str:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to the fleet's game server container group. The ARN value also identifies the specific container group definition version in use.

        :cloudformationAttribute: GameServerContainerGroupDefinitionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGameServerContainerGroupDefinitionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrMaximumGameServerContainerGroupsPerInstance")
    def attr_maximum_game_server_container_groups_per_instance(self) -> jsii.Number:
        '''The calculated maximum number of game server container group that can be deployed on each fleet instance.

        The calculation depends on the resource needs of the container group and the CPU and memory resources of the fleet's instance type.

        :cloudformationAttribute: MaximumGameServerContainerGroupsPerInstance
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrMaximumGameServerContainerGroupsPerInstance"))

    @builtins.property
    @jsii.member(jsii_name="attrPerInstanceContainerGroupDefinitionArn")
    def attr_per_instance_container_group_definition_arn(self) -> builtins.str:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to the fleet's per-instance container group. The ARN value also identifies the specific container group definition version in use.

        :cloudformationAttribute: PerInstanceContainerGroupDefinitionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPerInstanceContainerGroupDefinitionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The current status of the container fleet.

        - ``PENDING`` -- A new container fleet has been requested.
        - ``CREATING`` -- A new container fleet resource is being created.
        - ``CREATED`` -- A new container fleet resource has been created. No fleet instances have been deployed.
        - ``ACTIVATING`` -- New container fleet instances are being deployed.
        - ``ACTIVE`` -- The container fleet has been deployed and is ready to host game sessions.
        - ``UPDATING`` -- Updates to the container fleet is being updated. A deployment is in progress.

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
    @jsii.member(jsii_name="fleetRoleArn")
    def fleet_role_arn(self) -> builtins.str:
        '''The unique identifier for an AWS Identity and Access Management (IAM) role with permissions to run your containers on resources that are managed by Amazon GameLift Servers.'''
        return typing.cast(builtins.str, jsii.get(self, "fleetRoleArn"))

    @fleet_role_arn.setter
    def fleet_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abbc02248f000ac12eb3d2fc54e95db4c9b42e040527d39b8128105822bfcef9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fleetRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="billingType")
    def billing_type(self) -> typing.Optional[builtins.str]:
        '''Indicates whether the fleet uses On-Demand or Spot instances for this fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "billingType"))

    @billing_type.setter
    def billing_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2584c4251bbc27920e48c58b31dee9f36c8dbf693670e559b54adf33a976a34b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "billingType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deploymentConfiguration")
    def deployment_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.DeploymentConfigurationProperty"]]:
        '''Set of rules for processing a deployment for a container fleet update.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.DeploymentConfigurationProperty"]], jsii.get(self, "deploymentConfiguration"))

    @deployment_configuration.setter
    def deployment_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.DeploymentConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef9932c78fa010240b75995b843da6e043ab92ac23a400685eeeebc9b2d9e5c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A meaningful description of the container fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3029a8fa3bd1fba1941cfbb7ca8c945357abf57a90aefe3243227816ca2aa894)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gameServerContainerGroupDefinitionName")
    def game_server_container_group_definition_name(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The name of the fleet's game server container group definition, which describes how to deploy containers with your game server build and support software onto each fleet instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gameServerContainerGroupDefinitionName"))

    @game_server_container_group_definition_name.setter
    def game_server_container_group_definition_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3c572d6543954cc606aa4cf4980b627e9dfb284c7521995845297b1b9c97a8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gameServerContainerGroupDefinitionName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gameServerContainerGroupsPerInstance")
    def game_server_container_groups_per_instance(self) -> typing.Optional[jsii.Number]:
        '''The number of times to replicate the game server container group on each fleet instance.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gameServerContainerGroupsPerInstance"))

    @game_server_container_groups_per_instance.setter
    def game_server_container_groups_per_instance(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b84912f0e8b5fe2e7b7394f1cfc1d121c2c0af1b8e7e0232c4ccba681f1970a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gameServerContainerGroupsPerInstance", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gameSessionCreationLimitPolicy")
    def game_session_creation_limit_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.GameSessionCreationLimitPolicyProperty"]]:
        '''A policy that limits the number of game sessions that each individual player can create on instances in this fleet.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.GameSessionCreationLimitPolicyProperty"]], jsii.get(self, "gameSessionCreationLimitPolicy"))

    @game_session_creation_limit_policy.setter
    def game_session_creation_limit_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.GameSessionCreationLimitPolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee374c5590b404e3cb8d6cde909b11f0fb3541f0c11fc73da3c85400628cec3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gameSessionCreationLimitPolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="instanceConnectionPortRange")
    def instance_connection_port_range(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.ConnectionPortRangeProperty"]]:
        '''The set of port numbers to open on each instance in a container fleet.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.ConnectionPortRangeProperty"]], jsii.get(self, "instanceConnectionPortRange"))

    @instance_connection_port_range.setter
    def instance_connection_port_range(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.ConnectionPortRangeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cd714c6adf18c5cdb2b4cad3d4dbf1a4a07bdbe94b6ffd5d751f200d7347426)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceConnectionPortRange", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="instanceInboundPermissions")
    def instance_inbound_permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.IpPermissionProperty"]]]]:
        '''The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.IpPermissionProperty"]]]], jsii.get(self, "instanceInboundPermissions"))

    @instance_inbound_permissions.setter
    def instance_inbound_permissions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.IpPermissionProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aae77cedd1161d46848109370fc6b6d65ab8d346c0a5f95f915a98f0d6efdbcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceInboundPermissions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 instance type to use for all instances in the fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe64b737dafa9c91cdecdbf4a073ad8425d495d7fb28182e46c423079e0b67c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="locations")
    def locations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.LocationConfigurationProperty"]]]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.LocationConfigurationProperty"]]]], jsii.get(self, "locations"))

    @locations.setter
    def locations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.LocationConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a36ecc94bdbfc4085b1baaf7462461cb77b4e640a5f1017b6653f6dc89c0b20f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logConfiguration")
    def log_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.LogConfigurationProperty"]]:
        '''The method that is used to collect container logs for the fleet.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.LogConfigurationProperty"]], jsii.get(self, "logConfiguration"))

    @log_configuration.setter
    def log_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.LogConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4618d18b990fa28be1054e4840c2f8afe6e85b406433ad49087577b8e2dfaf53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="metricGroups")
    def metric_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name of an AWS CloudWatch metric group to add this fleet to.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "metricGroups"))

    @metric_groups.setter
    def metric_groups(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43394effc64e297e079a5b571e85c8719269d3aa9af3d84206eb3fed35403442)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricGroups", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="newGameSessionProtectionPolicy")
    def new_game_session_protection_policy(self) -> typing.Optional[builtins.str]:
        '''Determines whether Amazon GameLift Servers can shut down game sessions on the fleet that are actively running and hosting players.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "newGameSessionProtectionPolicy"))

    @new_game_session_protection_policy.setter
    def new_game_session_protection_policy(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bf45e0a6202b79f4e6df01e65b4356da1371adf96524ef41997e3d3c531bf9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "newGameSessionProtectionPolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="perInstanceContainerGroupDefinitionName")
    def per_instance_container_group_definition_name(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The name of the fleet's per-instance container group definition.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "perInstanceContainerGroupDefinitionName"))

    @per_instance_container_group_definition_name.setter
    def per_instance_container_group_definition_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73062db2cea0b73eca7dbc19b367503a92d902e168720fb46aaaef0f68783f42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "perInstanceContainerGroupDefinitionName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scalingPolicies")
    def scaling_policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.ScalingPolicyProperty"]]]]:
        '''A list of rules that control how a fleet is scaled.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.ScalingPolicyProperty"]]]], jsii.get(self, "scalingPolicies"))

    @scaling_policies.setter
    def scaling_policies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.ScalingPolicyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b8d26c0f526c6120c09026205884464ccfb9805906c0810312a9ac8dc69119a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalingPolicies", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9b56d077e864bb1e2553942ee500751751ac23fc1e29dfd0bb471e69e99ff44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerFleet.ConnectionPortRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"from_port": "fromPort", "to_port": "toPort"},
    )
    class ConnectionPortRangeProperty:
        def __init__(self, *, from_port: jsii.Number, to_port: jsii.Number) -> None:
            '''The set of port numbers to open on each instance in a container fleet.

            Connection ports are used by inbound traffic to connect with processes that are running in containers on the fleet.

            :param from_port: Starting value for the port range.
            :param to_port: Ending value for the port. Port numbers are end-inclusive. This value must be equal to or greater than ``FromPort`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-connectionportrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                connection_port_range_property = gamelift.CfnContainerFleet.ConnectionPortRangeProperty(
                    from_port=123,
                    to_port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f5f97a49baa6b922fdd46128e0aecec92e3c04c61959b05e218e736635385be5)
                check_type(argname="argument from_port", value=from_port, expected_type=type_hints["from_port"])
                check_type(argname="argument to_port", value=to_port, expected_type=type_hints["to_port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "from_port": from_port,
                "to_port": to_port,
            }

        @builtins.property
        def from_port(self) -> jsii.Number:
            '''Starting value for the port range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-connectionportrange.html#cfn-gamelift-containerfleet-connectionportrange-fromport
            '''
            result = self._values.get("from_port")
            assert result is not None, "Required property 'from_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def to_port(self) -> jsii.Number:
            '''Ending value for the port.

            Port numbers are end-inclusive. This value must be equal to or greater than ``FromPort`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-connectionportrange.html#cfn-gamelift-containerfleet-connectionportrange-toport
            '''
            result = self._values.get("to_port")
            assert result is not None, "Required property 'to_port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectionPortRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerFleet.DeploymentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "impairment_strategy": "impairmentStrategy",
            "minimum_healthy_percentage": "minimumHealthyPercentage",
            "protection_strategy": "protectionStrategy",
        },
    )
    class DeploymentConfigurationProperty:
        def __init__(
            self,
            *,
            impairment_strategy: typing.Optional[builtins.str] = None,
            minimum_healthy_percentage: typing.Optional[jsii.Number] = None,
            protection_strategy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Set of rules for processing a deployment for a container fleet update.

            :param impairment_strategy: Determines what actions to take if a deployment fails. If the fleet is multi-location, this strategy applies across all fleet locations. With a rollback strategy, updated fleet instances are rolled back to the last successful deployment. Alternatively, you can maintain a few impaired containers for the purpose of debugging, while all other tasks return to the last successful deployment.
            :param minimum_healthy_percentage: Sets a minimum level of healthy tasks to maintain during deployment activity.
            :param protection_strategy: Determines how fleet deployment activity affects active game sessions on the fleet. With protection, a deployment honors game session protection, and delays actions that would interrupt a protected active game session until the game session ends. Without protection, deployment activity can shut down all running tasks, including active game sessions, regardless of game session protection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-deploymentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                deployment_configuration_property = gamelift.CfnContainerFleet.DeploymentConfigurationProperty(
                    impairment_strategy="impairmentStrategy",
                    minimum_healthy_percentage=123,
                    protection_strategy="protectionStrategy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__21e6530b63f555a4284f6eecf5700d25ca8c43cffae22ea8e225906f58003c4c)
                check_type(argname="argument impairment_strategy", value=impairment_strategy, expected_type=type_hints["impairment_strategy"])
                check_type(argname="argument minimum_healthy_percentage", value=minimum_healthy_percentage, expected_type=type_hints["minimum_healthy_percentage"])
                check_type(argname="argument protection_strategy", value=protection_strategy, expected_type=type_hints["protection_strategy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if impairment_strategy is not None:
                self._values["impairment_strategy"] = impairment_strategy
            if minimum_healthy_percentage is not None:
                self._values["minimum_healthy_percentage"] = minimum_healthy_percentage
            if protection_strategy is not None:
                self._values["protection_strategy"] = protection_strategy

        @builtins.property
        def impairment_strategy(self) -> typing.Optional[builtins.str]:
            '''Determines what actions to take if a deployment fails.

            If the fleet is multi-location, this strategy applies across all fleet locations. With a rollback strategy, updated fleet instances are rolled back to the last successful deployment. Alternatively, you can maintain a few impaired containers for the purpose of debugging, while all other tasks return to the last successful deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-deploymentconfiguration.html#cfn-gamelift-containerfleet-deploymentconfiguration-impairmentstrategy
            '''
            result = self._values.get("impairment_strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def minimum_healthy_percentage(self) -> typing.Optional[jsii.Number]:
            '''Sets a minimum level of healthy tasks to maintain during deployment activity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-deploymentconfiguration.html#cfn-gamelift-containerfleet-deploymentconfiguration-minimumhealthypercentage
            '''
            result = self._values.get("minimum_healthy_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def protection_strategy(self) -> typing.Optional[builtins.str]:
            '''Determines how fleet deployment activity affects active game sessions on the fleet.

            With protection, a deployment honors game session protection, and delays actions that would interrupt a protected active game session until the game session ends. Without protection, deployment activity can shut down all running tasks, including active game sessions, regardless of game session protection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-deploymentconfiguration.html#cfn-gamelift-containerfleet-deploymentconfiguration-protectionstrategy
            '''
            result = self._values.get("protection_strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerFleet.DeploymentDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"latest_deployment_id": "latestDeploymentId"},
    )
    class DeploymentDetailsProperty:
        def __init__(
            self,
            *,
            latest_deployment_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about the most recent deployment for the container fleet.

            :param latest_deployment_id: A unique identifier for a fleet deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-deploymentdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                deployment_details_property = gamelift.CfnContainerFleet.DeploymentDetailsProperty(
                    latest_deployment_id="latestDeploymentId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bb96aee76dbbe77d2c71ced0834b03d35c2b24b22e7f706d4c4a3476d575ad46)
                check_type(argname="argument latest_deployment_id", value=latest_deployment_id, expected_type=type_hints["latest_deployment_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if latest_deployment_id is not None:
                self._values["latest_deployment_id"] = latest_deployment_id

        @builtins.property
        def latest_deployment_id(self) -> typing.Optional[builtins.str]:
            '''A unique identifier for a fleet deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-deploymentdetails.html#cfn-gamelift-containerfleet-deploymentdetails-latestdeploymentid
            '''
            result = self._values.get("latest_deployment_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerFleet.GameSessionCreationLimitPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "new_game_sessions_per_creator": "newGameSessionsPerCreator",
            "policy_period_in_minutes": "policyPeriodInMinutes",
        },
    )
    class GameSessionCreationLimitPolicyProperty:
        def __init__(
            self,
            *,
            new_game_sessions_per_creator: typing.Optional[jsii.Number] = None,
            policy_period_in_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''A policy that puts limits on the number of game sessions that a player can create within a specified span of time.

            With this policy, you can control players' ability to consume available resources.

            The policy is evaluated when a player tries to create a new game session. On receiving a ``CreateGameSession`` request, Amazon GameLift Servers checks that the player (identified by ``CreatorId`` ) has created fewer than game session limit in the specified time period.

            :param new_game_sessions_per_creator: A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control players' ability to consume available resources. The policy evaluates when a player tries to create a new game session. On receiving a ``CreateGameSession`` request, Amazon GameLift Servers checks that the player (identified by ``CreatorId`` ) has created fewer than game session limit in the specified time period.
            :param policy_period_in_minutes: The time span used in evaluating the resource creation limit policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-gamesessioncreationlimitpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                game_session_creation_limit_policy_property = gamelift.CfnContainerFleet.GameSessionCreationLimitPolicyProperty(
                    new_game_sessions_per_creator=123,
                    policy_period_in_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f54af8dad70427c8dc70929770cd29dc6c981a2ee74ca5429adac683330a9932)
                check_type(argname="argument new_game_sessions_per_creator", value=new_game_sessions_per_creator, expected_type=type_hints["new_game_sessions_per_creator"])
                check_type(argname="argument policy_period_in_minutes", value=policy_period_in_minutes, expected_type=type_hints["policy_period_in_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if new_game_sessions_per_creator is not None:
                self._values["new_game_sessions_per_creator"] = new_game_sessions_per_creator
            if policy_period_in_minutes is not None:
                self._values["policy_period_in_minutes"] = policy_period_in_minutes

        @builtins.property
        def new_game_sessions_per_creator(self) -> typing.Optional[jsii.Number]:
            '''A policy that puts limits on the number of game sessions that a player can create within a specified span of time.

            With this policy, you can control players' ability to consume available resources.

            The policy evaluates when a player tries to create a new game session. On receiving a ``CreateGameSession`` request, Amazon GameLift Servers checks that the player (identified by ``CreatorId`` ) has created fewer than game session limit in the specified time period.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-gamesessioncreationlimitpolicy.html#cfn-gamelift-containerfleet-gamesessioncreationlimitpolicy-newgamesessionspercreator
            '''
            result = self._values.get("new_game_sessions_per_creator")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def policy_period_in_minutes(self) -> typing.Optional[jsii.Number]:
            '''The time span used in evaluating the resource creation limit policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-gamesessioncreationlimitpolicy.html#cfn-gamelift-containerfleet-gamesessioncreationlimitpolicy-policyperiodinminutes
            '''
            result = self._values.get("policy_period_in_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GameSessionCreationLimitPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerFleet.IpPermissionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "from_port": "fromPort",
            "ip_range": "ipRange",
            "protocol": "protocol",
            "to_port": "toPort",
        },
    )
    class IpPermissionProperty:
        def __init__(
            self,
            *,
            from_port: jsii.Number,
            ip_range: builtins.str,
            protocol: builtins.str,
            to_port: jsii.Number,
        ) -> None:
            '''A range of IP addresses and port settings that allow inbound traffic to connect to processes on an instance in a fleet.

            Processes are assigned an IP address/port number combination, which must fall into the fleet's allowed ranges.

            For Amazon GameLift Servers Realtime fleets, Amazon GameLift Servers automatically opens two port ranges, one for TCP messaging and one for UDP.

            :param from_port: A starting value for a range of allowed port numbers. For fleets using Linux builds, only ports ``22`` and ``1026-60000`` are valid. For fleets using Windows builds, only ports ``1026-60000`` are valid.
            :param ip_range: A range of allowed IP addresses. This value must be expressed in CIDR notation. Example: " ``000.000.000.000/[subnet mask]`` " or optionally the shortened version " ``0.0.0.0/[subnet mask]`` ".
            :param protocol: The network communication protocol used by the fleet.
            :param to_port: An ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than ``FromPort`` . For fleets using Linux builds, only ports ``22`` and ``1026-60000`` are valid. For fleets using Windows builds, only ports ``1026-60000`` are valid.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-ippermission.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                ip_permission_property = gamelift.CfnContainerFleet.IpPermissionProperty(
                    from_port=123,
                    ip_range="ipRange",
                    protocol="protocol",
                    to_port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3c74cebf3a79bd067a90f843de7a76b099cbe8aff962b812b7dcae7adae5eb58)
                check_type(argname="argument from_port", value=from_port, expected_type=type_hints["from_port"])
                check_type(argname="argument ip_range", value=ip_range, expected_type=type_hints["ip_range"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument to_port", value=to_port, expected_type=type_hints["to_port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "from_port": from_port,
                "ip_range": ip_range,
                "protocol": protocol,
                "to_port": to_port,
            }

        @builtins.property
        def from_port(self) -> jsii.Number:
            '''A starting value for a range of allowed port numbers.

            For fleets using Linux builds, only ports ``22`` and ``1026-60000`` are valid.

            For fleets using Windows builds, only ports ``1026-60000`` are valid.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-ippermission.html#cfn-gamelift-containerfleet-ippermission-fromport
            '''
            result = self._values.get("from_port")
            assert result is not None, "Required property 'from_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def ip_range(self) -> builtins.str:
            '''A range of allowed IP addresses.

            This value must be expressed in CIDR notation. Example: " ``000.000.000.000/[subnet mask]`` " or optionally the shortened version " ``0.0.0.0/[subnet mask]`` ".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-ippermission.html#cfn-gamelift-containerfleet-ippermission-iprange
            '''
            result = self._values.get("ip_range")
            assert result is not None, "Required property 'ip_range' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''The network communication protocol used by the fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-ippermission.html#cfn-gamelift-containerfleet-ippermission-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def to_port(self) -> jsii.Number:
            '''An ending value for a range of allowed port numbers.

            Port numbers are end-inclusive. This value must be equal to or greater than ``FromPort`` .

            For fleets using Linux builds, only ports ``22`` and ``1026-60000`` are valid.

            For fleets using Windows builds, only ports ``1026-60000`` are valid.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-ippermission.html#cfn-gamelift-containerfleet-ippermission-toport
            '''
            result = self._values.get("to_port")
            assert result is not None, "Required property 'to_port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IpPermissionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerFleet.LocationCapacityProperty",
        jsii_struct_bases=[],
        name_mapping={
            "desired_ec2_instances": "desiredEc2Instances",
            "max_size": "maxSize",
            "min_size": "minSize",
        },
    )
    class LocationCapacityProperty:
        def __init__(
            self,
            *,
            desired_ec2_instances: jsii.Number,
            max_size: jsii.Number,
            min_size: jsii.Number,
        ) -> None:
            '''Current resource capacity settings in a specified fleet or location.

            The location value might refer to a fleet's remote location or its home Region.

            :param desired_ec2_instances: The number of EC2 instances you want to maintain in the specified fleet location. This value must fall between the minimum and maximum size limits. If any auto-scaling policy is defined for the container fleet, the desired instance will only be applied once during fleet creation and will be ignored in updates to avoid conflicts with auto-scaling. During updates with any auto-scaling policy defined, if current desired instance is lower than the new MinSize, it will be increased to the new MinSize; if current desired instance is larger than the new MaxSize, it will be decreased to the new MaxSize.
            :param max_size: The maximum value that is allowed for the fleet's instance count for a location.
            :param min_size: The minimum value allowed for the fleet's instance count for a location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-locationcapacity.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                location_capacity_property = gamelift.CfnContainerFleet.LocationCapacityProperty(
                    desired_ec2_instances=123,
                    max_size=123,
                    min_size=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cfdc01eeb9f739a54f304b9e5cb1f66114e55233f5383f018ef7dd086a28ed10)
                check_type(argname="argument desired_ec2_instances", value=desired_ec2_instances, expected_type=type_hints["desired_ec2_instances"])
                check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
                check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "desired_ec2_instances": desired_ec2_instances,
                "max_size": max_size,
                "min_size": min_size,
            }

        @builtins.property
        def desired_ec2_instances(self) -> jsii.Number:
            '''The number of EC2 instances you want to maintain in the specified fleet location.

            This value must fall between the minimum and maximum size limits. If any auto-scaling policy is defined for the container fleet, the desired instance will only be applied once during fleet creation and will be ignored in updates to avoid conflicts with auto-scaling. During updates with any auto-scaling policy defined, if current desired instance is lower than the new MinSize, it will be increased to the new MinSize; if current desired instance is larger than the new MaxSize, it will be decreased to the new MaxSize.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-locationcapacity.html#cfn-gamelift-containerfleet-locationcapacity-desiredec2instances
            '''
            result = self._values.get("desired_ec2_instances")
            assert result is not None, "Required property 'desired_ec2_instances' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max_size(self) -> jsii.Number:
            '''The maximum value that is allowed for the fleet's instance count for a location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-locationcapacity.html#cfn-gamelift-containerfleet-locationcapacity-maxsize
            '''
            result = self._values.get("max_size")
            assert result is not None, "Required property 'max_size' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def min_size(self) -> jsii.Number:
            '''The minimum value allowed for the fleet's instance count for a location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-locationcapacity.html#cfn-gamelift-containerfleet-locationcapacity-minsize
            '''
            result = self._values.get("min_size")
            assert result is not None, "Required property 'min_size' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationCapacityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerFleet.LocationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "location": "location",
            "location_capacity": "locationCapacity",
            "stopped_actions": "stoppedActions",
        },
    )
    class LocationConfigurationProperty:
        def __init__(
            self,
            *,
            location: builtins.str,
            location_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerFleet.LocationCapacityProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            stopped_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A remote location where a multi-location fleet can deploy game servers for game hosting.

            :param location: An AWS Region code, such as ``us-west-2`` . For a list of supported Regions and Local Zones, see `Amazon GameLift Servers service locations <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html>`_ for managed hosting.
            :param location_capacity: Current resource capacity settings in a specified fleet or location. The location value might refer to a fleet's remote location or its home Region.
            :param stopped_actions: A list of fleet actions that have been suspended in the fleet location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-locationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                location_configuration_property = gamelift.CfnContainerFleet.LocationConfigurationProperty(
                    location="location",
                
                    # the properties below are optional
                    location_capacity=gamelift.CfnContainerFleet.LocationCapacityProperty(
                        desired_ec2_instances=123,
                        max_size=123,
                        min_size=123
                    ),
                    stopped_actions=["stoppedActions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6f0d55ebb1c8fdd9364a92df8152f6c91294e481bedd64b3458f3dff3c77ec80)
                check_type(argname="argument location", value=location, expected_type=type_hints["location"])
                check_type(argname="argument location_capacity", value=location_capacity, expected_type=type_hints["location_capacity"])
                check_type(argname="argument stopped_actions", value=stopped_actions, expected_type=type_hints["stopped_actions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "location": location,
            }
            if location_capacity is not None:
                self._values["location_capacity"] = location_capacity
            if stopped_actions is not None:
                self._values["stopped_actions"] = stopped_actions

        @builtins.property
        def location(self) -> builtins.str:
            '''An AWS Region code, such as ``us-west-2`` .

            For a list of supported Regions and Local Zones, see `Amazon GameLift Servers service locations <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html>`_ for managed hosting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-locationconfiguration.html#cfn-gamelift-containerfleet-locationconfiguration-location
            '''
            result = self._values.get("location")
            assert result is not None, "Required property 'location' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def location_capacity(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.LocationCapacityProperty"]]:
            '''Current resource capacity settings in a specified fleet or location.

            The location value might refer to a fleet's remote location or its home Region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-locationconfiguration.html#cfn-gamelift-containerfleet-locationconfiguration-locationcapacity
            '''
            result = self._values.get("location_capacity")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.LocationCapacityProperty"]], result)

        @builtins.property
        def stopped_actions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of fleet actions that have been suspended in the fleet location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-locationconfiguration.html#cfn-gamelift-containerfleet-locationconfiguration-stoppedactions
            '''
            result = self._values.get("stopped_actions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerFleet.LogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_destination": "logDestination",
            "log_group_arn": "logGroupArn",
            "s3_bucket_name": "s3BucketName",
        },
    )
    class LogConfigurationProperty:
        def __init__(
            self,
            *,
            log_destination: typing.Optional[builtins.str] = None,
            log_group_arn: typing.Optional[builtins.str] = None,
            s3_bucket_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A method for collecting container logs for the fleet.

            Amazon GameLift Servers saves all standard output for each container in logs, including game session logs. You can select from the following methods:

            :param log_destination: The type of log collection to use for a fleet. - ``CLOUDWATCH`` -- (default value) Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group. - ``S3`` -- Store logs in an Amazon S3 bucket that you define. This bucket must reside in the fleet's home AWS Region. - ``NONE`` -- Don't collect container logs.
            :param log_group_arn: If log destination is ``CLOUDWATCH`` , logs are sent to the specified log group in Amazon CloudWatch.
            :param s3_bucket_name: If log destination is ``S3`` , logs are sent to the specified Amazon S3 bucket name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-logconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                log_configuration_property = gamelift.CfnContainerFleet.LogConfigurationProperty(
                    log_destination="logDestination",
                    log_group_arn="logGroupArn",
                    s3_bucket_name="s3BucketName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__287854cb20cec032892a9072e611adf774cd43dcc343c3ffdda539be73bce563)
                check_type(argname="argument log_destination", value=log_destination, expected_type=type_hints["log_destination"])
                check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
                check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_destination is not None:
                self._values["log_destination"] = log_destination
            if log_group_arn is not None:
                self._values["log_group_arn"] = log_group_arn
            if s3_bucket_name is not None:
                self._values["s3_bucket_name"] = s3_bucket_name

        @builtins.property
        def log_destination(self) -> typing.Optional[builtins.str]:
            '''The type of log collection to use for a fleet.

            - ``CLOUDWATCH`` -- (default value) Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group.
            - ``S3`` -- Store logs in an Amazon S3 bucket that you define. This bucket must reside in the fleet's home AWS Region.
            - ``NONE`` -- Don't collect container logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-logconfiguration.html#cfn-gamelift-containerfleet-logconfiguration-logdestination
            '''
            result = self._values.get("log_destination")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_group_arn(self) -> typing.Optional[builtins.str]:
            '''If log destination is ``CLOUDWATCH`` , logs are sent to the specified log group in Amazon CloudWatch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-logconfiguration.html#cfn-gamelift-containerfleet-logconfiguration-loggrouparn
            '''
            result = self._values.get("log_group_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_bucket_name(self) -> typing.Optional[builtins.str]:
            '''If log destination is ``S3`` , logs are sent to the specified Amazon S3 bucket name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-logconfiguration.html#cfn-gamelift-containerfleet-logconfiguration-s3bucketname
            '''
            result = self._values.get("s3_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerFleet.ScalingPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_name": "metricName",
            "name": "name",
            "comparison_operator": "comparisonOperator",
            "evaluation_periods": "evaluationPeriods",
            "policy_type": "policyType",
            "scaling_adjustment": "scalingAdjustment",
            "scaling_adjustment_type": "scalingAdjustmentType",
            "target_configuration": "targetConfiguration",
            "threshold": "threshold",
        },
    )
    class ScalingPolicyProperty:
        def __init__(
            self,
            *,
            metric_name: builtins.str,
            name: builtins.str,
            comparison_operator: typing.Optional[builtins.str] = None,
            evaluation_periods: typing.Optional[jsii.Number] = None,
            policy_type: typing.Optional[builtins.str] = None,
            scaling_adjustment: typing.Optional[jsii.Number] = None,
            scaling_adjustment_type: typing.Optional[builtins.str] = None,
            target_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerFleet.TargetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            threshold: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Rule that controls how a fleet is scaled.

            Scaling policies are uniquely identified by the combination of name and fleet ID.

            :param metric_name: Name of the Amazon GameLift Servers-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see `Monitor Amazon GameLift Servers with Amazon CloudWatch <https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html>`_ . - *ActivatingGameSessions* -- Game sessions in the process of being created. - *ActiveGameSessions* -- Game sessions that are currently running. - *ActiveInstances* -- Fleet instances that are currently running at least one game session. - *AvailableGameSessions* -- Additional game sessions that fleet could host simultaneously, given current capacity. - *AvailablePlayerSessions* -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included. - *CurrentPlayerSessions* -- Player slots in active game sessions that are being used by a player or are reserved for a player. - *IdleInstances* -- Active instances that are currently hosting zero game sessions. - *PercentAvailableGameSessions* -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy. - *PercentIdleInstances* -- Percentage of the total number of active instances that are hosting zero game sessions. - *QueueDepth* -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination. - *WaitTime* -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
            :param name: A descriptive label that is associated with a fleet's scaling policy. Policy names do not need to be unique.
            :param comparison_operator: Comparison operator to use when measuring a metric against the threshold value.
            :param evaluation_periods: Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.
            :param policy_type: The type of scaling policy to create. For a target-based policy, set the parameter *MetricName* to 'PercentAvailableGameSessions' and specify a *TargetConfiguration* . For a rule-based policy set the following parameters: *MetricName* , *ComparisonOperator* , *Threshold* , *EvaluationPeriods* , *ScalingAdjustmentType* , and *ScalingAdjustment* .
            :param scaling_adjustment: Amount of adjustment to make, based on the scaling adjustment type.
            :param scaling_adjustment_type: The type of adjustment to make to a fleet's instance count. - *ChangeInCapacity* -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down. - *ExactCapacity* -- set the instance count to the scaling adjustment value. - *PercentChangeInCapacity* -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down.
            :param target_configuration: An object that contains settings for a target-based scaling policy.
            :param threshold: Metric value used to trigger a scaling event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-scalingpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                scaling_policy_property = gamelift.CfnContainerFleet.ScalingPolicyProperty(
                    metric_name="metricName",
                    name="name",
                
                    # the properties below are optional
                    comparison_operator="comparisonOperator",
                    evaluation_periods=123,
                    policy_type="policyType",
                    scaling_adjustment=123,
                    scaling_adjustment_type="scalingAdjustmentType",
                    target_configuration=gamelift.CfnContainerFleet.TargetConfigurationProperty(
                        target_value=123
                    ),
                    threshold=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__77733d66802ae69be5c6e0b5788b2caf6cc2db612ef32cb9e718cc475df0b111)
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
                check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
                check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
                check_type(argname="argument scaling_adjustment", value=scaling_adjustment, expected_type=type_hints["scaling_adjustment"])
                check_type(argname="argument scaling_adjustment_type", value=scaling_adjustment_type, expected_type=type_hints["scaling_adjustment_type"])
                check_type(argname="argument target_configuration", value=target_configuration, expected_type=type_hints["target_configuration"])
                check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "metric_name": metric_name,
                "name": name,
            }
            if comparison_operator is not None:
                self._values["comparison_operator"] = comparison_operator
            if evaluation_periods is not None:
                self._values["evaluation_periods"] = evaluation_periods
            if policy_type is not None:
                self._values["policy_type"] = policy_type
            if scaling_adjustment is not None:
                self._values["scaling_adjustment"] = scaling_adjustment
            if scaling_adjustment_type is not None:
                self._values["scaling_adjustment_type"] = scaling_adjustment_type
            if target_configuration is not None:
                self._values["target_configuration"] = target_configuration
            if threshold is not None:
                self._values["threshold"] = threshold

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''Name of the Amazon GameLift Servers-defined metric that is used to trigger a scaling adjustment.

            For detailed descriptions of fleet metrics, see `Monitor Amazon GameLift Servers with Amazon CloudWatch <https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html>`_ .

            - *ActivatingGameSessions* -- Game sessions in the process of being created.
            - *ActiveGameSessions* -- Game sessions that are currently running.
            - *ActiveInstances* -- Fleet instances that are currently running at least one game session.
            - *AvailableGameSessions* -- Additional game sessions that fleet could host simultaneously, given current capacity.
            - *AvailablePlayerSessions* -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.
            - *CurrentPlayerSessions* -- Player slots in active game sessions that are being used by a player or are reserved for a player.
            - *IdleInstances* -- Active instances that are currently hosting zero game sessions.
            - *PercentAvailableGameSessions* -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.
            - *PercentIdleInstances* -- Percentage of the total number of active instances that are hosting zero game sessions.
            - *QueueDepth* -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
            - *WaitTime* -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-scalingpolicy.html#cfn-gamelift-containerfleet-scalingpolicy-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''A descriptive label that is associated with a fleet's scaling policy.

            Policy names do not need to be unique.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-scalingpolicy.html#cfn-gamelift-containerfleet-scalingpolicy-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def comparison_operator(self) -> typing.Optional[builtins.str]:
            '''Comparison operator to use when measuring a metric against the threshold value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-scalingpolicy.html#cfn-gamelift-containerfleet-scalingpolicy-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def evaluation_periods(self) -> typing.Optional[jsii.Number]:
            '''Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-scalingpolicy.html#cfn-gamelift-containerfleet-scalingpolicy-evaluationperiods
            '''
            result = self._values.get("evaluation_periods")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def policy_type(self) -> typing.Optional[builtins.str]:
            '''The type of scaling policy to create.

            For a target-based policy, set the parameter *MetricName* to 'PercentAvailableGameSessions' and specify a *TargetConfiguration* . For a rule-based policy set the following parameters: *MetricName* , *ComparisonOperator* , *Threshold* , *EvaluationPeriods* , *ScalingAdjustmentType* , and *ScalingAdjustment* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-scalingpolicy.html#cfn-gamelift-containerfleet-scalingpolicy-policytype
            '''
            result = self._values.get("policy_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scaling_adjustment(self) -> typing.Optional[jsii.Number]:
            '''Amount of adjustment to make, based on the scaling adjustment type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-scalingpolicy.html#cfn-gamelift-containerfleet-scalingpolicy-scalingadjustment
            '''
            result = self._values.get("scaling_adjustment")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def scaling_adjustment_type(self) -> typing.Optional[builtins.str]:
            '''The type of adjustment to make to a fleet's instance count.

            - *ChangeInCapacity* -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.
            - *ExactCapacity* -- set the instance count to the scaling adjustment value.
            - *PercentChangeInCapacity* -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-scalingpolicy.html#cfn-gamelift-containerfleet-scalingpolicy-scalingadjustmenttype
            '''
            result = self._values.get("scaling_adjustment_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.TargetConfigurationProperty"]]:
            '''An object that contains settings for a target-based scaling policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-scalingpolicy.html#cfn-gamelift-containerfleet-scalingpolicy-targetconfiguration
            '''
            result = self._values.get("target_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerFleet.TargetConfigurationProperty"]], result)

        @builtins.property
        def threshold(self) -> typing.Optional[jsii.Number]:
            '''Metric value used to trigger a scaling event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-scalingpolicy.html#cfn-gamelift-containerfleet-scalingpolicy-threshold
            '''
            result = self._values.get("threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerFleet.TargetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"target_value": "targetValue"},
    )
    class TargetConfigurationProperty:
        def __init__(self, *, target_value: jsii.Number) -> None:
            '''Settings for a target-based scaling policy.

            A target-based policy tracks a particular fleet metric specifies a target value for the metric. As player usage changes, the policy triggers Amazon GameLift Servers to adjust capacity so that the metric returns to the target value. The target configuration specifies settings as needed for the target based policy, including the target value.

            :param target_value: Desired value to use with a target-based scaling policy. The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleet's buffer (the percent of capacity that should be idle and ready for new game sessions).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-targetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                target_configuration_property = gamelift.CfnContainerFleet.TargetConfigurationProperty(
                    target_value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3133704901a8cbe841212bef17b3e01ca8f97d737576c8860ee4bf4a44f4e8ca)
                check_type(argname="argument target_value", value=target_value, expected_type=type_hints["target_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_value": target_value,
            }

        @builtins.property
        def target_value(self) -> jsii.Number:
            '''Desired value to use with a target-based scaling policy.

            The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleet's buffer (the percent of capacity that should be idle and ready for new game sessions).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containerfleet-targetconfiguration.html#cfn-gamelift-containerfleet-targetconfiguration-targetvalue
            '''
            result = self._values.get("target_value")
            assert result is not None, "Required property 'target_value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerFleetProps",
    jsii_struct_bases=[],
    name_mapping={
        "fleet_role_arn": "fleetRoleArn",
        "billing_type": "billingType",
        "deployment_configuration": "deploymentConfiguration",
        "description": "description",
        "game_server_container_group_definition_name": "gameServerContainerGroupDefinitionName",
        "game_server_container_groups_per_instance": "gameServerContainerGroupsPerInstance",
        "game_session_creation_limit_policy": "gameSessionCreationLimitPolicy",
        "instance_connection_port_range": "instanceConnectionPortRange",
        "instance_inbound_permissions": "instanceInboundPermissions",
        "instance_type": "instanceType",
        "locations": "locations",
        "log_configuration": "logConfiguration",
        "metric_groups": "metricGroups",
        "new_game_session_protection_policy": "newGameSessionProtectionPolicy",
        "per_instance_container_group_definition_name": "perInstanceContainerGroupDefinitionName",
        "scaling_policies": "scalingPolicies",
        "tags": "tags",
    },
)
class CfnContainerFleetProps:
    def __init__(
        self,
        *,
        fleet_role_arn: builtins.str,
        billing_type: typing.Optional[builtins.str] = None,
        deployment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.DeploymentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        game_server_container_group_definition_name: typing.Optional[builtins.str] = None,
        game_server_container_groups_per_instance: typing.Optional[jsii.Number] = None,
        game_session_creation_limit_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.GameSessionCreationLimitPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        instance_connection_port_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.ConnectionPortRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        instance_inbound_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.IpPermissionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        instance_type: typing.Optional[builtins.str] = None,
        locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.LocationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        log_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        metric_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        new_game_session_protection_policy: typing.Optional[builtins.str] = None,
        per_instance_container_group_definition_name: typing.Optional[builtins.str] = None,
        scaling_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.ScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnContainerFleet``.

        :param fleet_role_arn: The unique identifier for an AWS Identity and Access Management (IAM) role with permissions to run your containers on resources that are managed by Amazon GameLift Servers. See `Set up an IAM service role <https://docs.aws.amazon.com/gamelift/latest/developerguide/setting-up-role.html>`_ . This fleet property can't be changed.
        :param billing_type: Indicates whether the fleet uses On-Demand or Spot instances for this fleet. Learn more about when to use `On-Demand versus Spot Instances <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot>`_ . You can't update this fleet property. By default, this property is set to ``ON_DEMAND`` .
        :param deployment_configuration: Set of rules for processing a deployment for a container fleet update.
        :param description: A meaningful description of the container fleet.
        :param game_server_container_group_definition_name: The name of the fleet's game server container group definition, which describes how to deploy containers with your game server build and support software onto each fleet instance.
        :param game_server_container_groups_per_instance: The number of times to replicate the game server container group on each fleet instance.
        :param game_session_creation_limit_policy: A policy that limits the number of game sessions that each individual player can create on instances in this fleet. The limit applies for a specified span of time.
        :param instance_connection_port_range: The set of port numbers to open on each instance in a container fleet. Connection ports are used by inbound traffic to connect with processes that are running in containers on the fleet.
        :param instance_inbound_permissions: The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet.
        :param instance_type: The Amazon EC2 instance type to use for all instances in the fleet. Instance type determines the computing resources and processing power that's available to host your game servers. This includes including CPU, memory, storage, and networking capacity. You can't update this fleet property.
        :param locations: 
        :param log_configuration: The method that is used to collect container logs for the fleet. Amazon GameLift Servers saves all standard output for each container in logs, including game session logs. - ``CLOUDWATCH`` -- Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group. - ``S3`` -- Store logs in an Amazon S3 bucket that you define. - ``NONE`` -- Don't collect container logs.
        :param metric_groups: The name of an AWS CloudWatch metric group to add this fleet to. Metric groups aggregate metrics for multiple fleets.
        :param new_game_session_protection_policy: Determines whether Amazon GameLift Servers can shut down game sessions on the fleet that are actively running and hosting players. Amazon GameLift Servers might prompt an instance shutdown when scaling down fleet capacity or when retiring unhealthy instances. You can also set game session protection for individual game sessions using `UpdateGameSession <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameSession.html>`_ . - *NoProtection* -- Game sessions can be shut down during active gameplay. - *FullProtection* -- Game sessions in ``ACTIVE`` status can't be shut down.
        :param per_instance_container_group_definition_name: The name of the fleet's per-instance container group definition.
        :param scaling_policies: A list of rules that control how a fleet is scaled.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_container_fleet_props = gamelift.CfnContainerFleetProps(
                fleet_role_arn="fleetRoleArn",
            
                # the properties below are optional
                billing_type="billingType",
                deployment_configuration=gamelift.CfnContainerFleet.DeploymentConfigurationProperty(
                    impairment_strategy="impairmentStrategy",
                    minimum_healthy_percentage=123,
                    protection_strategy="protectionStrategy"
                ),
                description="description",
                game_server_container_group_definition_name="gameServerContainerGroupDefinitionName",
                game_server_container_groups_per_instance=123,
                game_session_creation_limit_policy=gamelift.CfnContainerFleet.GameSessionCreationLimitPolicyProperty(
                    new_game_sessions_per_creator=123,
                    policy_period_in_minutes=123
                ),
                instance_connection_port_range=gamelift.CfnContainerFleet.ConnectionPortRangeProperty(
                    from_port=123,
                    to_port=123
                ),
                instance_inbound_permissions=[gamelift.CfnContainerFleet.IpPermissionProperty(
                    from_port=123,
                    ip_range="ipRange",
                    protocol="protocol",
                    to_port=123
                )],
                instance_type="instanceType",
                locations=[gamelift.CfnContainerFleet.LocationConfigurationProperty(
                    location="location",
            
                    # the properties below are optional
                    location_capacity=gamelift.CfnContainerFleet.LocationCapacityProperty(
                        desired_ec2_instances=123,
                        max_size=123,
                        min_size=123
                    ),
                    stopped_actions=["stoppedActions"]
                )],
                log_configuration=gamelift.CfnContainerFleet.LogConfigurationProperty(
                    log_destination="logDestination",
                    log_group_arn="logGroupArn",
                    s3_bucket_name="s3BucketName"
                ),
                metric_groups=["metricGroups"],
                new_game_session_protection_policy="newGameSessionProtectionPolicy",
                per_instance_container_group_definition_name="perInstanceContainerGroupDefinitionName",
                scaling_policies=[gamelift.CfnContainerFleet.ScalingPolicyProperty(
                    metric_name="metricName",
                    name="name",
            
                    # the properties below are optional
                    comparison_operator="comparisonOperator",
                    evaluation_periods=123,
                    policy_type="policyType",
                    scaling_adjustment=123,
                    scaling_adjustment_type="scalingAdjustmentType",
                    target_configuration=gamelift.CfnContainerFleet.TargetConfigurationProperty(
                        target_value=123
                    ),
                    threshold=123
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fbf4a66831e3b15f9023046fb41b590456b41ba1048fa4e59749ccd8f9d023c)
            check_type(argname="argument fleet_role_arn", value=fleet_role_arn, expected_type=type_hints["fleet_role_arn"])
            check_type(argname="argument billing_type", value=billing_type, expected_type=type_hints["billing_type"])
            check_type(argname="argument deployment_configuration", value=deployment_configuration, expected_type=type_hints["deployment_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument game_server_container_group_definition_name", value=game_server_container_group_definition_name, expected_type=type_hints["game_server_container_group_definition_name"])
            check_type(argname="argument game_server_container_groups_per_instance", value=game_server_container_groups_per_instance, expected_type=type_hints["game_server_container_groups_per_instance"])
            check_type(argname="argument game_session_creation_limit_policy", value=game_session_creation_limit_policy, expected_type=type_hints["game_session_creation_limit_policy"])
            check_type(argname="argument instance_connection_port_range", value=instance_connection_port_range, expected_type=type_hints["instance_connection_port_range"])
            check_type(argname="argument instance_inbound_permissions", value=instance_inbound_permissions, expected_type=type_hints["instance_inbound_permissions"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument locations", value=locations, expected_type=type_hints["locations"])
            check_type(argname="argument log_configuration", value=log_configuration, expected_type=type_hints["log_configuration"])
            check_type(argname="argument metric_groups", value=metric_groups, expected_type=type_hints["metric_groups"])
            check_type(argname="argument new_game_session_protection_policy", value=new_game_session_protection_policy, expected_type=type_hints["new_game_session_protection_policy"])
            check_type(argname="argument per_instance_container_group_definition_name", value=per_instance_container_group_definition_name, expected_type=type_hints["per_instance_container_group_definition_name"])
            check_type(argname="argument scaling_policies", value=scaling_policies, expected_type=type_hints["scaling_policies"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fleet_role_arn": fleet_role_arn,
        }
        if billing_type is not None:
            self._values["billing_type"] = billing_type
        if deployment_configuration is not None:
            self._values["deployment_configuration"] = deployment_configuration
        if description is not None:
            self._values["description"] = description
        if game_server_container_group_definition_name is not None:
            self._values["game_server_container_group_definition_name"] = game_server_container_group_definition_name
        if game_server_container_groups_per_instance is not None:
            self._values["game_server_container_groups_per_instance"] = game_server_container_groups_per_instance
        if game_session_creation_limit_policy is not None:
            self._values["game_session_creation_limit_policy"] = game_session_creation_limit_policy
        if instance_connection_port_range is not None:
            self._values["instance_connection_port_range"] = instance_connection_port_range
        if instance_inbound_permissions is not None:
            self._values["instance_inbound_permissions"] = instance_inbound_permissions
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if locations is not None:
            self._values["locations"] = locations
        if log_configuration is not None:
            self._values["log_configuration"] = log_configuration
        if metric_groups is not None:
            self._values["metric_groups"] = metric_groups
        if new_game_session_protection_policy is not None:
            self._values["new_game_session_protection_policy"] = new_game_session_protection_policy
        if per_instance_container_group_definition_name is not None:
            self._values["per_instance_container_group_definition_name"] = per_instance_container_group_definition_name
        if scaling_policies is not None:
            self._values["scaling_policies"] = scaling_policies
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def fleet_role_arn(self) -> builtins.str:
        '''The unique identifier for an AWS Identity and Access Management (IAM) role with permissions to run your containers on resources that are managed by Amazon GameLift Servers.

        See `Set up an IAM service role <https://docs.aws.amazon.com/gamelift/latest/developerguide/setting-up-role.html>`_ . This fleet property can't be changed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-fleetrolearn
        '''
        result = self._values.get("fleet_role_arn")
        assert result is not None, "Required property 'fleet_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def billing_type(self) -> typing.Optional[builtins.str]:
        '''Indicates whether the fleet uses On-Demand or Spot instances for this fleet.

        Learn more about when to use `On-Demand versus Spot Instances <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot>`_ . You can't update this fleet property.

        By default, this property is set to ``ON_DEMAND`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-billingtype
        '''
        result = self._values.get("billing_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.DeploymentConfigurationProperty]]:
        '''Set of rules for processing a deployment for a container fleet update.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-deploymentconfiguration
        '''
        result = self._values.get("deployment_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.DeploymentConfigurationProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A meaningful description of the container fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def game_server_container_group_definition_name(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The name of the fleet's game server container group definition, which describes how to deploy containers with your game server build and support software onto each fleet instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-gameservercontainergroupdefinitionname
        '''
        result = self._values.get("game_server_container_group_definition_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def game_server_container_groups_per_instance(self) -> typing.Optional[jsii.Number]:
        '''The number of times to replicate the game server container group on each fleet instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-gameservercontainergroupsperinstance
        '''
        result = self._values.get("game_server_container_groups_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def game_session_creation_limit_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.GameSessionCreationLimitPolicyProperty]]:
        '''A policy that limits the number of game sessions that each individual player can create on instances in this fleet.

        The limit applies for a specified span of time.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-gamesessioncreationlimitpolicy
        '''
        result = self._values.get("game_session_creation_limit_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.GameSessionCreationLimitPolicyProperty]], result)

    @builtins.property
    def instance_connection_port_range(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.ConnectionPortRangeProperty]]:
        '''The set of port numbers to open on each instance in a container fleet.

        Connection ports are used by inbound traffic to connect with processes that are running in containers on the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-instanceconnectionportrange
        '''
        result = self._values.get("instance_connection_port_range")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.ConnectionPortRangeProperty]], result)

    @builtins.property
    def instance_inbound_permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.IpPermissionProperty]]]]:
        '''The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-instanceinboundpermissions
        '''
        result = self._values.get("instance_inbound_permissions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.IpPermissionProperty]]]], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 instance type to use for all instances in the fleet.

        Instance type determines the computing resources and processing power that's available to host your game servers. This includes including CPU, memory, storage, and networking capacity. You can't update this fleet property.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-instancetype
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def locations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.LocationConfigurationProperty]]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-locations
        '''
        result = self._values.get("locations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.LocationConfigurationProperty]]]], result)

    @builtins.property
    def log_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.LogConfigurationProperty]]:
        '''The method that is used to collect container logs for the fleet.

        Amazon GameLift Servers saves all standard output for each container in logs, including game session logs.

        - ``CLOUDWATCH`` -- Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group.
        - ``S3`` -- Store logs in an Amazon S3 bucket that you define.
        - ``NONE`` -- Don't collect container logs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-logconfiguration
        '''
        result = self._values.get("log_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.LogConfigurationProperty]], result)

    @builtins.property
    def metric_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name of an AWS CloudWatch metric group to add this fleet to.

        Metric groups aggregate metrics for multiple fleets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-metricgroups
        '''
        result = self._values.get("metric_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def new_game_session_protection_policy(self) -> typing.Optional[builtins.str]:
        '''Determines whether Amazon GameLift Servers can shut down game sessions on the fleet that are actively running and hosting players.

        Amazon GameLift Servers might prompt an instance shutdown when scaling down fleet capacity or when retiring unhealthy instances. You can also set game session protection for individual game sessions using `UpdateGameSession <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameSession.html>`_ .

        - *NoProtection* -- Game sessions can be shut down during active gameplay.
        - *FullProtection* -- Game sessions in ``ACTIVE`` status can't be shut down.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-newgamesessionprotectionpolicy
        '''
        result = self._values.get("new_game_session_protection_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def per_instance_container_group_definition_name(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The name of the fleet's per-instance container group definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-perinstancecontainergroupdefinitionname
        '''
        result = self._values.get("per_instance_container_group_definition_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scaling_policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.ScalingPolicyProperty]]]]:
        '''A list of rules that control how a fleet is scaled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-scalingpolicies
        '''
        result = self._values.get("scaling_policies")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.ScalingPolicyProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containerfleet.html#cfn-gamelift-containerfleet-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContainerFleetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnContainerGroupDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition",
):
    '''The properties that describe a container group resource.

    You can update all properties of a container group definition properties. Updates to a container group definition are saved as new versions.

    *Used with:* `CreateContainerGroupDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html>`_

    *Returned by:* `DescribeContainerGroupDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeContainerGroupDefinition.html>`_ , `ListContainerGroupDefinitions <https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitions.html>`_ , `UpdateContainerGroupDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html
    :cloudformationResource: AWS::GameLift::ContainerGroupDefinition
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_container_group_definition = gamelift.CfnContainerGroupDefinition(self, "MyCfnContainerGroupDefinition",
            name="name",
            operating_system="operatingSystem",
            total_memory_limit_mebibytes=123,
            total_vcpu_limit=123,
        
            # the properties below are optional
            container_group_type="containerGroupType",
            game_server_container_definition=gamelift.CfnContainerGroupDefinition.GameServerContainerDefinitionProperty(
                container_name="containerName",
                image_uri="imageUri",
                server_sdk_version="serverSdkVersion",
        
                # the properties below are optional
                depends_on=[gamelift.CfnContainerGroupDefinition.ContainerDependencyProperty(
                    condition="condition",
                    container_name="containerName"
                )],
                environment_override=[gamelift.CfnContainerGroupDefinition.ContainerEnvironmentProperty(
                    name="name",
                    value="value"
                )],
                mount_points=[gamelift.CfnContainerGroupDefinition.ContainerMountPointProperty(
                    instance_path="instancePath",
        
                    # the properties below are optional
                    access_level="accessLevel",
                    container_path="containerPath"
                )],
                port_configuration=gamelift.CfnContainerGroupDefinition.PortConfigurationProperty(
                    container_port_ranges=[gamelift.CfnContainerGroupDefinition.ContainerPortRangeProperty(
                        from_port=123,
                        protocol="protocol",
                        to_port=123
                    )]
                ),
                resolved_image_digest="resolvedImageDigest"
            ),
            source_version_number=123,
            support_container_definitions=[gamelift.CfnContainerGroupDefinition.SupportContainerDefinitionProperty(
                container_name="containerName",
                image_uri="imageUri",
        
                # the properties below are optional
                depends_on=[gamelift.CfnContainerGroupDefinition.ContainerDependencyProperty(
                    condition="condition",
                    container_name="containerName"
                )],
                environment_override=[gamelift.CfnContainerGroupDefinition.ContainerEnvironmentProperty(
                    name="name",
                    value="value"
                )],
                essential=False,
                health_check=gamelift.CfnContainerGroupDefinition.ContainerHealthCheckProperty(
                    command=["command"],
        
                    # the properties below are optional
                    interval=123,
                    retries=123,
                    start_period=123,
                    timeout=123
                ),
                memory_hard_limit_mebibytes=123,
                mount_points=[gamelift.CfnContainerGroupDefinition.ContainerMountPointProperty(
                    instance_path="instancePath",
        
                    # the properties below are optional
                    access_level="accessLevel",
                    container_path="containerPath"
                )],
                port_configuration=gamelift.CfnContainerGroupDefinition.PortConfigurationProperty(
                    container_port_ranges=[gamelift.CfnContainerGroupDefinition.ContainerPortRangeProperty(
                        from_port=123,
                        protocol="protocol",
                        to_port=123
                    )]
                ),
                resolved_image_digest="resolvedImageDigest",
                vcpu=123
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            version_description="versionDescription"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        operating_system: builtins.str,
        total_memory_limit_mebibytes: jsii.Number,
        total_vcpu_limit: jsii.Number,
        container_group_type: typing.Optional[builtins.str] = None,
        game_server_container_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.GameServerContainerDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        source_version_number: typing.Optional[jsii.Number] = None,
        support_container_definitions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.SupportContainerDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A descriptive identifier for the container group definition. The name value is unique in an AWS Region.
        :param operating_system: The platform that all containers in the container group definition run on. .. epigraph:: Amazon Linux 2 (AL2) will reach end of support on 6/30/2025. See more details in the `Amazon Linux 2 FAQs <https://docs.aws.amazon.com/amazon-linux-2/faqs/>`_ . For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See `Migrate to server SDK version 5. <https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html>`_
        :param total_memory_limit_mebibytes: The amount of memory (in MiB) on a fleet instance to allocate for the container group. All containers in the group share these resources. You can set a limit for each container definition in the group. If individual containers have limits, this total value must be greater than any individual container's memory limit.
        :param total_vcpu_limit: The amount of vCPU units on a fleet instance to allocate for the container group (1 vCPU is equal to 1024 CPU units). All containers in the group share these resources. You can set a limit for each container definition in the group. If individual containers have limits, this total value must be equal to or greater than the sum of the limits for each container in the group.
        :param container_group_type: The type of container group. Container group type determines how Amazon GameLift Servers deploys the container group on each fleet instance.
        :param game_server_container_definition: The definition for the game server container in this group. This property is used only when the container group type is ``GAME_SERVER`` . This container definition specifies a container image with the game server build.
        :param source_version_number: A specific ContainerGroupDefinition version to be updated.
        :param support_container_definitions: The set of definitions for support containers in this group. A container group definition might have zero support container definitions. Support container can be used in any type of container group.
        :param tags: An array of key-value pairs to apply to this resource.
        :param version_description: An optional description that was provided for a container group definition update. Each version can have a unique description.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d0ad3aeb1243549bc05c0346bb1e8303d21326ec9f1a17ec63327d7e3f29a1e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnContainerGroupDefinitionProps(
            name=name,
            operating_system=operating_system,
            total_memory_limit_mebibytes=total_memory_limit_mebibytes,
            total_vcpu_limit=total_vcpu_limit,
            container_group_type=container_group_type,
            game_server_container_definition=game_server_container_definition,
            source_version_number=source_version_number,
            support_container_definitions=support_container_definitions,
            tags=tags,
            version_description=version_description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b07a706beb428681d6a41fe2a705cfe7e9f6f65c0df4708d633a856c73d6fa7b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__abcc96ad0c8f9f987fd719eb37179f12dda8829dbbc0b9fb28188a52044ec711)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrContainerGroupDefinitionArn")
    def attr_container_group_definition_arn(self) -> builtins.str:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to an Amazon GameLift Servers ``ContainerGroupDefinition`` resource. It uniquely identifies the resource across all AWS Regions. Format is ``arn:aws:gamelift:[region]::containergroupdefinition/[container group definition name]:[version]`` .

        :cloudformationAttribute: ContainerGroupDefinitionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrContainerGroupDefinitionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''A time stamp indicating when this data object was created.

        Format is a number expressed in Unix time as milliseconds (for example ``"1469498468.057"`` ).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Current status of the container group definition resource. Values include:.

        - ``COPYING`` -- Amazon GameLift Servers is in the process of making copies of all container images that are defined in the group. While in this state, the resource can't be used to create a container fleet.
        - ``READY`` -- Amazon GameLift Servers has copied the registry images for all containers that are defined in the group. You can use a container group definition in this status to create a container fleet.
        - ``FAILED`` -- Amazon GameLift Servers failed to create a valid container group definition resource. For more details on the cause of the failure, see ``StatusReason`` . A container group definition resource in failed status will be deleted within a few minutes.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusReason")
    def attr_status_reason(self) -> builtins.str:
        '''Additional information about a container group definition that's in ``FAILED`` status. Possible reasons include:.

        - An internal issue prevented Amazon GameLift Servers from creating the container group definition resource. Delete the failed resource and call `CreateContainerGroupDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html>`_ again.
        - An access-denied message means that you don't have permissions to access the container image on ECR. See `IAM permission examples <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-iam-policy-examples.html.html>`_ for help setting up required IAM permissions for Amazon GameLift Servers.
        - The ``ImageUri`` value for at least one of the containers in the container group definition was invalid or not found in the current AWS account.
        - At least one of the container images referenced in the container group definition exceeds the allowed size. For size limits, see `Amazon GameLift Servers endpoints and quotas <https://docs.aws.amazon.com/general/latest/gr/gamelift.html>`_ .
        - At least one of the container images referenced in the container group definition uses a different operating system than the one defined for the container group.

        :cloudformationAttribute: StatusReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusReason"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionNumber")
    def attr_version_number(self) -> jsii.Number:
        '''Indicates the version of a particular container group definition.

        This number is incremented automatically when you update a container group definition. You can view, update, or delete individual versions or the entire container group definition.

        :cloudformationAttribute: VersionNumber
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrVersionNumber"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A descriptive identifier for the container group definition.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90e8a024d1021ae9b57dadc57167a55f375efa5756fd3358541d1bbca8f16cf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="operatingSystem")
    def operating_system(self) -> builtins.str:
        '''The platform that all containers in the container group definition run on.'''
        return typing.cast(builtins.str, jsii.get(self, "operatingSystem"))

    @operating_system.setter
    def operating_system(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f85c42319aa42e6c796369d8760bfb73c97a6305632fa1b86497b93a214a2ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operatingSystem", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="totalMemoryLimitMebibytes")
    def total_memory_limit_mebibytes(self) -> jsii.Number:
        '''The amount of memory (in MiB) on a fleet instance to allocate for the container group.'''
        return typing.cast(jsii.Number, jsii.get(self, "totalMemoryLimitMebibytes"))

    @total_memory_limit_mebibytes.setter
    def total_memory_limit_mebibytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9806a412f491ae7e0701177df10f3e3f8f7c4f8fca4c26908502d2f9e2257026)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "totalMemoryLimitMebibytes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="totalVcpuLimit")
    def total_vcpu_limit(self) -> jsii.Number:
        '''The amount of vCPU units on a fleet instance to allocate for the container group (1 vCPU is equal to 1024 CPU units).'''
        return typing.cast(jsii.Number, jsii.get(self, "totalVcpuLimit"))

    @total_vcpu_limit.setter
    def total_vcpu_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cac0cc3ab1e2d26b478bc208c563a20312989d26048f9500230ad42e1300f7f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "totalVcpuLimit", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="containerGroupType")
    def container_group_type(self) -> typing.Optional[builtins.str]:
        '''The type of container group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerGroupType"))

    @container_group_type.setter
    def container_group_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__752739c32e65d44c30b88e307fe3881e0e9b34d2745e17aa9c60392ca6e6d97e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerGroupType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gameServerContainerDefinition")
    def game_server_container_definition(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.GameServerContainerDefinitionProperty"]]:
        '''The definition for the game server container in this group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.GameServerContainerDefinitionProperty"]], jsii.get(self, "gameServerContainerDefinition"))

    @game_server_container_definition.setter
    def game_server_container_definition(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.GameServerContainerDefinitionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c82cba9110173a8477c870dcd9dc5096dee3fc3981d5dbbdb3e909b3777f47d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gameServerContainerDefinition", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceVersionNumber")
    def source_version_number(self) -> typing.Optional[jsii.Number]:
        '''A specific ContainerGroupDefinition version to be updated.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sourceVersionNumber"))

    @source_version_number.setter
    def source_version_number(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5672891cfbdf9eecf6dc0835cad6505adf6ecd0957851f286608ea9077312f19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceVersionNumber", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="supportContainerDefinitions")
    def support_container_definitions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.SupportContainerDefinitionProperty"]]]]:
        '''The set of definitions for support containers in this group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.SupportContainerDefinitionProperty"]]]], jsii.get(self, "supportContainerDefinitions"))

    @support_container_definitions.setter
    def support_container_definitions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.SupportContainerDefinitionProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8eefcc08a08c4e2d5876a924350a3f3122337dadd842f4c45350099127878a77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportContainerDefinitions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39d9905e11429554186c96e0a5c07109b132519014161fc8e8d7aa9f4250218d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="versionDescription")
    def version_description(self) -> typing.Optional[builtins.str]:
        '''An optional description that was provided for a container group definition update.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionDescription"))

    @version_description.setter
    def version_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f96815347c81f9c90df0014b6a4de3f36fbcb0f246e66a58ef72af2f6caade8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionDescription", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition.ContainerDependencyProperty",
        jsii_struct_bases=[],
        name_mapping={"condition": "condition", "container_name": "containerName"},
    )
    class ContainerDependencyProperty:
        def __init__(
            self,
            *,
            condition: builtins.str,
            container_name: builtins.str,
        ) -> None:
            '''A container's dependency on another container in the same container group.

            The dependency impacts how the dependent container is able to start or shut down based the status of the other container.

            For example, *ContainerA* is configured with the following dependency: a ``START`` dependency on *ContainerB* . This means that *ContainerA* can't start until *ContainerB* has started. It also means that *ContainerA* must shut down before *ContainerB* .

            *Part of:* `GameServerContainerDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html>`_ , `GameServerContainerDefinitionInput <https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html>`_ , `SupportContainerDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html>`_ , `SupportContainerDefinitionInput <https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html>`_

            :param condition: The condition that the dependency container must reach before the dependent container can start. Valid conditions include:. - START - The dependency container must have started. - COMPLETE - The dependency container has run to completion (exits). Use this condition with nonessential containers, such as those that run a script and then exit. The dependency container can't be an essential container. - SUCCESS - The dependency container has run to completion and exited with a zero status. The dependency container can't be an essential container. - HEALTHY - The dependency container has passed its Docker health check. Use this condition with dependency containers that have health checks configured. This condition is confirmed at container group startup only.
            :param container_name: A descriptive label for the container definition that this container depends on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdependency.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                container_dependency_property = gamelift.CfnContainerGroupDefinition.ContainerDependencyProperty(
                    condition="condition",
                    container_name="containerName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e8424bed9ce9567d13ec372652e5d607735583e13219bd42143f538aee3feb1f)
                check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
                check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "condition": condition,
                "container_name": container_name,
            }

        @builtins.property
        def condition(self) -> builtins.str:
            '''The condition that the dependency container must reach before the dependent container can start. Valid conditions include:.

            - START - The dependency container must have started.
            - COMPLETE - The dependency container has run to completion (exits). Use this condition with nonessential containers, such as those that run a script and then exit. The dependency container can't be an essential container.
            - SUCCESS - The dependency container has run to completion and exited with a zero status. The dependency container can't be an essential container.
            - HEALTHY - The dependency container has passed its Docker health check. Use this condition with dependency containers that have health checks configured. This condition is confirmed at container group startup only.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdependency.html#cfn-gamelift-containergroupdefinition-containerdependency-condition
            '''
            result = self._values.get("condition")
            assert result is not None, "Required property 'condition' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def container_name(self) -> builtins.str:
            '''A descriptive label for the container definition that this container depends on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdependency.html#cfn-gamelift-containergroupdefinition-containerdependency-containername
            '''
            result = self._values.get("container_name")
            assert result is not None, "Required property 'container_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerDependencyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition.ContainerEnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class ContainerEnvironmentProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''An environment variable to set inside a container, in the form of a key-value pair.

            *Part of:* `GameServerContainerDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html>`_ , `GameServerContainerDefinitionInput <https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html>`_ , `SupportContainerDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html>`_ , `SupportContainerDefinitionInput <https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html>`_

            :param name: The environment variable name.
            :param value: The environment variable value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerenvironment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                container_environment_property = gamelift.CfnContainerGroupDefinition.ContainerEnvironmentProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c8a971f77ef4383909669846d3e4ee4a8463f7353ec0c1aa4da152ea7ec43bb9)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The environment variable name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerenvironment.html#cfn-gamelift-containergroupdefinition-containerenvironment-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The environment variable value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerenvironment.html#cfn-gamelift-containergroupdefinition-containerenvironment-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerEnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition.ContainerHealthCheckProperty",
        jsii_struct_bases=[],
        name_mapping={
            "command": "command",
            "interval": "interval",
            "retries": "retries",
            "start_period": "startPeriod",
            "timeout": "timeout",
        },
    )
    class ContainerHealthCheckProperty:
        def __init__(
            self,
            *,
            command: typing.Sequence[builtins.str],
            interval: typing.Optional[jsii.Number] = None,
            retries: typing.Optional[jsii.Number] = None,
            start_period: typing.Optional[jsii.Number] = None,
            timeout: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Instructions on when and how to check the health of a support container in a container fleet.

            These properties override any Docker health checks that are set in the container image. For more information on container health checks, see `HealthCheck command <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_HealthCheck.html#ECS-Type-HealthCheck-command>`_ in the *Amazon Elastic Container Service API* . Game server containers don't have a health check parameter; Amazon GameLift Servers automatically handles health checks for these containers.

            The following example instructs the container to initiate a health check command every 60 seconds and wait 10 seconds for it to succeed. If it fails, retry the command 3 times before flagging the container as unhealthy. It also tells the container to wait 100 seconds after launch before counting failed health checks.

            ``{"Command": [ "CMD-SHELL", "ps cax | grep "processmanager" || exit 1" ], "Interval": 60, "Timeout": 10, "Retries": 3, "StartPeriod": 100 }``

            *Part of:* `SupportContainerDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html>`_ , `SupportContainerDefinitionInput <https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html>`_

            :param command: A string array that specifies the command that the container runs to determine if it's healthy.
            :param interval: The time period (in seconds) between each health check.
            :param retries: The number of times to retry a failed health check before flagging the container unhealthy. The first run of the command does not count as a retry.
            :param start_period: The optional grace period (in seconds) to give a container time to bootstrap before the first failed health check counts toward the number of retries.
            :param timeout: The time period (in seconds) to wait for a health check to succeed before counting a failed health check.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerhealthcheck.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                container_health_check_property = gamelift.CfnContainerGroupDefinition.ContainerHealthCheckProperty(
                    command=["command"],
                
                    # the properties below are optional
                    interval=123,
                    retries=123,
                    start_period=123,
                    timeout=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__95b1e7083ac6b3d39e0bc5926b3c9ee368385be498c61499a81f860b155d0a1d)
                check_type(argname="argument command", value=command, expected_type=type_hints["command"])
                check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
                check_type(argname="argument retries", value=retries, expected_type=type_hints["retries"])
                check_type(argname="argument start_period", value=start_period, expected_type=type_hints["start_period"])
                check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "command": command,
            }
            if interval is not None:
                self._values["interval"] = interval
            if retries is not None:
                self._values["retries"] = retries
            if start_period is not None:
                self._values["start_period"] = start_period
            if timeout is not None:
                self._values["timeout"] = timeout

        @builtins.property
        def command(self) -> typing.List[builtins.str]:
            '''A string array that specifies the command that the container runs to determine if it's healthy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerhealthcheck.html#cfn-gamelift-containergroupdefinition-containerhealthcheck-command
            '''
            result = self._values.get("command")
            assert result is not None, "Required property 'command' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def interval(self) -> typing.Optional[jsii.Number]:
            '''The time period (in seconds) between each health check.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerhealthcheck.html#cfn-gamelift-containergroupdefinition-containerhealthcheck-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def retries(self) -> typing.Optional[jsii.Number]:
            '''The number of times to retry a failed health check before flagging the container unhealthy.

            The first run of the command does not count as a retry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerhealthcheck.html#cfn-gamelift-containergroupdefinition-containerhealthcheck-retries
            '''
            result = self._values.get("retries")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def start_period(self) -> typing.Optional[jsii.Number]:
            '''The optional grace period (in seconds) to give a container time to bootstrap before the first failed health check counts toward the number of retries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerhealthcheck.html#cfn-gamelift-containergroupdefinition-containerhealthcheck-startperiod
            '''
            result = self._values.get("start_period")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def timeout(self) -> typing.Optional[jsii.Number]:
            '''The time period (in seconds) to wait for a health check to succeed before counting a failed health check.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerhealthcheck.html#cfn-gamelift-containergroupdefinition-containerhealthcheck-timeout
            '''
            result = self._values.get("timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerHealthCheckProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition.ContainerMountPointProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_path": "instancePath",
            "access_level": "accessLevel",
            "container_path": "containerPath",
        },
    )
    class ContainerMountPointProperty:
        def __init__(
            self,
            *,
            instance_path: builtins.str,
            access_level: typing.Optional[builtins.str] = None,
            container_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A mount point that binds a container to a file or directory on the host system.

            *Part of:* `GameServerContainerDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinition.html>`_ , ` <https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html>`_ , `SupportContainerDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinition.html>`_ , ` <https://docs.aws.amazon.com/gamelift/latest/apireference/API_SupportContainerDefinitionInput.html>`_

            :param instance_path: The path to the source file or directory.
            :param access_level: The type of access for the container.
            :param container_path: The mount path on the container. If this property isn't set, the instance path is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containermountpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                container_mount_point_property = gamelift.CfnContainerGroupDefinition.ContainerMountPointProperty(
                    instance_path="instancePath",
                
                    # the properties below are optional
                    access_level="accessLevel",
                    container_path="containerPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__582a62e33c1aa361f9ef7ca37ba1315dfbf02275fd99e239191003b332a6b172)
                check_type(argname="argument instance_path", value=instance_path, expected_type=type_hints["instance_path"])
                check_type(argname="argument access_level", value=access_level, expected_type=type_hints["access_level"])
                check_type(argname="argument container_path", value=container_path, expected_type=type_hints["container_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_path": instance_path,
            }
            if access_level is not None:
                self._values["access_level"] = access_level
            if container_path is not None:
                self._values["container_path"] = container_path

        @builtins.property
        def instance_path(self) -> builtins.str:
            '''The path to the source file or directory.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containermountpoint.html#cfn-gamelift-containergroupdefinition-containermountpoint-instancepath
            '''
            result = self._values.get("instance_path")
            assert result is not None, "Required property 'instance_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def access_level(self) -> typing.Optional[builtins.str]:
            '''The type of access for the container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containermountpoint.html#cfn-gamelift-containergroupdefinition-containermountpoint-accesslevel
            '''
            result = self._values.get("access_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def container_path(self) -> typing.Optional[builtins.str]:
            '''The mount path on the container.

            If this property isn't set, the instance path is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containermountpoint.html#cfn-gamelift-containergroupdefinition-containermountpoint-containerpath
            '''
            result = self._values.get("container_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerMountPointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition.ContainerPortRangeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "from_port": "fromPort",
            "protocol": "protocol",
            "to_port": "toPort",
        },
    )
    class ContainerPortRangeProperty:
        def __init__(
            self,
            *,
            from_port: jsii.Number,
            protocol: builtins.str,
            to_port: jsii.Number,
        ) -> None:
            '''A set of one or more port numbers that can be opened on the container, and the supported network protocol.

            *Part of:* `ContainerPortConfiguration <https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerPortConfiguration.html>`_

            :param from_port: A starting value for the range of allowed port numbers.
            :param protocol: The network protocol that these ports support.
            :param to_port: An ending value for the range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than ``FromPort`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerportrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                container_port_range_property = gamelift.CfnContainerGroupDefinition.ContainerPortRangeProperty(
                    from_port=123,
                    protocol="protocol",
                    to_port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2d3e35cf8a42e8cbcdf12218e64e5ac29c19f0813f144c8d75e97d3e3313d396)
                check_type(argname="argument from_port", value=from_port, expected_type=type_hints["from_port"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument to_port", value=to_port, expected_type=type_hints["to_port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "from_port": from_port,
                "protocol": protocol,
                "to_port": to_port,
            }

        @builtins.property
        def from_port(self) -> jsii.Number:
            '''A starting value for the range of allowed port numbers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerportrange.html#cfn-gamelift-containergroupdefinition-containerportrange-fromport
            '''
            result = self._values.get("from_port")
            assert result is not None, "Required property 'from_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''The network protocol that these ports support.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerportrange.html#cfn-gamelift-containergroupdefinition-containerportrange-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def to_port(self) -> jsii.Number:
            '''An ending value for the range of allowed port numbers.

            Port numbers are end-inclusive. This value must be equal to or greater than ``FromPort`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerportrange.html#cfn-gamelift-containergroupdefinition-containerportrange-toport
            '''
            result = self._values.get("to_port")
            assert result is not None, "Required property 'to_port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerPortRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition.GameServerContainerDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_name": "containerName",
            "image_uri": "imageUri",
            "server_sdk_version": "serverSdkVersion",
            "depends_on": "dependsOn",
            "environment_override": "environmentOverride",
            "mount_points": "mountPoints",
            "port_configuration": "portConfiguration",
            "resolved_image_digest": "resolvedImageDigest",
        },
    )
    class GameServerContainerDefinitionProperty:
        def __init__(
            self,
            *,
            container_name: builtins.str,
            image_uri: builtins.str,
            server_sdk_version: builtins.str,
            depends_on: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.ContainerDependencyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            environment_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.ContainerEnvironmentProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            mount_points: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.ContainerMountPointProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            port_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.PortConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            resolved_image_digest: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the game server container in an existing game server container group.

            A game server container identifies a container image with your game server build. A game server container is automatically considered essential; if an essential container fails, the entire container group restarts.

            You can update a container definition and deploy the updates to an existing fleet. When creating or updating a game server container group definition, use the property ` <https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput>`_ .

            *Part of:* `ContainerGroupDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html>`_

            *Returned by:* `DescribeContainerGroupDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeContainerGroupDefinition.html>`_ , `ListContainerGroupDefinitions <https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitions.html>`_ , `UpdateContainerGroupDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html>`_

            :param container_name: The container definition identifier. Container names are unique within a container group definition.
            :param image_uri: The URI to the image that Amazon GameLift Servers uses when deploying this container to a container fleet. For a more specific identifier, see ``ResolvedImageDigest`` .
            :param server_sdk_version: The Amazon GameLift Servers server SDK version that the game server is integrated with. Only game servers using 5.2.0 or higher are compatible with container fleets.
            :param depends_on: Indicates that the container relies on the status of other containers in the same container group during startup and shutdown sequences. A container might have dependencies on multiple containers.
            :param environment_override: A set of environment variables that's passed to the container on startup. See the `ContainerDefinition::environment <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment>`_ parameter in the *Amazon Elastic Container Service API Reference* .
            :param mount_points: A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.
            :param port_configuration: The set of ports that are available to bind to processes in the container. For example, a game server process requires a container port to allow game clients to connect to it. Container ports aren't directly accessed by inbound traffic. Amazon GameLift Servers maps these container ports to externally accessible connection ports, which are assigned as needed from the container fleet's ``ConnectionPortRange`` .
            :param resolved_image_digest: A unique and immutable identifier for the container image. The digest is a SHA 256 hash of the container image manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-gameservercontainerdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                game_server_container_definition_property = gamelift.CfnContainerGroupDefinition.GameServerContainerDefinitionProperty(
                    container_name="containerName",
                    image_uri="imageUri",
                    server_sdk_version="serverSdkVersion",
                
                    # the properties below are optional
                    depends_on=[gamelift.CfnContainerGroupDefinition.ContainerDependencyProperty(
                        condition="condition",
                        container_name="containerName"
                    )],
                    environment_override=[gamelift.CfnContainerGroupDefinition.ContainerEnvironmentProperty(
                        name="name",
                        value="value"
                    )],
                    mount_points=[gamelift.CfnContainerGroupDefinition.ContainerMountPointProperty(
                        instance_path="instancePath",
                
                        # the properties below are optional
                        access_level="accessLevel",
                        container_path="containerPath"
                    )],
                    port_configuration=gamelift.CfnContainerGroupDefinition.PortConfigurationProperty(
                        container_port_ranges=[gamelift.CfnContainerGroupDefinition.ContainerPortRangeProperty(
                            from_port=123,
                            protocol="protocol",
                            to_port=123
                        )]
                    ),
                    resolved_image_digest="resolvedImageDigest"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__996969233fd34d51e9d9534744b87b0efc6e35f90fac9e44bd0cb26d5f2918f3)
                check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
                check_type(argname="argument image_uri", value=image_uri, expected_type=type_hints["image_uri"])
                check_type(argname="argument server_sdk_version", value=server_sdk_version, expected_type=type_hints["server_sdk_version"])
                check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
                check_type(argname="argument environment_override", value=environment_override, expected_type=type_hints["environment_override"])
                check_type(argname="argument mount_points", value=mount_points, expected_type=type_hints["mount_points"])
                check_type(argname="argument port_configuration", value=port_configuration, expected_type=type_hints["port_configuration"])
                check_type(argname="argument resolved_image_digest", value=resolved_image_digest, expected_type=type_hints["resolved_image_digest"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "container_name": container_name,
                "image_uri": image_uri,
                "server_sdk_version": server_sdk_version,
            }
            if depends_on is not None:
                self._values["depends_on"] = depends_on
            if environment_override is not None:
                self._values["environment_override"] = environment_override
            if mount_points is not None:
                self._values["mount_points"] = mount_points
            if port_configuration is not None:
                self._values["port_configuration"] = port_configuration
            if resolved_image_digest is not None:
                self._values["resolved_image_digest"] = resolved_image_digest

        @builtins.property
        def container_name(self) -> builtins.str:
            '''The container definition identifier.

            Container names are unique within a container group definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-gameservercontainerdefinition.html#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-containername
            '''
            result = self._values.get("container_name")
            assert result is not None, "Required property 'container_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_uri(self) -> builtins.str:
            '''The URI to the image that Amazon GameLift Servers uses when deploying this container to a container fleet.

            For a more specific identifier, see ``ResolvedImageDigest`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-gameservercontainerdefinition.html#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-imageuri
            '''
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def server_sdk_version(self) -> builtins.str:
            '''The Amazon GameLift Servers server SDK version that the game server is integrated with.

            Only game servers using 5.2.0 or higher are compatible with container fleets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-gameservercontainerdefinition.html#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-serversdkversion
            '''
            result = self._values.get("server_sdk_version")
            assert result is not None, "Required property 'server_sdk_version' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def depends_on(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerDependencyProperty"]]]]:
            '''Indicates that the container relies on the status of other containers in the same container group during startup and shutdown sequences.

            A container might have dependencies on multiple containers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-gameservercontainerdefinition.html#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-dependson
            '''
            result = self._values.get("depends_on")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerDependencyProperty"]]]], result)

        @builtins.property
        def environment_override(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerEnvironmentProperty"]]]]:
            '''A set of environment variables that's passed to the container on startup.

            See the `ContainerDefinition::environment <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment>`_ parameter in the *Amazon Elastic Container Service API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-gameservercontainerdefinition.html#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-environmentoverride
            '''
            result = self._values.get("environment_override")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerEnvironmentProperty"]]]], result)

        @builtins.property
        def mount_points(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerMountPointProperty"]]]]:
            '''A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-gameservercontainerdefinition.html#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-mountpoints
            '''
            result = self._values.get("mount_points")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerMountPointProperty"]]]], result)

        @builtins.property
        def port_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.PortConfigurationProperty"]]:
            '''The set of ports that are available to bind to processes in the container.

            For example, a game server process requires a container port to allow game clients to connect to it. Container ports aren't directly accessed by inbound traffic. Amazon GameLift Servers maps these container ports to externally accessible connection ports, which are assigned as needed from the container fleet's ``ConnectionPortRange`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-gameservercontainerdefinition.html#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-portconfiguration
            '''
            result = self._values.get("port_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.PortConfigurationProperty"]], result)

        @builtins.property
        def resolved_image_digest(self) -> typing.Optional[builtins.str]:
            '''A unique and immutable identifier for the container image.

            The digest is a SHA 256 hash of the container image manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-gameservercontainerdefinition.html#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition-resolvedimagedigest
            '''
            result = self._values.get("resolved_image_digest")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GameServerContainerDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition.PortConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"container_port_ranges": "containerPortRanges"},
    )
    class PortConfigurationProperty:
        def __init__(
            self,
            *,
            container_port_ranges: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.ContainerPortRangeProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Defines the ports on a container.

            :param container_port_ranges: Specifies one or more ranges of ports on a container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-portconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                port_configuration_property = gamelift.CfnContainerGroupDefinition.PortConfigurationProperty(
                    container_port_ranges=[gamelift.CfnContainerGroupDefinition.ContainerPortRangeProperty(
                        from_port=123,
                        protocol="protocol",
                        to_port=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__49796d7f2a6fb9a60e370fb5b8e88da33d84ca298d8833d8e64e3d80586cedf7)
                check_type(argname="argument container_port_ranges", value=container_port_ranges, expected_type=type_hints["container_port_ranges"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "container_port_ranges": container_port_ranges,
            }

        @builtins.property
        def container_port_ranges(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerPortRangeProperty"]]]:
            '''Specifies one or more ranges of ports on a container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-portconfiguration.html#cfn-gamelift-containergroupdefinition-portconfiguration-containerportranges
            '''
            result = self._values.get("container_port_ranges")
            assert result is not None, "Required property 'container_port_ranges' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerPortRangeProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition.SupportContainerDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_name": "containerName",
            "image_uri": "imageUri",
            "depends_on": "dependsOn",
            "environment_override": "environmentOverride",
            "essential": "essential",
            "health_check": "healthCheck",
            "memory_hard_limit_mebibytes": "memoryHardLimitMebibytes",
            "mount_points": "mountPoints",
            "port_configuration": "portConfiguration",
            "resolved_image_digest": "resolvedImageDigest",
            "vcpu": "vcpu",
        },
    )
    class SupportContainerDefinitionProperty:
        def __init__(
            self,
            *,
            container_name: builtins.str,
            image_uri: builtins.str,
            depends_on: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.ContainerDependencyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            environment_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.ContainerEnvironmentProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            essential: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            health_check: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.ContainerHealthCheckProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            memory_hard_limit_mebibytes: typing.Optional[jsii.Number] = None,
            mount_points: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.ContainerMountPointProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            port_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.PortConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            resolved_image_digest: typing.Optional[builtins.str] = None,
            vcpu: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes a support container in a container group.

            A support container might be in a game server container group or a per-instance container group. Support containers don't run game server processes.

            You can update a support container definition and deploy the updates to an existing fleet. When creating or updating a game server container group definition, use the property `GameServerContainerDefinitionInput <https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerContainerDefinitionInput.html>`_ .

            *Part of:* `ContainerGroupDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html>`_

            *Returned by:* `DescribeContainerGroupDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeContainerGroupDefinition.html>`_ , `ListContainerGroupDefinitions <https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitions.html>`_ , `UpdateContainerGroupDefinition <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html>`_

            :param container_name: The container definition identifier. Container names are unique within a container group definition.
            :param image_uri: The URI to the image that Amazon GameLift Servers deploys to a container fleet. For a more specific identifier, see ``ResolvedImageDigest`` .
            :param depends_on: Indicates that the container relies on the status of other containers in the same container group during its startup and shutdown sequences. A container might have dependencies on multiple containers.
            :param environment_override: A set of environment variables that's passed to the container on startup. See the `ContainerDefinition::environment <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment>`_ parameter in the *Amazon Elastic Container Service API Reference* .
            :param essential: Indicates whether the container is vital to the container group. If an essential container fails, the entire container group restarts.
            :param health_check: A configuration for a non-terminal health check. A support container automatically restarts if it stops functioning or if it fails this health check.
            :param memory_hard_limit_mebibytes: The amount of memory that Amazon GameLift Servers makes available to the container. If memory limits aren't set for an individual container, the container shares the container group's total memory allocation. *Related data type:* `ContainerGroupDefinition TotalMemoryLimitMebibytes <https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html>`_
            :param mount_points: A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.
            :param port_configuration: A set of ports that allow access to the container from external users. Processes running in the container can bind to a one of these ports. Container ports aren't directly accessed by inbound traffic. Amazon GameLift Servers maps these container ports to externally accessible connection ports, which are assigned as needed from the container fleet's ``ConnectionPortRange`` .
            :param resolved_image_digest: A unique and immutable identifier for the container image. The digest is a SHA 256 hash of the container image manifest.
            :param vcpu: The number of vCPU units that are reserved for the container. If no resources are reserved, the container shares the total vCPU limit for the container group. *Related data type:* `ContainerGroupDefinition TotalVcpuLimit <https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                support_container_definition_property = gamelift.CfnContainerGroupDefinition.SupportContainerDefinitionProperty(
                    container_name="containerName",
                    image_uri="imageUri",
                
                    # the properties below are optional
                    depends_on=[gamelift.CfnContainerGroupDefinition.ContainerDependencyProperty(
                        condition="condition",
                        container_name="containerName"
                    )],
                    environment_override=[gamelift.CfnContainerGroupDefinition.ContainerEnvironmentProperty(
                        name="name",
                        value="value"
                    )],
                    essential=False,
                    health_check=gamelift.CfnContainerGroupDefinition.ContainerHealthCheckProperty(
                        command=["command"],
                
                        # the properties below are optional
                        interval=123,
                        retries=123,
                        start_period=123,
                        timeout=123
                    ),
                    memory_hard_limit_mebibytes=123,
                    mount_points=[gamelift.CfnContainerGroupDefinition.ContainerMountPointProperty(
                        instance_path="instancePath",
                
                        # the properties below are optional
                        access_level="accessLevel",
                        container_path="containerPath"
                    )],
                    port_configuration=gamelift.CfnContainerGroupDefinition.PortConfigurationProperty(
                        container_port_ranges=[gamelift.CfnContainerGroupDefinition.ContainerPortRangeProperty(
                            from_port=123,
                            protocol="protocol",
                            to_port=123
                        )]
                    ),
                    resolved_image_digest="resolvedImageDigest",
                    vcpu=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6565c3caf0bf39eea0bc662ef87427d6cf77017b05483384a736fa1c260791c8)
                check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
                check_type(argname="argument image_uri", value=image_uri, expected_type=type_hints["image_uri"])
                check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
                check_type(argname="argument environment_override", value=environment_override, expected_type=type_hints["environment_override"])
                check_type(argname="argument essential", value=essential, expected_type=type_hints["essential"])
                check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
                check_type(argname="argument memory_hard_limit_mebibytes", value=memory_hard_limit_mebibytes, expected_type=type_hints["memory_hard_limit_mebibytes"])
                check_type(argname="argument mount_points", value=mount_points, expected_type=type_hints["mount_points"])
                check_type(argname="argument port_configuration", value=port_configuration, expected_type=type_hints["port_configuration"])
                check_type(argname="argument resolved_image_digest", value=resolved_image_digest, expected_type=type_hints["resolved_image_digest"])
                check_type(argname="argument vcpu", value=vcpu, expected_type=type_hints["vcpu"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "container_name": container_name,
                "image_uri": image_uri,
            }
            if depends_on is not None:
                self._values["depends_on"] = depends_on
            if environment_override is not None:
                self._values["environment_override"] = environment_override
            if essential is not None:
                self._values["essential"] = essential
            if health_check is not None:
                self._values["health_check"] = health_check
            if memory_hard_limit_mebibytes is not None:
                self._values["memory_hard_limit_mebibytes"] = memory_hard_limit_mebibytes
            if mount_points is not None:
                self._values["mount_points"] = mount_points
            if port_configuration is not None:
                self._values["port_configuration"] = port_configuration
            if resolved_image_digest is not None:
                self._values["resolved_image_digest"] = resolved_image_digest
            if vcpu is not None:
                self._values["vcpu"] = vcpu

        @builtins.property
        def container_name(self) -> builtins.str:
            '''The container definition identifier.

            Container names are unique within a container group definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition.html#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-containername
            '''
            result = self._values.get("container_name")
            assert result is not None, "Required property 'container_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_uri(self) -> builtins.str:
            '''The URI to the image that Amazon GameLift Servers deploys to a container fleet.

            For a more specific identifier, see ``ResolvedImageDigest`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition.html#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-imageuri
            '''
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def depends_on(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerDependencyProperty"]]]]:
            '''Indicates that the container relies on the status of other containers in the same container group during its startup and shutdown sequences.

            A container might have dependencies on multiple containers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition.html#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-dependson
            '''
            result = self._values.get("depends_on")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerDependencyProperty"]]]], result)

        @builtins.property
        def environment_override(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerEnvironmentProperty"]]]]:
            '''A set of environment variables that's passed to the container on startup.

            See the `ContainerDefinition::environment <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment>`_ parameter in the *Amazon Elastic Container Service API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition.html#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-environmentoverride
            '''
            result = self._values.get("environment_override")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerEnvironmentProperty"]]]], result)

        @builtins.property
        def essential(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the container is vital to the container group.

            If an essential container fails, the entire container group restarts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition.html#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-essential
            '''
            result = self._values.get("essential")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def health_check(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerHealthCheckProperty"]]:
            '''A configuration for a non-terminal health check.

            A support container automatically restarts if it stops functioning or if it fails this health check.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition.html#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-healthcheck
            '''
            result = self._values.get("health_check")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerHealthCheckProperty"]], result)

        @builtins.property
        def memory_hard_limit_mebibytes(self) -> typing.Optional[jsii.Number]:
            '''The amount of memory that Amazon GameLift Servers makes available to the container.

            If memory limits aren't set for an individual container, the container shares the container group's total memory allocation.

            *Related data type:* `ContainerGroupDefinition TotalMemoryLimitMebibytes <https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition.html#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-memoryhardlimitmebibytes
            '''
            result = self._values.get("memory_hard_limit_mebibytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def mount_points(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerMountPointProperty"]]]]:
            '''A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition.html#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-mountpoints
            '''
            result = self._values.get("mount_points")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerMountPointProperty"]]]], result)

        @builtins.property
        def port_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.PortConfigurationProperty"]]:
            '''A set of ports that allow access to the container from external users.

            Processes running in the container can bind to a one of these ports. Container ports aren't directly accessed by inbound traffic. Amazon GameLift Servers maps these container ports to externally accessible connection ports, which are assigned as needed from the container fleet's ``ConnectionPortRange`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition.html#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-portconfiguration
            '''
            result = self._values.get("port_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.PortConfigurationProperty"]], result)

        @builtins.property
        def resolved_image_digest(self) -> typing.Optional[builtins.str]:
            '''A unique and immutable identifier for the container image.

            The digest is a SHA 256 hash of the container image manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition.html#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-resolvedimagedigest
            '''
            result = self._values.get("resolved_image_digest")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vcpu(self) -> typing.Optional[jsii.Number]:
            '''The number of vCPU units that are reserved for the container.

            If no resources are reserved, the container shares the total vCPU limit for the container group.

            *Related data type:* `ContainerGroupDefinition TotalVcpuLimit <https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-supportcontainerdefinition.html#cfn-gamelift-containergroupdefinition-supportcontainerdefinition-vcpu
            '''
            result = self._values.get("vcpu")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SupportContainerDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "operating_system": "operatingSystem",
        "total_memory_limit_mebibytes": "totalMemoryLimitMebibytes",
        "total_vcpu_limit": "totalVcpuLimit",
        "container_group_type": "containerGroupType",
        "game_server_container_definition": "gameServerContainerDefinition",
        "source_version_number": "sourceVersionNumber",
        "support_container_definitions": "supportContainerDefinitions",
        "tags": "tags",
        "version_description": "versionDescription",
    },
)
class CfnContainerGroupDefinitionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        operating_system: builtins.str,
        total_memory_limit_mebibytes: jsii.Number,
        total_vcpu_limit: jsii.Number,
        container_group_type: typing.Optional[builtins.str] = None,
        game_server_container_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.GameServerContainerDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        source_version_number: typing.Optional[jsii.Number] = None,
        support_container_definitions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.SupportContainerDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        version_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnContainerGroupDefinition``.

        :param name: A descriptive identifier for the container group definition. The name value is unique in an AWS Region.
        :param operating_system: The platform that all containers in the container group definition run on. .. epigraph:: Amazon Linux 2 (AL2) will reach end of support on 6/30/2025. See more details in the `Amazon Linux 2 FAQs <https://docs.aws.amazon.com/amazon-linux-2/faqs/>`_ . For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See `Migrate to server SDK version 5. <https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html>`_
        :param total_memory_limit_mebibytes: The amount of memory (in MiB) on a fleet instance to allocate for the container group. All containers in the group share these resources. You can set a limit for each container definition in the group. If individual containers have limits, this total value must be greater than any individual container's memory limit.
        :param total_vcpu_limit: The amount of vCPU units on a fleet instance to allocate for the container group (1 vCPU is equal to 1024 CPU units). All containers in the group share these resources. You can set a limit for each container definition in the group. If individual containers have limits, this total value must be equal to or greater than the sum of the limits for each container in the group.
        :param container_group_type: The type of container group. Container group type determines how Amazon GameLift Servers deploys the container group on each fleet instance.
        :param game_server_container_definition: The definition for the game server container in this group. This property is used only when the container group type is ``GAME_SERVER`` . This container definition specifies a container image with the game server build.
        :param source_version_number: A specific ContainerGroupDefinition version to be updated.
        :param support_container_definitions: The set of definitions for support containers in this group. A container group definition might have zero support container definitions. Support container can be used in any type of container group.
        :param tags: An array of key-value pairs to apply to this resource.
        :param version_description: An optional description that was provided for a container group definition update. Each version can have a unique description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_container_group_definition_props = gamelift.CfnContainerGroupDefinitionProps(
                name="name",
                operating_system="operatingSystem",
                total_memory_limit_mebibytes=123,
                total_vcpu_limit=123,
            
                # the properties below are optional
                container_group_type="containerGroupType",
                game_server_container_definition=gamelift.CfnContainerGroupDefinition.GameServerContainerDefinitionProperty(
                    container_name="containerName",
                    image_uri="imageUri",
                    server_sdk_version="serverSdkVersion",
            
                    # the properties below are optional
                    depends_on=[gamelift.CfnContainerGroupDefinition.ContainerDependencyProperty(
                        condition="condition",
                        container_name="containerName"
                    )],
                    environment_override=[gamelift.CfnContainerGroupDefinition.ContainerEnvironmentProperty(
                        name="name",
                        value="value"
                    )],
                    mount_points=[gamelift.CfnContainerGroupDefinition.ContainerMountPointProperty(
                        instance_path="instancePath",
            
                        # the properties below are optional
                        access_level="accessLevel",
                        container_path="containerPath"
                    )],
                    port_configuration=gamelift.CfnContainerGroupDefinition.PortConfigurationProperty(
                        container_port_ranges=[gamelift.CfnContainerGroupDefinition.ContainerPortRangeProperty(
                            from_port=123,
                            protocol="protocol",
                            to_port=123
                        )]
                    ),
                    resolved_image_digest="resolvedImageDigest"
                ),
                source_version_number=123,
                support_container_definitions=[gamelift.CfnContainerGroupDefinition.SupportContainerDefinitionProperty(
                    container_name="containerName",
                    image_uri="imageUri",
            
                    # the properties below are optional
                    depends_on=[gamelift.CfnContainerGroupDefinition.ContainerDependencyProperty(
                        condition="condition",
                        container_name="containerName"
                    )],
                    environment_override=[gamelift.CfnContainerGroupDefinition.ContainerEnvironmentProperty(
                        name="name",
                        value="value"
                    )],
                    essential=False,
                    health_check=gamelift.CfnContainerGroupDefinition.ContainerHealthCheckProperty(
                        command=["command"],
            
                        # the properties below are optional
                        interval=123,
                        retries=123,
                        start_period=123,
                        timeout=123
                    ),
                    memory_hard_limit_mebibytes=123,
                    mount_points=[gamelift.CfnContainerGroupDefinition.ContainerMountPointProperty(
                        instance_path="instancePath",
            
                        # the properties below are optional
                        access_level="accessLevel",
                        container_path="containerPath"
                    )],
                    port_configuration=gamelift.CfnContainerGroupDefinition.PortConfigurationProperty(
                        container_port_ranges=[gamelift.CfnContainerGroupDefinition.ContainerPortRangeProperty(
                            from_port=123,
                            protocol="protocol",
                            to_port=123
                        )]
                    ),
                    resolved_image_digest="resolvedImageDigest",
                    vcpu=123
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                version_description="versionDescription"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b760a12182b9da0a53204aa5510dae28c2cda4c4fba1ef77f0245093da04ea4)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument operating_system", value=operating_system, expected_type=type_hints["operating_system"])
            check_type(argname="argument total_memory_limit_mebibytes", value=total_memory_limit_mebibytes, expected_type=type_hints["total_memory_limit_mebibytes"])
            check_type(argname="argument total_vcpu_limit", value=total_vcpu_limit, expected_type=type_hints["total_vcpu_limit"])
            check_type(argname="argument container_group_type", value=container_group_type, expected_type=type_hints["container_group_type"])
            check_type(argname="argument game_server_container_definition", value=game_server_container_definition, expected_type=type_hints["game_server_container_definition"])
            check_type(argname="argument source_version_number", value=source_version_number, expected_type=type_hints["source_version_number"])
            check_type(argname="argument support_container_definitions", value=support_container_definitions, expected_type=type_hints["support_container_definitions"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument version_description", value=version_description, expected_type=type_hints["version_description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "operating_system": operating_system,
            "total_memory_limit_mebibytes": total_memory_limit_mebibytes,
            "total_vcpu_limit": total_vcpu_limit,
        }
        if container_group_type is not None:
            self._values["container_group_type"] = container_group_type
        if game_server_container_definition is not None:
            self._values["game_server_container_definition"] = game_server_container_definition
        if source_version_number is not None:
            self._values["source_version_number"] = source_version_number
        if support_container_definitions is not None:
            self._values["support_container_definitions"] = support_container_definitions
        if tags is not None:
            self._values["tags"] = tags
        if version_description is not None:
            self._values["version_description"] = version_description

    @builtins.property
    def name(self) -> builtins.str:
        '''A descriptive identifier for the container group definition.

        The name value is unique in an AWS Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operating_system(self) -> builtins.str:
        '''The platform that all containers in the container group definition run on.

        .. epigraph::

           Amazon Linux 2 (AL2) will reach end of support on 6/30/2025. See more details in the `Amazon Linux 2 FAQs <https://docs.aws.amazon.com/amazon-linux-2/faqs/>`_ . For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See `Migrate to server SDK version 5. <https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-operatingsystem
        '''
        result = self._values.get("operating_system")
        assert result is not None, "Required property 'operating_system' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def total_memory_limit_mebibytes(self) -> jsii.Number:
        '''The amount of memory (in MiB) on a fleet instance to allocate for the container group.

        All containers in the group share these resources.

        You can set a limit for each container definition in the group. If individual containers have limits, this total value must be greater than any individual container's memory limit.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-totalmemorylimitmebibytes
        '''
        result = self._values.get("total_memory_limit_mebibytes")
        assert result is not None, "Required property 'total_memory_limit_mebibytes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def total_vcpu_limit(self) -> jsii.Number:
        '''The amount of vCPU units on a fleet instance to allocate for the container group (1 vCPU is equal to 1024 CPU units).

        All containers in the group share these resources. You can set a limit for each container definition in the group. If individual containers have limits, this total value must be equal to or greater than the sum of the limits for each container in the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-totalvcpulimit
        '''
        result = self._values.get("total_vcpu_limit")
        assert result is not None, "Required property 'total_vcpu_limit' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def container_group_type(self) -> typing.Optional[builtins.str]:
        '''The type of container group.

        Container group type determines how Amazon GameLift Servers deploys the container group on each fleet instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-containergrouptype
        '''
        result = self._values.get("container_group_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def game_server_container_definition(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerGroupDefinition.GameServerContainerDefinitionProperty]]:
        '''The definition for the game server container in this group.

        This property is used only when the container group type is ``GAME_SERVER`` . This container definition specifies a container image with the game server build.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-gameservercontainerdefinition
        '''
        result = self._values.get("game_server_container_definition")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerGroupDefinition.GameServerContainerDefinitionProperty]], result)

    @builtins.property
    def source_version_number(self) -> typing.Optional[jsii.Number]:
        '''A specific ContainerGroupDefinition version to be updated.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-sourceversionnumber
        '''
        result = self._values.get("source_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def support_container_definitions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerGroupDefinition.SupportContainerDefinitionProperty]]]]:
        '''The set of definitions for support containers in this group.

        A container group definition might have zero support container definitions. Support container can be used in any type of container group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-supportcontainerdefinitions
        '''
        result = self._values.get("support_container_definitions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerGroupDefinition.SupportContainerDefinitionProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def version_description(self) -> typing.Optional[builtins.str]:
        '''An optional description that was provided for a container group definition update.

        Each version can have a unique description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-versiondescription
        '''
        result = self._values.get("version_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContainerGroupDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnFleet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet",
):
    '''The ``AWS::GameLift::Fleet`` resource creates an Amazon GameLift (GameLift) fleet to host custom game server or Realtime Servers.

    A fleet is a set of EC2 instances, configured with instructions to run game servers on each instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html
    :cloudformationResource: AWS::GameLift::Fleet
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_fleet = gamelift.CfnFleet(self, "MyCfnFleet",
            name="name",
        
            # the properties below are optional
            anywhere_configuration=gamelift.CfnFleet.AnywhereConfigurationProperty(
                cost="cost"
            ),
            apply_capacity="applyCapacity",
            build_id="buildId",
            certificate_configuration=gamelift.CfnFleet.CertificateConfigurationProperty(
                certificate_type="certificateType"
            ),
            compute_type="computeType",
            description="description",
            desired_ec2_instances=123,
            ec2_inbound_permissions=[gamelift.CfnFleet.IpPermissionProperty(
                from_port=123,
                ip_range="ipRange",
                protocol="protocol",
                to_port=123
            )],
            ec2_instance_type="ec2InstanceType",
            fleet_type="fleetType",
            instance_role_arn="instanceRoleArn",
            instance_role_credentials_provider="instanceRoleCredentialsProvider",
            locations=[gamelift.CfnFleet.LocationConfigurationProperty(
                location="location",
        
                # the properties below are optional
                location_capacity=gamelift.CfnFleet.LocationCapacityProperty(
                    desired_ec2_instances=123,
                    max_size=123,
                    min_size=123
                )
            )],
            log_paths=["logPaths"],
            max_size=123,
            metric_groups=["metricGroups"],
            min_size=123,
            new_game_session_protection_policy="newGameSessionProtectionPolicy",
            peer_vpc_aws_account_id="peerVpcAwsAccountId",
            peer_vpc_id="peerVpcId",
            resource_creation_limit_policy=gamelift.CfnFleet.ResourceCreationLimitPolicyProperty(
                new_game_sessions_per_creator=123,
                policy_period_in_minutes=123
            ),
            runtime_configuration=gamelift.CfnFleet.RuntimeConfigurationProperty(
                game_session_activation_timeout_seconds=123,
                max_concurrent_game_session_activations=123,
                server_processes=[gamelift.CfnFleet.ServerProcessProperty(
                    concurrent_executions=123,
                    launch_path="launchPath",
        
                    # the properties below are optional
                    parameters="parameters"
                )]
            ),
            scaling_policies=[gamelift.CfnFleet.ScalingPolicyProperty(
                metric_name="metricName",
                name="name",
        
                # the properties below are optional
                comparison_operator="comparisonOperator",
                evaluation_periods=123,
                location="location",
                policy_type="policyType",
                scaling_adjustment=123,
                scaling_adjustment_type="scalingAdjustmentType",
                status="status",
                target_configuration=gamelift.CfnFleet.TargetConfigurationProperty(
                    target_value=123
                ),
                threshold=123,
                update_status="updateStatus"
            )],
            script_id="scriptId",
            server_launch_parameters="serverLaunchParameters",
            server_launch_path="serverLaunchPath",
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
        anywhere_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.AnywhereConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        apply_capacity: typing.Optional[builtins.str] = None,
        build_id: typing.Optional[builtins.str] = None,
        certificate_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.CertificateConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        compute_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        desired_ec2_instances: typing.Optional[jsii.Number] = None,
        ec2_inbound_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.IpPermissionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ec2_instance_type: typing.Optional[builtins.str] = None,
        fleet_type: typing.Optional[builtins.str] = None,
        instance_role_arn: typing.Optional[builtins.str] = None,
        instance_role_credentials_provider: typing.Optional[builtins.str] = None,
        locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.LocationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        log_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        metric_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        min_size: typing.Optional[jsii.Number] = None,
        new_game_session_protection_policy: typing.Optional[builtins.str] = None,
        peer_vpc_aws_account_id: typing.Optional[builtins.str] = None,
        peer_vpc_id: typing.Optional[builtins.str] = None,
        resource_creation_limit_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.ResourceCreationLimitPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        runtime_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.RuntimeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        scaling_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.ScalingPolicyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        script_id: typing.Optional[builtins.str] = None,
        server_launch_parameters: typing.Optional[builtins.str] = None,
        server_launch_path: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
        :param anywhere_configuration: Amazon GameLift Servers Anywhere configuration options.
        :param apply_capacity: Current resource capacity settings for managed EC2 fleets and managed container fleets. For multi-location fleets, location values might refer to a fleet's remote location or its home Region. *Returned by:* `DescribeFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html>`_ , `DescribeFleetLocationCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html>`_ , `UpdateFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html>`_
        :param build_id: A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a ``READY`` status. This fleet setting cannot be changed once the fleet is created.
        :param certificate_configuration: Prompts Amazon GameLift Servers to generate a TLS/SSL certificate for the fleet. Amazon GameLift Servers uses the certificates to encrypt traffic between game clients and the game servers running on Amazon GameLift Servers. By default, the ``CertificateConfiguration`` is ``DISABLED`` . You can't change this property after you create the fleet. AWS Certificate Manager (ACM) certificates expire after 13 months. Certificate expiration can cause fleets to fail, preventing players from connecting to instances in the fleet. We recommend you replace fleets before 13 months, consider using fleet aliases for a smooth transition. .. epigraph:: ACM isn't available in all AWS regions. A fleet creation request with certificate generation enabled in an unsupported Region, fails with a 4xx error. For more information about the supported Regions, see `Supported Regions <https://docs.aws.amazon.com/acm/latest/userguide/acm-regions.html>`_ in the *AWS Certificate Manager User Guide* .
        :param compute_type: The type of compute resource used to host your game servers. - ``EC2`` – The game server build is deployed to Amazon EC2 instances for cloud hosting. This is the default setting. - ``ANYWHERE`` – Game servers and supporting software are deployed to compute resources that you provide and manage. With this compute type, you can also set the ``AnywhereConfiguration`` parameter.
        :param description: A description for the fleet.
        :param desired_ec2_instances: (deprecated) [DEPRECATED] The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.
        :param ec2_inbound_permissions: The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet. Set this parameter for managed EC2 fleets. You can leave this parameter empty when creating the fleet, but you must call ` <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetPortSettings>`_ to set it before players can connect to game sessions. As a best practice, we recommend opening ports for remote access only when you need them and closing them when you're finished. For Amazon GameLift Servers Realtime fleets, Amazon GameLift Servers automatically sets TCP and UDP ranges.
        :param ec2_instance_type: The Amazon GameLift Servers-supported Amazon EC2 instance type to use with managed EC2 fleets. Instance type determines the computing resources that will be used to host your game servers, including CPU, memory, storage, and networking capacity. See `Amazon Elastic Compute Cloud Instance Types <https://docs.aws.amazon.com/ec2/instance-types/>`_ for detailed descriptions of Amazon EC2 instance types.
        :param fleet_type: Indicates whether to use On-Demand or Spot instances for this fleet. By default, this property is set to ``ON_DEMAND`` . Learn more about when to use `On-Demand versus Spot Instances <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot>`_ . This fleet property can't be changed after the fleet is created.
        :param instance_role_arn: A unique identifier for an IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN by using the `IAM dashboard <https://docs.aws.amazon.com/iam/>`_ in the AWS Management Console . Learn more about using on-box credentials for your game servers at `Access external resources from a game server <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`_ . This attribute is used with fleets where ``ComputeType`` is ``EC2`` .
        :param instance_role_credentials_provider: Indicates that fleet instances maintain a shared credentials file for the IAM role defined in ``InstanceRoleArn`` . Shared credentials allow applications that are deployed with the game server executable to communicate with other AWS resources. This property is used only when the game server is integrated with the server SDK version 5.x. For more information about using shared credentials, see `Communicate with other AWS resources from your fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`_ . This attribute is used with fleets where ``ComputeType`` is ``EC2`` .
        :param locations: A set of remote locations to deploy additional instances to and manage as a multi-location fleet. Use this parameter when creating a fleet in AWS Regions that support multiple locations. You can add any AWS Region or Local Zone that's supported by Amazon GameLift Servers. Provide a list of one or more AWS Region codes, such as ``us-west-2`` , or Local Zone names. When using this parameter, Amazon GameLift Servers requires you to include your home location in the request. For a list of supported Regions and Local Zones, see `Amazon GameLift Servers service locations <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html>`_ for managed hosting.
        :param log_paths: (deprecated) This parameter is no longer used. When hosting a custom game build, specify where Amazon GameLift should store log files using the Amazon GameLift server API call ProcessReady()
        :param max_size: (deprecated) [DEPRECATED] The maximum value that is allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "1". Once the fleet is active, you can change this value.
        :param metric_groups: The name of an AWS CloudWatch metric group to add this fleet to. A metric group is used to aggregate the metrics for multiple fleets. You can specify an existing metric group name or set a new name to create a new metric group. A fleet can be included in only one metric group at a time.
        :param min_size: (deprecated) [DEPRECATED] The minimum value allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "0". After the fleet is active, you can change this value.
        :param new_game_session_protection_policy: The status of termination protection for active game sessions on the fleet. By default, this property is set to ``NoProtection`` . - *NoProtection* - Game sessions can be terminated during active gameplay as a result of a scale-down event. - *FullProtection* - Game sessions in ``ACTIVE`` status cannot be terminated during a scale-down event.
        :param peer_vpc_aws_account_id: Used when peering your Amazon GameLift Servers fleet with a VPC, the unique identifier for the AWS account that owns the VPC. You can find your account ID in the AWS Management Console under account settings.
        :param peer_vpc_id: A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the `VPC Dashboard <https://docs.aws.amazon.com/vpc/>`_ in the AWS Management Console . Learn more about VPC peering in `VPC Peering with Amazon GameLift Servers Fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html>`_ .
        :param resource_creation_limit_policy: A policy that limits the number of game sessions that an individual player can create on instances in this fleet within a specified span of time.
        :param runtime_configuration: Instructions for how to launch and maintain server processes on instances in the fleet. The runtime configuration defines one or more server process configurations, each identifying a build executable or Realtime script file and the number of processes of that type to run concurrently. .. epigraph:: The ``RuntimeConfiguration`` parameter is required unless the fleet is being configured using the older parameters ``ServerLaunchPath`` and ``ServerLaunchParameters`` , which are still supported for backward compatibility.
        :param scaling_policies: Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the combination of name and fleet ID.
        :param script_id: The unique identifier for a Realtime configuration script to be deployed on fleet instances. You can use either the script ID or ARN. Scripts must be uploaded to Amazon GameLift Servers prior to creating the fleet. This fleet property cannot be changed later. .. epigraph:: You can't use the ``!Ref`` command to reference a script created with a CloudFormation template for the fleet property ``ScriptId`` . Instead, use ``Fn::GetAtt Script.Arn`` or ``Fn::GetAtt Script.Id`` to retrieve either of these properties as input for ``ScriptId`` . Alternatively, enter a ``ScriptId`` string manually.
        :param server_launch_parameters: (deprecated) This parameter is no longer used but is retained for backward compatibility. Instead, specify server launch parameters in the RuntimeConfiguration parameter. A request must specify either a runtime configuration or values for both ServerLaunchParameters and ServerLaunchPath.
        :param server_launch_path: (deprecated) This parameter is no longer used. Instead, specify a server launch path using the RuntimeConfiguration parameter. Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21fe09a90444788b3c862f454214d4e160757c9b02d0598d282f68b7f79d749f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFleetProps(
            name=name,
            anywhere_configuration=anywhere_configuration,
            apply_capacity=apply_capacity,
            build_id=build_id,
            certificate_configuration=certificate_configuration,
            compute_type=compute_type,
            description=description,
            desired_ec2_instances=desired_ec2_instances,
            ec2_inbound_permissions=ec2_inbound_permissions,
            ec2_instance_type=ec2_instance_type,
            fleet_type=fleet_type,
            instance_role_arn=instance_role_arn,
            instance_role_credentials_provider=instance_role_credentials_provider,
            locations=locations,
            log_paths=log_paths,
            max_size=max_size,
            metric_groups=metric_groups,
            min_size=min_size,
            new_game_session_protection_policy=new_game_session_protection_policy,
            peer_vpc_aws_account_id=peer_vpc_aws_account_id,
            peer_vpc_id=peer_vpc_id,
            resource_creation_limit_policy=resource_creation_limit_policy,
            runtime_configuration=runtime_configuration,
            scaling_policies=scaling_policies,
            script_id=script_id,
            server_launch_parameters=server_launch_parameters,
            server_launch_path=server_launch_path,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__264e19b1dd38619175091751b1eec860e08c2225c7798789a29ec89ab8971593)
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
            type_hints = typing.get_type_hints(_typecheckingstub__905cca04e4d534db21b7356373856ed4d0fb9130ab18a34d31eb7127b3ecdbc1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrFleetArn")
    def attr_fleet_arn(self) -> builtins.str:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is ``arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`` . In a GameLift fleet ARN, the resource ID matches the ``FleetId`` value.

        :cloudformationAttribute: FleetArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFleetArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFleetId")
    def attr_fleet_id(self) -> builtins.str:
        '''A unique identifier for the fleet.

        :cloudformationAttribute: FleetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFleetId"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A descriptive label that is associated with a fleet.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd3e6bf68da3a08ee0a6dbdff6b571a1a9348dfd6d1f15864e1efd85595ae689)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="anywhereConfiguration")
    def anywhere_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.AnywhereConfigurationProperty"]]:
        '''Amazon GameLift Servers Anywhere configuration options.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.AnywhereConfigurationProperty"]], jsii.get(self, "anywhereConfiguration"))

    @anywhere_configuration.setter
    def anywhere_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.AnywhereConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc575abdd043760dd1cbe4178328d65df4b96ee18072484d24bd88d2e2d340ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anywhereConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="applyCapacity")
    def apply_capacity(self) -> typing.Optional[builtins.str]:
        '''Current resource capacity settings for managed EC2 fleets and managed container fleets.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applyCapacity"))

    @apply_capacity.setter
    def apply_capacity(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e4da24e64fdcbb7830d9e09a27219d611e9c486d09dd2a970381192b5e97213)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyCapacity", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="buildId")
    def build_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for a build to be deployed on the new fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildId"))

    @build_id.setter
    def build_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fecb16629d96a3f0b5b4acdf8ba4a4b1a44a9314ada24ee4bf29122c11df18e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="certificateConfiguration")
    def certificate_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.CertificateConfigurationProperty"]]:
        '''Prompts Amazon GameLift Servers to generate a TLS/SSL certificate for the fleet.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.CertificateConfigurationProperty"]], jsii.get(self, "certificateConfiguration"))

    @certificate_configuration.setter
    def certificate_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.CertificateConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f46d27389fd45eb3384977842c4289c60e5795c4a4bd6e08002ec26643232bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="computeType")
    def compute_type(self) -> typing.Optional[builtins.str]:
        '''The type of compute resource used to host your game servers.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computeType"))

    @compute_type.setter
    def compute_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__022e8bf70858e61cedf1ac2f0bbe1af01706924dda3af7f4e655e78c1b5985db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eec78595476346beb2b42a6ac89d6890fb357c8bc49fbafff985bc1417bca206)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="desiredEc2Instances")
    def desired_ec2_instances(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) [DEPRECATED] The number of EC2 instances that you want this fleet to host.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredEc2Instances"))

    @desired_ec2_instances.setter
    def desired_ec2_instances(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4941614413c1e1554010809926c621b6030f9b38418b19c26a4dbbfc56fd9cfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredEc2Instances", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ec2InboundPermissions")
    def ec2_inbound_permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.IpPermissionProperty"]]]]:
        '''The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.IpPermissionProperty"]]]], jsii.get(self, "ec2InboundPermissions"))

    @ec2_inbound_permissions.setter
    def ec2_inbound_permissions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.IpPermissionProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d84bfe64c88748026f1ea76b00a3c1eeeffe26c5a9e7df3f052f9069032249c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2InboundPermissions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ec2InstanceType")
    def ec2_instance_type(self) -> typing.Optional[builtins.str]:
        '''The Amazon GameLift Servers-supported Amazon EC2 instance type to use with managed EC2 fleets.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2InstanceType"))

    @ec2_instance_type.setter
    def ec2_instance_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5edb81bb6e5f986aaa8654e60493e7ec0e42f57ed43a7481b48714433fb0b95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2InstanceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fleetType")
    def fleet_type(self) -> typing.Optional[builtins.str]:
        '''Indicates whether to use On-Demand or Spot instances for this fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fleetType"))

    @fleet_type.setter
    def fleet_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc9a52bd70aa79d8d459ba6e23d2020447c1f1d4faa157c8836aad4e87181d56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fleetType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="instanceRoleArn")
    def instance_role_arn(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for an IAM role that manages access to your AWS services.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceRoleArn"))

    @instance_role_arn.setter
    def instance_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7947f4ea6b160028fb5bbf20fcbd0cc9eb46ba122d737f3c792a6be5043d8577)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="instanceRoleCredentialsProvider")
    def instance_role_credentials_provider(self) -> typing.Optional[builtins.str]:
        '''Indicates that fleet instances maintain a shared credentials file for the IAM role defined in ``InstanceRoleArn`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceRoleCredentialsProvider"))

    @instance_role_credentials_provider.setter
    def instance_role_credentials_provider(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6765d7366d76df2864c4535568d1edf808ceec869046e302b0c842674b46c102)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceRoleCredentialsProvider", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="locations")
    def locations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.LocationConfigurationProperty"]]]]:
        '''A set of remote locations to deploy additional instances to and manage as a multi-location fleet.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.LocationConfigurationProperty"]]]], jsii.get(self, "locations"))

    @locations.setter
    def locations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.LocationConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1377dfdecc90d2457b2fe3e90aa35cecb44bf218eb1836fc28cbc15b7a4812f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logPaths")
    def log_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(deprecated) This parameter is no longer used.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "logPaths"))

    @log_paths.setter
    def log_paths(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35b29d2e11870cd4d0ea412c5de5d02fbb8bb765ed67873227f57868f234fe52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logPaths", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) [DEPRECATED] The maximum value that is allowed for the fleet's instance count.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSize"))

    @max_size.setter
    def max_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbc74cb38ce8a622308c22d16cb5fe99f9f601acdfd26460b9b33bd15037e42f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSize", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="metricGroups")
    def metric_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name of an AWS CloudWatch metric group to add this fleet to.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "metricGroups"))

    @metric_groups.setter
    def metric_groups(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02facc74087efba3bcf2b21fc12cd9fae063e33440abacb0fdfdf65ecb3fe7ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricGroups", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) [DEPRECATED] The minimum value allowed for the fleet's instance count.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d460bc2f634afc1e2c222819f53ddf45b2647b9ccf197380a1419dfb4b91c61a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSize", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="newGameSessionProtectionPolicy")
    def new_game_session_protection_policy(self) -> typing.Optional[builtins.str]:
        '''The status of termination protection for active game sessions on the fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "newGameSessionProtectionPolicy"))

    @new_game_session_protection_policy.setter
    def new_game_session_protection_policy(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c8b79569fe310aaed26b6fa78159b7101d72974e478dd380ca0713aea1d9a9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "newGameSessionProtectionPolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="peerVpcAwsAccountId")
    def peer_vpc_aws_account_id(self) -> typing.Optional[builtins.str]:
        '''Used when peering your Amazon GameLift Servers fleet with a VPC, the unique identifier for the AWS account that owns the VPC.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerVpcAwsAccountId"))

    @peer_vpc_aws_account_id.setter
    def peer_vpc_aws_account_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a648f419a89a6e5926858e8481241ede65ca343e3b797aecd480dec6c8b20939)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerVpcAwsAccountId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="peerVpcId")
    def peer_vpc_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerVpcId"))

    @peer_vpc_id.setter
    def peer_vpc_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fd0ab83e874e8110a1f4093ff1e48395bf94729c8f475c6e23b4d22971f3428)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerVpcId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceCreationLimitPolicy")
    def resource_creation_limit_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.ResourceCreationLimitPolicyProperty"]]:
        '''A policy that limits the number of game sessions that an individual player can create on instances in this fleet within a specified span of time.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.ResourceCreationLimitPolicyProperty"]], jsii.get(self, "resourceCreationLimitPolicy"))

    @resource_creation_limit_policy.setter
    def resource_creation_limit_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.ResourceCreationLimitPolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21ee8415ef994fb87ac2edf852ffd98a21384f9eccc26d3a0537563c2b00fbed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceCreationLimitPolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="runtimeConfiguration")
    def runtime_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.RuntimeConfigurationProperty"]]:
        '''Instructions for how to launch and maintain server processes on instances in the fleet.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.RuntimeConfigurationProperty"]], jsii.get(self, "runtimeConfiguration"))

    @runtime_configuration.setter
    def runtime_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.RuntimeConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91bbc8eaa0f72d2032ef5cfd51906c5fc923f7ed24ede99b907cb24fe23da499)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scalingPolicies")
    def scaling_policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.ScalingPolicyProperty"]]]]:
        '''Rule that controls how a fleet is scaled.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.ScalingPolicyProperty"]]]], jsii.get(self, "scalingPolicies"))

    @scaling_policies.setter
    def scaling_policies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.ScalingPolicyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__082c3456142a6049adc9dd4639e8b2ca94a21dbf9412cc70d0ea2e1babccf7c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalingPolicies", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scriptId")
    def script_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier for a Realtime configuration script to be deployed on fleet instances.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scriptId"))

    @script_id.setter
    def script_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d89c92d80f54ea7b8f3b7a14762b9c71a927d074d3727f05bc330349648ba92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scriptId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serverLaunchParameters")
    def server_launch_parameters(self) -> typing.Optional[builtins.str]:
        '''(deprecated) This parameter is no longer used but is retained for backward compatibility.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverLaunchParameters"))

    @server_launch_parameters.setter
    def server_launch_parameters(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b86e485f6c758ba0a09838614ee6f5e63a4ba69e6100fd77af039cc9f223b152)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverLaunchParameters", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serverLaunchPath")
    def server_launch_path(self) -> typing.Optional[builtins.str]:
        '''(deprecated) This parameter is no longer used.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverLaunchPath"))

    @server_launch_path.setter
    def server_launch_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63d5bf96be81c4a6b00ef1deb4d8846acf0053313fb89efd0ded1f0931c66844)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverLaunchPath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27ef86cf1bf34b50ec355a45305857c52751912f8408dec34a63b8a26665856d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.AnywhereConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"cost": "cost"},
    )
    class AnywhereConfigurationProperty:
        def __init__(self, *, cost: builtins.str) -> None:
            '''Amazon GameLift Servers configuration options for your Anywhere fleets.

            :param cost: The cost to run your fleet per hour. Amazon GameLift Servers uses the provided cost of your fleet to balance usage in queues. For more information about queues, see `Setting up queues <https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html>`_ in the *Amazon GameLift Servers Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-anywhereconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                anywhere_configuration_property = gamelift.CfnFleet.AnywhereConfigurationProperty(
                    cost="cost"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3897ffc82938e5bf4e6384b3a83b22f50c7189a71eb0fc30ea8f17642db5ef9)
                check_type(argname="argument cost", value=cost, expected_type=type_hints["cost"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cost": cost,
            }

        @builtins.property
        def cost(self) -> builtins.str:
            '''The cost to run your fleet per hour.

            Amazon GameLift Servers uses the provided cost of your fleet to balance usage in queues. For more information about queues, see `Setting up queues <https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html>`_ in the *Amazon GameLift Servers Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-anywhereconfiguration.html#cfn-gamelift-fleet-anywhereconfiguration-cost
            '''
            result = self._values.get("cost")
            assert result is not None, "Required property 'cost' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnywhereConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.CertificateConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"certificate_type": "certificateType"},
    )
    class CertificateConfigurationProperty:
        def __init__(self, *, certificate_type: builtins.str) -> None:
            '''Determines whether a TLS/SSL certificate is generated for a fleet.

            This feature must be enabled when creating the fleet. All instances in a fleet share the same certificate. The certificate can be retrieved by calling the `GameLift Server SDK <https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk.html>`_ operation ``GetInstanceCertificate`` .

            :param certificate_type: Indicates whether a TLS/SSL certificate is generated for a fleet. Valid values include: - *GENERATED* - Generate a TLS/SSL certificate for this fleet. - *DISABLED* - (default) Do not generate a TLS/SSL certificate for this fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-certificateconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                certificate_configuration_property = gamelift.CfnFleet.CertificateConfigurationProperty(
                    certificate_type="certificateType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4c3cca5919f32f3e2cb6c385afda08bf3b194b8baf60b4d20e5f9f580659cc84)
                check_type(argname="argument certificate_type", value=certificate_type, expected_type=type_hints["certificate_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "certificate_type": certificate_type,
            }

        @builtins.property
        def certificate_type(self) -> builtins.str:
            '''Indicates whether a TLS/SSL certificate is generated for a fleet.

            Valid values include:

            - *GENERATED* - Generate a TLS/SSL certificate for this fleet.
            - *DISABLED* - (default) Do not generate a TLS/SSL certificate for this fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-certificateconfiguration.html#cfn-gamelift-fleet-certificateconfiguration-certificatetype
            '''
            result = self._values.get("certificate_type")
            assert result is not None, "Required property 'certificate_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CertificateConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.IpPermissionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "from_port": "fromPort",
            "ip_range": "ipRange",
            "protocol": "protocol",
            "to_port": "toPort",
        },
    )
    class IpPermissionProperty:
        def __init__(
            self,
            *,
            from_port: jsii.Number,
            ip_range: builtins.str,
            protocol: builtins.str,
            to_port: jsii.Number,
        ) -> None:
            '''A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an instance in a fleet.

            New game sessions are assigned an IP address/port number combination, which must fall into the fleet's allowed ranges. Fleets with custom game builds must have permissions explicitly set. For Realtime Servers fleets, GameLift automatically opens two port ranges, one for TCP messaging and one for UDP.

            :param from_port: A starting value for a range of allowed port numbers. For fleets using Linux builds, only ports ``22`` and ``1026-60000`` are valid. For fleets using Windows builds, only ports ``1026-60000`` are valid.
            :param ip_range: A range of allowed IP addresses. This value must be expressed in CIDR notation. Example: " ``000.000.000.000/[subnet mask]`` " or optionally the shortened version " ``0.0.0.0/[subnet mask]`` ".
            :param protocol: The network communication protocol used by the fleet.
            :param to_port: An ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than ``FromPort`` . For fleets using Linux builds, only ports ``22`` and ``1026-60000`` are valid. For fleets using Windows builds, only ports ``1026-60000`` are valid.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ippermission.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                ip_permission_property = gamelift.CfnFleet.IpPermissionProperty(
                    from_port=123,
                    ip_range="ipRange",
                    protocol="protocol",
                    to_port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__70f885be25c9084dbab3b02a36601be0e37c43ab741ea7dd646494423839333a)
                check_type(argname="argument from_port", value=from_port, expected_type=type_hints["from_port"])
                check_type(argname="argument ip_range", value=ip_range, expected_type=type_hints["ip_range"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument to_port", value=to_port, expected_type=type_hints["to_port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "from_port": from_port,
                "ip_range": ip_range,
                "protocol": protocol,
                "to_port": to_port,
            }

        @builtins.property
        def from_port(self) -> jsii.Number:
            '''A starting value for a range of allowed port numbers.

            For fleets using Linux builds, only ports ``22`` and ``1026-60000`` are valid.

            For fleets using Windows builds, only ports ``1026-60000`` are valid.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ippermission.html#cfn-gamelift-fleet-ippermission-fromport
            '''
            result = self._values.get("from_port")
            assert result is not None, "Required property 'from_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def ip_range(self) -> builtins.str:
            '''A range of allowed IP addresses.

            This value must be expressed in CIDR notation. Example: " ``000.000.000.000/[subnet mask]`` " or optionally the shortened version " ``0.0.0.0/[subnet mask]`` ".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ippermission.html#cfn-gamelift-fleet-ippermission-iprange
            '''
            result = self._values.get("ip_range")
            assert result is not None, "Required property 'ip_range' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''The network communication protocol used by the fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ippermission.html#cfn-gamelift-fleet-ippermission-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def to_port(self) -> jsii.Number:
            '''An ending value for a range of allowed port numbers.

            Port numbers are end-inclusive. This value must be equal to or greater than ``FromPort`` .

            For fleets using Linux builds, only ports ``22`` and ``1026-60000`` are valid.

            For fleets using Windows builds, only ports ``1026-60000`` are valid.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ippermission.html#cfn-gamelift-fleet-ippermission-toport
            '''
            result = self._values.get("to_port")
            assert result is not None, "Required property 'to_port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IpPermissionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.LocationCapacityProperty",
        jsii_struct_bases=[],
        name_mapping={
            "desired_ec2_instances": "desiredEc2Instances",
            "max_size": "maxSize",
            "min_size": "minSize",
        },
    )
    class LocationCapacityProperty:
        def __init__(
            self,
            *,
            desired_ec2_instances: jsii.Number,
            max_size: jsii.Number,
            min_size: jsii.Number,
        ) -> None:
            '''Current resource capacity settings for managed EC2 fleets and managed container fleets.

            For multi-location fleets, location values might refer to a fleet's remote location or its home Region.

            *Returned by:* `DescribeFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html>`_ , `DescribeFleetLocationCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html>`_ , `UpdateFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html>`_

            :param desired_ec2_instances: The number of Amazon EC2 instances you want to maintain in the specified fleet location. This value must fall between the minimum and maximum size limits. Changes in desired instance value can take up to 1 minute to be reflected when viewing the fleet's capacity settings.
            :param max_size: The maximum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 1.
            :param min_size: The minimum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 0.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationcapacity.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                location_capacity_property = gamelift.CfnFleet.LocationCapacityProperty(
                    desired_ec2_instances=123,
                    max_size=123,
                    min_size=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__76847ac983ab72ef92adc1b0579d769ca62af002ef71c76165cbd879da8645fc)
                check_type(argname="argument desired_ec2_instances", value=desired_ec2_instances, expected_type=type_hints["desired_ec2_instances"])
                check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
                check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "desired_ec2_instances": desired_ec2_instances,
                "max_size": max_size,
                "min_size": min_size,
            }

        @builtins.property
        def desired_ec2_instances(self) -> jsii.Number:
            '''The number of Amazon EC2 instances you want to maintain in the specified fleet location.

            This value must fall between the minimum and maximum size limits. Changes in desired instance value can take up to 1 minute to be reflected when viewing the fleet's capacity settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationcapacity.html#cfn-gamelift-fleet-locationcapacity-desiredec2instances
            '''
            result = self._values.get("desired_ec2_instances")
            assert result is not None, "Required property 'desired_ec2_instances' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max_size(self) -> jsii.Number:
            '''The maximum number of instances that are allowed in the specified fleet location.

            If this parameter is not set, the default is 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationcapacity.html#cfn-gamelift-fleet-locationcapacity-maxsize
            '''
            result = self._values.get("max_size")
            assert result is not None, "Required property 'max_size' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def min_size(self) -> jsii.Number:
            '''The minimum number of instances that are allowed in the specified fleet location.

            If this parameter is not set, the default is 0.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationcapacity.html#cfn-gamelift-fleet-locationcapacity-minsize
            '''
            result = self._values.get("min_size")
            assert result is not None, "Required property 'min_size' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationCapacityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.LocationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"location": "location", "location_capacity": "locationCapacity"},
    )
    class LocationConfigurationProperty:
        def __init__(
            self,
            *,
            location: builtins.str,
            location_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.LocationCapacityProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A remote location where a multi-location fleet can deploy game servers for game hosting.

            :param location: An AWS Region code, such as ``us-west-2`` . For a list of supported Regions and Local Zones, see `Amazon GameLift Servers service locations <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html>`_ for managed hosting.
            :param location_capacity: Current resource capacity settings for managed EC2 fleets and managed container fleets. For multi-location fleets, location values might refer to a fleet's remote location or its home Region. *Returned by:* `DescribeFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html>`_ , `DescribeFleetLocationCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html>`_ , `UpdateFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                location_configuration_property = gamelift.CfnFleet.LocationConfigurationProperty(
                    location="location",
                
                    # the properties below are optional
                    location_capacity=gamelift.CfnFleet.LocationCapacityProperty(
                        desired_ec2_instances=123,
                        max_size=123,
                        min_size=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__716ff23eda74da42620dc64832ed27ab5a267661bd90b16577ee48991436d14c)
                check_type(argname="argument location", value=location, expected_type=type_hints["location"])
                check_type(argname="argument location_capacity", value=location_capacity, expected_type=type_hints["location_capacity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "location": location,
            }
            if location_capacity is not None:
                self._values["location_capacity"] = location_capacity

        @builtins.property
        def location(self) -> builtins.str:
            '''An AWS Region code, such as ``us-west-2`` .

            For a list of supported Regions and Local Zones, see `Amazon GameLift Servers service locations <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html>`_ for managed hosting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationconfiguration.html#cfn-gamelift-fleet-locationconfiguration-location
            '''
            result = self._values.get("location")
            assert result is not None, "Required property 'location' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def location_capacity(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.LocationCapacityProperty"]]:
            '''Current resource capacity settings for managed EC2 fleets and managed container fleets.

            For multi-location fleets, location values might refer to a fleet's remote location or its home Region.

            *Returned by:* `DescribeFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html>`_ , `DescribeFleetLocationCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html>`_ , `UpdateFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationconfiguration.html#cfn-gamelift-fleet-locationconfiguration-locationcapacity
            '''
            result = self._values.get("location_capacity")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.LocationCapacityProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.ResourceCreationLimitPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "new_game_sessions_per_creator": "newGameSessionsPerCreator",
            "policy_period_in_minutes": "policyPeriodInMinutes",
        },
    )
    class ResourceCreationLimitPolicyProperty:
        def __init__(
            self,
            *,
            new_game_sessions_per_creator: typing.Optional[jsii.Number] = None,
            policy_period_in_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''A policy that limits the number of game sessions a player can create on the same fleet.

            This optional policy gives game owners control over how players can consume available game server resources. A resource creation policy makes the following statement: "An individual player can create a maximum number of new game sessions within a specified time period".

            The policy is evaluated when a player tries to create a new game session. For example, assume you have a policy of 10 new game sessions and a time period of 60 minutes. On receiving a ``CreateGameSession`` request, Amazon GameLift checks that the player (identified by ``CreatorId`` ) has created fewer than 10 game sessions in the past 60 minutes.

            :param new_game_sessions_per_creator: A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control players' ability to consume available resources. The policy is evaluated when a player tries to create a new game session. On receiving a ``CreateGameSession`` request, Amazon GameLift Servers checks that the player (identified by ``CreatorId`` ) has created fewer than game session limit in the specified time period.
            :param policy_period_in_minutes: The time span used in evaluating the resource creation limit policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-resourcecreationlimitpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                resource_creation_limit_policy_property = gamelift.CfnFleet.ResourceCreationLimitPolicyProperty(
                    new_game_sessions_per_creator=123,
                    policy_period_in_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1b5bf70d1fc5987b674dcb2717a733f347f6ff57d29689b7a2a12d07ccfab884)
                check_type(argname="argument new_game_sessions_per_creator", value=new_game_sessions_per_creator, expected_type=type_hints["new_game_sessions_per_creator"])
                check_type(argname="argument policy_period_in_minutes", value=policy_period_in_minutes, expected_type=type_hints["policy_period_in_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if new_game_sessions_per_creator is not None:
                self._values["new_game_sessions_per_creator"] = new_game_sessions_per_creator
            if policy_period_in_minutes is not None:
                self._values["policy_period_in_minutes"] = policy_period_in_minutes

        @builtins.property
        def new_game_sessions_per_creator(self) -> typing.Optional[jsii.Number]:
            '''A policy that puts limits on the number of game sessions that a player can create within a specified span of time.

            With this policy, you can control players' ability to consume available resources.

            The policy is evaluated when a player tries to create a new game session. On receiving a ``CreateGameSession`` request, Amazon GameLift Servers checks that the player (identified by ``CreatorId`` ) has created fewer than game session limit in the specified time period.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-resourcecreationlimitpolicy.html#cfn-gamelift-fleet-resourcecreationlimitpolicy-newgamesessionspercreator
            '''
            result = self._values.get("new_game_sessions_per_creator")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def policy_period_in_minutes(self) -> typing.Optional[jsii.Number]:
            '''The time span used in evaluating the resource creation limit policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-resourcecreationlimitpolicy.html#cfn-gamelift-fleet-resourcecreationlimitpolicy-policyperiodinminutes
            '''
            result = self._values.get("policy_period_in_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceCreationLimitPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.RuntimeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "game_session_activation_timeout_seconds": "gameSessionActivationTimeoutSeconds",
            "max_concurrent_game_session_activations": "maxConcurrentGameSessionActivations",
            "server_processes": "serverProcesses",
        },
    )
    class RuntimeConfigurationProperty:
        def __init__(
            self,
            *,
            game_session_activation_timeout_seconds: typing.Optional[jsii.Number] = None,
            max_concurrent_game_session_activations: typing.Optional[jsii.Number] = None,
            server_processes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.ServerProcessProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''A collection of server process configurations that describe the set of processes to run on each instance in a fleet.

            Server processes run either an executable in a custom game build or a Realtime Servers script. GameLift launches the configured processes, manages their life cycle, and replaces them as needed. Each instance checks regularly for an updated runtime configuration.

            A GameLift instance is limited to 50 processes running concurrently. To calculate the total number of processes in a runtime configuration, add the values of the ``ConcurrentExecutions`` parameter for each ServerProcess. Learn more about `Running Multiple Processes on a Fleet <https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-multiprocess.html>`_ .

            :param game_session_activation_timeout_seconds: The maximum amount of time (in seconds) allowed to launch a new game session and have it report ready to host players. During this time, the game session is in status ``ACTIVATING`` . If the game session does not become active before the timeout, it is ended and the game session status is changed to ``TERMINATED`` .
            :param max_concurrent_game_session_activations: The number of game sessions in status ``ACTIVATING`` to allow on an instance or compute. This setting limits the instance resources that can be used for new game activations at any one time.
            :param server_processes: A collection of server process configurations that identify what server processes to run on fleet computes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                runtime_configuration_property = gamelift.CfnFleet.RuntimeConfigurationProperty(
                    game_session_activation_timeout_seconds=123,
                    max_concurrent_game_session_activations=123,
                    server_processes=[gamelift.CfnFleet.ServerProcessProperty(
                        concurrent_executions=123,
                        launch_path="launchPath",
                
                        # the properties below are optional
                        parameters="parameters"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ae990fc53511e6175c77d897f3a8a6bc35be77827bfc0f1be6b1f8d7967e54c3)
                check_type(argname="argument game_session_activation_timeout_seconds", value=game_session_activation_timeout_seconds, expected_type=type_hints["game_session_activation_timeout_seconds"])
                check_type(argname="argument max_concurrent_game_session_activations", value=max_concurrent_game_session_activations, expected_type=type_hints["max_concurrent_game_session_activations"])
                check_type(argname="argument server_processes", value=server_processes, expected_type=type_hints["server_processes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if game_session_activation_timeout_seconds is not None:
                self._values["game_session_activation_timeout_seconds"] = game_session_activation_timeout_seconds
            if max_concurrent_game_session_activations is not None:
                self._values["max_concurrent_game_session_activations"] = max_concurrent_game_session_activations
            if server_processes is not None:
                self._values["server_processes"] = server_processes

        @builtins.property
        def game_session_activation_timeout_seconds(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The maximum amount of time (in seconds) allowed to launch a new game session and have it report ready to host players.

            During this time, the game session is in status ``ACTIVATING`` . If the game session does not become active before the timeout, it is ended and the game session status is changed to ``TERMINATED`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html#cfn-gamelift-fleet-runtimeconfiguration-gamesessionactivationtimeoutseconds
            '''
            result = self._values.get("game_session_activation_timeout_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_concurrent_game_session_activations(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The number of game sessions in status ``ACTIVATING`` to allow on an instance or compute.

            This setting limits the instance resources that can be used for new game activations at any one time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html#cfn-gamelift-fleet-runtimeconfiguration-maxconcurrentgamesessionactivations
            '''
            result = self._values.get("max_concurrent_game_session_activations")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def server_processes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.ServerProcessProperty"]]]]:
            '''A collection of server process configurations that identify what server processes to run on fleet computes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html#cfn-gamelift-fleet-runtimeconfiguration-serverprocesses
            '''
            result = self._values.get("server_processes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.ServerProcessProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuntimeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.ScalingPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_name": "metricName",
            "name": "name",
            "comparison_operator": "comparisonOperator",
            "evaluation_periods": "evaluationPeriods",
            "location": "location",
            "policy_type": "policyType",
            "scaling_adjustment": "scalingAdjustment",
            "scaling_adjustment_type": "scalingAdjustmentType",
            "status": "status",
            "target_configuration": "targetConfiguration",
            "threshold": "threshold",
            "update_status": "updateStatus",
        },
    )
    class ScalingPolicyProperty:
        def __init__(
            self,
            *,
            metric_name: builtins.str,
            name: builtins.str,
            comparison_operator: typing.Optional[builtins.str] = None,
            evaluation_periods: typing.Optional[jsii.Number] = None,
            location: typing.Optional[builtins.str] = None,
            policy_type: typing.Optional[builtins.str] = None,
            scaling_adjustment: typing.Optional[jsii.Number] = None,
            scaling_adjustment_type: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
            target_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.TargetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            threshold: typing.Optional[jsii.Number] = None,
            update_status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Rule that controls how a fleet is scaled.

            Scaling policies are uniquely identified by the combination of name and fleet ID.

            :param metric_name: Name of the Amazon GameLift Servers-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see `Monitor Amazon GameLift Servers with Amazon CloudWatch <https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html>`_ . - *ActivatingGameSessions* -- Game sessions in the process of being created. - *ActiveGameSessions* -- Game sessions that are currently running. - *ActiveInstances* -- Fleet instances that are currently running at least one game session. - *AvailableGameSessions* -- Additional game sessions that fleet could host simultaneously, given current capacity. - *AvailablePlayerSessions* -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included. - *CurrentPlayerSessions* -- Player slots in active game sessions that are being used by a player or are reserved for a player. - *IdleInstances* -- Active instances that are currently hosting zero game sessions. - *PercentAvailableGameSessions* -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy. - *PercentIdleInstances* -- Percentage of the total number of active instances that are hosting zero game sessions. - *QueueDepth* -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination. - *WaitTime* -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
            :param name: A descriptive label that is associated with a fleet's scaling policy. Policy names do not need to be unique.
            :param comparison_operator: Comparison operator to use when measuring a metric against the threshold value.
            :param evaluation_periods: Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.
            :param location: The fleet location.
            :param policy_type: The type of scaling policy to create. For a target-based policy, set the parameter *MetricName* to 'PercentAvailableGameSessions' and specify a *TargetConfiguration* . For a rule-based policy set the following parameters: *MetricName* , *ComparisonOperator* , *Threshold* , *EvaluationPeriods* , *ScalingAdjustmentType* , and *ScalingAdjustment* .
            :param scaling_adjustment: Amount of adjustment to make, based on the scaling adjustment type.
            :param scaling_adjustment_type: The type of adjustment to make to a fleet's instance count. - *ChangeInCapacity* -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down. - *ExactCapacity* -- set the instance count to the scaling adjustment value. - *PercentChangeInCapacity* -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down.
            :param status: Current status of the scaling policy. The scaling policy can be in force only when in an ``ACTIVE`` status. Scaling policies can be suspended for individual fleets. If the policy is suspended for a fleet, the policy status does not change. - *ACTIVE* -- The scaling policy can be used for auto-scaling a fleet. - *UPDATE_REQUESTED* -- A request to update the scaling policy has been received. - *UPDATING* -- A change is being made to the scaling policy. - *DELETE_REQUESTED* -- A request to delete the scaling policy has been received. - *DELETING* -- The scaling policy is being deleted. - *DELETED* -- The scaling policy has been deleted. - *ERROR* -- An error occurred in creating the policy. It should be removed and recreated.
            :param target_configuration: An object that contains settings for a target-based scaling policy.
            :param threshold: Metric value used to trigger a scaling event.
            :param update_status: The current status of the fleet's scaling policies in a requested fleet location. The status ``PENDING_UPDATE`` indicates that an update was requested for the fleet but has not yet been completed for the location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                scaling_policy_property = gamelift.CfnFleet.ScalingPolicyProperty(
                    metric_name="metricName",
                    name="name",
                
                    # the properties below are optional
                    comparison_operator="comparisonOperator",
                    evaluation_periods=123,
                    location="location",
                    policy_type="policyType",
                    scaling_adjustment=123,
                    scaling_adjustment_type="scalingAdjustmentType",
                    status="status",
                    target_configuration=gamelift.CfnFleet.TargetConfigurationProperty(
                        target_value=123
                    ),
                    threshold=123,
                    update_status="updateStatus"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e8690870b8fddf2f2747a9a00d8f1a693d624b5f4f72283ed427b04667f02bd8)
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
                check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
                check_type(argname="argument location", value=location, expected_type=type_hints["location"])
                check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
                check_type(argname="argument scaling_adjustment", value=scaling_adjustment, expected_type=type_hints["scaling_adjustment"])
                check_type(argname="argument scaling_adjustment_type", value=scaling_adjustment_type, expected_type=type_hints["scaling_adjustment_type"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument target_configuration", value=target_configuration, expected_type=type_hints["target_configuration"])
                check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
                check_type(argname="argument update_status", value=update_status, expected_type=type_hints["update_status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "metric_name": metric_name,
                "name": name,
            }
            if comparison_operator is not None:
                self._values["comparison_operator"] = comparison_operator
            if evaluation_periods is not None:
                self._values["evaluation_periods"] = evaluation_periods
            if location is not None:
                self._values["location"] = location
            if policy_type is not None:
                self._values["policy_type"] = policy_type
            if scaling_adjustment is not None:
                self._values["scaling_adjustment"] = scaling_adjustment
            if scaling_adjustment_type is not None:
                self._values["scaling_adjustment_type"] = scaling_adjustment_type
            if status is not None:
                self._values["status"] = status
            if target_configuration is not None:
                self._values["target_configuration"] = target_configuration
            if threshold is not None:
                self._values["threshold"] = threshold
            if update_status is not None:
                self._values["update_status"] = update_status

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''Name of the Amazon GameLift Servers-defined metric that is used to trigger a scaling adjustment.

            For detailed descriptions of fleet metrics, see `Monitor Amazon GameLift Servers with Amazon CloudWatch <https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html>`_ .

            - *ActivatingGameSessions* -- Game sessions in the process of being created.
            - *ActiveGameSessions* -- Game sessions that are currently running.
            - *ActiveInstances* -- Fleet instances that are currently running at least one game session.
            - *AvailableGameSessions* -- Additional game sessions that fleet could host simultaneously, given current capacity.
            - *AvailablePlayerSessions* -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.
            - *CurrentPlayerSessions* -- Player slots in active game sessions that are being used by a player or are reserved for a player.
            - *IdleInstances* -- Active instances that are currently hosting zero game sessions.
            - *PercentAvailableGameSessions* -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.
            - *PercentIdleInstances* -- Percentage of the total number of active instances that are hosting zero game sessions.
            - *QueueDepth* -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
            - *WaitTime* -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''A descriptive label that is associated with a fleet's scaling policy.

            Policy names do not need to be unique.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def comparison_operator(self) -> typing.Optional[builtins.str]:
            '''Comparison operator to use when measuring a metric against the threshold value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def evaluation_periods(self) -> typing.Optional[jsii.Number]:
            '''Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-evaluationperiods
            '''
            result = self._values.get("evaluation_periods")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def location(self) -> typing.Optional[builtins.str]:
            '''The fleet location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-location
            '''
            result = self._values.get("location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def policy_type(self) -> typing.Optional[builtins.str]:
            '''The type of scaling policy to create.

            For a target-based policy, set the parameter *MetricName* to 'PercentAvailableGameSessions' and specify a *TargetConfiguration* . For a rule-based policy set the following parameters: *MetricName* , *ComparisonOperator* , *Threshold* , *EvaluationPeriods* , *ScalingAdjustmentType* , and *ScalingAdjustment* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-policytype
            '''
            result = self._values.get("policy_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scaling_adjustment(self) -> typing.Optional[jsii.Number]:
            '''Amount of adjustment to make, based on the scaling adjustment type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-scalingadjustment
            '''
            result = self._values.get("scaling_adjustment")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def scaling_adjustment_type(self) -> typing.Optional[builtins.str]:
            '''The type of adjustment to make to a fleet's instance count.

            - *ChangeInCapacity* -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.
            - *ExactCapacity* -- set the instance count to the scaling adjustment value.
            - *PercentChangeInCapacity* -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-scalingadjustmenttype
            '''
            result = self._values.get("scaling_adjustment_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''Current status of the scaling policy.

            The scaling policy can be in force only when in an ``ACTIVE`` status. Scaling policies can be suspended for individual fleets. If the policy is suspended for a fleet, the policy status does not change.

            - *ACTIVE* -- The scaling policy can be used for auto-scaling a fleet.
            - *UPDATE_REQUESTED* -- A request to update the scaling policy has been received.
            - *UPDATING* -- A change is being made to the scaling policy.
            - *DELETE_REQUESTED* -- A request to delete the scaling policy has been received.
            - *DELETING* -- The scaling policy is being deleted.
            - *DELETED* -- The scaling policy has been deleted.
            - *ERROR* -- An error occurred in creating the policy. It should be removed and recreated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.TargetConfigurationProperty"]]:
            '''An object that contains settings for a target-based scaling policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-targetconfiguration
            '''
            result = self._values.get("target_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.TargetConfigurationProperty"]], result)

        @builtins.property
        def threshold(self) -> typing.Optional[jsii.Number]:
            '''Metric value used to trigger a scaling event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-threshold
            '''
            result = self._values.get("threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def update_status(self) -> typing.Optional[builtins.str]:
            '''The current status of the fleet's scaling policies in a requested fleet location.

            The status ``PENDING_UPDATE`` indicates that an update was requested for the fleet but has not yet been completed for the location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-updatestatus
            '''
            result = self._values.get("update_status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.ServerProcessProperty",
        jsii_struct_bases=[],
        name_mapping={
            "concurrent_executions": "concurrentExecutions",
            "launch_path": "launchPath",
            "parameters": "parameters",
        },
    )
    class ServerProcessProperty:
        def __init__(
            self,
            *,
            concurrent_executions: jsii.Number,
            launch_path: builtins.str,
            parameters: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A set of instructions for launching server processes on each instance in a fleet.

            Server processes run either an executable in a custom game build or a Realtime Servers script.

            :param concurrent_executions: The number of server processes using this configuration that run concurrently on each instance or compute.
            :param launch_path: The location of a game build executable or Realtime script. Game builds and Realtime scripts are installed on instances at the root: - Windows (custom game builds only): ``C:\\game`` . Example: " ``C:\\game\\MyGame\\server.exe`` " - Linux: ``/local/game`` . Examples: " ``/local/game/MyGame/server.exe`` " or " ``/local/game/MyRealtimeScript.js`` " .. epigraph:: Amazon GameLift Servers doesn't support the use of setup scripts that launch the game executable. For custom game builds, this parameter must indicate the executable that calls the server SDK operations ``initSDK()`` and ``ProcessReady()`` .
            :param parameters: An optional list of parameters to pass to the server executable or Realtime script on launch. Length Constraints: Minimum length of 1. Maximum length of 1024. Pattern: [A-Za-z0-9_:.+/\\- =@{},?'[]"]+

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                server_process_property = gamelift.CfnFleet.ServerProcessProperty(
                    concurrent_executions=123,
                    launch_path="launchPath",
                
                    # the properties below are optional
                    parameters="parameters"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fc845ade67d7aff6536f53651c26f049fc04883863968a83da759b79b0a6d035)
                check_type(argname="argument concurrent_executions", value=concurrent_executions, expected_type=type_hints["concurrent_executions"])
                check_type(argname="argument launch_path", value=launch_path, expected_type=type_hints["launch_path"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "concurrent_executions": concurrent_executions,
                "launch_path": launch_path,
            }
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def concurrent_executions(self) -> jsii.Number:
            '''The number of server processes using this configuration that run concurrently on each instance or compute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html#cfn-gamelift-fleet-serverprocess-concurrentexecutions
            '''
            result = self._values.get("concurrent_executions")
            assert result is not None, "Required property 'concurrent_executions' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def launch_path(self) -> builtins.str:
            '''The location of a game build executable or Realtime script.

            Game builds and Realtime scripts are installed on instances at the root:

            - Windows (custom game builds only): ``C:\\game`` . Example: " ``C:\\game\\MyGame\\server.exe`` "
            - Linux: ``/local/game`` . Examples: " ``/local/game/MyGame/server.exe`` " or " ``/local/game/MyRealtimeScript.js`` "

            .. epigraph::

               Amazon GameLift Servers doesn't support the use of setup scripts that launch the game executable. For custom game builds, this parameter must indicate the executable that calls the server SDK operations ``initSDK()`` and ``ProcessReady()`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html#cfn-gamelift-fleet-serverprocess-launchpath
            '''
            result = self._values.get("launch_path")
            assert result is not None, "Required property 'launch_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameters(self) -> typing.Optional[builtins.str]:
            '''An optional list of parameters to pass to the server executable or Realtime script on launch.

            Length Constraints: Minimum length of 1. Maximum length of 1024.

            Pattern: [A-Za-z0-9_:.+/- =@{},?'[]"]+

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html#cfn-gamelift-fleet-serverprocess-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerProcessProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.TargetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"target_value": "targetValue"},
    )
    class TargetConfigurationProperty:
        def __init__(self, *, target_value: jsii.Number) -> None:
            '''Settings for a target-based scaling policy.

            A target-based policy tracks a particular fleet metric specifies a target value for the metric. As player usage changes, the policy triggers Amazon GameLift Servers to adjust capacity so that the metric returns to the target value. The target configuration specifies settings as needed for the target based policy, including the target value.

            :param target_value: Desired value to use with a target-based scaling policy. The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleet's buffer (the percent of capacity that should be idle and ready for new game sessions).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-targetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                target_configuration_property = gamelift.CfnFleet.TargetConfigurationProperty(
                    target_value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__472ce4c72467f1a69fc974099623863890460564fbbe1e98eb694a9a4b1546b7)
                check_type(argname="argument target_value", value=target_value, expected_type=type_hints["target_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_value": target_value,
            }

        @builtins.property
        def target_value(self) -> jsii.Number:
            '''Desired value to use with a target-based scaling policy.

            The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleet's buffer (the percent of capacity that should be idle and ready for new game sessions).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-targetconfiguration.html#cfn-gamelift-fleet-targetconfiguration-targetvalue
            '''
            result = self._values.get("target_value")
            assert result is not None, "Required property 'target_value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnFleetProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "anywhere_configuration": "anywhereConfiguration",
        "apply_capacity": "applyCapacity",
        "build_id": "buildId",
        "certificate_configuration": "certificateConfiguration",
        "compute_type": "computeType",
        "description": "description",
        "desired_ec2_instances": "desiredEc2Instances",
        "ec2_inbound_permissions": "ec2InboundPermissions",
        "ec2_instance_type": "ec2InstanceType",
        "fleet_type": "fleetType",
        "instance_role_arn": "instanceRoleArn",
        "instance_role_credentials_provider": "instanceRoleCredentialsProvider",
        "locations": "locations",
        "log_paths": "logPaths",
        "max_size": "maxSize",
        "metric_groups": "metricGroups",
        "min_size": "minSize",
        "new_game_session_protection_policy": "newGameSessionProtectionPolicy",
        "peer_vpc_aws_account_id": "peerVpcAwsAccountId",
        "peer_vpc_id": "peerVpcId",
        "resource_creation_limit_policy": "resourceCreationLimitPolicy",
        "runtime_configuration": "runtimeConfiguration",
        "scaling_policies": "scalingPolicies",
        "script_id": "scriptId",
        "server_launch_parameters": "serverLaunchParameters",
        "server_launch_path": "serverLaunchPath",
        "tags": "tags",
    },
)
class CfnFleetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        anywhere_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.AnywhereConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        apply_capacity: typing.Optional[builtins.str] = None,
        build_id: typing.Optional[builtins.str] = None,
        certificate_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.CertificateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        compute_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        desired_ec2_instances: typing.Optional[jsii.Number] = None,
        ec2_inbound_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.IpPermissionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ec2_instance_type: typing.Optional[builtins.str] = None,
        fleet_type: typing.Optional[builtins.str] = None,
        instance_role_arn: typing.Optional[builtins.str] = None,
        instance_role_credentials_provider: typing.Optional[builtins.str] = None,
        locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.LocationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        log_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        metric_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        min_size: typing.Optional[jsii.Number] = None,
        new_game_session_protection_policy: typing.Optional[builtins.str] = None,
        peer_vpc_aws_account_id: typing.Optional[builtins.str] = None,
        peer_vpc_id: typing.Optional[builtins.str] = None,
        resource_creation_limit_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ResourceCreationLimitPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        runtime_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.RuntimeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        scaling_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        script_id: typing.Optional[builtins.str] = None,
        server_launch_parameters: typing.Optional[builtins.str] = None,
        server_launch_path: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFleet``.

        :param name: A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
        :param anywhere_configuration: Amazon GameLift Servers Anywhere configuration options.
        :param apply_capacity: Current resource capacity settings for managed EC2 fleets and managed container fleets. For multi-location fleets, location values might refer to a fleet's remote location or its home Region. *Returned by:* `DescribeFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html>`_ , `DescribeFleetLocationCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html>`_ , `UpdateFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html>`_
        :param build_id: A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a ``READY`` status. This fleet setting cannot be changed once the fleet is created.
        :param certificate_configuration: Prompts Amazon GameLift Servers to generate a TLS/SSL certificate for the fleet. Amazon GameLift Servers uses the certificates to encrypt traffic between game clients and the game servers running on Amazon GameLift Servers. By default, the ``CertificateConfiguration`` is ``DISABLED`` . You can't change this property after you create the fleet. AWS Certificate Manager (ACM) certificates expire after 13 months. Certificate expiration can cause fleets to fail, preventing players from connecting to instances in the fleet. We recommend you replace fleets before 13 months, consider using fleet aliases for a smooth transition. .. epigraph:: ACM isn't available in all AWS regions. A fleet creation request with certificate generation enabled in an unsupported Region, fails with a 4xx error. For more information about the supported Regions, see `Supported Regions <https://docs.aws.amazon.com/acm/latest/userguide/acm-regions.html>`_ in the *AWS Certificate Manager User Guide* .
        :param compute_type: The type of compute resource used to host your game servers. - ``EC2`` – The game server build is deployed to Amazon EC2 instances for cloud hosting. This is the default setting. - ``ANYWHERE`` – Game servers and supporting software are deployed to compute resources that you provide and manage. With this compute type, you can also set the ``AnywhereConfiguration`` parameter.
        :param description: A description for the fleet.
        :param desired_ec2_instances: (deprecated) [DEPRECATED] The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.
        :param ec2_inbound_permissions: The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet. Set this parameter for managed EC2 fleets. You can leave this parameter empty when creating the fleet, but you must call ` <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetPortSettings>`_ to set it before players can connect to game sessions. As a best practice, we recommend opening ports for remote access only when you need them and closing them when you're finished. For Amazon GameLift Servers Realtime fleets, Amazon GameLift Servers automatically sets TCP and UDP ranges.
        :param ec2_instance_type: The Amazon GameLift Servers-supported Amazon EC2 instance type to use with managed EC2 fleets. Instance type determines the computing resources that will be used to host your game servers, including CPU, memory, storage, and networking capacity. See `Amazon Elastic Compute Cloud Instance Types <https://docs.aws.amazon.com/ec2/instance-types/>`_ for detailed descriptions of Amazon EC2 instance types.
        :param fleet_type: Indicates whether to use On-Demand or Spot instances for this fleet. By default, this property is set to ``ON_DEMAND`` . Learn more about when to use `On-Demand versus Spot Instances <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot>`_ . This fleet property can't be changed after the fleet is created.
        :param instance_role_arn: A unique identifier for an IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN by using the `IAM dashboard <https://docs.aws.amazon.com/iam/>`_ in the AWS Management Console . Learn more about using on-box credentials for your game servers at `Access external resources from a game server <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`_ . This attribute is used with fleets where ``ComputeType`` is ``EC2`` .
        :param instance_role_credentials_provider: Indicates that fleet instances maintain a shared credentials file for the IAM role defined in ``InstanceRoleArn`` . Shared credentials allow applications that are deployed with the game server executable to communicate with other AWS resources. This property is used only when the game server is integrated with the server SDK version 5.x. For more information about using shared credentials, see `Communicate with other AWS resources from your fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`_ . This attribute is used with fleets where ``ComputeType`` is ``EC2`` .
        :param locations: A set of remote locations to deploy additional instances to and manage as a multi-location fleet. Use this parameter when creating a fleet in AWS Regions that support multiple locations. You can add any AWS Region or Local Zone that's supported by Amazon GameLift Servers. Provide a list of one or more AWS Region codes, such as ``us-west-2`` , or Local Zone names. When using this parameter, Amazon GameLift Servers requires you to include your home location in the request. For a list of supported Regions and Local Zones, see `Amazon GameLift Servers service locations <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html>`_ for managed hosting.
        :param log_paths: (deprecated) This parameter is no longer used. When hosting a custom game build, specify where Amazon GameLift should store log files using the Amazon GameLift server API call ProcessReady()
        :param max_size: (deprecated) [DEPRECATED] The maximum value that is allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "1". Once the fleet is active, you can change this value.
        :param metric_groups: The name of an AWS CloudWatch metric group to add this fleet to. A metric group is used to aggregate the metrics for multiple fleets. You can specify an existing metric group name or set a new name to create a new metric group. A fleet can be included in only one metric group at a time.
        :param min_size: (deprecated) [DEPRECATED] The minimum value allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "0". After the fleet is active, you can change this value.
        :param new_game_session_protection_policy: The status of termination protection for active game sessions on the fleet. By default, this property is set to ``NoProtection`` . - *NoProtection* - Game sessions can be terminated during active gameplay as a result of a scale-down event. - *FullProtection* - Game sessions in ``ACTIVE`` status cannot be terminated during a scale-down event.
        :param peer_vpc_aws_account_id: Used when peering your Amazon GameLift Servers fleet with a VPC, the unique identifier for the AWS account that owns the VPC. You can find your account ID in the AWS Management Console under account settings.
        :param peer_vpc_id: A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the `VPC Dashboard <https://docs.aws.amazon.com/vpc/>`_ in the AWS Management Console . Learn more about VPC peering in `VPC Peering with Amazon GameLift Servers Fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html>`_ .
        :param resource_creation_limit_policy: A policy that limits the number of game sessions that an individual player can create on instances in this fleet within a specified span of time.
        :param runtime_configuration: Instructions for how to launch and maintain server processes on instances in the fleet. The runtime configuration defines one or more server process configurations, each identifying a build executable or Realtime script file and the number of processes of that type to run concurrently. .. epigraph:: The ``RuntimeConfiguration`` parameter is required unless the fleet is being configured using the older parameters ``ServerLaunchPath`` and ``ServerLaunchParameters`` , which are still supported for backward compatibility.
        :param scaling_policies: Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the combination of name and fleet ID.
        :param script_id: The unique identifier for a Realtime configuration script to be deployed on fleet instances. You can use either the script ID or ARN. Scripts must be uploaded to Amazon GameLift Servers prior to creating the fleet. This fleet property cannot be changed later. .. epigraph:: You can't use the ``!Ref`` command to reference a script created with a CloudFormation template for the fleet property ``ScriptId`` . Instead, use ``Fn::GetAtt Script.Arn`` or ``Fn::GetAtt Script.Id`` to retrieve either of these properties as input for ``ScriptId`` . Alternatively, enter a ``ScriptId`` string manually.
        :param server_launch_parameters: (deprecated) This parameter is no longer used but is retained for backward compatibility. Instead, specify server launch parameters in the RuntimeConfiguration parameter. A request must specify either a runtime configuration or values for both ServerLaunchParameters and ServerLaunchPath.
        :param server_launch_path: (deprecated) This parameter is no longer used. Instead, specify a server launch path using the RuntimeConfiguration parameter. Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_fleet_props = gamelift.CfnFleetProps(
                name="name",
            
                # the properties below are optional
                anywhere_configuration=gamelift.CfnFleet.AnywhereConfigurationProperty(
                    cost="cost"
                ),
                apply_capacity="applyCapacity",
                build_id="buildId",
                certificate_configuration=gamelift.CfnFleet.CertificateConfigurationProperty(
                    certificate_type="certificateType"
                ),
                compute_type="computeType",
                description="description",
                desired_ec2_instances=123,
                ec2_inbound_permissions=[gamelift.CfnFleet.IpPermissionProperty(
                    from_port=123,
                    ip_range="ipRange",
                    protocol="protocol",
                    to_port=123
                )],
                ec2_instance_type="ec2InstanceType",
                fleet_type="fleetType",
                instance_role_arn="instanceRoleArn",
                instance_role_credentials_provider="instanceRoleCredentialsProvider",
                locations=[gamelift.CfnFleet.LocationConfigurationProperty(
                    location="location",
            
                    # the properties below are optional
                    location_capacity=gamelift.CfnFleet.LocationCapacityProperty(
                        desired_ec2_instances=123,
                        max_size=123,
                        min_size=123
                    )
                )],
                log_paths=["logPaths"],
                max_size=123,
                metric_groups=["metricGroups"],
                min_size=123,
                new_game_session_protection_policy="newGameSessionProtectionPolicy",
                peer_vpc_aws_account_id="peerVpcAwsAccountId",
                peer_vpc_id="peerVpcId",
                resource_creation_limit_policy=gamelift.CfnFleet.ResourceCreationLimitPolicyProperty(
                    new_game_sessions_per_creator=123,
                    policy_period_in_minutes=123
                ),
                runtime_configuration=gamelift.CfnFleet.RuntimeConfigurationProperty(
                    game_session_activation_timeout_seconds=123,
                    max_concurrent_game_session_activations=123,
                    server_processes=[gamelift.CfnFleet.ServerProcessProperty(
                        concurrent_executions=123,
                        launch_path="launchPath",
            
                        # the properties below are optional
                        parameters="parameters"
                    )]
                ),
                scaling_policies=[gamelift.CfnFleet.ScalingPolicyProperty(
                    metric_name="metricName",
                    name="name",
            
                    # the properties below are optional
                    comparison_operator="comparisonOperator",
                    evaluation_periods=123,
                    location="location",
                    policy_type="policyType",
                    scaling_adjustment=123,
                    scaling_adjustment_type="scalingAdjustmentType",
                    status="status",
                    target_configuration=gamelift.CfnFleet.TargetConfigurationProperty(
                        target_value=123
                    ),
                    threshold=123,
                    update_status="updateStatus"
                )],
                script_id="scriptId",
                server_launch_parameters="serverLaunchParameters",
                server_launch_path="serverLaunchPath",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a51a418ba5b606bdfc45dc50c3172e280a12e078a7392f3258d5d329e037a55)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument anywhere_configuration", value=anywhere_configuration, expected_type=type_hints["anywhere_configuration"])
            check_type(argname="argument apply_capacity", value=apply_capacity, expected_type=type_hints["apply_capacity"])
            check_type(argname="argument build_id", value=build_id, expected_type=type_hints["build_id"])
            check_type(argname="argument certificate_configuration", value=certificate_configuration, expected_type=type_hints["certificate_configuration"])
            check_type(argname="argument compute_type", value=compute_type, expected_type=type_hints["compute_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument desired_ec2_instances", value=desired_ec2_instances, expected_type=type_hints["desired_ec2_instances"])
            check_type(argname="argument ec2_inbound_permissions", value=ec2_inbound_permissions, expected_type=type_hints["ec2_inbound_permissions"])
            check_type(argname="argument ec2_instance_type", value=ec2_instance_type, expected_type=type_hints["ec2_instance_type"])
            check_type(argname="argument fleet_type", value=fleet_type, expected_type=type_hints["fleet_type"])
            check_type(argname="argument instance_role_arn", value=instance_role_arn, expected_type=type_hints["instance_role_arn"])
            check_type(argname="argument instance_role_credentials_provider", value=instance_role_credentials_provider, expected_type=type_hints["instance_role_credentials_provider"])
            check_type(argname="argument locations", value=locations, expected_type=type_hints["locations"])
            check_type(argname="argument log_paths", value=log_paths, expected_type=type_hints["log_paths"])
            check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            check_type(argname="argument metric_groups", value=metric_groups, expected_type=type_hints["metric_groups"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument new_game_session_protection_policy", value=new_game_session_protection_policy, expected_type=type_hints["new_game_session_protection_policy"])
            check_type(argname="argument peer_vpc_aws_account_id", value=peer_vpc_aws_account_id, expected_type=type_hints["peer_vpc_aws_account_id"])
            check_type(argname="argument peer_vpc_id", value=peer_vpc_id, expected_type=type_hints["peer_vpc_id"])
            check_type(argname="argument resource_creation_limit_policy", value=resource_creation_limit_policy, expected_type=type_hints["resource_creation_limit_policy"])
            check_type(argname="argument runtime_configuration", value=runtime_configuration, expected_type=type_hints["runtime_configuration"])
            check_type(argname="argument scaling_policies", value=scaling_policies, expected_type=type_hints["scaling_policies"])
            check_type(argname="argument script_id", value=script_id, expected_type=type_hints["script_id"])
            check_type(argname="argument server_launch_parameters", value=server_launch_parameters, expected_type=type_hints["server_launch_parameters"])
            check_type(argname="argument server_launch_path", value=server_launch_path, expected_type=type_hints["server_launch_path"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if anywhere_configuration is not None:
            self._values["anywhere_configuration"] = anywhere_configuration
        if apply_capacity is not None:
            self._values["apply_capacity"] = apply_capacity
        if build_id is not None:
            self._values["build_id"] = build_id
        if certificate_configuration is not None:
            self._values["certificate_configuration"] = certificate_configuration
        if compute_type is not None:
            self._values["compute_type"] = compute_type
        if description is not None:
            self._values["description"] = description
        if desired_ec2_instances is not None:
            self._values["desired_ec2_instances"] = desired_ec2_instances
        if ec2_inbound_permissions is not None:
            self._values["ec2_inbound_permissions"] = ec2_inbound_permissions
        if ec2_instance_type is not None:
            self._values["ec2_instance_type"] = ec2_instance_type
        if fleet_type is not None:
            self._values["fleet_type"] = fleet_type
        if instance_role_arn is not None:
            self._values["instance_role_arn"] = instance_role_arn
        if instance_role_credentials_provider is not None:
            self._values["instance_role_credentials_provider"] = instance_role_credentials_provider
        if locations is not None:
            self._values["locations"] = locations
        if log_paths is not None:
            self._values["log_paths"] = log_paths
        if max_size is not None:
            self._values["max_size"] = max_size
        if metric_groups is not None:
            self._values["metric_groups"] = metric_groups
        if min_size is not None:
            self._values["min_size"] = min_size
        if new_game_session_protection_policy is not None:
            self._values["new_game_session_protection_policy"] = new_game_session_protection_policy
        if peer_vpc_aws_account_id is not None:
            self._values["peer_vpc_aws_account_id"] = peer_vpc_aws_account_id
        if peer_vpc_id is not None:
            self._values["peer_vpc_id"] = peer_vpc_id
        if resource_creation_limit_policy is not None:
            self._values["resource_creation_limit_policy"] = resource_creation_limit_policy
        if runtime_configuration is not None:
            self._values["runtime_configuration"] = runtime_configuration
        if scaling_policies is not None:
            self._values["scaling_policies"] = scaling_policies
        if script_id is not None:
            self._values["script_id"] = script_id
        if server_launch_parameters is not None:
            self._values["server_launch_parameters"] = server_launch_parameters
        if server_launch_path is not None:
            self._values["server_launch_path"] = server_launch_path
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A descriptive label that is associated with a fleet.

        Fleet names do not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def anywhere_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.AnywhereConfigurationProperty]]:
        '''Amazon GameLift Servers Anywhere configuration options.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-anywhereconfiguration
        '''
        result = self._values.get("anywhere_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.AnywhereConfigurationProperty]], result)

    @builtins.property
    def apply_capacity(self) -> typing.Optional[builtins.str]:
        '''Current resource capacity settings for managed EC2 fleets and managed container fleets.

        For multi-location fleets, location values might refer to a fleet's remote location or its home Region.

        *Returned by:* `DescribeFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html>`_ , `DescribeFleetLocationCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html>`_ , `UpdateFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-applycapacity
        '''
        result = self._values.get("apply_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def build_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for a build to be deployed on the new fleet.

        If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a ``READY`` status. This fleet setting cannot be changed once the fleet is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-buildid
        '''
        result = self._values.get("build_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.CertificateConfigurationProperty]]:
        '''Prompts Amazon GameLift Servers to generate a TLS/SSL certificate for the fleet.

        Amazon GameLift Servers uses the certificates to encrypt traffic between game clients and the game servers running on Amazon GameLift Servers. By default, the ``CertificateConfiguration`` is ``DISABLED`` . You can't change this property after you create the fleet.

        AWS Certificate Manager (ACM) certificates expire after 13 months. Certificate expiration can cause fleets to fail, preventing players from connecting to instances in the fleet. We recommend you replace fleets before 13 months, consider using fleet aliases for a smooth transition.
        .. epigraph::

           ACM isn't available in all AWS regions. A fleet creation request with certificate generation enabled in an unsupported Region, fails with a 4xx error. For more information about the supported Regions, see `Supported Regions <https://docs.aws.amazon.com/acm/latest/userguide/acm-regions.html>`_ in the *AWS Certificate Manager User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-certificateconfiguration
        '''
        result = self._values.get("certificate_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.CertificateConfigurationProperty]], result)

    @builtins.property
    def compute_type(self) -> typing.Optional[builtins.str]:
        '''The type of compute resource used to host your game servers.

        - ``EC2`` – The game server build is deployed to Amazon EC2 instances for cloud hosting. This is the default setting.
        - ``ANYWHERE`` – Game servers and supporting software are deployed to compute resources that you provide and manage. With this compute type, you can also set the ``AnywhereConfiguration`` parameter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-computetype
        '''
        result = self._values.get("compute_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def desired_ec2_instances(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) [DEPRECATED] The number of EC2 instances that you want this fleet to host.

        When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-desiredec2instances
        :stability: deprecated
        '''
        result = self._values.get("desired_ec2_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ec2_inbound_permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.IpPermissionProperty]]]]:
        '''The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet.

        Set this parameter for managed EC2 fleets. You can leave this parameter empty when creating the fleet, but you must call ` <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetPortSettings>`_ to set it before players can connect to game sessions. As a best practice, we recommend opening ports for remote access only when you need them and closing them when you're finished. For Amazon GameLift Servers Realtime fleets, Amazon GameLift Servers automatically sets TCP and UDP ranges.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-ec2inboundpermissions
        '''
        result = self._values.get("ec2_inbound_permissions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.IpPermissionProperty]]]], result)

    @builtins.property
    def ec2_instance_type(self) -> typing.Optional[builtins.str]:
        '''The Amazon GameLift Servers-supported Amazon EC2 instance type to use with managed EC2 fleets.

        Instance type determines the computing resources that will be used to host your game servers, including CPU, memory, storage, and networking capacity. See `Amazon Elastic Compute Cloud Instance Types <https://docs.aws.amazon.com/ec2/instance-types/>`_ for detailed descriptions of Amazon EC2 instance types.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-ec2instancetype
        '''
        result = self._values.get("ec2_instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fleet_type(self) -> typing.Optional[builtins.str]:
        '''Indicates whether to use On-Demand or Spot instances for this fleet.

        By default, this property is set to ``ON_DEMAND`` . Learn more about when to use `On-Demand versus Spot Instances <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot>`_ . This fleet property can't be changed after the fleet is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-fleettype
        '''
        result = self._values.get("fleet_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_role_arn(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for an IAM role that manages access to your AWS services.

        With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN by using the `IAM dashboard <https://docs.aws.amazon.com/iam/>`_ in the AWS Management Console . Learn more about using on-box credentials for your game servers at `Access external resources from a game server <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`_ . This attribute is used with fleets where ``ComputeType`` is ``EC2`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-instancerolearn
        '''
        result = self._values.get("instance_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_role_credentials_provider(self) -> typing.Optional[builtins.str]:
        '''Indicates that fleet instances maintain a shared credentials file for the IAM role defined in ``InstanceRoleArn`` .

        Shared credentials allow applications that are deployed with the game server executable to communicate with other AWS resources. This property is used only when the game server is integrated with the server SDK version 5.x. For more information about using shared credentials, see `Communicate with other AWS resources from your fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`_ . This attribute is used with fleets where ``ComputeType`` is ``EC2`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-instancerolecredentialsprovider
        '''
        result = self._values.get("instance_role_credentials_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def locations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.LocationConfigurationProperty]]]]:
        '''A set of remote locations to deploy additional instances to and manage as a multi-location fleet.

        Use this parameter when creating a fleet in AWS Regions that support multiple locations. You can add any AWS Region or Local Zone that's supported by Amazon GameLift Servers. Provide a list of one or more AWS Region codes, such as ``us-west-2`` , or Local Zone names. When using this parameter, Amazon GameLift Servers requires you to include your home location in the request. For a list of supported Regions and Local Zones, see `Amazon GameLift Servers service locations <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html>`_ for managed hosting.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-locations
        '''
        result = self._values.get("locations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.LocationConfigurationProperty]]]], result)

    @builtins.property
    def log_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(deprecated) This parameter is no longer used.

        When hosting a custom game build, specify where Amazon GameLift should store log files using the Amazon GameLift server API call ProcessReady()

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-logpaths
        :stability: deprecated
        '''
        result = self._values.get("log_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) [DEPRECATED] The maximum value that is allowed for the fleet's instance count.

        When creating a new fleet, GameLift automatically sets this value to "1". Once the fleet is active, you can change this value.

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-maxsize
        :stability: deprecated
        '''
        result = self._values.get("max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metric_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name of an AWS CloudWatch metric group to add this fleet to.

        A metric group is used to aggregate the metrics for multiple fleets. You can specify an existing metric group name or set a new name to create a new metric group. A fleet can be included in only one metric group at a time.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-metricgroups
        '''
        result = self._values.get("metric_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) [DEPRECATED] The minimum value allowed for the fleet's instance count.

        When creating a new fleet, GameLift automatically sets this value to "0". After the fleet is active, you can change this value.

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-minsize
        :stability: deprecated
        '''
        result = self._values.get("min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def new_game_session_protection_policy(self) -> typing.Optional[builtins.str]:
        '''The status of termination protection for active game sessions on the fleet.

        By default, this property is set to ``NoProtection`` .

        - *NoProtection* - Game sessions can be terminated during active gameplay as a result of a scale-down event.
        - *FullProtection* - Game sessions in ``ACTIVE`` status cannot be terminated during a scale-down event.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-newgamesessionprotectionpolicy
        '''
        result = self._values.get("new_game_session_protection_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def peer_vpc_aws_account_id(self) -> typing.Optional[builtins.str]:
        '''Used when peering your Amazon GameLift Servers fleet with a VPC, the unique identifier for the AWS account that owns the VPC.

        You can find your account ID in the AWS Management Console under account settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-peervpcawsaccountid
        '''
        result = self._values.get("peer_vpc_aws_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def peer_vpc_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet.

        The VPC must be in the same Region as your fleet. To look up a VPC ID, use the `VPC Dashboard <https://docs.aws.amazon.com/vpc/>`_ in the AWS Management Console . Learn more about VPC peering in `VPC Peering with Amazon GameLift Servers Fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-peervpcid
        '''
        result = self._values.get("peer_vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_creation_limit_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.ResourceCreationLimitPolicyProperty]]:
        '''A policy that limits the number of game sessions that an individual player can create on instances in this fleet within a specified span of time.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-resourcecreationlimitpolicy
        '''
        result = self._values.get("resource_creation_limit_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.ResourceCreationLimitPolicyProperty]], result)

    @builtins.property
    def runtime_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.RuntimeConfigurationProperty]]:
        '''Instructions for how to launch and maintain server processes on instances in the fleet.

        The runtime configuration defines one or more server process configurations, each identifying a build executable or Realtime script file and the number of processes of that type to run concurrently.
        .. epigraph::

           The ``RuntimeConfiguration`` parameter is required unless the fleet is being configured using the older parameters ``ServerLaunchPath`` and ``ServerLaunchParameters`` , which are still supported for backward compatibility.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-runtimeconfiguration
        '''
        result = self._values.get("runtime_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.RuntimeConfigurationProperty]], result)

    @builtins.property
    def scaling_policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.ScalingPolicyProperty]]]]:
        '''Rule that controls how a fleet is scaled.

        Scaling policies are uniquely identified by the combination of name and fleet ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-scalingpolicies
        '''
        result = self._values.get("scaling_policies")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.ScalingPolicyProperty]]]], result)

    @builtins.property
    def script_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier for a Realtime configuration script to be deployed on fleet instances.

        You can use either the script ID or ARN. Scripts must be uploaded to Amazon GameLift Servers prior to creating the fleet. This fleet property cannot be changed later.
        .. epigraph::

           You can't use the ``!Ref`` command to reference a script created with a CloudFormation template for the fleet property ``ScriptId`` . Instead, use ``Fn::GetAtt Script.Arn`` or ``Fn::GetAtt Script.Id`` to retrieve either of these properties as input for ``ScriptId`` . Alternatively, enter a ``ScriptId`` string manually.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-scriptid
        '''
        result = self._values.get("script_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_launch_parameters(self) -> typing.Optional[builtins.str]:
        '''(deprecated) This parameter is no longer used but is retained for backward compatibility.

        Instead, specify server launch parameters in the RuntimeConfiguration parameter. A request must specify either a runtime configuration or values for both ServerLaunchParameters and ServerLaunchPath.

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-serverlaunchparameters
        :stability: deprecated
        '''
        result = self._values.get("server_launch_parameters")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_launch_path(self) -> typing.Optional[builtins.str]:
        '''(deprecated) This parameter is no longer used.

        Instead, specify a server launch path using the RuntimeConfiguration parameter. Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-serverlaunchpath
        :stability: deprecated
        '''
        result = self._values.get("server_launch_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFleetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnGameServerGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnGameServerGroup",
):
    '''*This operation is used with the Amazon GameLift FleetIQ solution and game server groups.*.

    Creates a GameLift FleetIQ game server group for managing game hosting on a collection of Amazon EC2 instances for game hosting. This operation creates the game server group, creates an Auto Scaling group in your AWS account , and establishes a link between the two groups. You can view the status of your game server groups in the GameLift console. Game server group metrics and events are emitted to Amazon CloudWatch.

    Before creating a new game server group, you must have the following:

    - An Amazon EC2 launch template that specifies how to launch Amazon EC2 instances with your game server build. For more information, see `Launching an Instance from a Launch Template <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html>`_ in the *Amazon EC2 User Guide* .
    - An IAM role that extends limited access to your AWS account to allow GameLift FleetIQ to create and interact with the Auto Scaling group. For more information, see `Create IAM roles for cross-service interaction <https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-iam-permissions-roles.html>`_ in the *GameLift FleetIQ Developer Guide* .

    To create a new game server group, specify a unique group name, IAM role and Amazon EC2 launch template, and provide a list of instance types that can be used in the group. You must also set initial maximum and minimum limits on the group's instance count. You can optionally set an Auto Scaling policy with target tracking based on a GameLift FleetIQ metric.

    Once the game server group and corresponding Auto Scaling group are created, you have full access to change the Auto Scaling group's configuration as needed. Several properties that are set when creating a game server group, including maximum/minimum size and auto-scaling policy settings, must be updated directly in the Auto Scaling group. Keep in mind that some Auto Scaling group properties are periodically updated by GameLift FleetIQ as part of its balancing activities to optimize for availability and cost.

    *Learn more*

    `GameLift FleetIQ Guide <https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html
    :cloudformationResource: AWS::GameLift::GameServerGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_game_server_group = gamelift.CfnGameServerGroup(self, "MyCfnGameServerGroup",
            game_server_group_name="gameServerGroupName",
            instance_definitions=[gamelift.CfnGameServerGroup.InstanceDefinitionProperty(
                instance_type="instanceType",
        
                # the properties below are optional
                weighted_capacity="weightedCapacity"
            )],
            role_arn="roleArn",
        
            # the properties below are optional
            auto_scaling_policy=gamelift.CfnGameServerGroup.AutoScalingPolicyProperty(
                target_tracking_configuration=gamelift.CfnGameServerGroup.TargetTrackingConfigurationProperty(
                    target_value=123
                ),
        
                # the properties below are optional
                estimated_instance_warmup=123
            ),
            balancing_strategy="balancingStrategy",
            delete_option="deleteOption",
            game_server_protection_policy="gameServerProtectionPolicy",
            launch_template=gamelift.CfnGameServerGroup.LaunchTemplateProperty(
                launch_template_id="launchTemplateId",
                launch_template_name="launchTemplateName",
                version="version"
            ),
            max_size=123,
            min_size=123,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_subnets=["vpcSubnets"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        game_server_group_name: builtins.str,
        instance_definitions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGameServerGroup.InstanceDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]]],
        role_arn: builtins.str,
        auto_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGameServerGroup.AutoScalingPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        balancing_strategy: typing.Optional[builtins.str] = None,
        delete_option: typing.Optional[builtins.str] = None,
        game_server_protection_policy: typing.Optional[builtins.str] = None,
        launch_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGameServerGroup.LaunchTemplateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param game_server_group_name: A developer-defined identifier for the game server group. The name is unique for each Region in each AWS account.
        :param instance_definitions: The set of Amazon EC2 instance types that Amazon GameLift Servers FleetIQ can use when balancing and automatically scaling instances in the corresponding Auto Scaling group.
        :param role_arn: The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) for an IAM role that allows Amazon GameLift Servers to access your Amazon EC2 Auto Scaling groups.
        :param auto_scaling_policy: Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting. The scaling policy uses the metric ``"PercentUtilizedGameServers"`` to maintain a buffer of idle game servers that can immediately accommodate new games and players. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
        :param balancing_strategy: Indicates how Amazon GameLift Servers FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group. Method options include the following: - ``SPOT_ONLY`` - Only Spot Instances are used in the game server group. If Spot Instances are unavailable or not viable for game hosting, the game server group provides no hosting capacity until Spot Instances can again be used. Until then, no new instances are started, and the existing nonviable Spot Instances are terminated (after current gameplay ends) and are not replaced. - ``SPOT_PREFERRED`` - (default value) Spot Instances are used whenever available in the game server group. If Spot Instances are unavailable, the game server group continues to provide hosting capacity by falling back to On-Demand Instances. Existing nonviable Spot Instances are terminated (after current gameplay ends) and are replaced with new On-Demand Instances. - ``ON_DEMAND_ONLY`` - Only On-Demand Instances are used in the game server group. No Spot Instances are used, even when available, while this balancing strategy is in force.
        :param delete_option: The type of delete to perform. To delete a game server group, specify the ``DeleteOption`` . Options include the following: - ``SAFE_DELETE`` – (default) Terminates the game server group and Amazon EC2 Auto Scaling group only when it has no game servers that are in ``UTILIZED`` status. - ``FORCE_DELETE`` – Terminates the game server group, including all active game servers regardless of their utilization status, and the Amazon EC2 Auto Scaling group. - ``RETAIN`` – Does a safe delete of the game server group but retains the Amazon EC2 Auto Scaling group as is.
        :param game_server_protection_policy: A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running might be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see ). An exception to this is with Spot Instances, which can be terminated by AWS regardless of protection status.
        :param launch_template: The Amazon EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group. You can specify the template using either the template name or ID. For help with creating a launch template, see `Creating a Launch Template for an Auto Scaling Group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html>`_ in the *Amazon Elastic Compute Cloud Auto Scaling User Guide* . After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs. .. epigraph:: If you specify network interfaces in your launch template, you must explicitly set the property ``AssociatePublicIpAddress`` to "true". If no network interface is specified in the launch template, Amazon GameLift Servers FleetIQ uses your account's default VPC.
        :param max_size: The maximum number of instances allowed in the Amazon EC2 Auto Scaling group. During automatic scaling events, Amazon GameLift Servers FleetIQ and EC2 do not scale up the group above this maximum. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
        :param min_size: The minimum number of instances allowed in the Amazon EC2 Auto Scaling group. During automatic scaling events, Amazon GameLift Servers FleetIQ and Amazon EC2 do not scale down the group below this minimum. In production, this value should be set to at least 1. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
        :param tags: A list of labels to assign to the new game server group resource. Tags are developer-defined key-value pairs. Tagging AWS resources is useful for resource management, access management, and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags, respectively. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
        :param vpc_subnets: A list of virtual private cloud (VPC) subnets to use with instances in the game server group. By default, all Amazon GameLift Servers FleetIQ-supported Availability Zones are used. You can use this parameter to specify VPCs that you've set up. This property cannot be updated after the game server group is created, and the corresponding Auto Scaling group will always use the property value that is set with this request, even if the Auto Scaling group is updated directly.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39a0d4e260fba686f866a885f9a542286a05d085037e114d8febabfdd92cfd24)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGameServerGroupProps(
            game_server_group_name=game_server_group_name,
            instance_definitions=instance_definitions,
            role_arn=role_arn,
            auto_scaling_policy=auto_scaling_policy,
            balancing_strategy=balancing_strategy,
            delete_option=delete_option,
            game_server_protection_policy=game_server_protection_policy,
            launch_template=launch_template,
            max_size=max_size,
            min_size=min_size,
            tags=tags,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32ac0616025cd3de739c7101cea4baa4d9d85d9755bd18a18599fd247f47e000)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3a77b5aa43581e64c5c91459806a51ceb403900395eac9fb9f2cdec42c5c7fad)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAutoScalingGroupArn")
    def attr_auto_scaling_group_arn(self) -> builtins.str:
        '''A unique identifier for the auto scaling group.

        :cloudformationAttribute: AutoScalingGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAutoScalingGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="attrGameServerGroupArn")
    def attr_game_server_group_arn(self) -> builtins.str:
        '''A unique identifier for the game server group.

        :cloudformationAttribute: GameServerGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGameServerGroupArn"))

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
    @jsii.member(jsii_name="gameServerGroupName")
    def game_server_group_name(self) -> builtins.str:
        '''A developer-defined identifier for the game server group.'''
        return typing.cast(builtins.str, jsii.get(self, "gameServerGroupName"))

    @game_server_group_name.setter
    def game_server_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89556427a3cb2e1aa05738182ce0459e80e576c3c25bd0cc1d7dc630a122bd67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gameServerGroupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="instanceDefinitions")
    def instance_definitions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.InstanceDefinitionProperty"]]]:
        '''The set of Amazon EC2 instance types that Amazon GameLift Servers FleetIQ can use when balancing and automatically scaling instances in the corresponding Auto Scaling group.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.InstanceDefinitionProperty"]]], jsii.get(self, "instanceDefinitions"))

    @instance_definitions.setter
    def instance_definitions(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.InstanceDefinitionProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__868421ea021122381c2075a524c1d4785b63637a5ae0e28ee1747043ceaf14fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceDefinitions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) for an IAM role that allows Amazon GameLift Servers to access your Amazon EC2 Auto Scaling groups.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c76aa84abc5cd589d0abb99434e1ecea33850fb0ccbb6eee11380bfa754fc482)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="autoScalingPolicy")
    def auto_scaling_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.AutoScalingPolicyProperty"]]:
        '''Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.AutoScalingPolicyProperty"]], jsii.get(self, "autoScalingPolicy"))

    @auto_scaling_policy.setter
    def auto_scaling_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.AutoScalingPolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5ee0eb377684162644f965e1106f08af9e4431bca94796da59b89abc7ffd998)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoScalingPolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="balancingStrategy")
    def balancing_strategy(self) -> typing.Optional[builtins.str]:
        '''Indicates how Amazon GameLift Servers FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "balancingStrategy"))

    @balancing_strategy.setter
    def balancing_strategy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5fc25560f0a78783f5ed8bb510e2e86e267d9629bd271a2403e866afa14e22e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "balancingStrategy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deleteOption")
    def delete_option(self) -> typing.Optional[builtins.str]:
        '''The type of delete to perform.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteOption"))

    @delete_option.setter
    def delete_option(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a84355ef62b2fd37a277a26c39b2735a06cf204ad010f5de3744a8280e5be056)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteOption", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gameServerProtectionPolicy")
    def game_server_protection_policy(self) -> typing.Optional[builtins.str]:
        '''A flag that indicates whether instances in the game server group are protected from early termination.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gameServerProtectionPolicy"))

    @game_server_protection_policy.setter
    def game_server_protection_policy(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29b538c5660178a7532c29be9d3acb184e85dfbac80460c002d5f219fa429d79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gameServerProtectionPolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.LaunchTemplateProperty"]]:
        '''The Amazon EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.LaunchTemplateProperty"]], jsii.get(self, "launchTemplate"))

    @launch_template.setter
    def launch_template(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.LaunchTemplateProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e1b30118131dd3fcdd29554603028109f41bf9f28d638ff1f26fc0de989e8b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of instances allowed in the Amazon EC2 Auto Scaling group.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSize"))

    @max_size.setter
    def max_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c07d732b195687bb610c12d0db39761316bbb61e6416116d630f224124000c66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSize", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of instances allowed in the Amazon EC2 Auto Scaling group.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7e884c21390c0adc461578e34ea9d201ce75716ffda1892218e4f39b5f6ae3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSize", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new game server group resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dba0594bea5d13fc9125228769f878f9679d696d511472809787acd5605b3e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcSubnets")
    def vpc_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of virtual private cloud (VPC) subnets to use with instances in the game server group.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSubnets"))

    @vpc_subnets.setter
    def vpc_subnets(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b4d5326a42c1fdc1afa97e1f31ad389e2aac7fbe1c4f2c6a3f614b0d23761c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSubnets", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameServerGroup.AutoScalingPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "target_tracking_configuration": "targetTrackingConfiguration",
            "estimated_instance_warmup": "estimatedInstanceWarmup",
        },
    )
    class AutoScalingPolicyProperty:
        def __init__(
            self,
            *,
            target_tracking_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnGameServerGroup.TargetTrackingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            estimated_instance_warmup: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''*This data type is used with the GameLift FleetIQ and game server groups.*.

            Configuration settings for intelligent automatic scaling that uses target tracking. After the Auto Scaling group is created, all updates to Auto Scaling policies, including changing this policy and adding or removing other policies, is done directly on the Auto Scaling group.

            :param target_tracking_configuration: Settings for a target-based scaling policy applied to Auto Scaling group. These settings are used to create a target-based policy that tracks the GameLift FleetIQ metric ``PercentUtilizedGameServers`` and specifies a target value for the metric. As player usage changes, the policy triggers to adjust the game server group capacity so that the metric returns to the target value.
            :param estimated_instance_warmup: Length of time, in seconds, it takes for a new instance to start new game server processes and register with Amazon GameLift Servers FleetIQ. Specifying a warm-up time can be useful, particularly with game servers that take a long time to start up, because it avoids prematurely starting new instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-autoscalingpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                auto_scaling_policy_property = gamelift.CfnGameServerGroup.AutoScalingPolicyProperty(
                    target_tracking_configuration=gamelift.CfnGameServerGroup.TargetTrackingConfigurationProperty(
                        target_value=123
                    ),
                
                    # the properties below are optional
                    estimated_instance_warmup=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3ca9dc4f6076efea7dd9c18ae3d0d4e330ecd050951dbb0b731443e8b262e56)
                check_type(argname="argument target_tracking_configuration", value=target_tracking_configuration, expected_type=type_hints["target_tracking_configuration"])
                check_type(argname="argument estimated_instance_warmup", value=estimated_instance_warmup, expected_type=type_hints["estimated_instance_warmup"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_tracking_configuration": target_tracking_configuration,
            }
            if estimated_instance_warmup is not None:
                self._values["estimated_instance_warmup"] = estimated_instance_warmup

        @builtins.property
        def target_tracking_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.TargetTrackingConfigurationProperty"]:
            '''Settings for a target-based scaling policy applied to Auto Scaling group.

            These settings are used to create a target-based policy that tracks the GameLift FleetIQ metric ``PercentUtilizedGameServers`` and specifies a target value for the metric. As player usage changes, the policy triggers to adjust the game server group capacity so that the metric returns to the target value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-autoscalingpolicy.html#cfn-gamelift-gameservergroup-autoscalingpolicy-targettrackingconfiguration
            '''
            result = self._values.get("target_tracking_configuration")
            assert result is not None, "Required property 'target_tracking_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.TargetTrackingConfigurationProperty"], result)

        @builtins.property
        def estimated_instance_warmup(self) -> typing.Optional[jsii.Number]:
            '''Length of time, in seconds, it takes for a new instance to start new game server processes and register with Amazon GameLift Servers FleetIQ.

            Specifying a warm-up time can be useful, particularly with game servers that take a long time to start up, because it avoids prematurely starting new instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-autoscalingpolicy.html#cfn-gamelift-gameservergroup-autoscalingpolicy-estimatedinstancewarmup
            '''
            result = self._values.get("estimated_instance_warmup")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoScalingPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameServerGroup.InstanceDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_type": "instanceType",
            "weighted_capacity": "weightedCapacity",
        },
    )
    class InstanceDefinitionProperty:
        def __init__(
            self,
            *,
            instance_type: builtins.str,
            weighted_capacity: typing.Optional[builtins.str] = None,
        ) -> None:
            '''*This data type is used with the Amazon GameLift FleetIQ and game server groups.*.

            An allowed instance type for a ``GameServerGroup`` . All game server groups must have at least two instance types defined for it. GameLift FleetIQ periodically evaluates each defined instance type for viability. It then updates the Auto Scaling group with the list of viable instance types.

            :param instance_type: An Amazon EC2 instance type designation.
            :param weighted_capacity: Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group. Instance weights are used by Amazon GameLift Servers FleetIQ to calculate the instance type's cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see `Instance Weighting <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html>`_ in the *Amazon Elastic Compute Cloud Auto Scaling User Guide* . Default value is "1".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-instancedefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                instance_definition_property = gamelift.CfnGameServerGroup.InstanceDefinitionProperty(
                    instance_type="instanceType",
                
                    # the properties below are optional
                    weighted_capacity="weightedCapacity"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b295ebcaf7cae28b09dfaf0a8c5a7fe40fd9a1dfa65423b6093711f0f56e28fc)
                check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
                check_type(argname="argument weighted_capacity", value=weighted_capacity, expected_type=type_hints["weighted_capacity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_type": instance_type,
            }
            if weighted_capacity is not None:
                self._values["weighted_capacity"] = weighted_capacity

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''An Amazon EC2 instance type designation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-instancedefinition.html#cfn-gamelift-gameservergroup-instancedefinition-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def weighted_capacity(self) -> typing.Optional[builtins.str]:
            '''Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group.

            Instance weights are used by Amazon GameLift Servers FleetIQ to calculate the instance type's cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see `Instance Weighting <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html>`_ in the *Amazon Elastic Compute Cloud Auto Scaling User Guide* . Default value is "1".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-instancedefinition.html#cfn-gamelift-gameservergroup-instancedefinition-weightedcapacity
            '''
            result = self._values.get("weighted_capacity")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameServerGroup.LaunchTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "launch_template_id": "launchTemplateId",
            "launch_template_name": "launchTemplateName",
            "version": "version",
        },
    )
    class LaunchTemplateProperty:
        def __init__(
            self,
            *,
            launch_template_id: typing.Optional[builtins.str] = None,
            launch_template_name: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''*This data type is used with the GameLift FleetIQ and game server groups.*.

            An Amazon EC2 launch template that contains configuration settings and game server code to be deployed to all instances in a game server group. The launch template is specified when creating a new game server group with ``GameServerGroup`` .

            :param launch_template_id: A unique identifier for an existing Amazon EC2 launch template.
            :param launch_template_name: A readable identifier for an existing Amazon EC2 launch template.
            :param version: The version of the Amazon EC2 launch template to use. If no version is specified, the default version will be used. With Amazon EC2, you can specify a default version for a launch template. If none is set, the default is the first version created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-launchtemplate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                launch_template_property = gamelift.CfnGameServerGroup.LaunchTemplateProperty(
                    launch_template_id="launchTemplateId",
                    launch_template_name="launchTemplateName",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__25060a9b2c2773d45ef64eabb5fbdc70d6c95644145351fecb4e3d70bd06f5e2)
                check_type(argname="argument launch_template_id", value=launch_template_id, expected_type=type_hints["launch_template_id"])
                check_type(argname="argument launch_template_name", value=launch_template_name, expected_type=type_hints["launch_template_name"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if launch_template_id is not None:
                self._values["launch_template_id"] = launch_template_id
            if launch_template_name is not None:
                self._values["launch_template_name"] = launch_template_name
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def launch_template_id(self) -> typing.Optional[builtins.str]:
            '''A unique identifier for an existing Amazon EC2 launch template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-launchtemplate.html#cfn-gamelift-gameservergroup-launchtemplate-launchtemplateid
            '''
            result = self._values.get("launch_template_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def launch_template_name(self) -> typing.Optional[builtins.str]:
            '''A readable identifier for an existing Amazon EC2 launch template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-launchtemplate.html#cfn-gamelift-gameservergroup-launchtemplate-launchtemplatename
            '''
            result = self._values.get("launch_template_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The version of the Amazon EC2 launch template to use.

            If no version is specified, the default version will be used. With Amazon EC2, you can specify a default version for a launch template. If none is set, the default is the first version created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-launchtemplate.html#cfn-gamelift-gameservergroup-launchtemplate-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LaunchTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameServerGroup.TargetTrackingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"target_value": "targetValue"},
    )
    class TargetTrackingConfigurationProperty:
        def __init__(self, *, target_value: jsii.Number) -> None:
            '''*This data type is used with the Amazon GameLift FleetIQ and game server groups.*.

            Settings for a target-based scaling policy as part of a ``GameServerGroupAutoScalingPolicy`` . These settings are used to create a target-based policy that tracks the GameLift FleetIQ metric ``"PercentUtilizedGameServers"`` and specifies a target value for the metric. As player usage changes, the policy triggers to adjust the game server group capacity so that the metric returns to the target value.

            :param target_value: Desired value to use with a game server group target-based scaling policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-targettrackingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                target_tracking_configuration_property = gamelift.CfnGameServerGroup.TargetTrackingConfigurationProperty(
                    target_value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ef13423f0408e9300989065f2e1f7a323aeaaef1367e95591fe66bbfc152a818)
                check_type(argname="argument target_value", value=target_value, expected_type=type_hints["target_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_value": target_value,
            }

        @builtins.property
        def target_value(self) -> jsii.Number:
            '''Desired value to use with a game server group target-based scaling policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-targettrackingconfiguration.html#cfn-gamelift-gameservergroup-targettrackingconfiguration-targetvalue
            '''
            result = self._values.get("target_value")
            assert result is not None, "Required property 'target_value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetTrackingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnGameServerGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "game_server_group_name": "gameServerGroupName",
        "instance_definitions": "instanceDefinitions",
        "role_arn": "roleArn",
        "auto_scaling_policy": "autoScalingPolicy",
        "balancing_strategy": "balancingStrategy",
        "delete_option": "deleteOption",
        "game_server_protection_policy": "gameServerProtectionPolicy",
        "launch_template": "launchTemplate",
        "max_size": "maxSize",
        "min_size": "minSize",
        "tags": "tags",
        "vpc_subnets": "vpcSubnets",
    },
)
class CfnGameServerGroupProps:
    def __init__(
        self,
        *,
        game_server_group_name: builtins.str,
        instance_definitions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.InstanceDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]],
        role_arn: builtins.str,
        auto_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.AutoScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        balancing_strategy: typing.Optional[builtins.str] = None,
        delete_option: typing.Optional[builtins.str] = None,
        game_server_protection_policy: typing.Optional[builtins.str] = None,
        launch_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.LaunchTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGameServerGroup``.

        :param game_server_group_name: A developer-defined identifier for the game server group. The name is unique for each Region in each AWS account.
        :param instance_definitions: The set of Amazon EC2 instance types that Amazon GameLift Servers FleetIQ can use when balancing and automatically scaling instances in the corresponding Auto Scaling group.
        :param role_arn: The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) for an IAM role that allows Amazon GameLift Servers to access your Amazon EC2 Auto Scaling groups.
        :param auto_scaling_policy: Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting. The scaling policy uses the metric ``"PercentUtilizedGameServers"`` to maintain a buffer of idle game servers that can immediately accommodate new games and players. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
        :param balancing_strategy: Indicates how Amazon GameLift Servers FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group. Method options include the following: - ``SPOT_ONLY`` - Only Spot Instances are used in the game server group. If Spot Instances are unavailable or not viable for game hosting, the game server group provides no hosting capacity until Spot Instances can again be used. Until then, no new instances are started, and the existing nonviable Spot Instances are terminated (after current gameplay ends) and are not replaced. - ``SPOT_PREFERRED`` - (default value) Spot Instances are used whenever available in the game server group. If Spot Instances are unavailable, the game server group continues to provide hosting capacity by falling back to On-Demand Instances. Existing nonviable Spot Instances are terminated (after current gameplay ends) and are replaced with new On-Demand Instances. - ``ON_DEMAND_ONLY`` - Only On-Demand Instances are used in the game server group. No Spot Instances are used, even when available, while this balancing strategy is in force.
        :param delete_option: The type of delete to perform. To delete a game server group, specify the ``DeleteOption`` . Options include the following: - ``SAFE_DELETE`` – (default) Terminates the game server group and Amazon EC2 Auto Scaling group only when it has no game servers that are in ``UTILIZED`` status. - ``FORCE_DELETE`` – Terminates the game server group, including all active game servers regardless of their utilization status, and the Amazon EC2 Auto Scaling group. - ``RETAIN`` – Does a safe delete of the game server group but retains the Amazon EC2 Auto Scaling group as is.
        :param game_server_protection_policy: A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running might be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see ). An exception to this is with Spot Instances, which can be terminated by AWS regardless of protection status.
        :param launch_template: The Amazon EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group. You can specify the template using either the template name or ID. For help with creating a launch template, see `Creating a Launch Template for an Auto Scaling Group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html>`_ in the *Amazon Elastic Compute Cloud Auto Scaling User Guide* . After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs. .. epigraph:: If you specify network interfaces in your launch template, you must explicitly set the property ``AssociatePublicIpAddress`` to "true". If no network interface is specified in the launch template, Amazon GameLift Servers FleetIQ uses your account's default VPC.
        :param max_size: The maximum number of instances allowed in the Amazon EC2 Auto Scaling group. During automatic scaling events, Amazon GameLift Servers FleetIQ and EC2 do not scale up the group above this maximum. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
        :param min_size: The minimum number of instances allowed in the Amazon EC2 Auto Scaling group. During automatic scaling events, Amazon GameLift Servers FleetIQ and Amazon EC2 do not scale down the group below this minimum. In production, this value should be set to at least 1. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
        :param tags: A list of labels to assign to the new game server group resource. Tags are developer-defined key-value pairs. Tagging AWS resources is useful for resource management, access management, and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags, respectively. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
        :param vpc_subnets: A list of virtual private cloud (VPC) subnets to use with instances in the game server group. By default, all Amazon GameLift Servers FleetIQ-supported Availability Zones are used. You can use this parameter to specify VPCs that you've set up. This property cannot be updated after the game server group is created, and the corresponding Auto Scaling group will always use the property value that is set with this request, even if the Auto Scaling group is updated directly.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_game_server_group_props = gamelift.CfnGameServerGroupProps(
                game_server_group_name="gameServerGroupName",
                instance_definitions=[gamelift.CfnGameServerGroup.InstanceDefinitionProperty(
                    instance_type="instanceType",
            
                    # the properties below are optional
                    weighted_capacity="weightedCapacity"
                )],
                role_arn="roleArn",
            
                # the properties below are optional
                auto_scaling_policy=gamelift.CfnGameServerGroup.AutoScalingPolicyProperty(
                    target_tracking_configuration=gamelift.CfnGameServerGroup.TargetTrackingConfigurationProperty(
                        target_value=123
                    ),
            
                    # the properties below are optional
                    estimated_instance_warmup=123
                ),
                balancing_strategy="balancingStrategy",
                delete_option="deleteOption",
                game_server_protection_policy="gameServerProtectionPolicy",
                launch_template=gamelift.CfnGameServerGroup.LaunchTemplateProperty(
                    launch_template_id="launchTemplateId",
                    launch_template_name="launchTemplateName",
                    version="version"
                ),
                max_size=123,
                min_size=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_subnets=["vpcSubnets"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb2b330cbc0b2bd24b542707e03f7de3d6d3afa7d8fa0efaac64771d13b95db1)
            check_type(argname="argument game_server_group_name", value=game_server_group_name, expected_type=type_hints["game_server_group_name"])
            check_type(argname="argument instance_definitions", value=instance_definitions, expected_type=type_hints["instance_definitions"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument auto_scaling_policy", value=auto_scaling_policy, expected_type=type_hints["auto_scaling_policy"])
            check_type(argname="argument balancing_strategy", value=balancing_strategy, expected_type=type_hints["balancing_strategy"])
            check_type(argname="argument delete_option", value=delete_option, expected_type=type_hints["delete_option"])
            check_type(argname="argument game_server_protection_policy", value=game_server_protection_policy, expected_type=type_hints["game_server_protection_policy"])
            check_type(argname="argument launch_template", value=launch_template, expected_type=type_hints["launch_template"])
            check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "game_server_group_name": game_server_group_name,
            "instance_definitions": instance_definitions,
            "role_arn": role_arn,
        }
        if auto_scaling_policy is not None:
            self._values["auto_scaling_policy"] = auto_scaling_policy
        if balancing_strategy is not None:
            self._values["balancing_strategy"] = balancing_strategy
        if delete_option is not None:
            self._values["delete_option"] = delete_option
        if game_server_protection_policy is not None:
            self._values["game_server_protection_policy"] = game_server_protection_policy
        if launch_template is not None:
            self._values["launch_template"] = launch_template
        if max_size is not None:
            self._values["max_size"] = max_size
        if min_size is not None:
            self._values["min_size"] = min_size
        if tags is not None:
            self._values["tags"] = tags
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def game_server_group_name(self) -> builtins.str:
        '''A developer-defined identifier for the game server group.

        The name is unique for each Region in each AWS account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-gameservergroupname
        '''
        result = self._values.get("game_server_group_name")
        assert result is not None, "Required property 'game_server_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_definitions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.InstanceDefinitionProperty]]]:
        '''The set of Amazon EC2 instance types that Amazon GameLift Servers FleetIQ can use when balancing and automatically scaling instances in the corresponding Auto Scaling group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-instancedefinitions
        '''
        result = self._values.get("instance_definitions")
        assert result is not None, "Required property 'instance_definitions' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.InstanceDefinitionProperty]]], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) for an IAM role that allows Amazon GameLift Servers to access your Amazon EC2 Auto Scaling groups.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_scaling_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.AutoScalingPolicyProperty]]:
        '''Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting.

        The scaling policy uses the metric ``"PercentUtilizedGameServers"`` to maintain a buffer of idle game servers that can immediately accommodate new games and players. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-autoscalingpolicy
        '''
        result = self._values.get("auto_scaling_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.AutoScalingPolicyProperty]], result)

    @builtins.property
    def balancing_strategy(self) -> typing.Optional[builtins.str]:
        '''Indicates how Amazon GameLift Servers FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group.

        Method options include the following:

        - ``SPOT_ONLY`` - Only Spot Instances are used in the game server group. If Spot Instances are unavailable or not viable for game hosting, the game server group provides no hosting capacity until Spot Instances can again be used. Until then, no new instances are started, and the existing nonviable Spot Instances are terminated (after current gameplay ends) and are not replaced.
        - ``SPOT_PREFERRED`` - (default value) Spot Instances are used whenever available in the game server group. If Spot Instances are unavailable, the game server group continues to provide hosting capacity by falling back to On-Demand Instances. Existing nonviable Spot Instances are terminated (after current gameplay ends) and are replaced with new On-Demand Instances.
        - ``ON_DEMAND_ONLY`` - Only On-Demand Instances are used in the game server group. No Spot Instances are used, even when available, while this balancing strategy is in force.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-balancingstrategy
        '''
        result = self._values.get("balancing_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_option(self) -> typing.Optional[builtins.str]:
        '''The type of delete to perform.

        To delete a game server group, specify the ``DeleteOption`` . Options include the following:

        - ``SAFE_DELETE`` – (default) Terminates the game server group and Amazon EC2 Auto Scaling group only when it has no game servers that are in ``UTILIZED`` status.
        - ``FORCE_DELETE`` – Terminates the game server group, including all active game servers regardless of their utilization status, and the Amazon EC2 Auto Scaling group.
        - ``RETAIN`` – Does a safe delete of the game server group but retains the Amazon EC2 Auto Scaling group as is.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-deleteoption
        '''
        result = self._values.get("delete_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def game_server_protection_policy(self) -> typing.Optional[builtins.str]:
        '''A flag that indicates whether instances in the game server group are protected from early termination.

        Unprotected instances that have active game servers running might be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see ). An exception to this is with Spot Instances, which can be terminated by AWS regardless of protection status.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-gameserverprotectionpolicy
        '''
        result = self._values.get("game_server_protection_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_template(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.LaunchTemplateProperty]]:
        '''The Amazon EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group.

        You can specify the template using either the template name or ID. For help with creating a launch template, see `Creating a Launch Template for an Auto Scaling Group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html>`_ in the *Amazon Elastic Compute Cloud Auto Scaling User Guide* . After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
        .. epigraph::

           If you specify network interfaces in your launch template, you must explicitly set the property ``AssociatePublicIpAddress`` to "true". If no network interface is specified in the launch template, Amazon GameLift Servers FleetIQ uses your account's default VPC.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-launchtemplate
        '''
        result = self._values.get("launch_template")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.LaunchTemplateProperty]], result)

    @builtins.property
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of instances allowed in the Amazon EC2 Auto Scaling group.

        During automatic scaling events, Amazon GameLift Servers FleetIQ and EC2 do not scale up the group above this maximum. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-maxsize
        '''
        result = self._values.get("max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of instances allowed in the Amazon EC2 Auto Scaling group.

        During automatic scaling events, Amazon GameLift Servers FleetIQ and Amazon EC2 do not scale down the group below this minimum. In production, this value should be set to at least 1. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-minsize
        '''
        result = self._values.get("min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new game server group resource.

        Tags are developer-defined key-value pairs. Tagging AWS resources is useful for resource management, access management, and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags, respectively. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of virtual private cloud (VPC) subnets to use with instances in the game server group.

        By default, all Amazon GameLift Servers FleetIQ-supported Availability Zones are used. You can use this parameter to specify VPCs that you've set up. This property cannot be updated after the game server group is created, and the corresponding Auto Scaling group will always use the property value that is set with this request, even if the Auto Scaling group is updated directly.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-vpcsubnets
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGameServerGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnGameSessionQueue(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnGameSessionQueue",
):
    '''The ``AWS::GameLift::GameSessionQueue`` resource creates a placement queue that processes requests for new game sessions.

    A queue uses FleetIQ algorithms to determine the best placement locations and find an available game server, then prompts the game server to start a new game session. Queues can have destinations (GameLift fleets or aliases), which determine where the queue can place new game sessions. A queue can have destinations with varied fleet type (Spot and On-Demand), instance type, and AWS Region .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html
    :cloudformationResource: AWS::GameLift::GameSessionQueue
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_game_session_queue = gamelift.CfnGameSessionQueue(self, "MyCfnGameSessionQueue",
            name="name",
        
            # the properties below are optional
            custom_event_data="customEventData",
            destinations=[gamelift.CfnGameSessionQueue.DestinationProperty(
                destination_arn="destinationArn"
            )],
            filter_configuration=gamelift.CfnGameSessionQueue.FilterConfigurationProperty(
                allowed_locations=["allowedLocations"]
            ),
            notification_target="notificationTarget",
            player_latency_policies=[gamelift.CfnGameSessionQueue.PlayerLatencyPolicyProperty(
                maximum_individual_player_latency_milliseconds=123,
                policy_duration_seconds=123
            )],
            priority_configuration=gamelift.CfnGameSessionQueue.PriorityConfigurationProperty(
                location_order=["locationOrder"],
                priority_order=["priorityOrder"]
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            timeout_in_seconds=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        custom_event_data: typing.Optional[builtins.str] = None,
        destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGameSessionQueue.DestinationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        filter_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGameSessionQueue.FilterConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        notification_target: typing.Optional[builtins.str] = None,
        player_latency_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGameSessionQueue.PlayerLatencyPolicyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        priority_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGameSessionQueue.PriorityConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A descriptive label that is associated with game session queue. Queue names must be unique within each Region.
        :param custom_event_data: Information to be added to all events that are related to this game session queue.
        :param destinations: A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue. Destinations are identified by either a fleet ARN or a fleet alias ARN, and are listed in order of placement preference.
        :param filter_configuration: A list of locations where a queue is allowed to place new game sessions. Locations are specified in the form of AWS Region codes, such as ``us-west-2`` . If this parameter is not set, game sessions can be placed in any queue location.
        :param notification_target: An SNS topic ARN that is set up to receive game session placement notifications. See `Setting up notifications for game session placement <https://docs.aws.amazon.com/gamelift/latest/developerguide/queue-notification.html>`_ .
        :param player_latency_policies: A set of policies that enforce a sliding cap on player latency when processing game sessions placement requests. Use multiple policies to gradually relax the cap over time if Amazon GameLift Servers can't make a placement. Policies are evaluated in order starting with the lowest maximum latency value.
        :param priority_configuration: Custom settings to use when prioritizing destinations and locations for game session placements. This configuration replaces the FleetIQ default prioritization process. Priority types that are not explicitly named will be automatically applied at the end of the prioritization process.
        :param tags: A list of labels to assign to the new game session queue resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
        :param timeout_in_seconds: The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a ``TIMED_OUT`` status. If you don't specify a request timeout, the queue uses a default value.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2435e37790a5987d49478948c0c1ac36c9e463fa29441c46ba0aa4d567f2c585)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGameSessionQueueProps(
            name=name,
            custom_event_data=custom_event_data,
            destinations=destinations,
            filter_configuration=filter_configuration,
            notification_target=notification_target,
            player_latency_policies=player_latency_policies,
            priority_configuration=priority_configuration,
            tags=tags,
            timeout_in_seconds=timeout_in_seconds,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cc05027a8472775374b6846f6c9ab499cc41f64fa8ed31ccbfd79e142b8b76d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b257e875617af0371cc9d2c1574fb2ba9c0e4ecbacf958d56eabd8a77d1fa023)
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
        '''The unique Amazon Resource Name (ARN) for the ``GameSessionQueue`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''A descriptive label that is associated with a game session queue.

        Names are unique within each Region.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
        '''A descriptive label that is associated with game session queue.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac381d2dd8ded0682b62f79246a99597b2aca0600afaa30c9f48b5f1411bbfa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="customEventData")
    def custom_event_data(self) -> typing.Optional[builtins.str]:
        '''Information to be added to all events that are related to this game session queue.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customEventData"))

    @custom_event_data.setter
    def custom_event_data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d8260843224b7180260627c762aaa0ae5afbcd912f5da71a3c576430e069f9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customEventData", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="destinations")
    def destinations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.DestinationProperty"]]]]:
        '''A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.DestinationProperty"]]]], jsii.get(self, "destinations"))

    @destinations.setter
    def destinations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.DestinationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f656db0c32504c821ba5c5d5067bac317db7def96a39500c5847a853576e95ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="filterConfiguration")
    def filter_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.FilterConfigurationProperty"]]:
        '''A list of locations where a queue is allowed to place new game sessions.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.FilterConfigurationProperty"]], jsii.get(self, "filterConfiguration"))

    @filter_configuration.setter
    def filter_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.FilterConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08e5b9b16ae8732de19b82da87c71cb00a9d06d7a37c8d217314158c063bf0f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="notificationTarget")
    def notification_target(self) -> typing.Optional[builtins.str]:
        '''An SNS topic ARN that is set up to receive game session placement notifications.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTarget"))

    @notification_target.setter
    def notification_target(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f838580d46a0a1a08c09d8b8b17de066bfb74896289f61432e755d32429e2a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationTarget", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="playerLatencyPolicies")
    def player_latency_policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.PlayerLatencyPolicyProperty"]]]]:
        '''A set of policies that enforce a sliding cap on player latency when processing game sessions placement requests.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.PlayerLatencyPolicyProperty"]]]], jsii.get(self, "playerLatencyPolicies"))

    @player_latency_policies.setter
    def player_latency_policies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.PlayerLatencyPolicyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3da0f541db3f4dba488790dc678e2dd0872a5271bf05bb0ddcb181884f5dfb80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "playerLatencyPolicies", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="priorityConfiguration")
    def priority_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.PriorityConfigurationProperty"]]:
        '''Custom settings to use when prioritizing destinations and locations for game session placements.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.PriorityConfigurationProperty"]], jsii.get(self, "priorityConfiguration"))

    @priority_configuration.setter
    def priority_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.PriorityConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__622dc07e672d46f719db763d6bf2dec499f84a17b72186d593df03f3fcb1ae7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priorityConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new game session queue resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3a8c431c366d3fa711cfb42cebf2d1647b8f2a1a5e129b5536c91cdf0135eb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="timeoutInSeconds")
    def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''The maximum time, in seconds, that a new game session placement request remains in the queue.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInSeconds"))

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ad24ec0156a0a24d8fe08ecf8470df28f9f1501a3ab442e887e2d1c5ef03df4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutInSeconds", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameSessionQueue.DestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"destination_arn": "destinationArn"},
    )
    class DestinationProperty:
        def __init__(
            self,
            *,
            destination_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param destination_arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-destination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                destination_property = gamelift.CfnGameSessionQueue.DestinationProperty(
                    destination_arn="destinationArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9d1ad7f562ade1312178a63d9196a21119d0e6500b9d651931481a59d709d462)
                check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_arn is not None:
                self._values["destination_arn"] = destination_arn

        @builtins.property
        def destination_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-destination.html#cfn-gamelift-gamesessionqueue-destination-destinationarn
            '''
            result = self._values.get("destination_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameSessionQueue.FilterConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"allowed_locations": "allowedLocations"},
    )
    class FilterConfigurationProperty:
        def __init__(
            self,
            *,
            allowed_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A list of fleet locations where a game session queue can place new game sessions.

            You can use a filter to temporarily turn off placements for specific locations. For queues that have multi-location fleets, you can use a filter configuration allow placement with some, but not all of these locations.

            :param allowed_locations: A list of locations to allow game session placement in, in the form of AWS Region codes such as ``us-west-2`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-filterconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                filter_configuration_property = gamelift.CfnGameSessionQueue.FilterConfigurationProperty(
                    allowed_locations=["allowedLocations"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a18c067b373a2989add73f26fd5a7da221d485dae82bf0842dcedf8017b6ad5f)
                check_type(argname="argument allowed_locations", value=allowed_locations, expected_type=type_hints["allowed_locations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allowed_locations is not None:
                self._values["allowed_locations"] = allowed_locations

        @builtins.property
        def allowed_locations(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of locations to allow game session placement in, in the form of AWS Region codes such as ``us-west-2`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-filterconfiguration.html#cfn-gamelift-gamesessionqueue-filterconfiguration-allowedlocations
            '''
            result = self._values.get("allowed_locations")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameSessionQueue.GameSessionQueueDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"destination_arn": "destinationArn"},
    )
    class GameSessionQueueDestinationProperty:
        def __init__(
            self,
            *,
            destination_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A fleet or alias designated in a game session queue.

            Queues fulfill requests for new game sessions by placing a new game session on any of the queue's destinations.

            :param destination_arn: The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-gamesessionqueuedestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                game_session_queue_destination_property = gamelift.CfnGameSessionQueue.GameSessionQueueDestinationProperty(
                    destination_arn="destinationArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__682a2ca85600f7cf3e8fc279fa7f5c2ecab05f65cc96301b5afab09b2da5c684)
                check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_arn is not None:
                self._values["destination_arn"] = destination_arn

        @builtins.property
        def destination_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias.

            ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-gamesessionqueuedestination.html#cfn-gamelift-gamesessionqueue-gamesessionqueuedestination-destinationarn
            '''
            result = self._values.get("destination_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GameSessionQueueDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameSessionQueue.PlayerLatencyPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "maximum_individual_player_latency_milliseconds": "maximumIndividualPlayerLatencyMilliseconds",
            "policy_duration_seconds": "policyDurationSeconds",
        },
    )
    class PlayerLatencyPolicyProperty:
        def __init__(
            self,
            *,
            maximum_individual_player_latency_milliseconds: typing.Optional[jsii.Number] = None,
            policy_duration_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The queue setting that determines the highest latency allowed for individual players when placing a game session.

            When a latency policy is in force, a game session cannot be placed with any fleet in a Region where a player reports latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.

            :param maximum_individual_player_latency_milliseconds: The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
            :param policy_duration_seconds: The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-playerlatencypolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                player_latency_policy_property = gamelift.CfnGameSessionQueue.PlayerLatencyPolicyProperty(
                    maximum_individual_player_latency_milliseconds=123,
                    policy_duration_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7a9bd74ee679564c60f66c08f4f2d7739a8abfa4c61e93feedbd8457081f585)
                check_type(argname="argument maximum_individual_player_latency_milliseconds", value=maximum_individual_player_latency_milliseconds, expected_type=type_hints["maximum_individual_player_latency_milliseconds"])
                check_type(argname="argument policy_duration_seconds", value=policy_duration_seconds, expected_type=type_hints["policy_duration_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if maximum_individual_player_latency_milliseconds is not None:
                self._values["maximum_individual_player_latency_milliseconds"] = maximum_individual_player_latency_milliseconds
            if policy_duration_seconds is not None:
                self._values["policy_duration_seconds"] = policy_duration_seconds

        @builtins.property
        def maximum_individual_player_latency_milliseconds(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The maximum latency value that is allowed for any player, in milliseconds.

            All policies must have a value set for this property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-playerlatencypolicy.html#cfn-gamelift-gamesessionqueue-playerlatencypolicy-maximumindividualplayerlatencymilliseconds
            '''
            result = self._values.get("maximum_individual_player_latency_milliseconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def policy_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''The length of time, in seconds, that the policy is enforced while placing a new game session.

            A null value for this property means that the policy is enforced until the queue times out.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-playerlatencypolicy.html#cfn-gamelift-gamesessionqueue-playerlatencypolicy-policydurationseconds
            '''
            result = self._values.get("policy_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PlayerLatencyPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameSessionQueue.PriorityConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "location_order": "locationOrder",
            "priority_order": "priorityOrder",
        },
    )
    class PriorityConfigurationProperty:
        def __init__(
            self,
            *,
            location_order: typing.Optional[typing.Sequence[builtins.str]] = None,
            priority_order: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Custom prioritization settings for use by a game session queue when placing new game sessions with available game servers.

            When defined, this configuration replaces the default FleetIQ prioritization process, which is as follows:

            - If player latency data is included in a game session request, destinations and locations are prioritized first based on lowest average latency (1), then on lowest hosting cost (2), then on destination list order (3), and finally on location (alphabetical) (4). This approach ensures that the queue's top priority is to place game sessions where average player latency is lowest, and--if latency is the same--where the hosting cost is less, etc.
            - If player latency data is not included, destinations and locations are prioritized first on destination list order (1), and then on location (alphabetical) (2). This approach ensures that the queue's top priority is to place game sessions on the first destination fleet listed. If that fleet has multiple locations, the game session is placed on the first location (when listed alphabetically).

            Changing the priority order will affect how game sessions are placed.

            :param location_order: The prioritization order to use for fleet locations, when the ``PriorityOrder`` property includes ``LOCATION`` . Locations can include AWS Region codes (such as ``us-west-2`` ), local zones, and custom locations (for Anywhere fleets). Each location must be listed only once. For details, see `Amazon GameLift Servers service locations. <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html>`_
            :param priority_order: A custom sequence to use when prioritizing where to place new game sessions. Each priority type is listed once. - ``LATENCY`` -- Amazon GameLift Servers prioritizes locations where the average player latency is lowest. Player latency data is provided in each game session placement request. - ``COST`` -- Amazon GameLift Servers prioritizes queue destinations with the lowest current hosting costs. Cost is evaluated based on the destination's location, instance type, and fleet type (Spot or On-Demand). - ``DESTINATION`` -- Amazon GameLift Servers prioritizes based on the list order of destinations in the queue configuration. - ``LOCATION`` -- Amazon GameLift Servers prioritizes based on the provided order of locations, as defined in ``LocationOrder`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-priorityconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                priority_configuration_property = gamelift.CfnGameSessionQueue.PriorityConfigurationProperty(
                    location_order=["locationOrder"],
                    priority_order=["priorityOrder"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bffce6e10d5ec1968a817a7df177891e44b6ec986ec424c92d4e71dd599b36ac)
                check_type(argname="argument location_order", value=location_order, expected_type=type_hints["location_order"])
                check_type(argname="argument priority_order", value=priority_order, expected_type=type_hints["priority_order"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if location_order is not None:
                self._values["location_order"] = location_order
            if priority_order is not None:
                self._values["priority_order"] = priority_order

        @builtins.property
        def location_order(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The prioritization order to use for fleet locations, when the ``PriorityOrder`` property includes ``LOCATION`` .

            Locations can include AWS Region codes (such as ``us-west-2`` ), local zones, and custom locations (for Anywhere fleets). Each location must be listed only once. For details, see `Amazon GameLift Servers service locations. <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-priorityconfiguration.html#cfn-gamelift-gamesessionqueue-priorityconfiguration-locationorder
            '''
            result = self._values.get("location_order")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def priority_order(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A custom sequence to use when prioritizing where to place new game sessions. Each priority type is listed once.

            - ``LATENCY`` -- Amazon GameLift Servers prioritizes locations where the average player latency is lowest. Player latency data is provided in each game session placement request.
            - ``COST`` -- Amazon GameLift Servers prioritizes queue destinations with the lowest current hosting costs. Cost is evaluated based on the destination's location, instance type, and fleet type (Spot or On-Demand).
            - ``DESTINATION`` -- Amazon GameLift Servers prioritizes based on the list order of destinations in the queue configuration.
            - ``LOCATION`` -- Amazon GameLift Servers prioritizes based on the provided order of locations, as defined in ``LocationOrder`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-priorityconfiguration.html#cfn-gamelift-gamesessionqueue-priorityconfiguration-priorityorder
            '''
            result = self._values.get("priority_order")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PriorityConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnGameSessionQueueProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "custom_event_data": "customEventData",
        "destinations": "destinations",
        "filter_configuration": "filterConfiguration",
        "notification_target": "notificationTarget",
        "player_latency_policies": "playerLatencyPolicies",
        "priority_configuration": "priorityConfiguration",
        "tags": "tags",
        "timeout_in_seconds": "timeoutInSeconds",
    },
)
class CfnGameSessionQueueProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        custom_event_data: typing.Optional[builtins.str] = None,
        destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.DestinationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        filter_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.FilterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        notification_target: typing.Optional[builtins.str] = None,
        player_latency_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.PlayerLatencyPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        priority_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.PriorityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnGameSessionQueue``.

        :param name: A descriptive label that is associated with game session queue. Queue names must be unique within each Region.
        :param custom_event_data: Information to be added to all events that are related to this game session queue.
        :param destinations: A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue. Destinations are identified by either a fleet ARN or a fleet alias ARN, and are listed in order of placement preference.
        :param filter_configuration: A list of locations where a queue is allowed to place new game sessions. Locations are specified in the form of AWS Region codes, such as ``us-west-2`` . If this parameter is not set, game sessions can be placed in any queue location.
        :param notification_target: An SNS topic ARN that is set up to receive game session placement notifications. See `Setting up notifications for game session placement <https://docs.aws.amazon.com/gamelift/latest/developerguide/queue-notification.html>`_ .
        :param player_latency_policies: A set of policies that enforce a sliding cap on player latency when processing game sessions placement requests. Use multiple policies to gradually relax the cap over time if Amazon GameLift Servers can't make a placement. Policies are evaluated in order starting with the lowest maximum latency value.
        :param priority_configuration: Custom settings to use when prioritizing destinations and locations for game session placements. This configuration replaces the FleetIQ default prioritization process. Priority types that are not explicitly named will be automatically applied at the end of the prioritization process.
        :param tags: A list of labels to assign to the new game session queue resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
        :param timeout_in_seconds: The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a ``TIMED_OUT`` status. If you don't specify a request timeout, the queue uses a default value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_game_session_queue_props = gamelift.CfnGameSessionQueueProps(
                name="name",
            
                # the properties below are optional
                custom_event_data="customEventData",
                destinations=[gamelift.CfnGameSessionQueue.DestinationProperty(
                    destination_arn="destinationArn"
                )],
                filter_configuration=gamelift.CfnGameSessionQueue.FilterConfigurationProperty(
                    allowed_locations=["allowedLocations"]
                ),
                notification_target="notificationTarget",
                player_latency_policies=[gamelift.CfnGameSessionQueue.PlayerLatencyPolicyProperty(
                    maximum_individual_player_latency_milliseconds=123,
                    policy_duration_seconds=123
                )],
                priority_configuration=gamelift.CfnGameSessionQueue.PriorityConfigurationProperty(
                    location_order=["locationOrder"],
                    priority_order=["priorityOrder"]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                timeout_in_seconds=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b18cdd98f5e3e7424d6d930e416c9690c2e3cdcc56ac70f4688a8984ea0e8b7)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument custom_event_data", value=custom_event_data, expected_type=type_hints["custom_event_data"])
            check_type(argname="argument destinations", value=destinations, expected_type=type_hints["destinations"])
            check_type(argname="argument filter_configuration", value=filter_configuration, expected_type=type_hints["filter_configuration"])
            check_type(argname="argument notification_target", value=notification_target, expected_type=type_hints["notification_target"])
            check_type(argname="argument player_latency_policies", value=player_latency_policies, expected_type=type_hints["player_latency_policies"])
            check_type(argname="argument priority_configuration", value=priority_configuration, expected_type=type_hints["priority_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeout_in_seconds", value=timeout_in_seconds, expected_type=type_hints["timeout_in_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if custom_event_data is not None:
            self._values["custom_event_data"] = custom_event_data
        if destinations is not None:
            self._values["destinations"] = destinations
        if filter_configuration is not None:
            self._values["filter_configuration"] = filter_configuration
        if notification_target is not None:
            self._values["notification_target"] = notification_target
        if player_latency_policies is not None:
            self._values["player_latency_policies"] = player_latency_policies
        if priority_configuration is not None:
            self._values["priority_configuration"] = priority_configuration
        if tags is not None:
            self._values["tags"] = tags
        if timeout_in_seconds is not None:
            self._values["timeout_in_seconds"] = timeout_in_seconds

    @builtins.property
    def name(self) -> builtins.str:
        '''A descriptive label that is associated with game session queue.

        Queue names must be unique within each Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_event_data(self) -> typing.Optional[builtins.str]:
        '''Information to be added to all events that are related to this game session queue.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-customeventdata
        '''
        result = self._values.get("custom_event_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destinations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.DestinationProperty]]]]:
        '''A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue.

        Destinations are identified by either a fleet ARN or a fleet alias ARN, and are listed in order of placement preference.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-destinations
        '''
        result = self._values.get("destinations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.DestinationProperty]]]], result)

    @builtins.property
    def filter_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.FilterConfigurationProperty]]:
        '''A list of locations where a queue is allowed to place new game sessions.

        Locations are specified in the form of AWS Region codes, such as ``us-west-2`` . If this parameter is not set, game sessions can be placed in any queue location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-filterconfiguration
        '''
        result = self._values.get("filter_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.FilterConfigurationProperty]], result)

    @builtins.property
    def notification_target(self) -> typing.Optional[builtins.str]:
        '''An SNS topic ARN that is set up to receive game session placement notifications.

        See `Setting up notifications for game session placement <https://docs.aws.amazon.com/gamelift/latest/developerguide/queue-notification.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-notificationtarget
        '''
        result = self._values.get("notification_target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def player_latency_policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.PlayerLatencyPolicyProperty]]]]:
        '''A set of policies that enforce a sliding cap on player latency when processing game sessions placement requests.

        Use multiple policies to gradually relax the cap over time if Amazon GameLift Servers can't make a placement. Policies are evaluated in order starting with the lowest maximum latency value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-playerlatencypolicies
        '''
        result = self._values.get("player_latency_policies")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.PlayerLatencyPolicyProperty]]]], result)

    @builtins.property
    def priority_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.PriorityConfigurationProperty]]:
        '''Custom settings to use when prioritizing destinations and locations for game session placements.

        This configuration replaces the FleetIQ default prioritization process. Priority types that are not explicitly named will be automatically applied at the end of the prioritization process.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-priorityconfiguration
        '''
        result = self._values.get("priority_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.PriorityConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new game session queue resource.

        Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''The maximum time, in seconds, that a new game session placement request remains in the queue.

        When a request exceeds this time, the game session placement changes to a ``TIMED_OUT`` status. If you don't specify a request timeout, the queue uses a default value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-timeoutinseconds
        '''
        result = self._values.get("timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGameSessionQueueProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLocation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnLocation",
):
    '''The AWS::GameLift::Location resource creates a custom location for use in an Anywhere fleet.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-location.html
    :cloudformationResource: AWS::GameLift::Location
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_location = gamelift.CfnLocation(self, "MyCfnLocation",
            location_name="locationName",
        
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
        location_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param location_name: A descriptive name for the custom location.
        :param tags: A list of labels to assign to the new resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management, and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Rareference* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__404fc5857cf63bdcf757784b5c810e73ce1c99d8d82c264eec7a145724580816)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLocationProps(location_name=location_name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d95943640733fe4e543a0c2a9e0a647a118d84274c6945f59f0598a9585e4a4b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a18532e89ee9aa9c91c15cc19d2c9f2345325702005b9a2708e43204329266ae)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''A unique identifier for the custom location.

        For example, ``arn:aws:gamelift:[region]::location/location-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`` .

        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

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
    @jsii.member(jsii_name="locationName")
    def location_name(self) -> builtins.str:
        '''A descriptive name for the custom location.'''
        return typing.cast(builtins.str, jsii.get(self, "locationName"))

    @location_name.setter
    def location_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50f9bf4f89ef7693448c9209f894d6900bab55884642fc136222c211e82f3015)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db22dc038d314307a9d7182d88d8959bd024bf2feff9aee7f03deba1df46ca5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnLocationProps",
    jsii_struct_bases=[],
    name_mapping={"location_name": "locationName", "tags": "tags"},
)
class CfnLocationProps:
    def __init__(
        self,
        *,
        location_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLocation``.

        :param location_name: A descriptive name for the custom location.
        :param tags: A list of labels to assign to the new resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management, and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Rareference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-location.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_location_props = gamelift.CfnLocationProps(
                location_name="locationName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98ffffd954dd9a648cdd22ea8069e64a916e69b5690bde3de5bb865f1a555e5d)
            check_type(argname="argument location_name", value=location_name, expected_type=type_hints["location_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location_name": location_name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def location_name(self) -> builtins.str:
        '''A descriptive name for the custom location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-location.html#cfn-gamelift-location-locationname
        '''
        result = self._values.get("location_name")
        assert result is not None, "Required property 'location_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new resource.

        Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management, and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Rareference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-location.html#cfn-gamelift-location-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnMatchmakingConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnMatchmakingConfiguration",
):
    '''The ``AWS::GameLift::MatchmakingConfiguration`` resource defines a new matchmaking configuration for use with FlexMatch.

    Whether you're using FlexMatch with GameLift hosting or as a standalone matchmaking service, the matchmaking configuration sets out rules for matching players and forming teams. If you're using GameLift hosting, it also defines how to start game sessions for each match. Your matchmaking system can use multiple configurations to handle different game scenarios. All matchmaking requests identify the matchmaking configuration to use and provide player attributes that are consistent with that configuration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html
    :cloudformationResource: AWS::GameLift::MatchmakingConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_matchmaking_configuration = gamelift.CfnMatchmakingConfiguration(self, "MyCfnMatchmakingConfiguration",
            acceptance_required=False,
            name="name",
            request_timeout_seconds=123,
            rule_set_name="ruleSetName",
        
            # the properties below are optional
            acceptance_timeout_seconds=123,
            additional_player_count=123,
            backfill_mode="backfillMode",
            creation_time="creationTime",
            custom_event_data="customEventData",
            description="description",
            flex_match_mode="flexMatchMode",
            game_properties=[gamelift.CfnMatchmakingConfiguration.GamePropertyProperty(
                key="key",
                value="value"
            )],
            game_session_data="gameSessionData",
            game_session_queue_arns=["gameSessionQueueArns"],
            notification_target="notificationTarget",
            rule_set_arn="ruleSetArn",
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
        acceptance_required: typing.Union[builtins.bool, _IResolvable_da3f097b],
        name: builtins.str,
        request_timeout_seconds: jsii.Number,
        rule_set_name: builtins.str,
        acceptance_timeout_seconds: typing.Optional[jsii.Number] = None,
        additional_player_count: typing.Optional[jsii.Number] = None,
        backfill_mode: typing.Optional[builtins.str] = None,
        creation_time: typing.Optional[builtins.str] = None,
        custom_event_data: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        flex_match_mode: typing.Optional[builtins.str] = None,
        game_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMatchmakingConfiguration.GamePropertyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        game_session_data: typing.Optional[builtins.str] = None,
        game_session_queue_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        notification_target: typing.Optional[builtins.str] = None,
        rule_set_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param acceptance_required: A flag that determines whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to ``TRUE`` . With this option enabled, matchmaking tickets use the status ``REQUIRES_ACCEPTANCE`` to indicate when a completed potential match is waiting for player acceptance.
        :param name: A unique identifier for the matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.
        :param request_timeout_seconds: The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.
        :param rule_set_name: A unique identifier for the matchmaking rule set to use with this configuration. You can use either the rule set name or ARN value. A matchmaking configuration can only use rule sets that are defined in the same Region.
        :param acceptance_timeout_seconds: The length of time (in seconds) to wait for players to accept a proposed match, if acceptance is required.
        :param additional_player_count: The number of player slots in a match to keep open for future players. For example, if the configuration's rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match. This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param backfill_mode: The method used to backfill game sessions that are created with this matchmaking configuration. Specify ``MANUAL`` when your game manages backfill requests manually or does not use the match backfill feature. Specify ``AUTOMATIC`` to have GameLift create a ``StartMatchBackfill`` request whenever a game session has one or more open slots. Learn more about manual and automatic backfill in `Backfill Existing Games with FlexMatch <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-backfill.html>`_ . Automatic backfill is not available when ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param creation_time: A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example ``"1469498468.057"`` ).
        :param custom_event_data: Information to add to all events related to the matchmaking configuration.
        :param description: A description for the matchmaking configuration.
        :param flex_match_mode: Indicates whether this matchmaking configuration is being used with Amazon GameLift Servers hosting or as a standalone matchmaking solution. - *STANDALONE* - FlexMatch forms matches and returns match information, including players and team assignments, in a `MatchmakingSucceeded <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html#match-events-matchmakingsucceeded>`_ event. - *WITH_QUEUE* - FlexMatch forms matches and uses the specified Amazon GameLift Servers queue to start a game session for the match.
        :param game_properties: A set of custom properties for a game session, formatted as key-value pairs. These properties are passed to a game server process with a request to start a new game session. See `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`_ . This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param game_session_data: A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. See `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`_ . This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param game_session_queue_arns: The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to a Amazon GameLift Servers game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is ``arn:aws:gamelift:<region>::gamesessionqueue/<queue name>`` . Queues can be located in any Region. Queues are used to start new Amazon GameLift Servers-hosted game sessions for matches that are created with this matchmaking configuration. If ``FlexMatchMode`` is set to ``STANDALONE`` , do not set this parameter.
        :param notification_target: An SNS topic ARN that is set up to receive matchmaking notifications. See `Setting up notifications for matchmaking <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html>`_ for more information.
        :param rule_set_arn: The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) associated with the GameLift matchmaking rule set resource that this configuration uses.
        :param tags: A list of labels to assign to the new matchmaking configuration resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5991dfcf120df852e2fd4ce6291a275a648645c817c923b70181ea8f56e61574)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMatchmakingConfigurationProps(
            acceptance_required=acceptance_required,
            name=name,
            request_timeout_seconds=request_timeout_seconds,
            rule_set_name=rule_set_name,
            acceptance_timeout_seconds=acceptance_timeout_seconds,
            additional_player_count=additional_player_count,
            backfill_mode=backfill_mode,
            creation_time=creation_time,
            custom_event_data=custom_event_data,
            description=description,
            flex_match_mode=flex_match_mode,
            game_properties=game_properties,
            game_session_data=game_session_data,
            game_session_queue_arns=game_session_queue_arns,
            notification_target=notification_target,
            rule_set_arn=rule_set_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97ef86c5f161a3f7e4debb1e365142a6bed6fcfa0560f9575501529b34dee619)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f090e32e05cfaeb363b1750dd5ec26197130f385a7f9bddfe37da83c98c9462c)
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
        '''The unique Amazon Resource Name (ARN) for the ``MatchmakingConfiguration`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The ``MatchmakingConfiguration`` name, which is unique.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
    @jsii.member(jsii_name="acceptanceRequired")
    def acceptance_required(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''A flag that determines whether a match that was created with this configuration must be accepted by the matched players.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "acceptanceRequired"))

    @acceptance_required.setter
    def acceptance_required(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22e4fb0874509d31426b22f3ffefc8f7d3c205a887689be775fe8344351315b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptanceRequired", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A unique identifier for the matchmaking configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50207e3d686076a987e377c81a96125dab3ab3f1620c58f788384cb08b17f088)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="requestTimeoutSeconds")
    def request_timeout_seconds(self) -> jsii.Number:
        '''The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out.'''
        return typing.cast(jsii.Number, jsii.get(self, "requestTimeoutSeconds"))

    @request_timeout_seconds.setter
    def request_timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a26beba0933992ac93ce4a627f18fa7a10ad26da6a35a99b1e377d5afa493b78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestTimeoutSeconds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ruleSetName")
    def rule_set_name(self) -> builtins.str:
        '''A unique identifier for the matchmaking rule set to use with this configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleSetName"))

    @rule_set_name.setter
    def rule_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e22642273b822aeccc60cfa3d9595fa6bc154a168c63626eefb68d6a746ffad0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleSetName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="acceptanceTimeoutSeconds")
    def acceptance_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''The length of time (in seconds) to wait for players to accept a proposed match, if acceptance is required.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "acceptanceTimeoutSeconds"))

    @acceptance_timeout_seconds.setter
    def acceptance_timeout_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c28ab17b4e7b606d702229a14a7e46b7f9e86cb64d8dc6e0585fbcb058d0b242)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptanceTimeoutSeconds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="additionalPlayerCount")
    def additional_player_count(self) -> typing.Optional[jsii.Number]:
        '''The number of player slots in a match to keep open for future players.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "additionalPlayerCount"))

    @additional_player_count.setter
    def additional_player_count(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92699d7bd325a7ad10bdb62647176ac995f2c17688efde0d91661c8f0815eda7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalPlayerCount", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="backfillMode")
    def backfill_mode(self) -> typing.Optional[builtins.str]:
        '''The method used to backfill game sessions that are created with this matchmaking configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backfillMode"))

    @backfill_mode.setter
    def backfill_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b63753d38be440877984c0aa86a81bd07b6d2ce3aec33c9d8dd34c0ccde356c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backfillMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> typing.Optional[builtins.str]:
        '''A time stamp indicating when this data object was created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "creationTime"))

    @creation_time.setter
    def creation_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31d3fbc33faadd8b20143f6719f4142fc516a089f7e572e974783578c57954d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creationTime", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="customEventData")
    def custom_event_data(self) -> typing.Optional[builtins.str]:
        '''Information to add to all events related to the matchmaking configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customEventData"))

    @custom_event_data.setter
    def custom_event_data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fac8d8c2d6825f23811aeea9f440bf664e97a02184ef417460a8d92056b2fb27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customEventData", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the matchmaking configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a956b02b663049817a64e32bfd1f09f9857feedac28f4eca2d36141c326cc5e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flexMatchMode")
    def flex_match_mode(self) -> typing.Optional[builtins.str]:
        '''Indicates whether this matchmaking configuration is being used with Amazon GameLift Servers hosting or as a standalone matchmaking solution.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flexMatchMode"))

    @flex_match_mode.setter
    def flex_match_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a047908ff094a894704a6965c30654d87bb94e2aff3bd57abb16673fd6e98318)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flexMatchMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gameProperties")
    def game_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMatchmakingConfiguration.GamePropertyProperty"]]]]:
        '''A set of custom properties for a game session, formatted as key-value pairs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMatchmakingConfiguration.GamePropertyProperty"]]]], jsii.get(self, "gameProperties"))

    @game_properties.setter
    def game_properties(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMatchmakingConfiguration.GamePropertyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0086331ec6c1fe164de53253519ecf95f522026cd3c4b9b2c0b16c300b99ceb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gameProperties", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gameSessionData")
    def game_session_data(self) -> typing.Optional[builtins.str]:
        '''A set of custom game session properties, formatted as a single string value.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gameSessionData"))

    @game_session_data.setter
    def game_session_data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad31d919af9b1fb2de550bd5b00fcb306185a91f87127b6250e135a48937df4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gameSessionData", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gameSessionQueueArns")
    def game_session_queue_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to a Amazon GameLift Servers game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is ``arn:aws:gamelift:<region>::gamesessionqueue/<queue name>`` . Queues can be located in any Region. Queues are used to start new Amazon GameLift Servers-hosted game sessions for matches that are created with this matchmaking configuration. If ``FlexMatchMode`` is set to ``STANDALONE`` , do not set this parameter.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "gameSessionQueueArns"))

    @game_session_queue_arns.setter
    def game_session_queue_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beae0e02206ffef8c392d9dd656f3a5ac2476b679628f1884cf15a4e8092c49d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gameSessionQueueArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="notificationTarget")
    def notification_target(self) -> typing.Optional[builtins.str]:
        '''An SNS topic ARN that is set up to receive matchmaking notifications.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTarget"))

    @notification_target.setter
    def notification_target(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83e843d11896164f9fbc52e89ade017c17b6cce0da297e20b5f554281c6c8e7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationTarget", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ruleSetArn")
    def rule_set_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) associated with the GameLift matchmaking rule set resource that this configuration uses.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleSetArn"))

    @rule_set_arn.setter
    def rule_set_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b47741240f35249cfb706757b5199576646836e89e8f9fcd9e6bb884d238a3c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleSetArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new matchmaking configuration resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9777adaa1c91123290fcf69dfad3f29c9d5affe68344eb61a6147f7c78954b2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnMatchmakingConfiguration.GamePropertyProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class GamePropertyProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''This key-value pair can store custom data about a game session.

            For example, you might use a ``GameProperty`` to track a game session's map, level of difficulty, or remaining time. The difficulty level could be specified like this: ``{"Key": "difficulty", "Value":"Novice"}`` .

            You can set game properties when creating a game session. You can also modify game properties of an active game session. When searching for game sessions, you can filter on game property keys and values. You can't delete game properties from a game session.

            For examples of working with game properties, see `Create a game session with properties <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#game-properties>`_ .

            :param key: The game property identifier.
            :param value: The game property value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                game_property_property = gamelift.CfnMatchmakingConfiguration.GamePropertyProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f2a4ff02870ac5c61154789061383399d6e97942338fe5b3af997be3c7938c3f)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The game property identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html#cfn-gamelift-matchmakingconfiguration-gameproperty-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The game property value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html#cfn-gamelift-matchmakingconfiguration-gameproperty-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GamePropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnMatchmakingConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "acceptance_required": "acceptanceRequired",
        "name": "name",
        "request_timeout_seconds": "requestTimeoutSeconds",
        "rule_set_name": "ruleSetName",
        "acceptance_timeout_seconds": "acceptanceTimeoutSeconds",
        "additional_player_count": "additionalPlayerCount",
        "backfill_mode": "backfillMode",
        "creation_time": "creationTime",
        "custom_event_data": "customEventData",
        "description": "description",
        "flex_match_mode": "flexMatchMode",
        "game_properties": "gameProperties",
        "game_session_data": "gameSessionData",
        "game_session_queue_arns": "gameSessionQueueArns",
        "notification_target": "notificationTarget",
        "rule_set_arn": "ruleSetArn",
        "tags": "tags",
    },
)
class CfnMatchmakingConfigurationProps:
    def __init__(
        self,
        *,
        acceptance_required: typing.Union[builtins.bool, _IResolvable_da3f097b],
        name: builtins.str,
        request_timeout_seconds: jsii.Number,
        rule_set_name: builtins.str,
        acceptance_timeout_seconds: typing.Optional[jsii.Number] = None,
        additional_player_count: typing.Optional[jsii.Number] = None,
        backfill_mode: typing.Optional[builtins.str] = None,
        creation_time: typing.Optional[builtins.str] = None,
        custom_event_data: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        flex_match_mode: typing.Optional[builtins.str] = None,
        game_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchmakingConfiguration.GamePropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        game_session_data: typing.Optional[builtins.str] = None,
        game_session_queue_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        notification_target: typing.Optional[builtins.str] = None,
        rule_set_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMatchmakingConfiguration``.

        :param acceptance_required: A flag that determines whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to ``TRUE`` . With this option enabled, matchmaking tickets use the status ``REQUIRES_ACCEPTANCE`` to indicate when a completed potential match is waiting for player acceptance.
        :param name: A unique identifier for the matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.
        :param request_timeout_seconds: The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.
        :param rule_set_name: A unique identifier for the matchmaking rule set to use with this configuration. You can use either the rule set name or ARN value. A matchmaking configuration can only use rule sets that are defined in the same Region.
        :param acceptance_timeout_seconds: The length of time (in seconds) to wait for players to accept a proposed match, if acceptance is required.
        :param additional_player_count: The number of player slots in a match to keep open for future players. For example, if the configuration's rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match. This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param backfill_mode: The method used to backfill game sessions that are created with this matchmaking configuration. Specify ``MANUAL`` when your game manages backfill requests manually or does not use the match backfill feature. Specify ``AUTOMATIC`` to have GameLift create a ``StartMatchBackfill`` request whenever a game session has one or more open slots. Learn more about manual and automatic backfill in `Backfill Existing Games with FlexMatch <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-backfill.html>`_ . Automatic backfill is not available when ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param creation_time: A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example ``"1469498468.057"`` ).
        :param custom_event_data: Information to add to all events related to the matchmaking configuration.
        :param description: A description for the matchmaking configuration.
        :param flex_match_mode: Indicates whether this matchmaking configuration is being used with Amazon GameLift Servers hosting or as a standalone matchmaking solution. - *STANDALONE* - FlexMatch forms matches and returns match information, including players and team assignments, in a `MatchmakingSucceeded <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html#match-events-matchmakingsucceeded>`_ event. - *WITH_QUEUE* - FlexMatch forms matches and uses the specified Amazon GameLift Servers queue to start a game session for the match.
        :param game_properties: A set of custom properties for a game session, formatted as key-value pairs. These properties are passed to a game server process with a request to start a new game session. See `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`_ . This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param game_session_data: A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. See `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`_ . This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param game_session_queue_arns: The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to a Amazon GameLift Servers game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is ``arn:aws:gamelift:<region>::gamesessionqueue/<queue name>`` . Queues can be located in any Region. Queues are used to start new Amazon GameLift Servers-hosted game sessions for matches that are created with this matchmaking configuration. If ``FlexMatchMode`` is set to ``STANDALONE`` , do not set this parameter.
        :param notification_target: An SNS topic ARN that is set up to receive matchmaking notifications. See `Setting up notifications for matchmaking <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html>`_ for more information.
        :param rule_set_arn: The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) associated with the GameLift matchmaking rule set resource that this configuration uses.
        :param tags: A list of labels to assign to the new matchmaking configuration resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_matchmaking_configuration_props = gamelift.CfnMatchmakingConfigurationProps(
                acceptance_required=False,
                name="name",
                request_timeout_seconds=123,
                rule_set_name="ruleSetName",
            
                # the properties below are optional
                acceptance_timeout_seconds=123,
                additional_player_count=123,
                backfill_mode="backfillMode",
                creation_time="creationTime",
                custom_event_data="customEventData",
                description="description",
                flex_match_mode="flexMatchMode",
                game_properties=[gamelift.CfnMatchmakingConfiguration.GamePropertyProperty(
                    key="key",
                    value="value"
                )],
                game_session_data="gameSessionData",
                game_session_queue_arns=["gameSessionQueueArns"],
                notification_target="notificationTarget",
                rule_set_arn="ruleSetArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db0695f9efae852f4e3e7ce492e734297825efd4ac43986ef67506d40163a838)
            check_type(argname="argument acceptance_required", value=acceptance_required, expected_type=type_hints["acceptance_required"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument request_timeout_seconds", value=request_timeout_seconds, expected_type=type_hints["request_timeout_seconds"])
            check_type(argname="argument rule_set_name", value=rule_set_name, expected_type=type_hints["rule_set_name"])
            check_type(argname="argument acceptance_timeout_seconds", value=acceptance_timeout_seconds, expected_type=type_hints["acceptance_timeout_seconds"])
            check_type(argname="argument additional_player_count", value=additional_player_count, expected_type=type_hints["additional_player_count"])
            check_type(argname="argument backfill_mode", value=backfill_mode, expected_type=type_hints["backfill_mode"])
            check_type(argname="argument creation_time", value=creation_time, expected_type=type_hints["creation_time"])
            check_type(argname="argument custom_event_data", value=custom_event_data, expected_type=type_hints["custom_event_data"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument flex_match_mode", value=flex_match_mode, expected_type=type_hints["flex_match_mode"])
            check_type(argname="argument game_properties", value=game_properties, expected_type=type_hints["game_properties"])
            check_type(argname="argument game_session_data", value=game_session_data, expected_type=type_hints["game_session_data"])
            check_type(argname="argument game_session_queue_arns", value=game_session_queue_arns, expected_type=type_hints["game_session_queue_arns"])
            check_type(argname="argument notification_target", value=notification_target, expected_type=type_hints["notification_target"])
            check_type(argname="argument rule_set_arn", value=rule_set_arn, expected_type=type_hints["rule_set_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "acceptance_required": acceptance_required,
            "name": name,
            "request_timeout_seconds": request_timeout_seconds,
            "rule_set_name": rule_set_name,
        }
        if acceptance_timeout_seconds is not None:
            self._values["acceptance_timeout_seconds"] = acceptance_timeout_seconds
        if additional_player_count is not None:
            self._values["additional_player_count"] = additional_player_count
        if backfill_mode is not None:
            self._values["backfill_mode"] = backfill_mode
        if creation_time is not None:
            self._values["creation_time"] = creation_time
        if custom_event_data is not None:
            self._values["custom_event_data"] = custom_event_data
        if description is not None:
            self._values["description"] = description
        if flex_match_mode is not None:
            self._values["flex_match_mode"] = flex_match_mode
        if game_properties is not None:
            self._values["game_properties"] = game_properties
        if game_session_data is not None:
            self._values["game_session_data"] = game_session_data
        if game_session_queue_arns is not None:
            self._values["game_session_queue_arns"] = game_session_queue_arns
        if notification_target is not None:
            self._values["notification_target"] = notification_target
        if rule_set_arn is not None:
            self._values["rule_set_arn"] = rule_set_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def acceptance_required(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''A flag that determines whether a match that was created with this configuration must be accepted by the matched players.

        To require acceptance, set to ``TRUE`` . With this option enabled, matchmaking tickets use the status ``REQUIRES_ACCEPTANCE`` to indicate when a completed potential match is waiting for player acceptance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-acceptancerequired
        '''
        result = self._values.get("acceptance_required")
        assert result is not None, "Required property 'acceptance_required' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A unique identifier for the matchmaking configuration.

        This name is used to identify the configuration associated with a matchmaking request or ticket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def request_timeout_seconds(self) -> jsii.Number:
        '''The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out.

        Requests that fail due to timing out can be resubmitted as needed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-requesttimeoutseconds
        '''
        result = self._values.get("request_timeout_seconds")
        assert result is not None, "Required property 'request_timeout_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def rule_set_name(self) -> builtins.str:
        '''A unique identifier for the matchmaking rule set to use with this configuration.

        You can use either the rule set name or ARN value. A matchmaking configuration can only use rule sets that are defined in the same Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-rulesetname
        '''
        result = self._values.get("rule_set_name")
        assert result is not None, "Required property 'rule_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def acceptance_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''The length of time (in seconds) to wait for players to accept a proposed match, if acceptance is required.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-acceptancetimeoutseconds
        '''
        result = self._values.get("acceptance_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def additional_player_count(self) -> typing.Optional[jsii.Number]:
        '''The number of player slots in a match to keep open for future players.

        For example, if the configuration's rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match. This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-additionalplayercount
        '''
        result = self._values.get("additional_player_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def backfill_mode(self) -> typing.Optional[builtins.str]:
        '''The method used to backfill game sessions that are created with this matchmaking configuration.

        Specify ``MANUAL`` when your game manages backfill requests manually or does not use the match backfill feature. Specify ``AUTOMATIC`` to have GameLift create a ``StartMatchBackfill`` request whenever a game session has one or more open slots. Learn more about manual and automatic backfill in `Backfill Existing Games with FlexMatch <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-backfill.html>`_ . Automatic backfill is not available when ``FlexMatchMode`` is set to ``STANDALONE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-backfillmode
        '''
        result = self._values.get("backfill_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creation_time(self) -> typing.Optional[builtins.str]:
        '''A time stamp indicating when this data object was created.

        Format is a number expressed in Unix time as milliseconds (for example ``"1469498468.057"`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-creationtime
        '''
        result = self._values.get("creation_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_event_data(self) -> typing.Optional[builtins.str]:
        '''Information to add to all events related to the matchmaking configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-customeventdata
        '''
        result = self._values.get("custom_event_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the matchmaking configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flex_match_mode(self) -> typing.Optional[builtins.str]:
        '''Indicates whether this matchmaking configuration is being used with Amazon GameLift Servers hosting or as a standalone matchmaking solution.

        - *STANDALONE* - FlexMatch forms matches and returns match information, including players and team assignments, in a `MatchmakingSucceeded <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html#match-events-matchmakingsucceeded>`_ event.
        - *WITH_QUEUE* - FlexMatch forms matches and uses the specified Amazon GameLift Servers queue to start a game session for the match.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-flexmatchmode
        '''
        result = self._values.get("flex_match_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def game_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMatchmakingConfiguration.GamePropertyProperty]]]]:
        '''A set of custom properties for a game session, formatted as key-value pairs.

        These properties are passed to a game server process with a request to start a new game session. See `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`_ . This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gameproperties
        '''
        result = self._values.get("game_properties")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMatchmakingConfiguration.GamePropertyProperty]]]], result)

    @builtins.property
    def game_session_data(self) -> typing.Optional[builtins.str]:
        '''A set of custom game session properties, formatted as a single string value.

        This data is passed to a game server process with a request to start a new game session. See `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`_ . This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gamesessiondata
        '''
        result = self._values.get("game_session_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def game_session_queue_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to a Amazon GameLift Servers game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is ``arn:aws:gamelift:<region>::gamesessionqueue/<queue name>`` . Queues can be located in any Region. Queues are used to start new Amazon GameLift Servers-hosted game sessions for matches that are created with this matchmaking configuration. If ``FlexMatchMode`` is set to ``STANDALONE`` , do not set this parameter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gamesessionqueuearns
        '''
        result = self._values.get("game_session_queue_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def notification_target(self) -> typing.Optional[builtins.str]:
        '''An SNS topic ARN that is set up to receive matchmaking notifications.

        See `Setting up notifications for matchmaking <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html>`_ for more information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-notificationtarget
        '''
        result = self._values.get("notification_target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_set_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) associated with the GameLift matchmaking rule set resource that this configuration uses.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-rulesetarn
        '''
        result = self._values.get("rule_set_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new matchmaking configuration resource.

        Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMatchmakingConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnMatchmakingRuleSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnMatchmakingRuleSet",
):
    '''Creates a new rule set for FlexMatch matchmaking.

    A rule set describes the type of match to create, such as the number and size of teams. It also sets the parameters for acceptable player matches, such as minimum skill level or character type.

    To create a matchmaking rule set, provide unique rule set name and the rule set body in JSON format. Rule sets must be defined in the same Region as the matchmaking configuration they are used with.

    Since matchmaking rule sets cannot be edited, it is a good idea to check the rule set syntax.

    *Learn more*

    - `Build a rule set <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-rulesets.html>`_
    - `Design a matchmaker <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-configuration.html>`_
    - `Matchmaking with FlexMatch <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-intro.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html
    :cloudformationResource: AWS::GameLift::MatchmakingRuleSet
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_matchmaking_rule_set = gamelift.CfnMatchmakingRuleSet(self, "MyCfnMatchmakingRuleSet",
            name="name",
            rule_set_body="ruleSetBody",
        
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
        name: builtins.str,
        rule_set_body: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A unique identifier for the matchmaking rule set. A matchmaking configuration identifies the rule set it uses by this name value. Note that the rule set name is different from the optional ``name`` field in the rule set body.
        :param rule_set_body: A collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in JSON, but most elements support a description field.
        :param tags: A list of labels to assign to the new matchmaking rule set resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18ad8102fb28f35f09c9f78c601c99b706ee4e13284fddfd4e85f0e7b2b9cf57)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMatchmakingRuleSetProps(
            name=name, rule_set_body=rule_set_body, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d61a78aff0b1528ed82cb81e325639d2c75504b437ae15a2e7aac55347f0a30)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d30b78f916dd39df63fb4f2b2f869f31a7016f89e96d8e5620551a28085c667)
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
        '''The unique Amazon Resource Name (ARN) assigned to the rule set.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''A time stamp indicating when this data object was created.

        Format is a number expressed in Unix time as milliseconds (for example ``"1469498468.057"`` ).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The unique name of the rule set.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
        '''A unique identifier for the matchmaking rule set.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e140482b102c49c4f1893c669d34c3cb70704179735bb2d142748745913c03a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ruleSetBody")
    def rule_set_body(self) -> builtins.str:
        '''A collection of matchmaking rules, formatted as a JSON string.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleSetBody"))

    @rule_set_body.setter
    def rule_set_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2901f58b94659dc1e7b989a5220ec6f85b0fd07e208ae745469d1ed13b3ecb5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleSetBody", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new matchmaking rule set resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b8486d81489f869526b41e6ebf2b191599f06a6370135adbf247ac933792cd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnMatchmakingRuleSetProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "rule_set_body": "ruleSetBody", "tags": "tags"},
)
class CfnMatchmakingRuleSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        rule_set_body: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMatchmakingRuleSet``.

        :param name: A unique identifier for the matchmaking rule set. A matchmaking configuration identifies the rule set it uses by this name value. Note that the rule set name is different from the optional ``name`` field in the rule set body.
        :param rule_set_body: A collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in JSON, but most elements support a description field.
        :param tags: A list of labels to assign to the new matchmaking rule set resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_matchmaking_rule_set_props = gamelift.CfnMatchmakingRuleSetProps(
                name="name",
                rule_set_body="ruleSetBody",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bc1d10bdb780b0aa1af65a9211c041b6a3e7bb4893d0bfc3a61136195a863d6)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rule_set_body", value=rule_set_body, expected_type=type_hints["rule_set_body"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "rule_set_body": rule_set_body,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A unique identifier for the matchmaking rule set.

        A matchmaking configuration identifies the rule set it uses by this name value. Note that the rule set name is different from the optional ``name`` field in the rule set body.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html#cfn-gamelift-matchmakingruleset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_set_body(self) -> builtins.str:
        '''A collection of matchmaking rules, formatted as a JSON string.

        Comments are not allowed in JSON, but most elements support a description field.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html#cfn-gamelift-matchmakingruleset-rulesetbody
        '''
        result = self._values.get("rule_set_body")
        assert result is not None, "Required property 'rule_set_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new matchmaking rule set resource.

        Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html#cfn-gamelift-matchmakingruleset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMatchmakingRuleSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnScript(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnScript",
):
    '''The ``AWS::GameLift::Script`` resource creates a new script record for your Realtime Servers script.

    Realtime scripts are JavaScript that provide configuration settings and optional custom game logic for your game. The script is deployed when you create a Realtime Servers fleet to host your game sessions. Script logic is executed during an active game session.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html
    :cloudformationResource: AWS::GameLift::Script
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_script = gamelift.CfnScript(self, "MyCfnScript",
            storage_location=gamelift.CfnScript.S3LocationProperty(
                bucket="bucket",
                key="key",
                role_arn="roleArn",
        
                # the properties below are optional
                object_version="objectVersion"
            ),
        
            # the properties below are optional
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            version="version"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        storage_location: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScript.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]],
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param storage_location: The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift Servers to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift Servers uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the ``ObjectVersion`` parameter to specify an earlier version.
        :param name: A descriptive label that is associated with a script. Script names do not need to be unique.
        :param tags: A list of labels to assign to the new script resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
        :param version: The version that is associated with a build or script. Version strings do not need to be unique.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a610f7d9791794a98e26c23e6a2c7f57a2aceb363ba1a205d32cc00112745595)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScriptProps(
            storage_location=storage_location, name=name, tags=tags, version=version
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e467306a2b7b42d3bd4d40de8ebac0e5dbae11f33d3c54e42eae339fc88bc56b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bc786feeaa63a2566413adc42f5f2b3c38ba00daa4986115963a8d6d6c1a1f30)
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
        '''The unique Amazon Resource Name (ARN) for the script.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''A time stamp indicating when this data object was created.

        Format is a number expressed in Unix time as milliseconds (for example ``"1469498468.057"`` ).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''A unique identifier for a Realtime script.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrSizeOnDisk")
    def attr_size_on_disk(self) -> jsii.Number:
        '''The file size of the uploaded Realtime script, expressed in bytes.

        When files are uploaded from an S3 location, this value remains at "0".

        :cloudformationAttribute: SizeOnDisk
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrSizeOnDisk"))

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
    @jsii.member(jsii_name="storageLocation")
    def storage_location(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnScript.S3LocationProperty"]:
        '''The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScript.S3LocationProperty"], jsii.get(self, "storageLocation"))

    @storage_location.setter
    def storage_location(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnScript.S3LocationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67239519d512a22693f642bf29d26d0bffc0cf4f5f242e2295be3b8cf8bc1f30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageLocation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A descriptive label that is associated with a script.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df6266bf40e8b346c6a57c12d46137c3fe4f29ca8b9c37ef0dfb5715f82fbbf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new script resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59fee6448a284bb6932305c7159828353c13832415292cceb7a74453dd8177cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[builtins.str]:
        '''The version that is associated with a build or script.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "version"))

    @version.setter
    def version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22d619527b7b1b8b21c8e5ffa7ab4abbd6f2c76a23e5179dd879485530ec9e39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnScript.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "key": "key",
            "role_arn": "roleArn",
            "object_version": "objectVersion",
        },
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: builtins.str,
            role_arn: builtins.str,
            object_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The location in Amazon S3 where build or script files can be stored for access by Amazon GameLift.

            :param bucket: An Amazon S3 bucket identifier. Thename of the S3 bucket. .. epigraph:: Amazon GameLift Servers doesn't support uploading from Amazon S3 buckets with names that contain a dot (.).
            :param key: The name of the zip file that contains the build files or script files.
            :param role_arn: The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) for an IAM role that allows Amazon GameLift Servers to access the S3 bucket.
            :param object_version: The version of the file, if object versioning is turned on for the bucket. Amazon GameLift Servers uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                s3_location_property = gamelift.CfnScript.S3LocationProperty(
                    bucket="bucket",
                    key="key",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    object_version="objectVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1bc9de7e6777aff8308976cae56a2f5dd2d0e14f8555821f0396e5b81605502e)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
                "role_arn": role_arn,
            }
            if object_version is not None:
                self._values["object_version"] = object_version

        @builtins.property
        def bucket(self) -> builtins.str:
            '''An Amazon S3 bucket identifier. Thename of the S3 bucket.

            .. epigraph::

               Amazon GameLift Servers doesn't support uploading from Amazon S3 buckets with names that contain a dot (.).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html#cfn-gamelift-script-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''The name of the zip file that contains the build files or script files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html#cfn-gamelift-script-s3location-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) for an IAM role that allows Amazon GameLift Servers to access the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html#cfn-gamelift-script-s3location-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_version(self) -> typing.Optional[builtins.str]:
            '''The version of the file, if object versioning is turned on for the bucket.

            Amazon GameLift Servers uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html#cfn-gamelift-script-s3location-objectversion
            '''
            result = self._values.get("object_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnScriptProps",
    jsii_struct_bases=[],
    name_mapping={
        "storage_location": "storageLocation",
        "name": "name",
        "tags": "tags",
        "version": "version",
    },
)
class CfnScriptProps:
    def __init__(
        self,
        *,
        storage_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScript.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnScript``.

        :param storage_location: The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift Servers to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift Servers uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the ``ObjectVersion`` parameter to specify an earlier version.
        :param name: A descriptive label that is associated with a script. Script names do not need to be unique.
        :param tags: A list of labels to assign to the new script resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
        :param version: The version that is associated with a build or script. Version strings do not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_script_props = gamelift.CfnScriptProps(
                storage_location=gamelift.CfnScript.S3LocationProperty(
                    bucket="bucket",
                    key="key",
                    role_arn="roleArn",
            
                    # the properties below are optional
                    object_version="objectVersion"
                ),
            
                # the properties below are optional
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                version="version"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4a56c9731d882f4e0af0b136c973132c594cdb2f6c8607aa9bd92978d6d80b5)
            check_type(argname="argument storage_location", value=storage_location, expected_type=type_hints["storage_location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_location": storage_location,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def storage_location(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnScript.S3LocationProperty]:
        '''The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored.

        The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift Servers to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift Servers uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the ``ObjectVersion`` parameter to specify an earlier version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-storagelocation
        '''
        result = self._values.get("storage_location")
        assert result is not None, "Required property 'storage_location' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnScript.S3LocationProperty], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A descriptive label that is associated with a script.

        Script names do not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new script resource.

        Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''The version that is associated with a build or script.

        Version strings do not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScriptProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAlias",
    "CfnAliasProps",
    "CfnBuild",
    "CfnBuildProps",
    "CfnContainerFleet",
    "CfnContainerFleetProps",
    "CfnContainerGroupDefinition",
    "CfnContainerGroupDefinitionProps",
    "CfnFleet",
    "CfnFleetProps",
    "CfnGameServerGroup",
    "CfnGameServerGroupProps",
    "CfnGameSessionQueue",
    "CfnGameSessionQueueProps",
    "CfnLocation",
    "CfnLocationProps",
    "CfnMatchmakingConfiguration",
    "CfnMatchmakingConfigurationProps",
    "CfnMatchmakingRuleSet",
    "CfnMatchmakingRuleSetProps",
    "CfnScript",
    "CfnScriptProps",
]

publication.publish()

def _typecheckingstub__6a91f3a4a7dfbcf1655ec6812682d7a8824bfb46a9ce2a65e3c859108e3633c8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    routing_strategy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlias.RoutingStrategyProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6c7223e714d0339897da2cbb4b67d9e03a5022aa12f568680b86e828460d501(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1fbbe6ec42c9ed6d59226c8fe9df0391ca1a181a605b688f9e6267ea6f2a055(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8666b32153f5438f8d6ea2d03ad01cbf8c67bad1071d8e1cdc42963a8912ad3c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__529d8fec4c06eafb4c38da47298670dd8132ede4d21975eafb43f51a366a3d82(
    value: typing.Union[_IResolvable_da3f097b, CfnAlias.RoutingStrategyProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98d25b43c56fe6060dfb6e36792550c92a6a537d6d2e31b8c97947858787f55a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc43df2fa439cbdde0361a6e15a7a3a916a006856add3cb38bca18959f9c8775(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4057d890d9c2fba51db14d6885375c0c7263cd6b07fb4401e3fb51d7676734f9(
    *,
    type: builtins.str,
    fleet_id: typing.Optional[builtins.str] = None,
    message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e74c18c4446e0f846baf63e2e707aa2ba663f37170623164846853f1176d7891(
    *,
    name: builtins.str,
    routing_strategy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlias.RoutingStrategyProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2f3884df6574dd3d4e76d857acf05a15fdc616d818da1cebcfcce4084ca8ddc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: typing.Optional[builtins.str] = None,
    operating_system: typing.Optional[builtins.str] = None,
    server_sdk_version: typing.Optional[builtins.str] = None,
    storage_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBuild.StorageLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dabd8e19951007a8e9f2bcb21f9e872c9fc5b6a638701939005bc4d813c12a3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52be0a2eff399965a7232bfe5d136a98b17426adc22dd0fe1be4ebd8de6c3b47(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a86d40dd79232f1b81dd44ba375e9a9432429c05c3444beaf1128ab336d19dc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__086f4a5a0a253ca19c97937d0f25a8ade9bb623ef1c01cacdc76233a24f4ef0a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb7f1e9548565a4821c004b0e86bae438a45b45de61043075555fb43127d349d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdd3e9ea10aa8547b05a398258efac5d3e786e68d7875c76104c89d2a3178e02(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBuild.StorageLocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61f5c317acb9e4d0abf34641df15710032d796e858c0b0962748ce1d84bf6d9d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f69e6e764a220fcdeac2ac30cce1d3fbf57e0ef02b497976b1bb0e8162a6a67(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d6726269ab0714348382710795aeac31efd3f1d29c3bac05a4aefa5c90bcba4(
    *,
    bucket: builtins.str,
    key: builtins.str,
    role_arn: builtins.str,
    object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ea486b468f726c96f63f78347aac31445ce3b0bd1ea282f6fce30ca4e8642d7(
    *,
    name: typing.Optional[builtins.str] = None,
    operating_system: typing.Optional[builtins.str] = None,
    server_sdk_version: typing.Optional[builtins.str] = None,
    storage_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBuild.StorageLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d30a780826320cc5d36af5934da7151d1abdd72973e8cb82c8f063951d6fe96d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    fleet_role_arn: builtins.str,
    billing_type: typing.Optional[builtins.str] = None,
    deployment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.DeploymentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    game_server_container_group_definition_name: typing.Optional[builtins.str] = None,
    game_server_container_groups_per_instance: typing.Optional[jsii.Number] = None,
    game_session_creation_limit_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.GameSessionCreationLimitPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    instance_connection_port_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.ConnectionPortRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    instance_inbound_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.IpPermissionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    instance_type: typing.Optional[builtins.str] = None,
    locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.LocationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    log_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    metric_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    new_game_session_protection_policy: typing.Optional[builtins.str] = None,
    per_instance_container_group_definition_name: typing.Optional[builtins.str] = None,
    scaling_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.ScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8beb89172335ad10958d248c189bbeedc924ed5525d311d2bf335e603ec0616c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f53d6bba4bd4d54dbd42a8199fcf6ff8c140c57e7fdcf6ef20d3b79946767cd0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abbc02248f000ac12eb3d2fc54e95db4c9b42e040527d39b8128105822bfcef9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2584c4251bbc27920e48c58b31dee9f36c8dbf693670e559b54adf33a976a34b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef9932c78fa010240b75995b843da6e043ab92ac23a400685eeeebc9b2d9e5c4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.DeploymentConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3029a8fa3bd1fba1941cfbb7ca8c945357abf57a90aefe3243227816ca2aa894(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3c572d6543954cc606aa4cf4980b627e9dfb284c7521995845297b1b9c97a8b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b84912f0e8b5fe2e7b7394f1cfc1d121c2c0af1b8e7e0232c4ccba681f1970a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee374c5590b404e3cb8d6cde909b11f0fb3541f0c11fc73da3c85400628cec3d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.GameSessionCreationLimitPolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cd714c6adf18c5cdb2b4cad3d4dbf1a4a07bdbe94b6ffd5d751f200d7347426(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.ConnectionPortRangeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aae77cedd1161d46848109370fc6b6d65ab8d346c0a5f95f915a98f0d6efdbcd(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.IpPermissionProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe64b737dafa9c91cdecdbf4a073ad8425d495d7fb28182e46c423079e0b67c2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a36ecc94bdbfc4085b1baaf7462461cb77b4e640a5f1017b6653f6dc89c0b20f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.LocationConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4618d18b990fa28be1054e4840c2f8afe6e85b406433ad49087577b8e2dfaf53(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.LogConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43394effc64e297e079a5b571e85c8719269d3aa9af3d84206eb3fed35403442(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bf45e0a6202b79f4e6df01e65b4356da1371adf96524ef41997e3d3c531bf9b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73062db2cea0b73eca7dbc19b367503a92d902e168720fb46aaaef0f68783f42(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b8d26c0f526c6120c09026205884464ccfb9805906c0810312a9ac8dc69119a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerFleet.ScalingPolicyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9b56d077e864bb1e2553942ee500751751ac23fc1e29dfd0bb471e69e99ff44(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5f97a49baa6b922fdd46128e0aecec92e3c04c61959b05e218e736635385be5(
    *,
    from_port: jsii.Number,
    to_port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21e6530b63f555a4284f6eecf5700d25ca8c43cffae22ea8e225906f58003c4c(
    *,
    impairment_strategy: typing.Optional[builtins.str] = None,
    minimum_healthy_percentage: typing.Optional[jsii.Number] = None,
    protection_strategy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb96aee76dbbe77d2c71ced0834b03d35c2b24b22e7f706d4c4a3476d575ad46(
    *,
    latest_deployment_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f54af8dad70427c8dc70929770cd29dc6c981a2ee74ca5429adac683330a9932(
    *,
    new_game_sessions_per_creator: typing.Optional[jsii.Number] = None,
    policy_period_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c74cebf3a79bd067a90f843de7a76b099cbe8aff962b812b7dcae7adae5eb58(
    *,
    from_port: jsii.Number,
    ip_range: builtins.str,
    protocol: builtins.str,
    to_port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfdc01eeb9f739a54f304b9e5cb1f66114e55233f5383f018ef7dd086a28ed10(
    *,
    desired_ec2_instances: jsii.Number,
    max_size: jsii.Number,
    min_size: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f0d55ebb1c8fdd9364a92df8152f6c91294e481bedd64b3458f3dff3c77ec80(
    *,
    location: builtins.str,
    location_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.LocationCapacityProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    stopped_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__287854cb20cec032892a9072e611adf774cd43dcc343c3ffdda539be73bce563(
    *,
    log_destination: typing.Optional[builtins.str] = None,
    log_group_arn: typing.Optional[builtins.str] = None,
    s3_bucket_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77733d66802ae69be5c6e0b5788b2caf6cc2db612ef32cb9e718cc475df0b111(
    *,
    metric_name: builtins.str,
    name: builtins.str,
    comparison_operator: typing.Optional[builtins.str] = None,
    evaluation_periods: typing.Optional[jsii.Number] = None,
    policy_type: typing.Optional[builtins.str] = None,
    scaling_adjustment: typing.Optional[jsii.Number] = None,
    scaling_adjustment_type: typing.Optional[builtins.str] = None,
    target_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.TargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    threshold: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3133704901a8cbe841212bef17b3e01ca8f97d737576c8860ee4bf4a44f4e8ca(
    *,
    target_value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fbf4a66831e3b15f9023046fb41b590456b41ba1048fa4e59749ccd8f9d023c(
    *,
    fleet_role_arn: builtins.str,
    billing_type: typing.Optional[builtins.str] = None,
    deployment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.DeploymentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    game_server_container_group_definition_name: typing.Optional[builtins.str] = None,
    game_server_container_groups_per_instance: typing.Optional[jsii.Number] = None,
    game_session_creation_limit_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.GameSessionCreationLimitPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    instance_connection_port_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.ConnectionPortRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    instance_inbound_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.IpPermissionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    instance_type: typing.Optional[builtins.str] = None,
    locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.LocationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    log_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    metric_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    new_game_session_protection_policy: typing.Optional[builtins.str] = None,
    per_instance_container_group_definition_name: typing.Optional[builtins.str] = None,
    scaling_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerFleet.ScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d0ad3aeb1243549bc05c0346bb1e8303d21326ec9f1a17ec63327d7e3f29a1e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    operating_system: builtins.str,
    total_memory_limit_mebibytes: jsii.Number,
    total_vcpu_limit: jsii.Number,
    container_group_type: typing.Optional[builtins.str] = None,
    game_server_container_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.GameServerContainerDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_version_number: typing.Optional[jsii.Number] = None,
    support_container_definitions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.SupportContainerDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    version_description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b07a706beb428681d6a41fe2a705cfe7e9f6f65c0df4708d633a856c73d6fa7b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abcc96ad0c8f9f987fd719eb37179f12dda8829dbbc0b9fb28188a52044ec711(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90e8a024d1021ae9b57dadc57167a55f375efa5756fd3358541d1bbca8f16cf0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f85c42319aa42e6c796369d8760bfb73c97a6305632fa1b86497b93a214a2ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9806a412f491ae7e0701177df10f3e3f8f7c4f8fca4c26908502d2f9e2257026(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cac0cc3ab1e2d26b478bc208c563a20312989d26048f9500230ad42e1300f7f0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__752739c32e65d44c30b88e307fe3881e0e9b34d2745e17aa9c60392ca6e6d97e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c82cba9110173a8477c870dcd9dc5096dee3fc3981d5dbbdb3e909b3777f47d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerGroupDefinition.GameServerContainerDefinitionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5672891cfbdf9eecf6dc0835cad6505adf6ecd0957851f286608ea9077312f19(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8eefcc08a08c4e2d5876a924350a3f3122337dadd842f4c45350099127878a77(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerGroupDefinition.SupportContainerDefinitionProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39d9905e11429554186c96e0a5c07109b132519014161fc8e8d7aa9f4250218d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f96815347c81f9c90df0014b6a4de3f36fbcb0f246e66a58ef72af2f6caade8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8424bed9ce9567d13ec372652e5d607735583e13219bd42143f538aee3feb1f(
    *,
    condition: builtins.str,
    container_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8a971f77ef4383909669846d3e4ee4a8463f7353ec0c1aa4da152ea7ec43bb9(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b1e7083ac6b3d39e0bc5926b3c9ee368385be498c61499a81f860b155d0a1d(
    *,
    command: typing.Sequence[builtins.str],
    interval: typing.Optional[jsii.Number] = None,
    retries: typing.Optional[jsii.Number] = None,
    start_period: typing.Optional[jsii.Number] = None,
    timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__582a62e33c1aa361f9ef7ca37ba1315dfbf02275fd99e239191003b332a6b172(
    *,
    instance_path: builtins.str,
    access_level: typing.Optional[builtins.str] = None,
    container_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d3e35cf8a42e8cbcdf12218e64e5ac29c19f0813f144c8d75e97d3e3313d396(
    *,
    from_port: jsii.Number,
    protocol: builtins.str,
    to_port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__996969233fd34d51e9d9534744b87b0efc6e35f90fac9e44bd0cb26d5f2918f3(
    *,
    container_name: builtins.str,
    image_uri: builtins.str,
    server_sdk_version: builtins.str,
    depends_on: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.ContainerDependencyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    environment_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.ContainerEnvironmentProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    mount_points: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.ContainerMountPointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    port_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.PortConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resolved_image_digest: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49796d7f2a6fb9a60e370fb5b8e88da33d84ca298d8833d8e64e3d80586cedf7(
    *,
    container_port_ranges: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.ContainerPortRangeProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6565c3caf0bf39eea0bc662ef87427d6cf77017b05483384a736fa1c260791c8(
    *,
    container_name: builtins.str,
    image_uri: builtins.str,
    depends_on: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.ContainerDependencyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    environment_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.ContainerEnvironmentProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    essential: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    health_check: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.ContainerHealthCheckProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    memory_hard_limit_mebibytes: typing.Optional[jsii.Number] = None,
    mount_points: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.ContainerMountPointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    port_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.PortConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resolved_image_digest: typing.Optional[builtins.str] = None,
    vcpu: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b760a12182b9da0a53204aa5510dae28c2cda4c4fba1ef77f0245093da04ea4(
    *,
    name: builtins.str,
    operating_system: builtins.str,
    total_memory_limit_mebibytes: jsii.Number,
    total_vcpu_limit: jsii.Number,
    container_group_type: typing.Optional[builtins.str] = None,
    game_server_container_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.GameServerContainerDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_version_number: typing.Optional[jsii.Number] = None,
    support_container_definitions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.SupportContainerDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    version_description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21fe09a90444788b3c862f454214d4e160757c9b02d0598d282f68b7f79d749f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    anywhere_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.AnywhereConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    apply_capacity: typing.Optional[builtins.str] = None,
    build_id: typing.Optional[builtins.str] = None,
    certificate_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.CertificateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    compute_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    desired_ec2_instances: typing.Optional[jsii.Number] = None,
    ec2_inbound_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.IpPermissionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ec2_instance_type: typing.Optional[builtins.str] = None,
    fleet_type: typing.Optional[builtins.str] = None,
    instance_role_arn: typing.Optional[builtins.str] = None,
    instance_role_credentials_provider: typing.Optional[builtins.str] = None,
    locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.LocationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    log_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    max_size: typing.Optional[jsii.Number] = None,
    metric_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    min_size: typing.Optional[jsii.Number] = None,
    new_game_session_protection_policy: typing.Optional[builtins.str] = None,
    peer_vpc_aws_account_id: typing.Optional[builtins.str] = None,
    peer_vpc_id: typing.Optional[builtins.str] = None,
    resource_creation_limit_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ResourceCreationLimitPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    runtime_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.RuntimeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scaling_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    script_id: typing.Optional[builtins.str] = None,
    server_launch_parameters: typing.Optional[builtins.str] = None,
    server_launch_path: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__264e19b1dd38619175091751b1eec860e08c2225c7798789a29ec89ab8971593(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__905cca04e4d534db21b7356373856ed4d0fb9130ab18a34d31eb7127b3ecdbc1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd3e6bf68da3a08ee0a6dbdff6b571a1a9348dfd6d1f15864e1efd85595ae689(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc575abdd043760dd1cbe4178328d65df4b96ee18072484d24bd88d2e2d340ac(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.AnywhereConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e4da24e64fdcbb7830d9e09a27219d611e9c486d09dd2a970381192b5e97213(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fecb16629d96a3f0b5b4acdf8ba4a4b1a44a9314ada24ee4bf29122c11df18e7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f46d27389fd45eb3384977842c4289c60e5795c4a4bd6e08002ec26643232bc(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.CertificateConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__022e8bf70858e61cedf1ac2f0bbe1af01706924dda3af7f4e655e78c1b5985db(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eec78595476346beb2b42a6ac89d6890fb357c8bc49fbafff985bc1417bca206(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4941614413c1e1554010809926c621b6030f9b38418b19c26a4dbbfc56fd9cfd(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d84bfe64c88748026f1ea76b00a3c1eeeffe26c5a9e7df3f052f9069032249c9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.IpPermissionProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5edb81bb6e5f986aaa8654e60493e7ec0e42f57ed43a7481b48714433fb0b95(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc9a52bd70aa79d8d459ba6e23d2020447c1f1d4faa157c8836aad4e87181d56(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7947f4ea6b160028fb5bbf20fcbd0cc9eb46ba122d737f3c792a6be5043d8577(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6765d7366d76df2864c4535568d1edf808ceec869046e302b0c842674b46c102(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1377dfdecc90d2457b2fe3e90aa35cecb44bf218eb1836fc28cbc15b7a4812f3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.LocationConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35b29d2e11870cd4d0ea412c5de5d02fbb8bb765ed67873227f57868f234fe52(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbc74cb38ce8a622308c22d16cb5fe99f9f601acdfd26460b9b33bd15037e42f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02facc74087efba3bcf2b21fc12cd9fae063e33440abacb0fdfdf65ecb3fe7ad(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d460bc2f634afc1e2c222819f53ddf45b2647b9ccf197380a1419dfb4b91c61a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c8b79569fe310aaed26b6fa78159b7101d72974e478dd380ca0713aea1d9a9f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a648f419a89a6e5926858e8481241ede65ca343e3b797aecd480dec6c8b20939(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fd0ab83e874e8110a1f4093ff1e48395bf94729c8f475c6e23b4d22971f3428(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21ee8415ef994fb87ac2edf852ffd98a21384f9eccc26d3a0537563c2b00fbed(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.ResourceCreationLimitPolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91bbc8eaa0f72d2032ef5cfd51906c5fc923f7ed24ede99b907cb24fe23da499(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.RuntimeConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__082c3456142a6049adc9dd4639e8b2ca94a21dbf9412cc70d0ea2e1babccf7c3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.ScalingPolicyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d89c92d80f54ea7b8f3b7a14762b9c71a927d074d3727f05bc330349648ba92(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b86e485f6c758ba0a09838614ee6f5e63a4ba69e6100fd77af039cc9f223b152(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63d5bf96be81c4a6b00ef1deb4d8846acf0053313fb89efd0ded1f0931c66844(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27ef86cf1bf34b50ec355a45305857c52751912f8408dec34a63b8a26665856d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3897ffc82938e5bf4e6384b3a83b22f50c7189a71eb0fc30ea8f17642db5ef9(
    *,
    cost: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c3cca5919f32f3e2cb6c385afda08bf3b194b8baf60b4d20e5f9f580659cc84(
    *,
    certificate_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f885be25c9084dbab3b02a36601be0e37c43ab741ea7dd646494423839333a(
    *,
    from_port: jsii.Number,
    ip_range: builtins.str,
    protocol: builtins.str,
    to_port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76847ac983ab72ef92adc1b0579d769ca62af002ef71c76165cbd879da8645fc(
    *,
    desired_ec2_instances: jsii.Number,
    max_size: jsii.Number,
    min_size: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__716ff23eda74da42620dc64832ed27ab5a267661bd90b16577ee48991436d14c(
    *,
    location: builtins.str,
    location_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.LocationCapacityProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b5bf70d1fc5987b674dcb2717a733f347f6ff57d29689b7a2a12d07ccfab884(
    *,
    new_game_sessions_per_creator: typing.Optional[jsii.Number] = None,
    policy_period_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae990fc53511e6175c77d897f3a8a6bc35be77827bfc0f1be6b1f8d7967e54c3(
    *,
    game_session_activation_timeout_seconds: typing.Optional[jsii.Number] = None,
    max_concurrent_game_session_activations: typing.Optional[jsii.Number] = None,
    server_processes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ServerProcessProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8690870b8fddf2f2747a9a00d8f1a693d624b5f4f72283ed427b04667f02bd8(
    *,
    metric_name: builtins.str,
    name: builtins.str,
    comparison_operator: typing.Optional[builtins.str] = None,
    evaluation_periods: typing.Optional[jsii.Number] = None,
    location: typing.Optional[builtins.str] = None,
    policy_type: typing.Optional[builtins.str] = None,
    scaling_adjustment: typing.Optional[jsii.Number] = None,
    scaling_adjustment_type: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    target_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.TargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    threshold: typing.Optional[jsii.Number] = None,
    update_status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc845ade67d7aff6536f53651c26f049fc04883863968a83da759b79b0a6d035(
    *,
    concurrent_executions: jsii.Number,
    launch_path: builtins.str,
    parameters: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__472ce4c72467f1a69fc974099623863890460564fbbe1e98eb694a9a4b1546b7(
    *,
    target_value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a51a418ba5b606bdfc45dc50c3172e280a12e078a7392f3258d5d329e037a55(
    *,
    name: builtins.str,
    anywhere_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.AnywhereConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    apply_capacity: typing.Optional[builtins.str] = None,
    build_id: typing.Optional[builtins.str] = None,
    certificate_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.CertificateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    compute_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    desired_ec2_instances: typing.Optional[jsii.Number] = None,
    ec2_inbound_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.IpPermissionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ec2_instance_type: typing.Optional[builtins.str] = None,
    fleet_type: typing.Optional[builtins.str] = None,
    instance_role_arn: typing.Optional[builtins.str] = None,
    instance_role_credentials_provider: typing.Optional[builtins.str] = None,
    locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.LocationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    log_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    max_size: typing.Optional[jsii.Number] = None,
    metric_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    min_size: typing.Optional[jsii.Number] = None,
    new_game_session_protection_policy: typing.Optional[builtins.str] = None,
    peer_vpc_aws_account_id: typing.Optional[builtins.str] = None,
    peer_vpc_id: typing.Optional[builtins.str] = None,
    resource_creation_limit_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ResourceCreationLimitPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    runtime_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.RuntimeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scaling_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    script_id: typing.Optional[builtins.str] = None,
    server_launch_parameters: typing.Optional[builtins.str] = None,
    server_launch_path: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39a0d4e260fba686f866a885f9a542286a05d085037e114d8febabfdd92cfd24(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    game_server_group_name: builtins.str,
    instance_definitions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.InstanceDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    role_arn: builtins.str,
    auto_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.AutoScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    balancing_strategy: typing.Optional[builtins.str] = None,
    delete_option: typing.Optional[builtins.str] = None,
    game_server_protection_policy: typing.Optional[builtins.str] = None,
    launch_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.LaunchTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_size: typing.Optional[jsii.Number] = None,
    min_size: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32ac0616025cd3de739c7101cea4baa4d9d85d9755bd18a18599fd247f47e000(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a77b5aa43581e64c5c91459806a51ceb403900395eac9fb9f2cdec42c5c7fad(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89556427a3cb2e1aa05738182ce0459e80e576c3c25bd0cc1d7dc630a122bd67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__868421ea021122381c2075a524c1d4785b63637a5ae0e28ee1747043ceaf14fc(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.InstanceDefinitionProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c76aa84abc5cd589d0abb99434e1ecea33850fb0ccbb6eee11380bfa754fc482(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5ee0eb377684162644f965e1106f08af9e4431bca94796da59b89abc7ffd998(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.AutoScalingPolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5fc25560f0a78783f5ed8bb510e2e86e267d9629bd271a2403e866afa14e22e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a84355ef62b2fd37a277a26c39b2735a06cf204ad010f5de3744a8280e5be056(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29b538c5660178a7532c29be9d3acb184e85dfbac80460c002d5f219fa429d79(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e1b30118131dd3fcdd29554603028109f41bf9f28d638ff1f26fc0de989e8b6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.LaunchTemplateProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c07d732b195687bb610c12d0db39761316bbb61e6416116d630f224124000c66(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7e884c21390c0adc461578e34ea9d201ce75716ffda1892218e4f39b5f6ae3e(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dba0594bea5d13fc9125228769f878f9679d696d511472809787acd5605b3e6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b4d5326a42c1fdc1afa97e1f31ad389e2aac7fbe1c4f2c6a3f614b0d23761c7(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3ca9dc4f6076efea7dd9c18ae3d0d4e330ecd050951dbb0b731443e8b262e56(
    *,
    target_tracking_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.TargetTrackingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    estimated_instance_warmup: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b295ebcaf7cae28b09dfaf0a8c5a7fe40fd9a1dfa65423b6093711f0f56e28fc(
    *,
    instance_type: builtins.str,
    weighted_capacity: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25060a9b2c2773d45ef64eabb5fbdc70d6c95644145351fecb4e3d70bd06f5e2(
    *,
    launch_template_id: typing.Optional[builtins.str] = None,
    launch_template_name: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef13423f0408e9300989065f2e1f7a323aeaaef1367e95591fe66bbfc152a818(
    *,
    target_value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb2b330cbc0b2bd24b542707e03f7de3d6d3afa7d8fa0efaac64771d13b95db1(
    *,
    game_server_group_name: builtins.str,
    instance_definitions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.InstanceDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    role_arn: builtins.str,
    auto_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.AutoScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    balancing_strategy: typing.Optional[builtins.str] = None,
    delete_option: typing.Optional[builtins.str] = None,
    game_server_protection_policy: typing.Optional[builtins.str] = None,
    launch_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.LaunchTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_size: typing.Optional[jsii.Number] = None,
    min_size: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2435e37790a5987d49478948c0c1ac36c9e463fa29441c46ba0aa4d567f2c585(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    custom_event_data: typing.Optional[builtins.str] = None,
    destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.DestinationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    filter_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.FilterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    notification_target: typing.Optional[builtins.str] = None,
    player_latency_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.PlayerLatencyPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    priority_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.PriorityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cc05027a8472775374b6846f6c9ab499cc41f64fa8ed31ccbfd79e142b8b76d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b257e875617af0371cc9d2c1574fb2ba9c0e4ecbacf958d56eabd8a77d1fa023(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac381d2dd8ded0682b62f79246a99597b2aca0600afaa30c9f48b5f1411bbfa8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d8260843224b7180260627c762aaa0ae5afbcd912f5da71a3c576430e069f9e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f656db0c32504c821ba5c5d5067bac317db7def96a39500c5847a853576e95ec(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.DestinationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08e5b9b16ae8732de19b82da87c71cb00a9d06d7a37c8d217314158c063bf0f7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.FilterConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f838580d46a0a1a08c09d8b8b17de066bfb74896289f61432e755d32429e2a4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3da0f541db3f4dba488790dc678e2dd0872a5271bf05bb0ddcb181884f5dfb80(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.PlayerLatencyPolicyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__622dc07e672d46f719db763d6bf2dec499f84a17b72186d593df03f3fcb1ae7f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.PriorityConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a8c431c366d3fa711cfb42cebf2d1647b8f2a1a5e129b5536c91cdf0135eb8(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ad24ec0156a0a24d8fe08ecf8470df28f9f1501a3ab442e887e2d1c5ef03df4(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d1ad7f562ade1312178a63d9196a21119d0e6500b9d651931481a59d709d462(
    *,
    destination_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a18c067b373a2989add73f26fd5a7da221d485dae82bf0842dcedf8017b6ad5f(
    *,
    allowed_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__682a2ca85600f7cf3e8fc279fa7f5c2ecab05f65cc96301b5afab09b2da5c684(
    *,
    destination_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7a9bd74ee679564c60f66c08f4f2d7739a8abfa4c61e93feedbd8457081f585(
    *,
    maximum_individual_player_latency_milliseconds: typing.Optional[jsii.Number] = None,
    policy_duration_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bffce6e10d5ec1968a817a7df177891e44b6ec986ec424c92d4e71dd599b36ac(
    *,
    location_order: typing.Optional[typing.Sequence[builtins.str]] = None,
    priority_order: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b18cdd98f5e3e7424d6d930e416c9690c2e3cdcc56ac70f4688a8984ea0e8b7(
    *,
    name: builtins.str,
    custom_event_data: typing.Optional[builtins.str] = None,
    destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.DestinationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    filter_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.FilterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    notification_target: typing.Optional[builtins.str] = None,
    player_latency_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.PlayerLatencyPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    priority_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.PriorityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__404fc5857cf63bdcf757784b5c810e73ce1c99d8d82c264eec7a145724580816(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    location_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d95943640733fe4e543a0c2a9e0a647a118d84274c6945f59f0598a9585e4a4b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a18532e89ee9aa9c91c15cc19d2c9f2345325702005b9a2708e43204329266ae(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50f9bf4f89ef7693448c9209f894d6900bab55884642fc136222c211e82f3015(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db22dc038d314307a9d7182d88d8959bd024bf2feff9aee7f03deba1df46ca5c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98ffffd954dd9a648cdd22ea8069e64a916e69b5690bde3de5bb865f1a555e5d(
    *,
    location_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5991dfcf120df852e2fd4ce6291a275a648645c817c923b70181ea8f56e61574(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    acceptance_required: typing.Union[builtins.bool, _IResolvable_da3f097b],
    name: builtins.str,
    request_timeout_seconds: jsii.Number,
    rule_set_name: builtins.str,
    acceptance_timeout_seconds: typing.Optional[jsii.Number] = None,
    additional_player_count: typing.Optional[jsii.Number] = None,
    backfill_mode: typing.Optional[builtins.str] = None,
    creation_time: typing.Optional[builtins.str] = None,
    custom_event_data: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    flex_match_mode: typing.Optional[builtins.str] = None,
    game_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchmakingConfiguration.GamePropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    game_session_data: typing.Optional[builtins.str] = None,
    game_session_queue_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    notification_target: typing.Optional[builtins.str] = None,
    rule_set_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97ef86c5f161a3f7e4debb1e365142a6bed6fcfa0560f9575501529b34dee619(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f090e32e05cfaeb363b1750dd5ec26197130f385a7f9bddfe37da83c98c9462c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22e4fb0874509d31426b22f3ffefc8f7d3c205a887689be775fe8344351315b4(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50207e3d686076a987e377c81a96125dab3ab3f1620c58f788384cb08b17f088(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a26beba0933992ac93ce4a627f18fa7a10ad26da6a35a99b1e377d5afa493b78(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e22642273b822aeccc60cfa3d9595fa6bc154a168c63626eefb68d6a746ffad0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c28ab17b4e7b606d702229a14a7e46b7f9e86cb64d8dc6e0585fbcb058d0b242(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92699d7bd325a7ad10bdb62647176ac995f2c17688efde0d91661c8f0815eda7(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b63753d38be440877984c0aa86a81bd07b6d2ce3aec33c9d8dd34c0ccde356c3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31d3fbc33faadd8b20143f6719f4142fc516a089f7e572e974783578c57954d8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fac8d8c2d6825f23811aeea9f440bf664e97a02184ef417460a8d92056b2fb27(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a956b02b663049817a64e32bfd1f09f9857feedac28f4eca2d36141c326cc5e1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a047908ff094a894704a6965c30654d87bb94e2aff3bd57abb16673fd6e98318(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0086331ec6c1fe164de53253519ecf95f522026cd3c4b9b2c0b16c300b99ceb2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMatchmakingConfiguration.GamePropertyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad31d919af9b1fb2de550bd5b00fcb306185a91f87127b6250e135a48937df4d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beae0e02206ffef8c392d9dd656f3a5ac2476b679628f1884cf15a4e8092c49d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83e843d11896164f9fbc52e89ade017c17b6cce0da297e20b5f554281c6c8e7e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b47741240f35249cfb706757b5199576646836e89e8f9fcd9e6bb884d238a3c9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9777adaa1c91123290fcf69dfad3f29c9d5affe68344eb61a6147f7c78954b2c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2a4ff02870ac5c61154789061383399d6e97942338fe5b3af997be3c7938c3f(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db0695f9efae852f4e3e7ce492e734297825efd4ac43986ef67506d40163a838(
    *,
    acceptance_required: typing.Union[builtins.bool, _IResolvable_da3f097b],
    name: builtins.str,
    request_timeout_seconds: jsii.Number,
    rule_set_name: builtins.str,
    acceptance_timeout_seconds: typing.Optional[jsii.Number] = None,
    additional_player_count: typing.Optional[jsii.Number] = None,
    backfill_mode: typing.Optional[builtins.str] = None,
    creation_time: typing.Optional[builtins.str] = None,
    custom_event_data: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    flex_match_mode: typing.Optional[builtins.str] = None,
    game_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchmakingConfiguration.GamePropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    game_session_data: typing.Optional[builtins.str] = None,
    game_session_queue_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    notification_target: typing.Optional[builtins.str] = None,
    rule_set_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18ad8102fb28f35f09c9f78c601c99b706ee4e13284fddfd4e85f0e7b2b9cf57(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    rule_set_body: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d61a78aff0b1528ed82cb81e325639d2c75504b437ae15a2e7aac55347f0a30(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d30b78f916dd39df63fb4f2b2f869f31a7016f89e96d8e5620551a28085c667(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e140482b102c49c4f1893c669d34c3cb70704179735bb2d142748745913c03a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2901f58b94659dc1e7b989a5220ec6f85b0fd07e208ae745469d1ed13b3ecb5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b8486d81489f869526b41e6ebf2b191599f06a6370135adbf247ac933792cd6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bc1d10bdb780b0aa1af65a9211c041b6a3e7bb4893d0bfc3a61136195a863d6(
    *,
    name: builtins.str,
    rule_set_body: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a610f7d9791794a98e26c23e6a2c7f57a2aceb363ba1a205d32cc00112745595(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    storage_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScript.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e467306a2b7b42d3bd4d40de8ebac0e5dbae11f33d3c54e42eae339fc88bc56b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc786feeaa63a2566413adc42f5f2b3c38ba00daa4986115963a8d6d6c1a1f30(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67239519d512a22693f642bf29d26d0bffc0cf4f5f242e2295be3b8cf8bc1f30(
    value: typing.Union[_IResolvable_da3f097b, CfnScript.S3LocationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df6266bf40e8b346c6a57c12d46137c3fe4f29ca8b9c37ef0dfb5715f82fbbf1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59fee6448a284bb6932305c7159828353c13832415292cceb7a74453dd8177cc(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22d619527b7b1b8b21c8e5ffa7ab4abbd6f2c76a23e5179dd879485530ec9e39(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bc9de7e6777aff8308976cae56a2f5dd2d0e14f8555821f0396e5b81605502e(
    *,
    bucket: builtins.str,
    key: builtins.str,
    role_arn: builtins.str,
    object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4a56c9731d882f4e0af0b136c973132c594cdb2f6c8607aa9bd92978d6d80b5(
    *,
    storage_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScript.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
