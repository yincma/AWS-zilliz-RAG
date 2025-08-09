r'''
# AWS::IVS Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_ivs as ivs
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IVS construct libraries](https://constructs.dev/search?q=ivs)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IVS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IVS.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-ivs-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IVS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IVS.html).

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
class CfnChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ivs.CfnChannel",
):
    '''The ``AWS::IVS::Channel`` resource specifies an  channel.

    A channel stores configuration information related to your live stream. For more information, see `CreateChannel <https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreateChannel.html>`_ in the *Amazon IVS Low-Latency Streaming API Reference* .
    .. epigraph::

       By default, the IVS API CreateChannel endpoint creates a stream key in addition to a channel. The  Channel resource *does not* create a stream key; to create a stream key, use the StreamKey resource instead.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html
    :cloudformationResource: AWS::IVS::Channel
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ivs as ivs
        
        cfn_channel = ivs.CfnChannel(self, "MyCfnChannel",
            authorized=False,
            container_format="containerFormat",
            insecure_ingest=False,
            latency_mode="latencyMode",
            multitrack_input_configuration=ivs.CfnChannel.MultitrackInputConfigurationProperty(
                enabled=False,
                maximum_resolution="maximumResolution",
                policy="policy"
            ),
            name="name",
            preset="preset",
            recording_configuration_arn="recordingConfigurationArn",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            type="type"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        authorized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        container_format: typing.Optional[builtins.str] = None,
        insecure_ingest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        latency_mode: typing.Optional[builtins.str] = None,
        multitrack_input_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnChannel.MultitrackInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        preset: typing.Optional[builtins.str] = None,
        recording_configuration_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param authorized: Whether the channel is authorized. Default: - false
        :param container_format: Indicates which content-packaging format is used (MPEG-TS or fMP4). If multitrackInputConfiguration is specified and enabled is true, then containerFormat is required and must be set to FRAGMENTED_MP4. Otherwise, containerFormat may be set to TS or FRAGMENTED_MP4. Default: TS. Default: - "TS"
        :param insecure_ingest: Whether the channel allows insecure ingest. Default: - false
        :param latency_mode: Channel latency mode. Default: - "LOW"
        :param multitrack_input_configuration: Object specifying multitrack input configuration. Default: no multitrack input configuration is specified.
        :param name: Channel. Default: - "-"
        :param preset: Optional transcode preset for the channel. This is selectable only for ADVANCED_HD and ADVANCED_SD channel types. For those channel types, the default preset is HIGHER_BANDWIDTH_DELIVERY. For other channel types (BASIC and STANDARD), preset is the empty string ("").
        :param recording_configuration_arn: Recording Configuration ARN. A value other than an empty string indicates that recording is enabled. Default: "" (recording is disabled). Default: - ""
        :param tags: A list of key-value pairs that contain metadata for the asset model.
        :param type: Channel type, which determines the allowable resolution and bitrate. If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately. Default: - "STANDARD"
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__998485c6924ca07e096c10b7976e238a36e5cfb75264ee66a67de472363369d6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnChannelProps(
            authorized=authorized,
            container_format=container_format,
            insecure_ingest=insecure_ingest,
            latency_mode=latency_mode,
            multitrack_input_configuration=multitrack_input_configuration,
            name=name,
            preset=preset,
            recording_configuration_arn=recording_configuration_arn,
            tags=tags,
            type=type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b2f270a2cc06d7958dc82935ff792ce64817de7fc16c4f4b5a7afa6f76cdd80)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0fa81ac5355ae77db888dc8d0fb4cbbff54f381372b1c5a191ceb5eb77a6442b)
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
        '''Channel ARN is automatically generated on creation and assigned as the unique identifier.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrIngestEndpoint")
    def attr_ingest_endpoint(self) -> builtins.str:
        '''Channel ingest endpoint, part of the definition of an ingest server, used when you set up streaming software.

        :cloudformationAttribute: IngestEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIngestEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrPlaybackUrl")
    def attr_playback_url(self) -> builtins.str:
        '''Channel Playback URL.

        :cloudformationAttribute: PlaybackUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPlaybackUrl"))

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
    @jsii.member(jsii_name="authorized")
    def authorized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the channel is authorized.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "authorized"))

    @authorized.setter
    def authorized(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e83b3a70b60de37a8aabc9c019b31db83c549e80f9c9c88a5b74fde72ecb20e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorized", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="containerFormat")
    def container_format(self) -> typing.Optional[builtins.str]:
        '''Indicates which content-packaging format is used (MPEG-TS or fMP4).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerFormat"))

    @container_format.setter
    def container_format(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5da102677f3042d402ff70f74aee693c78470595fd1a7c9b4900403983f7b74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerFormat", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="insecureIngest")
    def insecure_ingest(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the channel allows insecure ingest.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "insecureIngest"))

    @insecure_ingest.setter
    def insecure_ingest(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__734c5e1f9cdeabe74fb1ade992399b475d1594cbcdfd026823e8984eaa2d4eab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureIngest", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="latencyMode")
    def latency_mode(self) -> typing.Optional[builtins.str]:
        '''Channel latency mode.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "latencyMode"))

    @latency_mode.setter
    def latency_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd2cfeff050510b655ecd39d0e3b95c3c9e2af649e77e0903ad721d0f6428ab5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latencyMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="multitrackInputConfiguration")
    def multitrack_input_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.MultitrackInputConfigurationProperty"]]:
        '''Object specifying multitrack input configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.MultitrackInputConfigurationProperty"]], jsii.get(self, "multitrackInputConfiguration"))

    @multitrack_input_configuration.setter
    def multitrack_input_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.MultitrackInputConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__012c045fd3860567ed6aa28435a35d575d1dc0a881855d124b21f2d76102ba73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multitrackInputConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''Channel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15776afbbb29227b4807e807447939235926366be32ef5acc331c74f0acd9b41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="preset")
    def preset(self) -> typing.Optional[builtins.str]:
        '''Optional transcode preset for the channel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preset"))

    @preset.setter
    def preset(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95e047ef543e7e26080292a0481b6ce40457143e76918ac4c1c2d13855ce22ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preset", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="recordingConfigurationArn")
    def recording_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''Recording Configuration ARN.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordingConfigurationArn"))

    @recording_configuration_arn.setter
    def recording_configuration_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eb4132c8e5e803f734f8f894d72d2324ee00be84b0babafa7076d94d732c960)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordingConfigurationArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that contain metadata for the asset model.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da42cce1a703989106b1844fef6f10d0a57f43c733d171564b16f83c208e7196)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''Channel type, which determines the allowable resolution and bitrate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0be9a3a6192cfd130520f4e6ecd8c9091b1a8b4312f716182989ea3feb88dc8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ivs.CfnChannel.MultitrackInputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "maximum_resolution": "maximumResolution",
            "policy": "policy",
        },
    )
    class MultitrackInputConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            maximum_resolution: typing.Optional[builtins.str] = None,
            policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A complex type that specifies multitrack input configuration.

            :param enabled: Indicates whether multitrack input is enabled. Can be set to true only if channel type is STANDARD. Setting enabled to true with any other channel type will cause an exception. If true, then policy, maximumResolution, and containerFormat are required, and containerFormat must be set to FRAGMENTED_MP4. Default: false. Default: - false
            :param maximum_resolution: Maximum resolution for multitrack input. Required if enabled is true.
            :param policy: Indicates whether multitrack input is allowed or required. Required if enabled is true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-channel-multitrackinputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ivs as ivs
                
                multitrack_input_configuration_property = ivs.CfnChannel.MultitrackInputConfigurationProperty(
                    enabled=False,
                    maximum_resolution="maximumResolution",
                    policy="policy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__50f1752d428e0d083b8ac0b36e82de6eba9749ea58d877e914d9e63a503364d1)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument maximum_resolution", value=maximum_resolution, expected_type=type_hints["maximum_resolution"])
                check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if maximum_resolution is not None:
                self._values["maximum_resolution"] = maximum_resolution
            if policy is not None:
                self._values["policy"] = policy

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether multitrack input is enabled.

            Can be set to true only if channel type is STANDARD. Setting enabled to true with any other channel type will cause an exception. If true, then policy, maximumResolution, and containerFormat are required, and containerFormat must be set to FRAGMENTED_MP4. Default: false.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-channel-multitrackinputconfiguration.html#cfn-ivs-channel-multitrackinputconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def maximum_resolution(self) -> typing.Optional[builtins.str]:
            '''Maximum resolution for multitrack input.

            Required if enabled is true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-channel-multitrackinputconfiguration.html#cfn-ivs-channel-multitrackinputconfiguration-maximumresolution
            '''
            result = self._values.get("maximum_resolution")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def policy(self) -> typing.Optional[builtins.str]:
            '''Indicates whether multitrack input is allowed or required.

            Required if enabled is true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-channel-multitrackinputconfiguration.html#cfn-ivs-channel-multitrackinputconfiguration-policy
            '''
            result = self._values.get("policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MultitrackInputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ivs.CfnChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "authorized": "authorized",
        "container_format": "containerFormat",
        "insecure_ingest": "insecureIngest",
        "latency_mode": "latencyMode",
        "multitrack_input_configuration": "multitrackInputConfiguration",
        "name": "name",
        "preset": "preset",
        "recording_configuration_arn": "recordingConfigurationArn",
        "tags": "tags",
        "type": "type",
    },
)
class CfnChannelProps:
    def __init__(
        self,
        *,
        authorized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        container_format: typing.Optional[builtins.str] = None,
        insecure_ingest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        latency_mode: typing.Optional[builtins.str] = None,
        multitrack_input_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.MultitrackInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        preset: typing.Optional[builtins.str] = None,
        recording_configuration_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnChannel``.

        :param authorized: Whether the channel is authorized. Default: - false
        :param container_format: Indicates which content-packaging format is used (MPEG-TS or fMP4). If multitrackInputConfiguration is specified and enabled is true, then containerFormat is required and must be set to FRAGMENTED_MP4. Otherwise, containerFormat may be set to TS or FRAGMENTED_MP4. Default: TS. Default: - "TS"
        :param insecure_ingest: Whether the channel allows insecure ingest. Default: - false
        :param latency_mode: Channel latency mode. Default: - "LOW"
        :param multitrack_input_configuration: Object specifying multitrack input configuration. Default: no multitrack input configuration is specified.
        :param name: Channel. Default: - "-"
        :param preset: Optional transcode preset for the channel. This is selectable only for ADVANCED_HD and ADVANCED_SD channel types. For those channel types, the default preset is HIGHER_BANDWIDTH_DELIVERY. For other channel types (BASIC and STANDARD), preset is the empty string ("").
        :param recording_configuration_arn: Recording Configuration ARN. A value other than an empty string indicates that recording is enabled. Default: "" (recording is disabled). Default: - ""
        :param tags: A list of key-value pairs that contain metadata for the asset model.
        :param type: Channel type, which determines the allowable resolution and bitrate. If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately. Default: - "STANDARD"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ivs as ivs
            
            cfn_channel_props = ivs.CfnChannelProps(
                authorized=False,
                container_format="containerFormat",
                insecure_ingest=False,
                latency_mode="latencyMode",
                multitrack_input_configuration=ivs.CfnChannel.MultitrackInputConfigurationProperty(
                    enabled=False,
                    maximum_resolution="maximumResolution",
                    policy="policy"
                ),
                name="name",
                preset="preset",
                recording_configuration_arn="recordingConfigurationArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                type="type"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61646017dba4df4ec5b97fde61911670aebc6b8151847b927754a4e9c110979d)
            check_type(argname="argument authorized", value=authorized, expected_type=type_hints["authorized"])
            check_type(argname="argument container_format", value=container_format, expected_type=type_hints["container_format"])
            check_type(argname="argument insecure_ingest", value=insecure_ingest, expected_type=type_hints["insecure_ingest"])
            check_type(argname="argument latency_mode", value=latency_mode, expected_type=type_hints["latency_mode"])
            check_type(argname="argument multitrack_input_configuration", value=multitrack_input_configuration, expected_type=type_hints["multitrack_input_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument preset", value=preset, expected_type=type_hints["preset"])
            check_type(argname="argument recording_configuration_arn", value=recording_configuration_arn, expected_type=type_hints["recording_configuration_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if authorized is not None:
            self._values["authorized"] = authorized
        if container_format is not None:
            self._values["container_format"] = container_format
        if insecure_ingest is not None:
            self._values["insecure_ingest"] = insecure_ingest
        if latency_mode is not None:
            self._values["latency_mode"] = latency_mode
        if multitrack_input_configuration is not None:
            self._values["multitrack_input_configuration"] = multitrack_input_configuration
        if name is not None:
            self._values["name"] = name
        if preset is not None:
            self._values["preset"] = preset
        if recording_configuration_arn is not None:
            self._values["recording_configuration_arn"] = recording_configuration_arn
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def authorized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the channel is authorized.

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-authorized
        '''
        result = self._values.get("authorized")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def container_format(self) -> typing.Optional[builtins.str]:
        '''Indicates which content-packaging format is used (MPEG-TS or fMP4).

        If multitrackInputConfiguration is specified and enabled is true, then containerFormat is required and must be set to FRAGMENTED_MP4. Otherwise, containerFormat may be set to TS or FRAGMENTED_MP4. Default: TS.

        :default: - "TS"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-containerformat
        '''
        result = self._values.get("container_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_ingest(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the channel allows insecure ingest.

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-insecureingest
        '''
        result = self._values.get("insecure_ingest")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def latency_mode(self) -> typing.Optional[builtins.str]:
        '''Channel latency mode.

        :default: - "LOW"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-latencymode
        '''
        result = self._values.get("latency_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multitrack_input_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.MultitrackInputConfigurationProperty]]:
        '''Object specifying multitrack input configuration.

        Default: no multitrack input configuration is specified.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-multitrackinputconfiguration
        '''
        result = self._values.get("multitrack_input_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.MultitrackInputConfigurationProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Channel.

        :default: - "-"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preset(self) -> typing.Optional[builtins.str]:
        '''Optional transcode preset for the channel.

        This is selectable only for ADVANCED_HD and ADVANCED_SD channel types. For those channel types, the default preset is HIGHER_BANDWIDTH_DELIVERY. For other channel types (BASIC and STANDARD), preset is the empty string ("").

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-preset
        '''
        result = self._values.get("preset")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recording_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''Recording Configuration ARN.

        A value other than an empty string indicates that recording is enabled. Default: "" (recording is disabled).

        :default: - ""

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-recordingconfigurationarn
        '''
        result = self._values.get("recording_configuration_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that contain metadata for the asset model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Channel type, which determines the allowable resolution and bitrate.

        If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.

        :default: - "STANDARD"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnEncoderConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ivs.CfnEncoderConfiguration",
):
    '''The ``AWS::IVS::EncoderConfiguration`` resource specifies an  encoder configuration.

    An encoder configuration describes a stream’s video configuration. For more information, see `Streaming Configuration <https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/streaming-config.html>`_ in the *Amazon IVS Low-Latency Streaming User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-encoderconfiguration.html
    :cloudformationResource: AWS::IVS::EncoderConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ivs as ivs
        
        cfn_encoder_configuration = ivs.CfnEncoderConfiguration(self, "MyCfnEncoderConfiguration",
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            video=ivs.CfnEncoderConfiguration.VideoProperty(
                bitrate=123,
                framerate=123,
                height=123,
                width=123
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        video: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEncoderConfiguration.VideoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: Encoder cnfiguration name.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-encoderconfiguration-tag.html>`_ .
        :param video: Video configuration. Default: video resolution 1280x720, bitrate 2500 kbps, 30 fps. See the `Video <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-encoderconfiguration-video.html>`_ property type for more information.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0567625f957d978c482944a46fdbb2b7533ef9af0df4baffa7c6f443e004d9f9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEncoderConfigurationProps(name=name, tags=tags, video=video)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74f3191bc79bc285f7b8eefaf911f57a87950083af93a8ec3c39d61421b97b29)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5894ac5581a1dc1e629e1f66ec2014665b3f9227b553389ebce9188b817c4d61)
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
        '''The encoder-configuration ARN.

        For example: ``arn:aws:ivs:us-west-2:123456789012:encoder-configuration/abcdABCDefgh``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
        '''Encoder cnfiguration name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29237afd8a2086ac2e4d8c43148154a3bd8987f1c1e0ff26a989a10c5f072ba2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43c7ff5eb70740ddcbf72fae725c27870249dfb23fdbca3df5963221ac9c132f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="video")
    def video(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEncoderConfiguration.VideoProperty"]]:
        '''Video configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEncoderConfiguration.VideoProperty"]], jsii.get(self, "video"))

    @video.setter
    def video(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEncoderConfiguration.VideoProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f165a00a101e72d860585d7255e3d0ae733a51dcec3ea6dd3e616d27778b3415)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "video", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ivs.CfnEncoderConfiguration.VideoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bitrate": "bitrate",
            "framerate": "framerate",
            "height": "height",
            "width": "width",
        },
    )
    class VideoProperty:
        def __init__(
            self,
            *,
            bitrate: typing.Optional[jsii.Number] = None,
            framerate: typing.Optional[jsii.Number] = None,
            height: typing.Optional[jsii.Number] = None,
            width: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The Video property type describes a stream's video configuration.

            :param bitrate: Bitrate for generated output, in bps. Default: 2500000. Default: - 2500000
            :param framerate: Video frame rate, in fps. Default: 30. Default: - 30
            :param height: Video-resolution height. Note that the maximum value is determined by width times height, such that the maximum total pixels is 2073600 (1920x1080 or 1080x1920). Default: 720. Default: - 720
            :param width: Video-resolution width. Note that the maximum value is determined by width times height, such that the maximum total pixels is 2073600 (1920x1080 or 1080x1920). Default: 1280. Default: - 1280

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-encoderconfiguration-video.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ivs as ivs
                
                video_property = ivs.CfnEncoderConfiguration.VideoProperty(
                    bitrate=123,
                    framerate=123,
                    height=123,
                    width=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__34f2c1c7f794b153dbb8eef658c04b4e6467fa06e325f7b2c94dc782acbeab26)
                check_type(argname="argument bitrate", value=bitrate, expected_type=type_hints["bitrate"])
                check_type(argname="argument framerate", value=framerate, expected_type=type_hints["framerate"])
                check_type(argname="argument height", value=height, expected_type=type_hints["height"])
                check_type(argname="argument width", value=width, expected_type=type_hints["width"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bitrate is not None:
                self._values["bitrate"] = bitrate
            if framerate is not None:
                self._values["framerate"] = framerate
            if height is not None:
                self._values["height"] = height
            if width is not None:
                self._values["width"] = width

        @builtins.property
        def bitrate(self) -> typing.Optional[jsii.Number]:
            '''Bitrate for generated output, in bps.

            Default: 2500000.

            :default: - 2500000

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-encoderconfiguration-video.html#cfn-ivs-encoderconfiguration-video-bitrate
            '''
            result = self._values.get("bitrate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def framerate(self) -> typing.Optional[jsii.Number]:
            '''Video frame rate, in fps.

            Default: 30.

            :default: - 30

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-encoderconfiguration-video.html#cfn-ivs-encoderconfiguration-video-framerate
            '''
            result = self._values.get("framerate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def height(self) -> typing.Optional[jsii.Number]:
            '''Video-resolution height.

            Note that the maximum value is determined by width times height, such that the maximum total pixels is 2073600 (1920x1080 or 1080x1920). Default: 720.

            :default: - 720

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-encoderconfiguration-video.html#cfn-ivs-encoderconfiguration-video-height
            '''
            result = self._values.get("height")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def width(self) -> typing.Optional[jsii.Number]:
            '''Video-resolution width.

            Note that the maximum value is determined by width times height, such that the maximum total pixels is 2073600 (1920x1080 or 1080x1920). Default: 1280.

            :default: - 1280

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-encoderconfiguration-video.html#cfn-ivs-encoderconfiguration-video-width
            '''
            result = self._values.get("width")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ivs.CfnEncoderConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "tags": "tags", "video": "video"},
)
class CfnEncoderConfigurationProps:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        video: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEncoderConfiguration.VideoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEncoderConfiguration``.

        :param name: Encoder cnfiguration name.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-encoderconfiguration-tag.html>`_ .
        :param video: Video configuration. Default: video resolution 1280x720, bitrate 2500 kbps, 30 fps. See the `Video <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-encoderconfiguration-video.html>`_ property type for more information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-encoderconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ivs as ivs
            
            cfn_encoder_configuration_props = ivs.CfnEncoderConfigurationProps(
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                video=ivs.CfnEncoderConfiguration.VideoProperty(
                    bitrate=123,
                    framerate=123,
                    height=123,
                    width=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__663e73ad8dc18892ff8c6aa7cec15d284adf341fe58eeb580e68cff0a92ee161)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument video", value=video, expected_type=type_hints["video"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if video is not None:
            self._values["video"] = video

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Encoder cnfiguration name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-encoderconfiguration.html#cfn-ivs-encoderconfiguration-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-encoderconfiguration-tag.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-encoderconfiguration.html#cfn-ivs-encoderconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def video(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEncoderConfiguration.VideoProperty]]:
        '''Video configuration.

        Default: video resolution 1280x720, bitrate 2500 kbps, 30 fps. See the `Video <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-encoderconfiguration-video.html>`_ property type for more information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-encoderconfiguration.html#cfn-ivs-encoderconfiguration-video
        '''
        result = self._values.get("video")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEncoderConfiguration.VideoProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEncoderConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnIngestConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ivs.CfnIngestConfiguration",
):
    '''The ``AWS::IVS::IngestConfiguration`` resource specifies an ingest protocol to be used for a stage.

    For more information, see `Stream Ingest <https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html>`_ in the *Amazon IVS Real-Time Streaming User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-ingestconfiguration.html
    :cloudformationResource: AWS::IVS::IngestConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ivs as ivs
        
        cfn_ingest_configuration = ivs.CfnIngestConfiguration(self, "MyCfnIngestConfiguration",
            ingest_protocol="ingestProtocol",
            insecure_ingest=False,
            name="name",
            stage_arn="stageArn",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            user_id="userId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        ingest_protocol: typing.Optional[builtins.str] = None,
        insecure_ingest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        name: typing.Optional[builtins.str] = None,
        stage_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param ingest_protocol: Type of ingest protocol that the user employs for broadcasting. Default: - "RTMPS"
        :param insecure_ingest: Whether the channel allows insecure RTMP ingest. Default: ``false`` . Default: - false
        :param name: Ingest name. Default: - "-"
        :param stage_arn: ARN of the stage with which the IngestConfiguration is associated. Default: - ""
        :param tags: An array of key-value pairs to apply to this resource.
        :param user_id: Customer-assigned name to help identify the participant using the IngestConfiguration; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c56f46c8c3462fcf78f3e0898b4048a399a031987b0a76a9193f42a0a98fcd5e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIngestConfigurationProps(
            ingest_protocol=ingest_protocol,
            insecure_ingest=insecure_ingest,
            name=name,
            stage_arn=stage_arn,
            tags=tags,
            user_id=user_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7a53bbb588815f0015c227540b92fa7ba4a33256116e056573299d99ef57574)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f47d1d0418cb9d42da8be28f4cb517e4e83775aec57930b9ba318f95f6168c3)
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
        '''The ingest-configuration ARN.

        For example: ``arn:aws:ivs:us-west-2:123456789012:ingest-configuration/abcdABCDefgh``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrParticipantId")
    def attr_participant_id(self) -> builtins.str:
        '''ID of the participant within the stage.

        For example: ``abCDEf12GHIj``

        :cloudformationAttribute: ParticipantId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrParticipantId"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''State of the ingest configuration.

        It is ``ACTIVE`` if a publisher currently is publishing to the stage associated with the ingest configuration. Valid values: ``ACTIVE`` | ``INACTIVE`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="attrStreamKey")
    def attr_stream_key(self) -> builtins.str:
        '''Ingest-key value for the RTMP(S) protocol.

        For example: ``skSKABCDefgh``

        :cloudformationAttribute: StreamKey
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStreamKey"))

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
    @jsii.member(jsii_name="ingestProtocol")
    def ingest_protocol(self) -> typing.Optional[builtins.str]:
        '''Type of ingest protocol that the user employs for broadcasting.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ingestProtocol"))

    @ingest_protocol.setter
    def ingest_protocol(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__313ff481891bab6b5a8445b484bcb46c2d4e31789868f166495c526d0fe9002e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingestProtocol", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="insecureIngest")
    def insecure_ingest(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the channel allows insecure RTMP ingest.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "insecureIngest"))

    @insecure_ingest.setter
    def insecure_ingest(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d0984e439ef9b3c25fe01666d92f1599a4bb2f408cc94a9bac3809e4fb8c00c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureIngest", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''Ingest name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6ff791ee5d9887b8c66e010bf22c541fc5aa016c9908c44f04c9d7c7c5e71d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="stageArn")
    def stage_arn(self) -> typing.Optional[builtins.str]:
        '''ARN of the stage with which the IngestConfiguration is associated.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stageArn"))

    @stage_arn.setter
    def stage_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d63930d5464ce48d09d7120e42b1e7aa23bfb45a07d7c93dda8514184602ac2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stageArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87601b6a8bacd8fefd6cc75f708d5009dad0f359e9544422e980fffade00bb04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="userId")
    def user_id(self) -> typing.Optional[builtins.str]:
        '''Customer-assigned name to help identify the participant using the IngestConfiguration;'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userId"))

    @user_id.setter
    def user_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6c53b4493812dc096bfe5e107d3ab87615d06685c537ce27b9778a2701dd28b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userId", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ivs.CfnIngestConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "ingest_protocol": "ingestProtocol",
        "insecure_ingest": "insecureIngest",
        "name": "name",
        "stage_arn": "stageArn",
        "tags": "tags",
        "user_id": "userId",
    },
)
class CfnIngestConfigurationProps:
    def __init__(
        self,
        *,
        ingest_protocol: typing.Optional[builtins.str] = None,
        insecure_ingest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        name: typing.Optional[builtins.str] = None,
        stage_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnIngestConfiguration``.

        :param ingest_protocol: Type of ingest protocol that the user employs for broadcasting. Default: - "RTMPS"
        :param insecure_ingest: Whether the channel allows insecure RTMP ingest. Default: ``false`` . Default: - false
        :param name: Ingest name. Default: - "-"
        :param stage_arn: ARN of the stage with which the IngestConfiguration is associated. Default: - ""
        :param tags: An array of key-value pairs to apply to this resource.
        :param user_id: Customer-assigned name to help identify the participant using the IngestConfiguration; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-ingestconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ivs as ivs
            
            cfn_ingest_configuration_props = ivs.CfnIngestConfigurationProps(
                ingest_protocol="ingestProtocol",
                insecure_ingest=False,
                name="name",
                stage_arn="stageArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                user_id="userId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95e9b18dcfb57342b7d6f80c4ce0d7b8886a64f91d3622dce01cf4e958236e01)
            check_type(argname="argument ingest_protocol", value=ingest_protocol, expected_type=type_hints["ingest_protocol"])
            check_type(argname="argument insecure_ingest", value=insecure_ingest, expected_type=type_hints["insecure_ingest"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument stage_arn", value=stage_arn, expected_type=type_hints["stage_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ingest_protocol is not None:
            self._values["ingest_protocol"] = ingest_protocol
        if insecure_ingest is not None:
            self._values["insecure_ingest"] = insecure_ingest
        if name is not None:
            self._values["name"] = name
        if stage_arn is not None:
            self._values["stage_arn"] = stage_arn
        if tags is not None:
            self._values["tags"] = tags
        if user_id is not None:
            self._values["user_id"] = user_id

    @builtins.property
    def ingest_protocol(self) -> typing.Optional[builtins.str]:
        '''Type of ingest protocol that the user employs for broadcasting.

        :default: - "RTMPS"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-ingestconfiguration.html#cfn-ivs-ingestconfiguration-ingestprotocol
        '''
        result = self._values.get("ingest_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_ingest(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the channel allows insecure RTMP ingest.

        Default: ``false`` .

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-ingestconfiguration.html#cfn-ivs-ingestconfiguration-insecureingest
        '''
        result = self._values.get("insecure_ingest")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Ingest name.

        :default: - "-"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-ingestconfiguration.html#cfn-ivs-ingestconfiguration-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stage_arn(self) -> typing.Optional[builtins.str]:
        '''ARN of the stage with which the IngestConfiguration is associated.

        :default: - ""

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-ingestconfiguration.html#cfn-ivs-ingestconfiguration-stagearn
        '''
        result = self._values.get("stage_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-ingestconfiguration.html#cfn-ivs-ingestconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def user_id(self) -> typing.Optional[builtins.str]:
        '''Customer-assigned name to help identify the participant using the IngestConfiguration;

        this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-ingestconfiguration.html#cfn-ivs-ingestconfiguration-userid
        '''
        result = self._values.get("user_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIngestConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPlaybackKeyPair(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ivs.CfnPlaybackKeyPair",
):
    '''The ``AWS::IVS::PlaybackKeyPair`` resource specifies an  playback key pair.

    uses a public playback key to validate playback tokens that have been signed with the corresponding private key. For more information, see `Setting Up Private Channels <https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-channels.html>`_ in the *Amazon IVS Low-Latency Streaming User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackkeypair.html
    :cloudformationResource: AWS::IVS::PlaybackKeyPair
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ivs as ivs
        
        cfn_playback_key_pair = ivs.CfnPlaybackKeyPair(self, "MyCfnPlaybackKeyPair",
            name="name",
            public_key_material="publicKeyMaterial",
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
        name: typing.Optional[builtins.str] = None,
        public_key_material: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: Playback-key-pair name. The value does not need to be unique.
        :param public_key_material: The public portion of a customer-generated key pair. Note that this field is required to create the AWS::IVS::PlaybackKeyPair resource.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-playbackkeypair-tag.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8c9299641f93177a19cfd84cad783d859723e15238afc5b2487f08100163f85)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPlaybackKeyPairProps(
            name=name, public_key_material=public_key_material, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34197af23f293afc0148baab246f15cd2fe54b95571370449978a5aeca67fa11)
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
            type_hints = typing.get_type_hints(_typecheckingstub__032f36985f3069b4c60d8aea57dfc3994cc6fa0fc29cbdac055ac20e5f4aca7c)
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
        '''Key-pair ARN.

        For example: ``arn:aws:ivs:us-west-2:693991300569:playback-key/f99cde61-c2b0-4df3-8941-ca7d38acca1a``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFingerprint")
    def attr_fingerprint(self) -> builtins.str:
        '''Key-pair identifier.

        For example: ``98:0d:1a:a0:19:96:1e:ea:0a:0a:2c:9a:42:19:2b:e7``

        :cloudformationAttribute: Fingerprint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFingerprint"))

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
    def name(self) -> typing.Optional[builtins.str]:
        '''Playback-key-pair name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ec5d532530f73a41d36dd7016f4d18021d800813e68dbfa6f703cceca701478)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicKeyMaterial")
    def public_key_material(self) -> typing.Optional[builtins.str]:
        '''The public portion of a customer-generated key pair.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicKeyMaterial"))

    @public_key_material.setter
    def public_key_material(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4f35a09db8d81cf5fc7e7a397ca8172e49d613e64494c5a29798609a388e294)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKeyMaterial", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74338171e55e9802fbeae4e8f45a4f31375c3a5730c487b0609b721a4660ce32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ivs.CfnPlaybackKeyPairProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "public_key_material": "publicKeyMaterial",
        "tags": "tags",
    },
)
class CfnPlaybackKeyPairProps:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        public_key_material: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPlaybackKeyPair``.

        :param name: Playback-key-pair name. The value does not need to be unique.
        :param public_key_material: The public portion of a customer-generated key pair. Note that this field is required to create the AWS::IVS::PlaybackKeyPair resource.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-playbackkeypair-tag.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackkeypair.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ivs as ivs
            
            cfn_playback_key_pair_props = ivs.CfnPlaybackKeyPairProps(
                name="name",
                public_key_material="publicKeyMaterial",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a8be2c5b1653b9a20f33850cbab1a9c21d6b30034b5c68883e658d0e145e6a3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument public_key_material", value=public_key_material, expected_type=type_hints["public_key_material"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if public_key_material is not None:
            self._values["public_key_material"] = public_key_material
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Playback-key-pair name.

        The value does not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackkeypair.html#cfn-ivs-playbackkeypair-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_key_material(self) -> typing.Optional[builtins.str]:
        '''The public portion of a customer-generated key pair.

        Note that this field is required to create the AWS::IVS::PlaybackKeyPair resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackkeypair.html#cfn-ivs-playbackkeypair-publickeymaterial
        '''
        result = self._values.get("public_key_material")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-playbackkeypair-tag.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackkeypair.html#cfn-ivs-playbackkeypair-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPlaybackKeyPairProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnPlaybackRestrictionPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ivs.CfnPlaybackRestrictionPolicy",
):
    '''The ``AWS::IVS::PlaybackRestrictionPolicy`` resource specifies an  playback restriction policy.

    A playback restriction policy constrains playback by country and/or origin sites. For more information, see `Undesired Content and Viewers <https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/undesired-content.html>`_ in the *Amazon IVS Low-Latency Streaming User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackrestrictionpolicy.html
    :cloudformationResource: AWS::IVS::PlaybackRestrictionPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ivs as ivs
        
        cfn_playback_restriction_policy = ivs.CfnPlaybackRestrictionPolicy(self, "MyCfnPlaybackRestrictionPolicy",
            allowed_countries=["allowedCountries"],
            allowed_origins=["allowedOrigins"],
        
            # the properties below are optional
            enable_strict_origin_enforcement=False,
            name="name",
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
        allowed_countries: typing.Sequence[builtins.str],
        allowed_origins: typing.Sequence[builtins.str],
        enable_strict_origin_enforcement: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param allowed_countries: A list of country codes that control geoblocking restrictions. Allowed values are the officially assigned ISO 3166-1 alpha-2 codes. Default: All countries (an empty array).
        :param allowed_origins: A list of origin sites that control CORS restriction. Allowed values are the same as valid values of the Origin header defined at `https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin" <https://docs.aws.amazon.com/https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin>`_
        :param enable_strict_origin_enforcement: Whether channel playback is constrained by the origin site. Default: - false
        :param name: Playback-restriction-policy name.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-playbackrestrictionpolicy-tag.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__987a35e58d5c2ae76d6f7c41b5ef19dc05ac42c651fd8a03f9f28e044029b375)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPlaybackRestrictionPolicyProps(
            allowed_countries=allowed_countries,
            allowed_origins=allowed_origins,
            enable_strict_origin_enforcement=enable_strict_origin_enforcement,
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f3f6891340e6dab4eba842f305f96e563b405ee29ecb437451d108aecb54492)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0e57b154c63f829875b079b3d6baf6c33a6d6c377987d9ac6e9f4586303e9729)
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
        '''The playback-restriction-policy ARN.

        For example: ``arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/abcdABCDefgh``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="allowedCountries")
    def allowed_countries(self) -> typing.List[builtins.str]:
        '''A list of country codes that control geoblocking restrictions.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedCountries"))

    @allowed_countries.setter
    def allowed_countries(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6636af9e45dbeea2bcf7b5990280edcd8fec18083a4bfe23a76e19bd655ef03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedCountries", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="allowedOrigins")
    def allowed_origins(self) -> typing.List[builtins.str]:
        '''A list of origin sites that control CORS restriction.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedOrigins"))

    @allowed_origins.setter
    def allowed_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__773f5ee580b6a7c42904b5a38460c9ae7e7e147bde8b69e1c43edddd32d7dc69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOrigins", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enableStrictOriginEnforcement")
    def enable_strict_origin_enforcement(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether channel playback is constrained by the origin site.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableStrictOriginEnforcement"))

    @enable_strict_origin_enforcement.setter
    def enable_strict_origin_enforcement(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67d34a00cb21cb2e87b091d21364ddc0afcd5ff11075db95ae750d23e62e2808)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableStrictOriginEnforcement", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''Playback-restriction-policy name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b36ada0e65d44733ed151613d84de1502ed0c39b1d83d8f62ea23a0f231bba3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72c43ae8ddd92a7ae402fb8cc1729052bd0d141f4f2106265c702c75bd0b9369)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ivs.CfnPlaybackRestrictionPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_countries": "allowedCountries",
        "allowed_origins": "allowedOrigins",
        "enable_strict_origin_enforcement": "enableStrictOriginEnforcement",
        "name": "name",
        "tags": "tags",
    },
)
class CfnPlaybackRestrictionPolicyProps:
    def __init__(
        self,
        *,
        allowed_countries: typing.Sequence[builtins.str],
        allowed_origins: typing.Sequence[builtins.str],
        enable_strict_origin_enforcement: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPlaybackRestrictionPolicy``.

        :param allowed_countries: A list of country codes that control geoblocking restrictions. Allowed values are the officially assigned ISO 3166-1 alpha-2 codes. Default: All countries (an empty array).
        :param allowed_origins: A list of origin sites that control CORS restriction. Allowed values are the same as valid values of the Origin header defined at `https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin" <https://docs.aws.amazon.com/https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin>`_
        :param enable_strict_origin_enforcement: Whether channel playback is constrained by the origin site. Default: - false
        :param name: Playback-restriction-policy name.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-playbackrestrictionpolicy-tag.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackrestrictionpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ivs as ivs
            
            cfn_playback_restriction_policy_props = ivs.CfnPlaybackRestrictionPolicyProps(
                allowed_countries=["allowedCountries"],
                allowed_origins=["allowedOrigins"],
            
                # the properties below are optional
                enable_strict_origin_enforcement=False,
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feaf48f348987f686c52239e867f8aedc7a8a6debbbc2bec008fea1cc72c201f)
            check_type(argname="argument allowed_countries", value=allowed_countries, expected_type=type_hints["allowed_countries"])
            check_type(argname="argument allowed_origins", value=allowed_origins, expected_type=type_hints["allowed_origins"])
            check_type(argname="argument enable_strict_origin_enforcement", value=enable_strict_origin_enforcement, expected_type=type_hints["enable_strict_origin_enforcement"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allowed_countries": allowed_countries,
            "allowed_origins": allowed_origins,
        }
        if enable_strict_origin_enforcement is not None:
            self._values["enable_strict_origin_enforcement"] = enable_strict_origin_enforcement
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def allowed_countries(self) -> typing.List[builtins.str]:
        '''A list of country codes that control geoblocking restrictions.

        Allowed values are the officially assigned ISO 3166-1 alpha-2 codes. Default: All countries (an empty array).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackrestrictionpolicy.html#cfn-ivs-playbackrestrictionpolicy-allowedcountries
        '''
        result = self._values.get("allowed_countries")
        assert result is not None, "Required property 'allowed_countries' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def allowed_origins(self) -> typing.List[builtins.str]:
        '''A list of origin sites that control CORS restriction.

        Allowed values are the same as valid values of the Origin header defined at `https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin" <https://docs.aws.amazon.com/https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackrestrictionpolicy.html#cfn-ivs-playbackrestrictionpolicy-allowedorigins
        '''
        result = self._values.get("allowed_origins")
        assert result is not None, "Required property 'allowed_origins' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def enable_strict_origin_enforcement(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether channel playback is constrained by the origin site.

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackrestrictionpolicy.html#cfn-ivs-playbackrestrictionpolicy-enablestrictoriginenforcement
        '''
        result = self._values.get("enable_strict_origin_enforcement")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Playback-restriction-policy name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackrestrictionpolicy.html#cfn-ivs-playbackrestrictionpolicy-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-playbackrestrictionpolicy-tag.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackrestrictionpolicy.html#cfn-ivs-playbackrestrictionpolicy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPlaybackRestrictionPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnPublicKey(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ivs.CfnPublicKey",
):
    '''The ``AWS::IVS::PublicKey`` resource specifies an Amazon IVS public key used to sign stage participant tokens.

    For more information, see `Distribute Participant Tokens <https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html>`_ in the *Amazon IVS Real-Time Streaming User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-publickey.html
    :cloudformationResource: AWS::IVS::PublicKey
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ivs as ivs
        
        cfn_public_key = ivs.CfnPublicKey(self, "MyCfnPublicKey",
            name="name",
            public_key_material="publicKeyMaterial",
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
        name: typing.Optional[builtins.str] = None,
        public_key_material: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: Public key name. The value does not need to be unique.
        :param public_key_material: The public portion of a customer-generated key pair. Note that this field is required to create the AWS::IVS::PublicKey resource.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69566f8b07a347c045dd6b2f0dfca75d7b37273e69681243f26273b19e06cd09)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPublicKeyProps(
            name=name, public_key_material=public_key_material, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e6b8cd6799dd82e06ff9988e9e614506cad2cdb4fd21af49f6565f000590088)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e64d06031e9bc941f4698d06e7ad4d4c0b95c41a9c231c5cc51e05f1bb3c217b)
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
        '''The public key ARN.

        For example: ``arn:aws:ivs:us-west-2:123456789012:public-key/abcdABCDefgh``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFingerprint")
    def attr_fingerprint(self) -> builtins.str:
        '''The public key identifier.

        For example: ``98:0d:1a:a0:19:96:1e:ea:0a:0a:2c:9a:42:19:2b:e7``

        :cloudformationAttribute: Fingerprint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFingerprint"))

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
        '''Public key name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d17e9902ef9a61f0eff6eb979f114b77f3840a826d3a39b4893ea2a98275b4be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicKeyMaterial")
    def public_key_material(self) -> typing.Optional[builtins.str]:
        '''The public portion of a customer-generated key pair.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicKeyMaterial"))

    @public_key_material.setter
    def public_key_material(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a843701534e0f215185c3c60d4ab2be6eb1b19877fea3f91057d6b805e21bc31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKeyMaterial", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5f083992aecb52530dd61b06308422142992ddce014c2eca8bd7e50b14a98e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ivs.CfnPublicKeyProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "public_key_material": "publicKeyMaterial",
        "tags": "tags",
    },
)
class CfnPublicKeyProps:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        public_key_material: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPublicKey``.

        :param name: Public key name. The value does not need to be unique.
        :param public_key_material: The public portion of a customer-generated key pair. Note that this field is required to create the AWS::IVS::PublicKey resource.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-publickey.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ivs as ivs
            
            cfn_public_key_props = ivs.CfnPublicKeyProps(
                name="name",
                public_key_material="publicKeyMaterial",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e24b7446ff29c9bd2fdfcc82ce735007c1472e2e0a7ef6f06d261450515e6a4)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument public_key_material", value=public_key_material, expected_type=type_hints["public_key_material"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if public_key_material is not None:
            self._values["public_key_material"] = public_key_material
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Public key name.

        The value does not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-publickey.html#cfn-ivs-publickey-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_key_material(self) -> typing.Optional[builtins.str]:
        '''The public portion of a customer-generated key pair.

        Note that this field is required to create the AWS::IVS::PublicKey resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-publickey.html#cfn-ivs-publickey-publickeymaterial
        '''
        result = self._values.get("public_key_material")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-publickey.html#cfn-ivs-publickey-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPublicKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRecordingConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ivs.CfnRecordingConfiguration",
):
    '''The ``AWS::IVS::RecordingConfiguration`` resource specifies an  recording configuration.

    A recording configuration enables the recording of a channel’s live streams to a data store. Multiple channels can reference the same recording configuration. For more information, see `RecordingConfiguration <https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_RecordingConfiguration.html>`_ in the *Amazon IVS Low-Latency Streaming API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html
    :cloudformationResource: AWS::IVS::RecordingConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ivs as ivs
        
        cfn_recording_configuration = ivs.CfnRecordingConfiguration(self, "MyCfnRecordingConfiguration",
            destination_configuration=ivs.CfnRecordingConfiguration.DestinationConfigurationProperty(
                s3=ivs.CfnRecordingConfiguration.S3DestinationConfigurationProperty(
                    bucket_name="bucketName"
                )
            ),
        
            # the properties below are optional
            name="name",
            recording_reconnect_window_seconds=123,
            rendition_configuration=ivs.CfnRecordingConfiguration.RenditionConfigurationProperty(
                renditions=["renditions"],
                rendition_selection="renditionSelection"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            thumbnail_configuration=ivs.CfnRecordingConfiguration.ThumbnailConfigurationProperty(
                recording_mode="recordingMode",
                resolution="resolution",
                storage=["storage"],
                target_interval_seconds=123
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        destination_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordingConfiguration.DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        name: typing.Optional[builtins.str] = None,
        recording_reconnect_window_seconds: typing.Optional[jsii.Number] = None,
        rendition_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordingConfiguration.RenditionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        thumbnail_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordingConfiguration.ThumbnailConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destination_configuration: A destination configuration describes an S3 bucket where recorded video will be stored. See the DestinationConfiguration property type for more information.
        :param name: Recording-configuration name. The value does not need to be unique.
        :param recording_reconnect_window_seconds: If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together. *Default* : ``0`` Default: - 0
        :param rendition_configuration: A rendition configuration describes which renditions should be recorded for a stream. See the RenditionConfiguration property type for more information.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-tag.html>`_ .
        :param thumbnail_configuration: A thumbnail configuration enables/disables the recording of thumbnails for a live session and controls the interval at which thumbnails are generated for the live session. See the ThumbnailConfiguration property type for more information.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__541cdf033047e5777646c5f067e03131707927e43c41e609fd3ac9ee776ae419)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRecordingConfigurationProps(
            destination_configuration=destination_configuration,
            name=name,
            recording_reconnect_window_seconds=recording_reconnect_window_seconds,
            rendition_configuration=rendition_configuration,
            tags=tags,
            thumbnail_configuration=thumbnail_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d115d5ab74114a12edd8791ec11e4e4fd145cc6289d0579aac04f1c0c4089f8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3316cacec890424787de7224c6afcca2922a5899126aec97f005c3ea43409d1f)
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
        '''The recording configuration ARN.

        For example: ``arn:aws:ivs:us-west-2:123456789012:recording-configuration/abcdABCDefgh``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''Indicates the current state of the recording configuration.

        When the state is ``ACTIVE`` , the configuration is ready to record a channel stream. Valid values: ``CREATING`` | ``CREATE_FAILED`` | ``ACTIVE`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

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
    @jsii.member(jsii_name="destinationConfiguration")
    def destination_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.DestinationConfigurationProperty"]:
        '''A destination configuration describes an S3 bucket where recorded video will be stored.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.DestinationConfigurationProperty"], jsii.get(self, "destinationConfiguration"))

    @destination_configuration.setter
    def destination_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.DestinationConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a98f37a00ab2b8c5a3413e54b7f022ac0bdf7ee44225243da737d75b9412595a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''Recording-configuration name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6dd9b8dd365a2dac11937c93668ced572b553c203da9cbf1d9e0932d0e24faf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="recordingReconnectWindowSeconds")
    def recording_reconnect_window_seconds(self) -> typing.Optional[jsii.Number]:
        '''If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "recordingReconnectWindowSeconds"))

    @recording_reconnect_window_seconds.setter
    def recording_reconnect_window_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38ff85ea7b2f1195ae4ae39514f42471c20d787399e92729b09aa86def8d11c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordingReconnectWindowSeconds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="renditionConfiguration")
    def rendition_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.RenditionConfigurationProperty"]]:
        '''A rendition configuration describes which renditions should be recorded for a stream.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.RenditionConfigurationProperty"]], jsii.get(self, "renditionConfiguration"))

    @rendition_configuration.setter
    def rendition_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.RenditionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__607bfa50f9dd6b9828bada1c2c536f7277619bb3020e56c415227efdb3ba1fa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "renditionConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__980f42185f1f8239b1f7d72b3f84be9a9c93c5d02f84695a71964c0630115230)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="thumbnailConfiguration")
    def thumbnail_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.ThumbnailConfigurationProperty"]]:
        '''A thumbnail configuration enables/disables the recording of thumbnails for a live session and controls the interval at which thumbnails are generated for the live session.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.ThumbnailConfigurationProperty"]], jsii.get(self, "thumbnailConfiguration"))

    @thumbnail_configuration.setter
    def thumbnail_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.ThumbnailConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5cda01e5b9f5edb6a6ec7c5dce6ad1cecc2b7ce8727dd09a38d4b2b04befd3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thumbnailConfiguration", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ivs.CfnRecordingConfiguration.DestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3": "s3"},
    )
    class DestinationConfigurationProperty:
        def __init__(
            self,
            *,
            s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordingConfiguration.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The DestinationConfiguration property type describes the location where recorded videos will be stored.

            Each member represents a type of destination configuration. For recording, you define one and only one type of destination configuration.

            :param s3: An S3 destination configuration where recorded videos will be stored. See the `S3DestinationConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-s3destinationconfiguration.html>`_ property type for more information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-destinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ivs as ivs
                
                destination_configuration_property = ivs.CfnRecordingConfiguration.DestinationConfigurationProperty(
                    s3=ivs.CfnRecordingConfiguration.S3DestinationConfigurationProperty(
                        bucket_name="bucketName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__74552278e1b145c98ed786a3d8f29802876ef78e57a458c3030b125a545b6a0f)
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3 is not None:
                self._values["s3"] = s3

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.S3DestinationConfigurationProperty"]]:
            '''An S3 destination configuration where recorded videos will be stored.

            See the `S3DestinationConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-s3destinationconfiguration.html>`_ property type for more information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-destinationconfiguration.html#cfn-ivs-recordingconfiguration-destinationconfiguration-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.S3DestinationConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ivs.CfnRecordingConfiguration.RenditionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "renditions": "renditions",
            "rendition_selection": "renditionSelection",
        },
    )
    class RenditionConfigurationProperty:
        def __init__(
            self,
            *,
            renditions: typing.Optional[typing.Sequence[builtins.str]] = None,
            rendition_selection: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The RenditionConfiguration property type describes which renditions should be recorded for a stream.

            :param renditions: A list of which renditions are recorded for a stream, if ``renditionSelection`` is ``CUSTOM`` ; otherwise, this field is irrelevant. The selected renditions are recorded if they are available during the stream. If a selected rendition is unavailable, the best available rendition is recorded. For details on the resolution dimensions of each rendition, see `Auto-Record to Amazon S3 <https://docs.aws.amazon.com//ivs/latest/LowLatencyUserGuide/record-to-s3.html>`_ .
            :param rendition_selection: The set of renditions are recorded for a stream. For ``BASIC`` channels, the ``CUSTOM`` value has no effect. If ``CUSTOM`` is specified, a set of renditions can be specified in the ``renditions`` field. Default: ``ALL`` . Default: - "ALL"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-renditionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ivs as ivs
                
                rendition_configuration_property = ivs.CfnRecordingConfiguration.RenditionConfigurationProperty(
                    renditions=["renditions"],
                    rendition_selection="renditionSelection"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__556cbf534b885cc5fd04e7604c8916e78d98c9f230358bec7ded8f7e34aa0394)
                check_type(argname="argument renditions", value=renditions, expected_type=type_hints["renditions"])
                check_type(argname="argument rendition_selection", value=rendition_selection, expected_type=type_hints["rendition_selection"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if renditions is not None:
                self._values["renditions"] = renditions
            if rendition_selection is not None:
                self._values["rendition_selection"] = rendition_selection

        @builtins.property
        def renditions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of which renditions are recorded for a stream, if ``renditionSelection`` is ``CUSTOM`` ;

            otherwise, this field is irrelevant. The selected renditions are recorded if they are available during the stream. If a selected rendition is unavailable, the best available rendition is recorded. For details on the resolution dimensions of each rendition, see `Auto-Record to Amazon S3 <https://docs.aws.amazon.com//ivs/latest/LowLatencyUserGuide/record-to-s3.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-renditionconfiguration.html#cfn-ivs-recordingconfiguration-renditionconfiguration-renditions
            '''
            result = self._values.get("renditions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def rendition_selection(self) -> typing.Optional[builtins.str]:
            '''The set of renditions are recorded for a stream.

            For ``BASIC`` channels, the ``CUSTOM`` value has no effect. If ``CUSTOM`` is specified, a set of renditions can be specified in the ``renditions`` field. Default: ``ALL`` .

            :default: - "ALL"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-renditionconfiguration.html#cfn-ivs-recordingconfiguration-renditionconfiguration-renditionselection
            '''
            result = self._values.get("rendition_selection")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RenditionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ivs.CfnRecordingConfiguration.S3DestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName"},
    )
    class S3DestinationConfigurationProperty:
        def __init__(self, *, bucket_name: builtins.str) -> None:
            '''The S3DestinationConfiguration property type describes an S3 location where recorded videos will be stored.

            :param bucket_name: Location (S3 bucket name) where recorded videos will be stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-s3destinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ivs as ivs
                
                s3_destination_configuration_property = ivs.CfnRecordingConfiguration.S3DestinationConfigurationProperty(
                    bucket_name="bucketName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c973ee3e6df5393489017eab5a2edc4f798c18919ab571067170163085c0d659)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
            }

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''Location (S3 bucket name) where recorded videos will be stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-s3destinationconfiguration.html#cfn-ivs-recordingconfiguration-s3destinationconfiguration-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ivs.CfnRecordingConfiguration.ThumbnailConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "recording_mode": "recordingMode",
            "resolution": "resolution",
            "storage": "storage",
            "target_interval_seconds": "targetIntervalSeconds",
        },
    )
    class ThumbnailConfigurationProperty:
        def __init__(
            self,
            *,
            recording_mode: typing.Optional[builtins.str] = None,
            resolution: typing.Optional[builtins.str] = None,
            storage: typing.Optional[typing.Sequence[builtins.str]] = None,
            target_interval_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The ThumbnailConfiguration property type describes a configuration of thumbnails for recorded video.

            :param recording_mode: Thumbnail recording mode. Valid values:. - ``DISABLED`` : Use DISABLED to disable the generation of thumbnails for recorded video. - ``INTERVAL`` : Use INTERVAL to enable the generation of thumbnails for recorded video at a time interval controlled by the `TargetIntervalSeconds <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-targetintervalseconds>`_ property. *Default* : ``INTERVAL`` Default: - "INTERVAL"
            :param resolution: The desired resolution of recorded thumbnails for a stream. Thumbnails are recorded at the selected resolution if the corresponding rendition is available during the stream; otherwise, they are recorded at source resolution. For more information about resolution values and their corresponding height and width dimensions, see `Auto-Record to Amazon S3 <https://docs.aws.amazon.com//ivs/latest/LowLatencyUserGuide/record-to-s3.html>`_ .
            :param storage: The format in which thumbnails are recorded for a stream. ``SEQUENTIAL`` records all generated thumbnails in a serial manner, to the media/thumbnails directory. ``LATEST`` saves the latest thumbnail in media/thumbnails/latest/thumb.jpg and overwrites it at the interval specified by ``targetIntervalSeconds`` . You can enable both ``SEQUENTIAL`` and ``LATEST`` . Default: ``SEQUENTIAL`` .
            :param target_interval_seconds: The targeted thumbnail-generation interval in seconds. This is configurable (and required) only if `RecordingMode <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-recordingmode>`_ is ``INTERVAL`` . .. epigraph:: Setting a value for ``TargetIntervalSeconds`` does not guarantee that thumbnails are generated at the specified interval. For thumbnails to be generated at the ``TargetIntervalSeconds`` interval, the ``IDR/Keyframe`` value for the input video must be less than the ``TargetIntervalSeconds`` value. See `Amazon IVS Streaming Configuration <https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/streaming-config.html>`_ for information on setting ``IDR/Keyframe`` to the recommended value in video-encoder settings. *Default* : 60 Default: - 60

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ivs as ivs
                
                thumbnail_configuration_property = ivs.CfnRecordingConfiguration.ThumbnailConfigurationProperty(
                    recording_mode="recordingMode",
                    resolution="resolution",
                    storage=["storage"],
                    target_interval_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a4ff2be02860d22b7736feaee29733579c28da4de38d0a44a511a67d6659e786)
                check_type(argname="argument recording_mode", value=recording_mode, expected_type=type_hints["recording_mode"])
                check_type(argname="argument resolution", value=resolution, expected_type=type_hints["resolution"])
                check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
                check_type(argname="argument target_interval_seconds", value=target_interval_seconds, expected_type=type_hints["target_interval_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if recording_mode is not None:
                self._values["recording_mode"] = recording_mode
            if resolution is not None:
                self._values["resolution"] = resolution
            if storage is not None:
                self._values["storage"] = storage
            if target_interval_seconds is not None:
                self._values["target_interval_seconds"] = target_interval_seconds

        @builtins.property
        def recording_mode(self) -> typing.Optional[builtins.str]:
            '''Thumbnail recording mode. Valid values:.

            - ``DISABLED`` : Use DISABLED to disable the generation of thumbnails for recorded video.
            - ``INTERVAL`` : Use INTERVAL to enable the generation of thumbnails for recorded video at a time interval controlled by the `TargetIntervalSeconds <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-targetintervalseconds>`_ property.

            *Default* : ``INTERVAL``

            :default: - "INTERVAL"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-recordingmode
            '''
            result = self._values.get("recording_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resolution(self) -> typing.Optional[builtins.str]:
            '''The desired resolution of recorded thumbnails for a stream.

            Thumbnails are recorded at the selected resolution if the corresponding rendition is available during the stream; otherwise, they are recorded at source resolution. For more information about resolution values and their corresponding height and width dimensions, see `Auto-Record to Amazon S3 <https://docs.aws.amazon.com//ivs/latest/LowLatencyUserGuide/record-to-s3.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-resolution
            '''
            result = self._values.get("resolution")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def storage(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The format in which thumbnails are recorded for a stream.

            ``SEQUENTIAL`` records all generated thumbnails in a serial manner, to the media/thumbnails directory. ``LATEST`` saves the latest thumbnail in media/thumbnails/latest/thumb.jpg and overwrites it at the interval specified by ``targetIntervalSeconds`` . You can enable both ``SEQUENTIAL`` and ``LATEST`` . Default: ``SEQUENTIAL`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-storage
            '''
            result = self._values.get("storage")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def target_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''The targeted thumbnail-generation interval in seconds. This is configurable (and required) only if `RecordingMode <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-recordingmode>`_ is ``INTERVAL`` .

            .. epigraph::

               Setting a value for ``TargetIntervalSeconds`` does not guarantee that thumbnails are generated at the specified interval. For thumbnails to be generated at the ``TargetIntervalSeconds`` interval, the ``IDR/Keyframe`` value for the input video must be less than the ``TargetIntervalSeconds`` value. See `Amazon IVS Streaming Configuration <https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/streaming-config.html>`_ for information on setting ``IDR/Keyframe`` to the recommended value in video-encoder settings.

            *Default* : 60

            :default: - 60

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-targetintervalseconds
            '''
            result = self._values.get("target_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ThumbnailConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ivs.CfnRecordingConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_configuration": "destinationConfiguration",
        "name": "name",
        "recording_reconnect_window_seconds": "recordingReconnectWindowSeconds",
        "rendition_configuration": "renditionConfiguration",
        "tags": "tags",
        "thumbnail_configuration": "thumbnailConfiguration",
    },
)
class CfnRecordingConfigurationProps:
    def __init__(
        self,
        *,
        destination_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        name: typing.Optional[builtins.str] = None,
        recording_reconnect_window_seconds: typing.Optional[jsii.Number] = None,
        rendition_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.RenditionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        thumbnail_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.ThumbnailConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRecordingConfiguration``.

        :param destination_configuration: A destination configuration describes an S3 bucket where recorded video will be stored. See the DestinationConfiguration property type for more information.
        :param name: Recording-configuration name. The value does not need to be unique.
        :param recording_reconnect_window_seconds: If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together. *Default* : ``0`` Default: - 0
        :param rendition_configuration: A rendition configuration describes which renditions should be recorded for a stream. See the RenditionConfiguration property type for more information.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-tag.html>`_ .
        :param thumbnail_configuration: A thumbnail configuration enables/disables the recording of thumbnails for a live session and controls the interval at which thumbnails are generated for the live session. See the ThumbnailConfiguration property type for more information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ivs as ivs
            
            cfn_recording_configuration_props = ivs.CfnRecordingConfigurationProps(
                destination_configuration=ivs.CfnRecordingConfiguration.DestinationConfigurationProperty(
                    s3=ivs.CfnRecordingConfiguration.S3DestinationConfigurationProperty(
                        bucket_name="bucketName"
                    )
                ),
            
                # the properties below are optional
                name="name",
                recording_reconnect_window_seconds=123,
                rendition_configuration=ivs.CfnRecordingConfiguration.RenditionConfigurationProperty(
                    renditions=["renditions"],
                    rendition_selection="renditionSelection"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                thumbnail_configuration=ivs.CfnRecordingConfiguration.ThumbnailConfigurationProperty(
                    recording_mode="recordingMode",
                    resolution="resolution",
                    storage=["storage"],
                    target_interval_seconds=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba7ddd4570fd05b5ededda48336345665e566391438dd61208aea34c865f91c1)
            check_type(argname="argument destination_configuration", value=destination_configuration, expected_type=type_hints["destination_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument recording_reconnect_window_seconds", value=recording_reconnect_window_seconds, expected_type=type_hints["recording_reconnect_window_seconds"])
            check_type(argname="argument rendition_configuration", value=rendition_configuration, expected_type=type_hints["rendition_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument thumbnail_configuration", value=thumbnail_configuration, expected_type=type_hints["thumbnail_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_configuration": destination_configuration,
        }
        if name is not None:
            self._values["name"] = name
        if recording_reconnect_window_seconds is not None:
            self._values["recording_reconnect_window_seconds"] = recording_reconnect_window_seconds
        if rendition_configuration is not None:
            self._values["rendition_configuration"] = rendition_configuration
        if tags is not None:
            self._values["tags"] = tags
        if thumbnail_configuration is not None:
            self._values["thumbnail_configuration"] = thumbnail_configuration

    @builtins.property
    def destination_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnRecordingConfiguration.DestinationConfigurationProperty]:
        '''A destination configuration describes an S3 bucket where recorded video will be stored.

        See the DestinationConfiguration property type for more information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-destinationconfiguration
        '''
        result = self._values.get("destination_configuration")
        assert result is not None, "Required property 'destination_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnRecordingConfiguration.DestinationConfigurationProperty], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Recording-configuration name.

        The value does not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recording_reconnect_window_seconds(self) -> typing.Optional[jsii.Number]:
        '''If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together.

        *Default* : ``0``

        :default: - 0

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-recordingreconnectwindowseconds
        '''
        result = self._values.get("recording_reconnect_window_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rendition_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordingConfiguration.RenditionConfigurationProperty]]:
        '''A rendition configuration describes which renditions should be recorded for a stream.

        See the RenditionConfiguration property type for more information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-renditionconfiguration
        '''
        result = self._values.get("rendition_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordingConfiguration.RenditionConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-tag.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def thumbnail_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordingConfiguration.ThumbnailConfigurationProperty]]:
        '''A thumbnail configuration enables/disables the recording of thumbnails for a live session and controls the interval at which thumbnails are generated for the live session.

        See the ThumbnailConfiguration property type for more information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration
        '''
        result = self._values.get("thumbnail_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordingConfiguration.ThumbnailConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRecordingConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnStage(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ivs.CfnStage",
):
    '''The ``AWS::IVS::Stage`` resource specifies an  stage.

    A stage is a virtual space where participants can exchange video in real time. For more information, see `CreateStage <https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateStage.html>`_ in the *Amazon IVS Real-Time Streaming API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-stage.html
    :cloudformationResource: AWS::IVS::Stage
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ivs as ivs
        
        cfn_stage = ivs.CfnStage(self, "MyCfnStage",
            auto_participant_recording_configuration=ivs.CfnStage.AutoParticipantRecordingConfigurationProperty(
                storage_configuration_arn="storageConfigurationArn",
        
                # the properties below are optional
                media_types=["mediaTypes"]
            ),
            name="name",
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
        auto_participant_recording_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStage.AutoParticipantRecordingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param auto_participant_recording_configuration: Configuration object for individual participant recording, to attach to the new stage.
        :param name: Stage name.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-stage-tag.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95445d65024ea014afa24d3c5da7a1c325ecb6f520b50f18c628abc8468ad394)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStageProps(
            auto_participant_recording_configuration=auto_participant_recording_configuration,
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
            type_hints = typing.get_type_hints(_typecheckingstub__f30152ce06f8073bd50b8e496f375320497c078cc8206cb7c95344710fd6a98b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0236ad7c18356db2e70641309707f63a741f804d4d94814bedc5adeaab38d30c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrActiveSessionId")
    def attr_active_session_id(self) -> builtins.str:
        '''ID of the active session within the stage.

        For example: ``st-a1b2c3d4e5f6g``

        :cloudformationAttribute: ActiveSessionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrActiveSessionId"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The stage ARN.

        For example: ``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="autoParticipantRecordingConfiguration")
    def auto_participant_recording_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStage.AutoParticipantRecordingConfigurationProperty"]]:
        '''Configuration object for individual participant recording, to attach to the new stage.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStage.AutoParticipantRecordingConfigurationProperty"]], jsii.get(self, "autoParticipantRecordingConfiguration"))

    @auto_participant_recording_configuration.setter
    def auto_participant_recording_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStage.AutoParticipantRecordingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__288ad5976e299bf3facf5812af603311b1780e61570d5cc88abb63f8e5ce0757)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoParticipantRecordingConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''Stage name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa886ee78ed539f2863fcdc7d7f62035b31fa2118c7c2c34cf8ba71078c75632)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a345b4498f1ee0487e9359886004162443d2310aa5159615d98ad8d30ecf6f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ivs.CfnStage.AutoParticipantRecordingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "storage_configuration_arn": "storageConfigurationArn",
            "media_types": "mediaTypes",
        },
    )
    class AutoParticipantRecordingConfigurationProperty:
        def __init__(
            self,
            *,
            storage_configuration_arn: builtins.str,
            media_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The ``AWS::IVS::AutoParticipantRecordingConfiguration`` property type describes a configuration for individual participant recording.

            :param storage_configuration_arn: ARN of the StorageConfiguration resource to use for individual participant recording. Default: "" (empty string, no storage configuration is specified). Individual participant recording cannot be started unless a storage configuration is specified, when a Stage is created or updated.
            :param media_types: Types of media to be recorded. Default: ``AUDIO_VIDEO`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-stage-autoparticipantrecordingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ivs as ivs
                
                auto_participant_recording_configuration_property = ivs.CfnStage.AutoParticipantRecordingConfigurationProperty(
                    storage_configuration_arn="storageConfigurationArn",
                
                    # the properties below are optional
                    media_types=["mediaTypes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3aeae0e25427fa7c0b735f190d30738c3d5c425f52576a56e84290d192a62871)
                check_type(argname="argument storage_configuration_arn", value=storage_configuration_arn, expected_type=type_hints["storage_configuration_arn"])
                check_type(argname="argument media_types", value=media_types, expected_type=type_hints["media_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "storage_configuration_arn": storage_configuration_arn,
            }
            if media_types is not None:
                self._values["media_types"] = media_types

        @builtins.property
        def storage_configuration_arn(self) -> builtins.str:
            '''ARN of the StorageConfiguration resource to use for individual participant recording.

            Default: "" (empty string, no storage configuration is specified). Individual participant recording cannot be started unless a storage configuration is specified, when a Stage is created or updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-stage-autoparticipantrecordingconfiguration.html#cfn-ivs-stage-autoparticipantrecordingconfiguration-storageconfigurationarn
            '''
            result = self._values.get("storage_configuration_arn")
            assert result is not None, "Required property 'storage_configuration_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def media_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Types of media to be recorded.

            Default: ``AUDIO_VIDEO`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-stage-autoparticipantrecordingconfiguration.html#cfn-ivs-stage-autoparticipantrecordingconfiguration-mediatypes
            '''
            result = self._values.get("media_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoParticipantRecordingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ivs.CfnStageProps",
    jsii_struct_bases=[],
    name_mapping={
        "auto_participant_recording_configuration": "autoParticipantRecordingConfiguration",
        "name": "name",
        "tags": "tags",
    },
)
class CfnStageProps:
    def __init__(
        self,
        *,
        auto_participant_recording_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStage.AutoParticipantRecordingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStage``.

        :param auto_participant_recording_configuration: Configuration object for individual participant recording, to attach to the new stage.
        :param name: Stage name.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-stage-tag.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-stage.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ivs as ivs
            
            cfn_stage_props = ivs.CfnStageProps(
                auto_participant_recording_configuration=ivs.CfnStage.AutoParticipantRecordingConfigurationProperty(
                    storage_configuration_arn="storageConfigurationArn",
            
                    # the properties below are optional
                    media_types=["mediaTypes"]
                ),
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7a0020ee283466459b434f83d43a5d205fcf4dbcde3ddb35eef021e6e069bf5)
            check_type(argname="argument auto_participant_recording_configuration", value=auto_participant_recording_configuration, expected_type=type_hints["auto_participant_recording_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auto_participant_recording_configuration is not None:
            self._values["auto_participant_recording_configuration"] = auto_participant_recording_configuration
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def auto_participant_recording_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStage.AutoParticipantRecordingConfigurationProperty]]:
        '''Configuration object for individual participant recording, to attach to the new stage.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-stage.html#cfn-ivs-stage-autoparticipantrecordingconfiguration
        '''
        result = self._values.get("auto_participant_recording_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStage.AutoParticipantRecordingConfigurationProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Stage name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-stage.html#cfn-ivs-stage-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-stage-tag.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-stage.html#cfn-ivs-stage-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStageProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnStorageConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ivs.CfnStorageConfiguration",
):
    '''The ``AWS::IVS::StorageConfiguration`` resource specifies an  storage configuration.

    A storage configuration describes an S3 location where recorded videos will be stored. For more information, see `Auto-Record to Amazon S3 (Low-Latency Streaming) <https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/record-to-s3.html>`_ in the *Amazon IVS Low-Latency Streaming User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-storageconfiguration.html
    :cloudformationResource: AWS::IVS::StorageConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ivs as ivs
        
        cfn_storage_configuration = ivs.CfnStorageConfiguration(self, "MyCfnStorageConfiguration",
            s3=ivs.CfnStorageConfiguration.S3StorageConfigurationProperty(
                bucket_name="bucketName"
            ),
        
            # the properties below are optional
            name="name",
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
        s3: typing.Union[_IResolvable_da3f097b, typing.Union["CfnStorageConfiguration.S3StorageConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param s3: An S3 storage configuration contains information about where recorded video will be stored. See the `S3StorageConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-storageconfiguration-s3storageconfiguration.html>`_ property type for more information.
        :param name: Storage cnfiguration name.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-storageconfiguration-tag.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dce4d013deb7e0886892fdd53eb91ee35dbd9f9b177c89526d3247ebc9882881)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStorageConfigurationProps(s3=s3, name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2494a1ad7f068edf1f7c9065f8fab79a66a716614a7b447a5ad3f667c000931c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f04371e94acebb618807659e6214b479c084f311d8b8e55b0d7126c699b0095a)
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
        '''The storage-configuration ARN.

        For example: ``arn:aws:ivs:us-west-2:123456789012:storage-configuration/abcdABCDefgh``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="s3")
    def s3(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnStorageConfiguration.S3StorageConfigurationProperty"]:
        '''An S3 storage configuration contains information about where recorded video will be stored.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnStorageConfiguration.S3StorageConfigurationProperty"], jsii.get(self, "s3"))

    @s3.setter
    def s3(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnStorageConfiguration.S3StorageConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a41e5161b80f9addb1b0e4316f4d2265340c959af7b1d4c11af686d0a7447cac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''Storage cnfiguration name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c09664e580fb852260e35bce701abfe5d1c54a635fc151ec55bf483f45e7ac77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac4f224a45d80fb7934ebfc58d4a23ea231aeab0929608af10892ba63ba4e79b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ivs.CfnStorageConfiguration.S3StorageConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName"},
    )
    class S3StorageConfigurationProperty:
        def __init__(self, *, bucket_name: builtins.str) -> None:
            '''The S3StorageConfiguration property type describes an S3 location where recorded videos will be stored.

            :param bucket_name: Name of the S3 bucket where recorded video will be stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-storageconfiguration-s3storageconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ivs as ivs
                
                s3_storage_configuration_property = ivs.CfnStorageConfiguration.S3StorageConfigurationProperty(
                    bucket_name="bucketName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__69c0a188191cf8e78c91503f301a8af37a069a58e49a9e4b1175c595d36ec107)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
            }

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''Name of the S3 bucket where recorded video will be stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-storageconfiguration-s3storageconfiguration.html#cfn-ivs-storageconfiguration-s3storageconfiguration-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3StorageConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ivs.CfnStorageConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={"s3": "s3", "name": "name", "tags": "tags"},
)
class CfnStorageConfigurationProps:
    def __init__(
        self,
        *,
        s3: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStorageConfiguration.S3StorageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStorageConfiguration``.

        :param s3: An S3 storage configuration contains information about where recorded video will be stored. See the `S3StorageConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-storageconfiguration-s3storageconfiguration.html>`_ property type for more information.
        :param name: Storage cnfiguration name.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-storageconfiguration-tag.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-storageconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ivs as ivs
            
            cfn_storage_configuration_props = ivs.CfnStorageConfigurationProps(
                s3=ivs.CfnStorageConfiguration.S3StorageConfigurationProperty(
                    bucket_name="bucketName"
                ),
            
                # the properties below are optional
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72410106e250d1874fbd4f3d9ea6ae3d4ffef1a3d301f8dc3bce88a672f05e4e)
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3": s3,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def s3(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnStorageConfiguration.S3StorageConfigurationProperty]:
        '''An S3 storage configuration contains information about where recorded video will be stored.

        See the `S3StorageConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-storageconfiguration-s3storageconfiguration.html>`_ property type for more information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-storageconfiguration.html#cfn-ivs-storageconfiguration-s3
        '''
        result = self._values.get("s3")
        assert result is not None, "Required property 's3' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnStorageConfiguration.S3StorageConfigurationProperty], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Storage cnfiguration name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-storageconfiguration.html#cfn-ivs-storageconfiguration-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-storageconfiguration-tag.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-storageconfiguration.html#cfn-ivs-storageconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStorageConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStreamKey(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ivs.CfnStreamKey",
):
    '''The ``AWS::IVS::StreamKey`` resource specifies an  stream key associated with the referenced channel.

    Use a stream key to initiate a live stream.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-streamkey.html
    :cloudformationResource: AWS::IVS::StreamKey
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ivs as ivs
        
        cfn_stream_key = ivs.CfnStreamKey(self, "MyCfnStreamKey",
            channel_arn="channelArn",
        
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
        channel_arn: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param channel_arn: Channel ARN for the stream.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-streamkey-tag.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c508febc00a5b76d50ae6b38407e9fa4357bcef12dfb4180bbc821ced1e89112)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStreamKeyProps(channel_arn=channel_arn, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c99a5ab18db8efd571b038c0d95c39758a584cec29efba661700074d2cf30bde)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ace437399547bc58926abe652ff0b6b8e00340a20eb309b99e2b5335ded44a08)
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
        '''The stream-key ARN.

        For example: ``arn:aws:ivs:us-west-2:123456789012:stream-key/g1H2I3j4k5L6``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrValue")
    def attr_value(self) -> builtins.str:
        '''The stream-key value.

        For example: ``sk_us-west-2_abcdABCDefgh_567890abcdef``

        :cloudformationAttribute: Value
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrValue"))

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
    @jsii.member(jsii_name="channelArn")
    def channel_arn(self) -> builtins.str:
        '''Channel ARN for the stream.'''
        return typing.cast(builtins.str, jsii.get(self, "channelArn"))

    @channel_arn.setter
    def channel_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fd7a730586bf4c02632ce69c6183339889a337f21e75e7368edd67dd583ea34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b966c0532d39deb26a3bd43a45365e1ee3edf5d3158d0a479134abca9f6f9d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ivs.CfnStreamKeyProps",
    jsii_struct_bases=[],
    name_mapping={"channel_arn": "channelArn", "tags": "tags"},
)
class CfnStreamKeyProps:
    def __init__(
        self,
        *,
        channel_arn: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStreamKey``.

        :param channel_arn: Channel ARN for the stream.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-streamkey-tag.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-streamkey.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ivs as ivs
            
            cfn_stream_key_props = ivs.CfnStreamKeyProps(
                channel_arn="channelArn",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a1d6f99b4c86a24198701caf819ea7b5d402ec68c7406b7aff6a02facc7e7c0)
            check_type(argname="argument channel_arn", value=channel_arn, expected_type=type_hints["channel_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_arn": channel_arn,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def channel_arn(self) -> builtins.str:
        '''Channel ARN for the stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-streamkey.html#cfn-ivs-streamkey-channelarn
        '''
        result = self._values.get("channel_arn")
        assert result is not None, "Required property 'channel_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-streamkey-tag.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-streamkey.html#cfn-ivs-streamkey-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStreamKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnChannel",
    "CfnChannelProps",
    "CfnEncoderConfiguration",
    "CfnEncoderConfigurationProps",
    "CfnIngestConfiguration",
    "CfnIngestConfigurationProps",
    "CfnPlaybackKeyPair",
    "CfnPlaybackKeyPairProps",
    "CfnPlaybackRestrictionPolicy",
    "CfnPlaybackRestrictionPolicyProps",
    "CfnPublicKey",
    "CfnPublicKeyProps",
    "CfnRecordingConfiguration",
    "CfnRecordingConfigurationProps",
    "CfnStage",
    "CfnStageProps",
    "CfnStorageConfiguration",
    "CfnStorageConfigurationProps",
    "CfnStreamKey",
    "CfnStreamKeyProps",
]

publication.publish()

def _typecheckingstub__998485c6924ca07e096c10b7976e238a36e5cfb75264ee66a67de472363369d6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    authorized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    container_format: typing.Optional[builtins.str] = None,
    insecure_ingest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    latency_mode: typing.Optional[builtins.str] = None,
    multitrack_input_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.MultitrackInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    preset: typing.Optional[builtins.str] = None,
    recording_configuration_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b2f270a2cc06d7958dc82935ff792ce64817de7fc16c4f4b5a7afa6f76cdd80(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fa81ac5355ae77db888dc8d0fb4cbbff54f381372b1c5a191ceb5eb77a6442b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e83b3a70b60de37a8aabc9c019b31db83c549e80f9c9c88a5b74fde72ecb20e(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5da102677f3042d402ff70f74aee693c78470595fd1a7c9b4900403983f7b74(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__734c5e1f9cdeabe74fb1ade992399b475d1594cbcdfd026823e8984eaa2d4eab(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd2cfeff050510b655ecd39d0e3b95c3c9e2af649e77e0903ad721d0f6428ab5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__012c045fd3860567ed6aa28435a35d575d1dc0a881855d124b21f2d76102ba73(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.MultitrackInputConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15776afbbb29227b4807e807447939235926366be32ef5acc331c74f0acd9b41(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95e047ef543e7e26080292a0481b6ce40457143e76918ac4c1c2d13855ce22ee(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eb4132c8e5e803f734f8f894d72d2324ee00be84b0babafa7076d94d732c960(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da42cce1a703989106b1844fef6f10d0a57f43c733d171564b16f83c208e7196(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0be9a3a6192cfd130520f4e6ecd8c9091b1a8b4312f716182989ea3feb88dc8b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50f1752d428e0d083b8ac0b36e82de6eba9749ea58d877e914d9e63a503364d1(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    maximum_resolution: typing.Optional[builtins.str] = None,
    policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61646017dba4df4ec5b97fde61911670aebc6b8151847b927754a4e9c110979d(
    *,
    authorized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    container_format: typing.Optional[builtins.str] = None,
    insecure_ingest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    latency_mode: typing.Optional[builtins.str] = None,
    multitrack_input_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.MultitrackInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    preset: typing.Optional[builtins.str] = None,
    recording_configuration_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0567625f957d978c482944a46fdbb2b7533ef9af0df4baffa7c6f443e004d9f9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    video: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEncoderConfiguration.VideoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74f3191bc79bc285f7b8eefaf911f57a87950083af93a8ec3c39d61421b97b29(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5894ac5581a1dc1e629e1f66ec2014665b3f9227b553389ebce9188b817c4d61(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29237afd8a2086ac2e4d8c43148154a3bd8987f1c1e0ff26a989a10c5f072ba2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43c7ff5eb70740ddcbf72fae725c27870249dfb23fdbca3df5963221ac9c132f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f165a00a101e72d860585d7255e3d0ae733a51dcec3ea6dd3e616d27778b3415(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEncoderConfiguration.VideoProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34f2c1c7f794b153dbb8eef658c04b4e6467fa06e325f7b2c94dc782acbeab26(
    *,
    bitrate: typing.Optional[jsii.Number] = None,
    framerate: typing.Optional[jsii.Number] = None,
    height: typing.Optional[jsii.Number] = None,
    width: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__663e73ad8dc18892ff8c6aa7cec15d284adf341fe58eeb580e68cff0a92ee161(
    *,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    video: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEncoderConfiguration.VideoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c56f46c8c3462fcf78f3e0898b4048a399a031987b0a76a9193f42a0a98fcd5e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ingest_protocol: typing.Optional[builtins.str] = None,
    insecure_ingest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    name: typing.Optional[builtins.str] = None,
    stage_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7a53bbb588815f0015c227540b92fa7ba4a33256116e056573299d99ef57574(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f47d1d0418cb9d42da8be28f4cb517e4e83775aec57930b9ba318f95f6168c3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__313ff481891bab6b5a8445b484bcb46c2d4e31789868f166495c526d0fe9002e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d0984e439ef9b3c25fe01666d92f1599a4bb2f408cc94a9bac3809e4fb8c00c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6ff791ee5d9887b8c66e010bf22c541fc5aa016c9908c44f04c9d7c7c5e71d5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d63930d5464ce48d09d7120e42b1e7aa23bfb45a07d7c93dda8514184602ac2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87601b6a8bacd8fefd6cc75f708d5009dad0f359e9544422e980fffade00bb04(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6c53b4493812dc096bfe5e107d3ab87615d06685c537ce27b9778a2701dd28b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95e9b18dcfb57342b7d6f80c4ce0d7b8886a64f91d3622dce01cf4e958236e01(
    *,
    ingest_protocol: typing.Optional[builtins.str] = None,
    insecure_ingest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    name: typing.Optional[builtins.str] = None,
    stage_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8c9299641f93177a19cfd84cad783d859723e15238afc5b2487f08100163f85(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: typing.Optional[builtins.str] = None,
    public_key_material: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34197af23f293afc0148baab246f15cd2fe54b95571370449978a5aeca67fa11(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__032f36985f3069b4c60d8aea57dfc3994cc6fa0fc29cbdac055ac20e5f4aca7c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ec5d532530f73a41d36dd7016f4d18021d800813e68dbfa6f703cceca701478(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4f35a09db8d81cf5fc7e7a397ca8172e49d613e64494c5a29798609a388e294(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74338171e55e9802fbeae4e8f45a4f31375c3a5730c487b0609b721a4660ce32(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a8be2c5b1653b9a20f33850cbab1a9c21d6b30034b5c68883e658d0e145e6a3(
    *,
    name: typing.Optional[builtins.str] = None,
    public_key_material: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__987a35e58d5c2ae76d6f7c41b5ef19dc05ac42c651fd8a03f9f28e044029b375(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    allowed_countries: typing.Sequence[builtins.str],
    allowed_origins: typing.Sequence[builtins.str],
    enable_strict_origin_enforcement: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f3f6891340e6dab4eba842f305f96e563b405ee29ecb437451d108aecb54492(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e57b154c63f829875b079b3d6baf6c33a6d6c377987d9ac6e9f4586303e9729(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6636af9e45dbeea2bcf7b5990280edcd8fec18083a4bfe23a76e19bd655ef03(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__773f5ee580b6a7c42904b5a38460c9ae7e7e147bde8b69e1c43edddd32d7dc69(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67d34a00cb21cb2e87b091d21364ddc0afcd5ff11075db95ae750d23e62e2808(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b36ada0e65d44733ed151613d84de1502ed0c39b1d83d8f62ea23a0f231bba3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72c43ae8ddd92a7ae402fb8cc1729052bd0d141f4f2106265c702c75bd0b9369(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feaf48f348987f686c52239e867f8aedc7a8a6debbbc2bec008fea1cc72c201f(
    *,
    allowed_countries: typing.Sequence[builtins.str],
    allowed_origins: typing.Sequence[builtins.str],
    enable_strict_origin_enforcement: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69566f8b07a347c045dd6b2f0dfca75d7b37273e69681243f26273b19e06cd09(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: typing.Optional[builtins.str] = None,
    public_key_material: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e6b8cd6799dd82e06ff9988e9e614506cad2cdb4fd21af49f6565f000590088(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e64d06031e9bc941f4698d06e7ad4d4c0b95c41a9c231c5cc51e05f1bb3c217b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d17e9902ef9a61f0eff6eb979f114b77f3840a826d3a39b4893ea2a98275b4be(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a843701534e0f215185c3c60d4ab2be6eb1b19877fea3f91057d6b805e21bc31(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5f083992aecb52530dd61b06308422142992ddce014c2eca8bd7e50b14a98e3(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e24b7446ff29c9bd2fdfcc82ce735007c1472e2e0a7ef6f06d261450515e6a4(
    *,
    name: typing.Optional[builtins.str] = None,
    public_key_material: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__541cdf033047e5777646c5f067e03131707927e43c41e609fd3ac9ee776ae419(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
    recording_reconnect_window_seconds: typing.Optional[jsii.Number] = None,
    rendition_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.RenditionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    thumbnail_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.ThumbnailConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d115d5ab74114a12edd8791ec11e4e4fd145cc6289d0579aac04f1c0c4089f8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3316cacec890424787de7224c6afcca2922a5899126aec97f005c3ea43409d1f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a98f37a00ab2b8c5a3413e54b7f022ac0bdf7ee44225243da737d75b9412595a(
    value: typing.Union[_IResolvable_da3f097b, CfnRecordingConfiguration.DestinationConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6dd9b8dd365a2dac11937c93668ced572b553c203da9cbf1d9e0932d0e24faf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38ff85ea7b2f1195ae4ae39514f42471c20d787399e92729b09aa86def8d11c4(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__607bfa50f9dd6b9828bada1c2c536f7277619bb3020e56c415227efdb3ba1fa9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordingConfiguration.RenditionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__980f42185f1f8239b1f7d72b3f84be9a9c93c5d02f84695a71964c0630115230(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5cda01e5b9f5edb6a6ec7c5dce6ad1cecc2b7ce8727dd09a38d4b2b04befd3c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordingConfiguration.ThumbnailConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74552278e1b145c98ed786a3d8f29802876ef78e57a458c3030b125a545b6a0f(
    *,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__556cbf534b885cc5fd04e7604c8916e78d98c9f230358bec7ded8f7e34aa0394(
    *,
    renditions: typing.Optional[typing.Sequence[builtins.str]] = None,
    rendition_selection: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c973ee3e6df5393489017eab5a2edc4f798c18919ab571067170163085c0d659(
    *,
    bucket_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4ff2be02860d22b7736feaee29733579c28da4de38d0a44a511a67d6659e786(
    *,
    recording_mode: typing.Optional[builtins.str] = None,
    resolution: typing.Optional[builtins.str] = None,
    storage: typing.Optional[typing.Sequence[builtins.str]] = None,
    target_interval_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba7ddd4570fd05b5ededda48336345665e566391438dd61208aea34c865f91c1(
    *,
    destination_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
    recording_reconnect_window_seconds: typing.Optional[jsii.Number] = None,
    rendition_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.RenditionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    thumbnail_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.ThumbnailConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95445d65024ea014afa24d3c5da7a1c325ecb6f520b50f18c628abc8468ad394(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    auto_participant_recording_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStage.AutoParticipantRecordingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f30152ce06f8073bd50b8e496f375320497c078cc8206cb7c95344710fd6a98b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0236ad7c18356db2e70641309707f63a741f804d4d94814bedc5adeaab38d30c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__288ad5976e299bf3facf5812af603311b1780e61570d5cc88abb63f8e5ce0757(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStage.AutoParticipantRecordingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa886ee78ed539f2863fcdc7d7f62035b31fa2118c7c2c34cf8ba71078c75632(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a345b4498f1ee0487e9359886004162443d2310aa5159615d98ad8d30ecf6f7(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aeae0e25427fa7c0b735f190d30738c3d5c425f52576a56e84290d192a62871(
    *,
    storage_configuration_arn: builtins.str,
    media_types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7a0020ee283466459b434f83d43a5d205fcf4dbcde3ddb35eef021e6e069bf5(
    *,
    auto_participant_recording_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStage.AutoParticipantRecordingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dce4d013deb7e0886892fdd53eb91ee35dbd9f9b177c89526d3247ebc9882881(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    s3: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStorageConfiguration.S3StorageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2494a1ad7f068edf1f7c9065f8fab79a66a716614a7b447a5ad3f667c000931c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f04371e94acebb618807659e6214b479c084f311d8b8e55b0d7126c699b0095a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a41e5161b80f9addb1b0e4316f4d2265340c959af7b1d4c11af686d0a7447cac(
    value: typing.Union[_IResolvable_da3f097b, CfnStorageConfiguration.S3StorageConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c09664e580fb852260e35bce701abfe5d1c54a635fc151ec55bf483f45e7ac77(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac4f224a45d80fb7934ebfc58d4a23ea231aeab0929608af10892ba63ba4e79b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69c0a188191cf8e78c91503f301a8af37a069a58e49a9e4b1175c595d36ec107(
    *,
    bucket_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72410106e250d1874fbd4f3d9ea6ae3d4ffef1a3d301f8dc3bce88a672f05e4e(
    *,
    s3: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStorageConfiguration.S3StorageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c508febc00a5b76d50ae6b38407e9fa4357bcef12dfb4180bbc821ced1e89112(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    channel_arn: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c99a5ab18db8efd571b038c0d95c39758a584cec29efba661700074d2cf30bde(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ace437399547bc58926abe652ff0b6b8e00340a20eb309b99e2b5335ded44a08(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fd7a730586bf4c02632ce69c6183339889a337f21e75e7368edd67dd583ea34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b966c0532d39deb26a3bd43a45365e1ee3edf5d3158d0a479134abca9f6f9d2(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a1d6f99b4c86a24198701caf819ea7b5d402ec68c7406b7aff6a02facc7e7c0(
    *,
    channel_arn: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
