r'''
# AWS::MediaPackageV2 Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_mediapackagev2 as mediapackage
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for MediaPackageV2 construct libraries](https://constructs.dev/search?q=mediapackagev2)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::MediaPackageV2 resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaPackageV2.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::MediaPackageV2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaPackageV2.html).

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
class CfnChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnChannel",
):
    '''Creates a channel to receive content.

    After it's created, a channel provides static input URLs. These URLs remain the same throughout the lifetime of the channel, regardless of any failures or upgrades that might occur. Use these URLs to configure the outputs of your upstream encoder.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channel.html
    :cloudformationResource: AWS::MediaPackageV2::Channel
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediapackagev2 as mediapackagev2
        
        cfn_channel = mediapackagev2.CfnChannel(self, "MyCfnChannel",
            channel_group_name="channelGroupName",
            channel_name="channelName",
        
            # the properties below are optional
            description="description",
            input_switch_configuration=mediapackagev2.CfnChannel.InputSwitchConfigurationProperty(
                mqcs_input_switching=False,
                preferred_input=123
            ),
            input_type="inputType",
            output_header_configuration=mediapackagev2.CfnChannel.OutputHeaderConfigurationProperty(
                publish_mqcs=False
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
        channel_group_name: builtins.str,
        channel_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        input_switch_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnChannel.InputSwitchConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        input_type: typing.Optional[builtins.str] = None,
        output_header_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnChannel.OutputHeaderConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param channel_group_name: The name of the channel group associated with the channel configuration.
        :param channel_name: The name of the channel.
        :param description: The description of the channel.
        :param input_switch_configuration: The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive.
        :param input_type: The input type will be an immutable field which will be used to define whether the channel will allow CMAF ingest or HLS ingest. If unprovided, it will default to HLS to preserve current behavior. The allowed values are: - ``HLS`` - The HLS streaming specification (which defines M3U8 manifests and TS segments). - ``CMAF`` - The DASH-IF CMAF Ingest specification (which defines CMAF segments with optional DASH manifests).
        :param output_header_configuration: The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN.
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5f12d43fb05232f03795c27e5dde1f408f5762e93edacb27e01efb9e0e3c7c1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnChannelProps(
            channel_group_name=channel_group_name,
            channel_name=channel_name,
            description=description,
            input_switch_configuration=input_switch_configuration,
            input_type=input_type,
            output_header_configuration=output_header_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e420705ca6e035f67df6dc549d10387c546517b6ba6c086e3e8a2aa9d31185d9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__151c82108a0a47810b493e5e882a8c1cee0d53d834da01c686f370947109f4b2)
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
        '''The Amazon Resource Name (ARN) of the channel.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of the creation of the channel.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrIngestEndpoints")
    def attr_ingest_endpoints(self) -> _IResolvable_da3f097b:
        '''The ingest endpoints associated with the channel.

        :cloudformationAttribute: IngestEndpoints
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIngestEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="attrIngestEndpointUrls")
    def attr_ingest_endpoint_urls(self) -> typing.List[builtins.str]:
        '''The ingest domain URL where the source stream should be sent.

        :cloudformationAttribute: IngestEndpointUrls
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrIngestEndpointUrls"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''The timestamp of the modification of the channel.

        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

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
    @jsii.member(jsii_name="channelGroupName")
    def channel_group_name(self) -> builtins.str:
        '''The name of the channel group associated with the channel configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "channelGroupName"))

    @channel_group_name.setter
    def channel_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9226145b09f87b401f2f5e357dafd5cd14b0b6a288f53bb6f985030a67a2ac8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelGroupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="channelName")
    def channel_name(self) -> builtins.str:
        '''The name of the channel.'''
        return typing.cast(builtins.str, jsii.get(self, "channelName"))

    @channel_name.setter
    def channel_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1e91bde8ef4635665f6fef9c2cf22478a1d6e8a29ee675d883277fd4eb950f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the channel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee07183524d44b124938ad354f47b29384e1ea3a14ba4e7fa739d6847d2cdf12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="inputSwitchConfiguration")
    def input_switch_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.InputSwitchConfigurationProperty"]]:
        '''The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.InputSwitchConfigurationProperty"]], jsii.get(self, "inputSwitchConfiguration"))

    @input_switch_configuration.setter
    def input_switch_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.InputSwitchConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3390ae8163479dfdbac5df53086ecff4210fbf97553d12d70faac0b628fe5c00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputSwitchConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="inputType")
    def input_type(self) -> typing.Optional[builtins.str]:
        '''The input type will be an immutable field which will be used to define whether the channel will allow CMAF ingest or HLS ingest.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputType"))

    @input_type.setter
    def input_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fd45bf182a4bcd922fc7964817a4166c9d667e78eb548b915896743cf024664)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outputHeaderConfiguration")
    def output_header_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.OutputHeaderConfigurationProperty"]]:
        '''The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.OutputHeaderConfigurationProperty"]], jsii.get(self, "outputHeaderConfiguration"))

    @output_header_configuration.setter
    def output_header_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.OutputHeaderConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cd874b506cfe4b7e50b6cfa6b36888413d69d5ce0a7f4649d690587ed70c417)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputHeaderConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61a8d14ccc4954881d5a995d8d9c088f4870a4a3a28d0b44314514a2fbb02a01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnChannel.IngestEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "url": "url"},
    )
    class IngestEndpointProperty:
        def __init__(
            self,
            *,
            id: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The input URL where the source stream should be sent.

            :param id: The identifier associated with the ingest endpoint of the channel.
            :param url: The URL associated with the ingest endpoint of the channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-channel-ingestendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                ingest_endpoint_property = mediapackagev2.CfnChannel.IngestEndpointProperty(
                    id="id",
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__52a72049adc4af63f65ccfb6f3c098cecb2b442bbe00bad4a877f2099a4bea86)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The identifier associated with the ingest endpoint of the channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-channel-ingestendpoint.html#cfn-mediapackagev2-channel-ingestendpoint-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The URL associated with the ingest endpoint of the channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-channel-ingestendpoint.html#cfn-mediapackagev2-channel-ingestendpoint-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IngestEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnChannel.InputSwitchConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "mqcs_input_switching": "mqcsInputSwitching",
            "preferred_input": "preferredInput",
        },
    )
    class InputSwitchConfigurationProperty:
        def __init__(
            self,
            *,
            mqcs_input_switching: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            preferred_input: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive.

            :param mqcs_input_switching: When true, AWS Elemental MediaPackage performs input switching based on the MQCS. Default is true. This setting is valid only when ``InputType`` is ``CMAF`` .
            :param preferred_input: For CMAF inputs, indicates which input MediaPackage should prefer when both inputs have equal MQCS scores. Select ``1`` to prefer the first ingest endpoint, or ``2`` to prefer the second ingest endpoint. If you don't specify a preferred input, MediaPackage uses its default switching behavior when MQCS scores are equal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-channel-inputswitchconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                input_switch_configuration_property = mediapackagev2.CfnChannel.InputSwitchConfigurationProperty(
                    mqcs_input_switching=False,
                    preferred_input=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__116c8177c767f1c1239016dd387671ce140ac29b5e59b8e19832080acf68bef5)
                check_type(argname="argument mqcs_input_switching", value=mqcs_input_switching, expected_type=type_hints["mqcs_input_switching"])
                check_type(argname="argument preferred_input", value=preferred_input, expected_type=type_hints["preferred_input"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if mqcs_input_switching is not None:
                self._values["mqcs_input_switching"] = mqcs_input_switching
            if preferred_input is not None:
                self._values["preferred_input"] = preferred_input

        @builtins.property
        def mqcs_input_switching(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When true, AWS Elemental MediaPackage performs input switching based on the MQCS.

            Default is true. This setting is valid only when ``InputType`` is ``CMAF`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-channel-inputswitchconfiguration.html#cfn-mediapackagev2-channel-inputswitchconfiguration-mqcsinputswitching
            '''
            result = self._values.get("mqcs_input_switching")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def preferred_input(self) -> typing.Optional[jsii.Number]:
            '''For CMAF inputs, indicates which input MediaPackage should prefer when both inputs have equal MQCS scores.

            Select ``1`` to prefer the first ingest endpoint, or ``2`` to prefer the second ingest endpoint. If you don't specify a preferred input, MediaPackage uses its default switching behavior when MQCS scores are equal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-channel-inputswitchconfiguration.html#cfn-mediapackagev2-channel-inputswitchconfiguration-preferredinput
            '''
            result = self._values.get("preferred_input")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputSwitchConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnChannel.OutputHeaderConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"publish_mqcs": "publishMqcs"},
    )
    class OutputHeaderConfigurationProperty:
        def __init__(
            self,
            *,
            publish_mqcs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN.

            :param publish_mqcs: When true, AWS Elemental MediaPackage includes the MQCS in responses to the CDN. This setting is valid only when ``InputType`` is ``CMAF`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-channel-outputheaderconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                output_header_configuration_property = mediapackagev2.CfnChannel.OutputHeaderConfigurationProperty(
                    publish_mqcs=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__173b31e2a58ec560b57e45f11a2ad4c62727971f6e225559d90b8cf278b9f4f8)
                check_type(argname="argument publish_mqcs", value=publish_mqcs, expected_type=type_hints["publish_mqcs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if publish_mqcs is not None:
                self._values["publish_mqcs"] = publish_mqcs

        @builtins.property
        def publish_mqcs(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When true, AWS Elemental MediaPackage includes the MQCS in responses to the CDN.

            This setting is valid only when ``InputType`` is ``CMAF`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-channel-outputheaderconfiguration.html#cfn-mediapackagev2-channel-outputheaderconfiguration-publishmqcs
            '''
            result = self._values.get("publish_mqcs")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputHeaderConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnChannelGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnChannelGroup",
):
    '''Specifies the configuration for a MediaPackage V2 channel group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelgroup.html
    :cloudformationResource: AWS::MediaPackageV2::ChannelGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediapackagev2 as mediapackagev2
        
        cfn_channel_group = mediapackagev2.CfnChannelGroup(self, "MyCfnChannelGroup",
            channel_group_name="channelGroupName",
        
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
        channel_group_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param channel_group_name: The name of the channel group.
        :param description: The configuration for a MediaPackage V2 channel group.
        :param tags: The tags associated with the channel group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d830ced0539d40633bba571496a990f327b96c8fb475a589dba800d21ebab93)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnChannelGroupProps(
            channel_group_name=channel_group_name, description=description, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85339d527078ada2373603756ae52ddf1f0419ece647a7ea7d90b5a88cd80494)
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
            type_hints = typing.get_type_hints(_typecheckingstub__15b97c97551c59b98a88e9243bce42e0880ba6021ce928c5162f4d188e32c3d0)
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
        '''The Amazon Resource Name (ARN) of the channel group.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of the creation of the channel group.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrEgressDomain")
    def attr_egress_domain(self) -> builtins.str:
        '''The egress domain of the channel group.

        :cloudformationAttribute: EgressDomain
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEgressDomain"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''The timestamp of the modification of the channel group.

        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

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
    @jsii.member(jsii_name="channelGroupName")
    def channel_group_name(self) -> builtins.str:
        '''The name of the channel group.'''
        return typing.cast(builtins.str, jsii.get(self, "channelGroupName"))

    @channel_group_name.setter
    def channel_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab608f9f2545c6bf246db306be81d4790f5052ef181c364ada9dfba9527799b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelGroupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The configuration for a MediaPackage V2 channel group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7398d92754f71ac10dc5aea2094dad8322025c79ae1302b6a69e6216e4e16144)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags associated with the channel group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07fbb1a31d1fae7c89e591bbcc359f5dc55386649647301df2f2e0b4e9727f81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnChannelGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_group_name": "channelGroupName",
        "description": "description",
        "tags": "tags",
    },
)
class CfnChannelGroupProps:
    def __init__(
        self,
        *,
        channel_group_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnChannelGroup``.

        :param channel_group_name: The name of the channel group.
        :param description: The configuration for a MediaPackage V2 channel group.
        :param tags: The tags associated with the channel group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediapackagev2 as mediapackagev2
            
            cfn_channel_group_props = mediapackagev2.CfnChannelGroupProps(
                channel_group_name="channelGroupName",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c53e8c32bcc3339086fcebea2b9a32198690f58e488775d546eac1d98ce6635e)
            check_type(argname="argument channel_group_name", value=channel_group_name, expected_type=type_hints["channel_group_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_group_name": channel_group_name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def channel_group_name(self) -> builtins.str:
        '''The name of the channel group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelgroup.html#cfn-mediapackagev2-channelgroup-channelgroupname
        '''
        result = self._values.get("channel_group_name")
        assert result is not None, "Required property 'channel_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The configuration for a MediaPackage V2 channel group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelgroup.html#cfn-mediapackagev2-channelgroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags associated with the channel group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelgroup.html#cfn-mediapackagev2-channelgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChannelGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnChannelPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnChannelPolicy",
):
    '''Specifies the configuration parameters of a MediaPackage V2 channel policy.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelpolicy.html
    :cloudformationResource: AWS::MediaPackageV2::ChannelPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediapackagev2 as mediapackagev2
        
        # policy: Any
        
        cfn_channel_policy = mediapackagev2.CfnChannelPolicy(self, "MyCfnChannelPolicy",
            channel_group_name="channelGroupName",
            channel_name="channelName",
            policy=policy
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        channel_group_name: builtins.str,
        channel_name: builtins.str,
        policy: typing.Any,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param channel_group_name: The name of the channel group associated with the channel policy.
        :param channel_name: The name of the channel associated with the channel policy.
        :param policy: The policy associated with the channel.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3bd3df241e2da49b066856cd5205c086667bdeae2c7accc2fb87dc6c27afcca)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnChannelPolicyProps(
            channel_group_name=channel_group_name,
            channel_name=channel_name,
            policy=policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__876e67bc0ac491acabfef846d2cb0a4a12c7db69dc9b8510736610ce77094825)
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
            type_hints = typing.get_type_hints(_typecheckingstub__428a901c1d832a1ec31a5a15117cbe43d42edeb32192ef35e21682ad7114f777)
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
    @jsii.member(jsii_name="channelGroupName")
    def channel_group_name(self) -> builtins.str:
        '''The name of the channel group associated with the channel policy.'''
        return typing.cast(builtins.str, jsii.get(self, "channelGroupName"))

    @channel_group_name.setter
    def channel_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb6da332e5cbe78bc72a7af1de80f930372aa6490fa2d573b540c4b4050a16b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelGroupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="channelName")
    def channel_name(self) -> builtins.str:
        '''The name of the channel associated with the channel policy.'''
        return typing.cast(builtins.str, jsii.get(self, "channelName"))

    @channel_name.setter
    def channel_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffc77e98d707d0206432d1f5669baff83936b87558c5f6b3966d25c6d2682bcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Any:
        '''The policy associated with the channel.'''
        return typing.cast(typing.Any, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f9e54d124a239f2e45623971b96e9da027d679f90368ed2a8e63d67a707784f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnChannelPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_group_name": "channelGroupName",
        "channel_name": "channelName",
        "policy": "policy",
    },
)
class CfnChannelPolicyProps:
    def __init__(
        self,
        *,
        channel_group_name: builtins.str,
        channel_name: builtins.str,
        policy: typing.Any,
    ) -> None:
        '''Properties for defining a ``CfnChannelPolicy``.

        :param channel_group_name: The name of the channel group associated with the channel policy.
        :param channel_name: The name of the channel associated with the channel policy.
        :param policy: The policy associated with the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediapackagev2 as mediapackagev2
            
            # policy: Any
            
            cfn_channel_policy_props = mediapackagev2.CfnChannelPolicyProps(
                channel_group_name="channelGroupName",
                channel_name="channelName",
                policy=policy
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b390a62609d42c685f94c0572af995fa58a878e57dc79822886178cfbe0a33f)
            check_type(argname="argument channel_group_name", value=channel_group_name, expected_type=type_hints["channel_group_name"])
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
            "policy": policy,
        }

    @builtins.property
    def channel_group_name(self) -> builtins.str:
        '''The name of the channel group associated with the channel policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelpolicy.html#cfn-mediapackagev2-channelpolicy-channelgroupname
        '''
        result = self._values.get("channel_group_name")
        assert result is not None, "Required property 'channel_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_name(self) -> builtins.str:
        '''The name of the channel associated with the channel policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelpolicy.html#cfn-mediapackagev2-channelpolicy-channelname
        '''
        result = self._values.get("channel_name")
        assert result is not None, "Required property 'channel_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy(self) -> typing.Any:
        '''The policy associated with the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelpolicy.html#cfn-mediapackagev2-channelpolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChannelPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_group_name": "channelGroupName",
        "channel_name": "channelName",
        "description": "description",
        "input_switch_configuration": "inputSwitchConfiguration",
        "input_type": "inputType",
        "output_header_configuration": "outputHeaderConfiguration",
        "tags": "tags",
    },
)
class CfnChannelProps:
    def __init__(
        self,
        *,
        channel_group_name: builtins.str,
        channel_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        input_switch_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.InputSwitchConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        input_type: typing.Optional[builtins.str] = None,
        output_header_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.OutputHeaderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnChannel``.

        :param channel_group_name: The name of the channel group associated with the channel configuration.
        :param channel_name: The name of the channel.
        :param description: The description of the channel.
        :param input_switch_configuration: The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive.
        :param input_type: The input type will be an immutable field which will be used to define whether the channel will allow CMAF ingest or HLS ingest. If unprovided, it will default to HLS to preserve current behavior. The allowed values are: - ``HLS`` - The HLS streaming specification (which defines M3U8 manifests and TS segments). - ``CMAF`` - The DASH-IF CMAF Ingest specification (which defines CMAF segments with optional DASH manifests).
        :param output_header_configuration: The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN.
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediapackagev2 as mediapackagev2
            
            cfn_channel_props = mediapackagev2.CfnChannelProps(
                channel_group_name="channelGroupName",
                channel_name="channelName",
            
                # the properties below are optional
                description="description",
                input_switch_configuration=mediapackagev2.CfnChannel.InputSwitchConfigurationProperty(
                    mqcs_input_switching=False,
                    preferred_input=123
                ),
                input_type="inputType",
                output_header_configuration=mediapackagev2.CfnChannel.OutputHeaderConfigurationProperty(
                    publish_mqcs=False
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb84231dfbf08cdefe6ca207d49155a084aa492947c635c5e9ba404f1b3b987f)
            check_type(argname="argument channel_group_name", value=channel_group_name, expected_type=type_hints["channel_group_name"])
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument input_switch_configuration", value=input_switch_configuration, expected_type=type_hints["input_switch_configuration"])
            check_type(argname="argument input_type", value=input_type, expected_type=type_hints["input_type"])
            check_type(argname="argument output_header_configuration", value=output_header_configuration, expected_type=type_hints["output_header_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
        }
        if description is not None:
            self._values["description"] = description
        if input_switch_configuration is not None:
            self._values["input_switch_configuration"] = input_switch_configuration
        if input_type is not None:
            self._values["input_type"] = input_type
        if output_header_configuration is not None:
            self._values["output_header_configuration"] = output_header_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def channel_group_name(self) -> builtins.str:
        '''The name of the channel group associated with the channel configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channel.html#cfn-mediapackagev2-channel-channelgroupname
        '''
        result = self._values.get("channel_group_name")
        assert result is not None, "Required property 'channel_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_name(self) -> builtins.str:
        '''The name of the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channel.html#cfn-mediapackagev2-channel-channelname
        '''
        result = self._values.get("channel_name")
        assert result is not None, "Required property 'channel_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channel.html#cfn-mediapackagev2-channel-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_switch_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.InputSwitchConfigurationProperty]]:
        '''The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channel.html#cfn-mediapackagev2-channel-inputswitchconfiguration
        '''
        result = self._values.get("input_switch_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.InputSwitchConfigurationProperty]], result)

    @builtins.property
    def input_type(self) -> typing.Optional[builtins.str]:
        '''The input type will be an immutable field which will be used to define whether the channel will allow CMAF ingest or HLS ingest.

        If unprovided, it will default to HLS to preserve current behavior.

        The allowed values are:

        - ``HLS`` - The HLS streaming specification (which defines M3U8 manifests and TS segments).
        - ``CMAF`` - The DASH-IF CMAF Ingest specification (which defines CMAF segments with optional DASH manifests).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channel.html#cfn-mediapackagev2-channel-inputtype
        '''
        result = self._values.get("input_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_header_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.OutputHeaderConfigurationProperty]]:
        '''The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channel.html#cfn-mediapackagev2-channel-outputheaderconfiguration
        '''
        result = self._values.get("output_header_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.OutputHeaderConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channel.html#cfn-mediapackagev2-channel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnOriginEndpoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint",
):
    '''Specifies the configuration parameters for a MediaPackage V2 origin endpoint.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html
    :cloudformationResource: AWS::MediaPackageV2::OriginEndpoint
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediapackagev2 as mediapackagev2
        
        cfn_origin_endpoint = mediapackagev2.CfnOriginEndpoint(self, "MyCfnOriginEndpoint",
            channel_group_name="channelGroupName",
            channel_name="channelName",
            container_type="containerType",
            origin_endpoint_name="originEndpointName",
        
            # the properties below are optional
            dash_manifests=[mediapackagev2.CfnOriginEndpoint.DashManifestConfigurationProperty(
                manifest_name="manifestName",
        
                # the properties below are optional
                base_urls=[mediapackagev2.CfnOriginEndpoint.DashBaseUrlProperty(
                    url="url",
        
                    # the properties below are optional
                    dvb_priority=123,
                    dvb_weight=123,
                    service_location="serviceLocation"
                )],
                compactness="compactness",
                drm_signaling="drmSignaling",
                dvb_settings=mediapackagev2.CfnOriginEndpoint.DashDvbSettingsProperty(
                    error_metrics=[mediapackagev2.CfnOriginEndpoint.DashDvbMetricsReportingProperty(
                        reporting_url="reportingUrl",
        
                        # the properties below are optional
                        probability=123
                    )],
                    font_download=mediapackagev2.CfnOriginEndpoint.DashDvbFontDownloadProperty(
                        font_family="fontFamily",
                        mime_type="mimeType",
                        url="url"
                    )
                ),
                filter_configuration=mediapackagev2.CfnOriginEndpoint.FilterConfigurationProperty(
                    clip_start_time="clipStartTime",
                    end="end",
                    manifest_filter="manifestFilter",
                    start="start",
                    time_delay_seconds=123
                ),
                manifest_window_seconds=123,
                min_buffer_time_seconds=123,
                min_update_period_seconds=123,
                period_triggers=["periodTriggers"],
                profiles=["profiles"],
                program_information=mediapackagev2.CfnOriginEndpoint.DashProgramInformationProperty(
                    copyright="copyright",
                    language_code="languageCode",
                    more_information_url="moreInformationUrl",
                    source="source",
                    title="title"
                ),
                scte_dash=mediapackagev2.CfnOriginEndpoint.ScteDashProperty(
                    ad_marker_dash="adMarkerDash"
                ),
                segment_template_format="segmentTemplateFormat",
                subtitle_configuration=mediapackagev2.CfnOriginEndpoint.DashSubtitleConfigurationProperty(
                    ttml_configuration=mediapackagev2.CfnOriginEndpoint.DashTtmlConfigurationProperty(
                        ttml_profile="ttmlProfile"
                    )
                ),
                suggested_presentation_delay_seconds=123,
                utc_timing=mediapackagev2.CfnOriginEndpoint.DashUtcTimingProperty(
                    timing_mode="timingMode",
                    timing_source="timingSource"
                )
            )],
            description="description",
            force_endpoint_error_configuration=mediapackagev2.CfnOriginEndpoint.ForceEndpointErrorConfigurationProperty(
                endpoint_error_conditions=["endpointErrorConditions"]
            ),
            hls_manifests=[mediapackagev2.CfnOriginEndpoint.HlsManifestConfigurationProperty(
                manifest_name="manifestName",
        
                # the properties below are optional
                child_manifest_name="childManifestName",
                filter_configuration=mediapackagev2.CfnOriginEndpoint.FilterConfigurationProperty(
                    clip_start_time="clipStartTime",
                    end="end",
                    manifest_filter="manifestFilter",
                    start="start",
                    time_delay_seconds=123
                ),
                manifest_window_seconds=123,
                program_date_time_interval_seconds=123,
                scte_hls=mediapackagev2.CfnOriginEndpoint.ScteHlsProperty(
                    ad_marker_hls="adMarkerHls"
                ),
                start_tag=mediapackagev2.CfnOriginEndpoint.StartTagProperty(
                    time_offset=123,
        
                    # the properties below are optional
                    precise=False
                ),
                url="url",
                url_encode_child_manifest=False
            )],
            low_latency_hls_manifests=[mediapackagev2.CfnOriginEndpoint.LowLatencyHlsManifestConfigurationProperty(
                manifest_name="manifestName",
        
                # the properties below are optional
                child_manifest_name="childManifestName",
                filter_configuration=mediapackagev2.CfnOriginEndpoint.FilterConfigurationProperty(
                    clip_start_time="clipStartTime",
                    end="end",
                    manifest_filter="manifestFilter",
                    start="start",
                    time_delay_seconds=123
                ),
                manifest_window_seconds=123,
                program_date_time_interval_seconds=123,
                scte_hls=mediapackagev2.CfnOriginEndpoint.ScteHlsProperty(
                    ad_marker_hls="adMarkerHls"
                ),
                start_tag=mediapackagev2.CfnOriginEndpoint.StartTagProperty(
                    time_offset=123,
        
                    # the properties below are optional
                    precise=False
                ),
                url="url",
                url_encode_child_manifest=False
            )],
            segment=mediapackagev2.CfnOriginEndpoint.SegmentProperty(
                encryption=mediapackagev2.CfnOriginEndpoint.EncryptionProperty(
                    encryption_method=mediapackagev2.CfnOriginEndpoint.EncryptionMethodProperty(
                        cmaf_encryption_method="cmafEncryptionMethod",
                        ts_encryption_method="tsEncryptionMethod"
                    ),
                    speke_key_provider=mediapackagev2.CfnOriginEndpoint.SpekeKeyProviderProperty(
                        drm_systems=["drmSystems"],
                        encryption_contract_configuration=mediapackagev2.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        ),
                        resource_id="resourceId",
                        role_arn="roleArn",
                        url="url"
                    ),
        
                    # the properties below are optional
                    cmaf_exclude_segment_drm_metadata=False,
                    constant_initialization_vector="constantInitializationVector",
                    key_rotation_interval_seconds=123
                ),
                include_iframe_only_streams=False,
                scte=mediapackagev2.CfnOriginEndpoint.ScteProperty(
                    scte_filter=["scteFilter"]
                ),
                segment_duration_seconds=123,
                segment_name="segmentName",
                ts_include_dvb_subtitles=False,
                ts_use_audio_rendition_group=False
            ),
            startover_window_seconds=123,
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
        channel_group_name: builtins.str,
        channel_name: builtins.str,
        container_type: builtins.str,
        origin_endpoint_name: builtins.str,
        dash_manifests: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.DashManifestConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        force_endpoint_error_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.ForceEndpointErrorConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        hls_manifests: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.HlsManifestConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        low_latency_hls_manifests: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.LowLatencyHlsManifestConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        segment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.SegmentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        startover_window_seconds: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param channel_group_name: The name of the channel group associated with the origin endpoint configuration.
        :param channel_name: The channel name associated with the origin endpoint.
        :param container_type: The container type associated with the origin endpoint configuration.
        :param origin_endpoint_name: The name of the origin endpoint associated with the origin endpoint configuration.
        :param dash_manifests: A DASH manifest configuration.
        :param description: The description associated with the origin endpoint.
        :param force_endpoint_error_configuration: The failover settings for the endpoint.
        :param hls_manifests: The HLS manifests associated with the origin endpoint configuration.
        :param low_latency_hls_manifests: The low-latency HLS (LL-HLS) manifests associated with the origin endpoint.
        :param segment: The segment associated with the origin endpoint.
        :param startover_window_seconds: The size of the window (in seconds) to specify a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window.
        :param tags: The tags associated with the origin endpoint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dba3dfc2892c78e53aee7675a7a24aa25c0b29481aca92446e31a0d8e885454)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOriginEndpointProps(
            channel_group_name=channel_group_name,
            channel_name=channel_name,
            container_type=container_type,
            origin_endpoint_name=origin_endpoint_name,
            dash_manifests=dash_manifests,
            description=description,
            force_endpoint_error_configuration=force_endpoint_error_configuration,
            hls_manifests=hls_manifests,
            low_latency_hls_manifests=low_latency_hls_manifests,
            segment=segment,
            startover_window_seconds=startover_window_seconds,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e7f9bba2cb8ce16d2850e4d29968cd8a850c920cb1e5d66b966cd309dd0e90f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bffcdef090bba09d673a36358d5eb3ba86b040c5c727f2f4cc117a5fab72df6f)
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
        '''The Amazon Resource Name (ARN) of the origin endpoint.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of the creation of the origin endpoint.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDashManifestUrls")
    def attr_dash_manifest_urls(self) -> typing.List[builtins.str]:
        '''The egress domain URL for stream delivery from MediaPackage.

        :cloudformationAttribute: DashManifestUrls
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDashManifestUrls"))

    @builtins.property
    @jsii.member(jsii_name="attrHlsManifestUrls")
    def attr_hls_manifest_urls(self) -> typing.List[builtins.str]:
        '''The egress domain URL for stream delivery from MediaPackage.

        :cloudformationAttribute: HlsManifestUrls
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrHlsManifestUrls"))

    @builtins.property
    @jsii.member(jsii_name="attrLowLatencyHlsManifestUrls")
    def attr_low_latency_hls_manifest_urls(self) -> typing.List[builtins.str]:
        '''The egress domain URL for stream delivery from MediaPackage.

        :cloudformationAttribute: LowLatencyHlsManifestUrls
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrLowLatencyHlsManifestUrls"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''The timestamp of the modification of the origin endpoint.

        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

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
    @jsii.member(jsii_name="channelGroupName")
    def channel_group_name(self) -> builtins.str:
        '''The name of the channel group associated with the origin endpoint configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "channelGroupName"))

    @channel_group_name.setter
    def channel_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7078125edd1beb221f7e3a35a200ce058d31cb41756eb7b1dca1af5dfe90c96f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelGroupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="channelName")
    def channel_name(self) -> builtins.str:
        '''The channel name associated with the origin endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "channelName"))

    @channel_name.setter
    def channel_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__300d202906247d29b698e05c2891ad6a3e8f72748a5cb046f44ee1cde390954a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="containerType")
    def container_type(self) -> builtins.str:
        '''The container type associated with the origin endpoint configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "containerType"))

    @container_type.setter
    def container_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ded0ec9a4a78b0a13f4013526976d3ef27bae8928fb665d57679f95325a85b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="originEndpointName")
    def origin_endpoint_name(self) -> builtins.str:
        '''The name of the origin endpoint associated with the origin endpoint configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "originEndpointName"))

    @origin_endpoint_name.setter
    def origin_endpoint_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b645ac54fdc447a14891e1f23268d3a802e1d51ab06333dab9a1ae79ae88fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originEndpointName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dashManifests")
    def dash_manifests(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashManifestConfigurationProperty"]]]]:
        '''A DASH manifest configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashManifestConfigurationProperty"]]]], jsii.get(self, "dashManifests"))

    @dash_manifests.setter
    def dash_manifests(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashManifestConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__316fdfa36cde837c49bfecdf48716a30e11db3879a7276c8207beeff9aff9317)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashManifests", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description associated with the origin endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d2dcbe74f178ed4fd2315de3210f8a81e6084e3e73f7337556d68a41cc54333)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="forceEndpointErrorConfiguration")
    def force_endpoint_error_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.ForceEndpointErrorConfigurationProperty"]]:
        '''The failover settings for the endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.ForceEndpointErrorConfigurationProperty"]], jsii.get(self, "forceEndpointErrorConfiguration"))

    @force_endpoint_error_configuration.setter
    def force_endpoint_error_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.ForceEndpointErrorConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bd0bc6ee367a0d016a630be9b91f1bbb3565f44feb4d59db2010dbadda4a8a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceEndpointErrorConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hlsManifests")
    def hls_manifests(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.HlsManifestConfigurationProperty"]]]]:
        '''The HLS manifests associated with the origin endpoint configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.HlsManifestConfigurationProperty"]]]], jsii.get(self, "hlsManifests"))

    @hls_manifests.setter
    def hls_manifests(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.HlsManifestConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de310c90fc64be46bd788fedd55681eba63f450cc4f6537fe91890137af54019)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hlsManifests", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lowLatencyHlsManifests")
    def low_latency_hls_manifests(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.LowLatencyHlsManifestConfigurationProperty"]]]]:
        '''The low-latency HLS (LL-HLS) manifests associated with the origin endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.LowLatencyHlsManifestConfigurationProperty"]]]], jsii.get(self, "lowLatencyHlsManifests"))

    @low_latency_hls_manifests.setter
    def low_latency_hls_manifests(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.LowLatencyHlsManifestConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ab0da83ecaf5e8b2eb477e1a7bb2f955c99813829faeb44ce46e408a3739304)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lowLatencyHlsManifests", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="segment")
    def segment(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.SegmentProperty"]]:
        '''The segment associated with the origin endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.SegmentProperty"]], jsii.get(self, "segment"))

    @segment.setter
    def segment(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.SegmentProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__761931cab894d0c1a04fe9fe8aad0785de043e26b7f476c427bb231ae9fc1eeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "segment", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="startoverWindowSeconds")
    def startover_window_seconds(self) -> typing.Optional[jsii.Number]:
        '''The size of the window (in seconds) to specify a window of the live stream that's available for on-demand viewing.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startoverWindowSeconds"))

    @startover_window_seconds.setter
    def startover_window_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__285ecfef5a8ec9ebb3f1c4d2193922e98318f11cce543c9b9c4221cfee42fc11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startoverWindowSeconds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags associated with the origin endpoint.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65cc25545f38d01b8ccc61c9494f0994747ef22d12fc3c94c71cb091aff2f324)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.DashBaseUrlProperty",
        jsii_struct_bases=[],
        name_mapping={
            "url": "url",
            "dvb_priority": "dvbPriority",
            "dvb_weight": "dvbWeight",
            "service_location": "serviceLocation",
        },
    )
    class DashBaseUrlProperty:
        def __init__(
            self,
            *,
            url: builtins.str,
            dvb_priority: typing.Optional[jsii.Number] = None,
            dvb_weight: typing.Optional[jsii.Number] = None,
            service_location: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The base URLs to use for retrieving segments.

            You can specify multiple locations and indicate the priority and weight for when each should be used, for use in mutli-CDN workflows.

            :param url: A source location for segments.
            :param dvb_priority: For use with DVB-DASH profiles only. The priority of this location for servings segments. The lower the number, the higher the priority.
            :param dvb_weight: For use with DVB-DASH profiles only. The weighting for source locations that have the same priority.
            :param service_location: The name of the source location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashbaseurl.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                dash_base_url_property = mediapackagev2.CfnOriginEndpoint.DashBaseUrlProperty(
                    url="url",
                
                    # the properties below are optional
                    dvb_priority=123,
                    dvb_weight=123,
                    service_location="serviceLocation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be1d880fe401caed5e0186c4f4a6b76f8d63f2e78cf2fcbb490b66d185d4af29)
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument dvb_priority", value=dvb_priority, expected_type=type_hints["dvb_priority"])
                check_type(argname="argument dvb_weight", value=dvb_weight, expected_type=type_hints["dvb_weight"])
                check_type(argname="argument service_location", value=service_location, expected_type=type_hints["service_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "url": url,
            }
            if dvb_priority is not None:
                self._values["dvb_priority"] = dvb_priority
            if dvb_weight is not None:
                self._values["dvb_weight"] = dvb_weight
            if service_location is not None:
                self._values["service_location"] = service_location

        @builtins.property
        def url(self) -> builtins.str:
            '''A source location for segments.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashbaseurl.html#cfn-mediapackagev2-originendpoint-dashbaseurl-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dvb_priority(self) -> typing.Optional[jsii.Number]:
            '''For use with DVB-DASH profiles only.

            The priority of this location for servings segments. The lower the number, the higher the priority.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashbaseurl.html#cfn-mediapackagev2-originendpoint-dashbaseurl-dvbpriority
            '''
            result = self._values.get("dvb_priority")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dvb_weight(self) -> typing.Optional[jsii.Number]:
            '''For use with DVB-DASH profiles only.

            The weighting for source locations that have the same priority.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashbaseurl.html#cfn-mediapackagev2-originendpoint-dashbaseurl-dvbweight
            '''
            result = self._values.get("dvb_weight")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def service_location(self) -> typing.Optional[builtins.str]:
            '''The name of the source location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashbaseurl.html#cfn-mediapackagev2-originendpoint-dashbaseurl-servicelocation
            '''
            result = self._values.get("service_location")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashBaseUrlProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.DashDvbFontDownloadProperty",
        jsii_struct_bases=[],
        name_mapping={
            "font_family": "fontFamily",
            "mime_type": "mimeType",
            "url": "url",
        },
    )
    class DashDvbFontDownloadProperty:
        def __init__(
            self,
            *,
            font_family: typing.Optional[builtins.str] = None,
            mime_type: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''For use with DVB-DASH profiles only.

            The settings for font downloads that you want AWS Elemental MediaPackage to pass through to the manifest.

            :param font_family: The ``fontFamily`` name for subtitles, as described in `EBU-TT-D Subtitling Distribution Format <https://docs.aws.amazon.com/https://tech.ebu.ch/publications/tech3380>`_ .
            :param mime_type: The ``mimeType`` of the resource that's at the font download URL. For information about font MIME types, see the `MPEG-DASH Profile for Transport of ISO BMFF Based DVB Services over IP Based Networks <https://docs.aws.amazon.com/https://dvb.org/wp-content/uploads/2021/06/A168r4_MPEG-DASH-Profile-for-Transport-of-ISO-BMFF-Based-DVB-Services_Draft-ts_103-285-v140_November_2021.pdf>`_ document.
            :param url: The URL for downloading fonts for subtitles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashdvbfontdownload.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                dash_dvb_font_download_property = mediapackagev2.CfnOriginEndpoint.DashDvbFontDownloadProperty(
                    font_family="fontFamily",
                    mime_type="mimeType",
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__81c2694b55243cfd80ec8b5b8d807b1d991f3ae38973b41f6fb77d9d5ea24965)
                check_type(argname="argument font_family", value=font_family, expected_type=type_hints["font_family"])
                check_type(argname="argument mime_type", value=mime_type, expected_type=type_hints["mime_type"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if font_family is not None:
                self._values["font_family"] = font_family
            if mime_type is not None:
                self._values["mime_type"] = mime_type
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def font_family(self) -> typing.Optional[builtins.str]:
            '''The ``fontFamily`` name for subtitles, as described in `EBU-TT-D Subtitling Distribution Format <https://docs.aws.amazon.com/https://tech.ebu.ch/publications/tech3380>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashdvbfontdownload.html#cfn-mediapackagev2-originendpoint-dashdvbfontdownload-fontfamily
            '''
            result = self._values.get("font_family")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mime_type(self) -> typing.Optional[builtins.str]:
            '''The ``mimeType`` of the resource that's at the font download URL.

            For information about font MIME types, see the `MPEG-DASH Profile for Transport of ISO BMFF Based DVB Services over IP Based Networks <https://docs.aws.amazon.com/https://dvb.org/wp-content/uploads/2021/06/A168r4_MPEG-DASH-Profile-for-Transport-of-ISO-BMFF-Based-DVB-Services_Draft-ts_103-285-v140_November_2021.pdf>`_ document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashdvbfontdownload.html#cfn-mediapackagev2-originendpoint-dashdvbfontdownload-mimetype
            '''
            result = self._values.get("mime_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The URL for downloading fonts for subtitles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashdvbfontdownload.html#cfn-mediapackagev2-originendpoint-dashdvbfontdownload-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashDvbFontDownloadProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.DashDvbMetricsReportingProperty",
        jsii_struct_bases=[],
        name_mapping={"reporting_url": "reportingUrl", "probability": "probability"},
    )
    class DashDvbMetricsReportingProperty:
        def __init__(
            self,
            *,
            reporting_url: builtins.str,
            probability: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''For use with DVB-DASH profiles only.

            The settings for error reporting from the playback device that you want AWS Elemental MediaPackage to pass through to the manifest.

            :param reporting_url: The URL where playback devices send error reports.
            :param probability: The number of playback devices per 1000 that will send error reports to the reporting URL. This represents the probability that a playback device will be a reporting player for this session.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashdvbmetricsreporting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                dash_dvb_metrics_reporting_property = mediapackagev2.CfnOriginEndpoint.DashDvbMetricsReportingProperty(
                    reporting_url="reportingUrl",
                
                    # the properties below are optional
                    probability=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fadf127f9f82d1f5f09e73b8a4d72d5685c1236b84cdaa5c6132a7ab4774e495)
                check_type(argname="argument reporting_url", value=reporting_url, expected_type=type_hints["reporting_url"])
                check_type(argname="argument probability", value=probability, expected_type=type_hints["probability"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "reporting_url": reporting_url,
            }
            if probability is not None:
                self._values["probability"] = probability

        @builtins.property
        def reporting_url(self) -> builtins.str:
            '''The URL where playback devices send error reports.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashdvbmetricsreporting.html#cfn-mediapackagev2-originendpoint-dashdvbmetricsreporting-reportingurl
            '''
            result = self._values.get("reporting_url")
            assert result is not None, "Required property 'reporting_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def probability(self) -> typing.Optional[jsii.Number]:
            '''The number of playback devices per 1000 that will send error reports to the reporting URL.

            This represents the probability that a playback device will be a reporting player for this session.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashdvbmetricsreporting.html#cfn-mediapackagev2-originendpoint-dashdvbmetricsreporting-probability
            '''
            result = self._values.get("probability")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashDvbMetricsReportingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.DashDvbSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "error_metrics": "errorMetrics",
            "font_download": "fontDownload",
        },
    )
    class DashDvbSettingsProperty:
        def __init__(
            self,
            *,
            error_metrics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.DashDvbMetricsReportingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            font_download: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.DashDvbFontDownloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''For endpoints that use the DVB-DASH profile only.

            The font download and error reporting information that you want MediaPackage to pass through to the manifest.

            :param error_metrics: Playback device error reporting settings.
            :param font_download: Subtitle font settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashdvbsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                dash_dvb_settings_property = mediapackagev2.CfnOriginEndpoint.DashDvbSettingsProperty(
                    error_metrics=[mediapackagev2.CfnOriginEndpoint.DashDvbMetricsReportingProperty(
                        reporting_url="reportingUrl",
                
                        # the properties below are optional
                        probability=123
                    )],
                    font_download=mediapackagev2.CfnOriginEndpoint.DashDvbFontDownloadProperty(
                        font_family="fontFamily",
                        mime_type="mimeType",
                        url="url"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__280a149dc1f481cd4b69b2b250e75d424c71bee34e699369b2294841b0aed7d8)
                check_type(argname="argument error_metrics", value=error_metrics, expected_type=type_hints["error_metrics"])
                check_type(argname="argument font_download", value=font_download, expected_type=type_hints["font_download"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if error_metrics is not None:
                self._values["error_metrics"] = error_metrics
            if font_download is not None:
                self._values["font_download"] = font_download

        @builtins.property
        def error_metrics(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashDvbMetricsReportingProperty"]]]]:
            '''Playback device error reporting settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashdvbsettings.html#cfn-mediapackagev2-originendpoint-dashdvbsettings-errormetrics
            '''
            result = self._values.get("error_metrics")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashDvbMetricsReportingProperty"]]]], result)

        @builtins.property
        def font_download(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashDvbFontDownloadProperty"]]:
            '''Subtitle font settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashdvbsettings.html#cfn-mediapackagev2-originendpoint-dashdvbsettings-fontdownload
            '''
            result = self._values.get("font_download")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashDvbFontDownloadProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashDvbSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.DashManifestConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "manifest_name": "manifestName",
            "base_urls": "baseUrls",
            "compactness": "compactness",
            "drm_signaling": "drmSignaling",
            "dvb_settings": "dvbSettings",
            "filter_configuration": "filterConfiguration",
            "manifest_window_seconds": "manifestWindowSeconds",
            "min_buffer_time_seconds": "minBufferTimeSeconds",
            "min_update_period_seconds": "minUpdatePeriodSeconds",
            "period_triggers": "periodTriggers",
            "profiles": "profiles",
            "program_information": "programInformation",
            "scte_dash": "scteDash",
            "segment_template_format": "segmentTemplateFormat",
            "subtitle_configuration": "subtitleConfiguration",
            "suggested_presentation_delay_seconds": "suggestedPresentationDelaySeconds",
            "utc_timing": "utcTiming",
        },
    )
    class DashManifestConfigurationProperty:
        def __init__(
            self,
            *,
            manifest_name: builtins.str,
            base_urls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.DashBaseUrlProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            compactness: typing.Optional[builtins.str] = None,
            drm_signaling: typing.Optional[builtins.str] = None,
            dvb_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.DashDvbSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            filter_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.FilterConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            manifest_window_seconds: typing.Optional[jsii.Number] = None,
            min_buffer_time_seconds: typing.Optional[jsii.Number] = None,
            min_update_period_seconds: typing.Optional[jsii.Number] = None,
            period_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
            profiles: typing.Optional[typing.Sequence[builtins.str]] = None,
            program_information: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.DashProgramInformationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            scte_dash: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.ScteDashProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            segment_template_format: typing.Optional[builtins.str] = None,
            subtitle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.DashSubtitleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            suggested_presentation_delay_seconds: typing.Optional[jsii.Number] = None,
            utc_timing: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.DashUtcTimingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The DASH manifest configuration associated with the origin endpoint.

            :param manifest_name: A short string that's appended to the endpoint URL. The child manifest name creates a unique path to this endpoint.
            :param base_urls: The base URLs to use for retrieving segments.
            :param compactness: The layout of the DASH manifest that MediaPackage produces. ``STANDARD`` indicates a default manifest, which is compacted. ``NONE`` indicates a full manifest. For information about compactness, see `DASH manifest compactness <https://docs.aws.amazon.com/mediapackage/latest/userguide/compacted.html>`_ in the *AWS Elemental MediaPackage v2 User Guide* .
            :param drm_signaling: Determines how the DASH manifest signals the DRM content.
            :param dvb_settings: For endpoints that use the DVB-DASH profile only. The font download and error reporting information that you want MediaPackage to pass through to the manifest.
            :param filter_configuration: Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.
            :param manifest_window_seconds: The total duration (in seconds) of the manifest's content.
            :param min_buffer_time_seconds: Minimum amount of content (in seconds) that a player must keep available in the buffer.
            :param min_update_period_seconds: Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest.
            :param period_triggers: A list of triggers that controls when AWS Elemental MediaPackage separates the MPEG-DASH manifest into multiple periods. Type ``ADS`` to indicate that AWS Elemental MediaPackage must create periods in the output manifest that correspond to SCTE-35 ad markers in the input source. Leave this value empty to indicate that the manifest is contained all in one period. For more information about periods in the DASH manifest, see `Multi-period DASH in AWS Elemental MediaPackage <https://docs.aws.amazon.com/mediapackage/latest/userguide/multi-period.html>`_ .
            :param profiles: The profile that the output is compliant with.
            :param program_information: Details about the content that you want MediaPackage to pass through in the manifest to the playback device.
            :param scte_dash: The SCTE configuration.
            :param segment_template_format: Determines the type of variable used in the ``media`` URL of the ``SegmentTemplate`` tag in the manifest. Also specifies if segment timeline information is included in ``SegmentTimeline`` or ``SegmentTemplate`` . Value description: - ``NUMBER_WITH_TIMELINE`` - The ``$Number$`` variable is used in the ``media`` URL. The value of this variable is the sequential number of the segment. A full ``SegmentTimeline`` object is presented in each ``SegmentTemplate`` .
            :param subtitle_configuration: The configuration for DASH subtitles.
            :param suggested_presentation_delay_seconds: The amount of time (in seconds) that the player should be from the end of the manifest.
            :param utc_timing: Determines the type of UTC timing included in the DASH Media Presentation Description (MPD).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                dash_manifest_configuration_property = mediapackagev2.CfnOriginEndpoint.DashManifestConfigurationProperty(
                    manifest_name="manifestName",
                
                    # the properties below are optional
                    base_urls=[mediapackagev2.CfnOriginEndpoint.DashBaseUrlProperty(
                        url="url",
                
                        # the properties below are optional
                        dvb_priority=123,
                        dvb_weight=123,
                        service_location="serviceLocation"
                    )],
                    compactness="compactness",
                    drm_signaling="drmSignaling",
                    dvb_settings=mediapackagev2.CfnOriginEndpoint.DashDvbSettingsProperty(
                        error_metrics=[mediapackagev2.CfnOriginEndpoint.DashDvbMetricsReportingProperty(
                            reporting_url="reportingUrl",
                
                            # the properties below are optional
                            probability=123
                        )],
                        font_download=mediapackagev2.CfnOriginEndpoint.DashDvbFontDownloadProperty(
                            font_family="fontFamily",
                            mime_type="mimeType",
                            url="url"
                        )
                    ),
                    filter_configuration=mediapackagev2.CfnOriginEndpoint.FilterConfigurationProperty(
                        clip_start_time="clipStartTime",
                        end="end",
                        manifest_filter="manifestFilter",
                        start="start",
                        time_delay_seconds=123
                    ),
                    manifest_window_seconds=123,
                    min_buffer_time_seconds=123,
                    min_update_period_seconds=123,
                    period_triggers=["periodTriggers"],
                    profiles=["profiles"],
                    program_information=mediapackagev2.CfnOriginEndpoint.DashProgramInformationProperty(
                        copyright="copyright",
                        language_code="languageCode",
                        more_information_url="moreInformationUrl",
                        source="source",
                        title="title"
                    ),
                    scte_dash=mediapackagev2.CfnOriginEndpoint.ScteDashProperty(
                        ad_marker_dash="adMarkerDash"
                    ),
                    segment_template_format="segmentTemplateFormat",
                    subtitle_configuration=mediapackagev2.CfnOriginEndpoint.DashSubtitleConfigurationProperty(
                        ttml_configuration=mediapackagev2.CfnOriginEndpoint.DashTtmlConfigurationProperty(
                            ttml_profile="ttmlProfile"
                        )
                    ),
                    suggested_presentation_delay_seconds=123,
                    utc_timing=mediapackagev2.CfnOriginEndpoint.DashUtcTimingProperty(
                        timing_mode="timingMode",
                        timing_source="timingSource"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__20e3bfad4ae40517c778173bab356d7bd208497ee33a09fdc9e380135384dfc6)
                check_type(argname="argument manifest_name", value=manifest_name, expected_type=type_hints["manifest_name"])
                check_type(argname="argument base_urls", value=base_urls, expected_type=type_hints["base_urls"])
                check_type(argname="argument compactness", value=compactness, expected_type=type_hints["compactness"])
                check_type(argname="argument drm_signaling", value=drm_signaling, expected_type=type_hints["drm_signaling"])
                check_type(argname="argument dvb_settings", value=dvb_settings, expected_type=type_hints["dvb_settings"])
                check_type(argname="argument filter_configuration", value=filter_configuration, expected_type=type_hints["filter_configuration"])
                check_type(argname="argument manifest_window_seconds", value=manifest_window_seconds, expected_type=type_hints["manifest_window_seconds"])
                check_type(argname="argument min_buffer_time_seconds", value=min_buffer_time_seconds, expected_type=type_hints["min_buffer_time_seconds"])
                check_type(argname="argument min_update_period_seconds", value=min_update_period_seconds, expected_type=type_hints["min_update_period_seconds"])
                check_type(argname="argument period_triggers", value=period_triggers, expected_type=type_hints["period_triggers"])
                check_type(argname="argument profiles", value=profiles, expected_type=type_hints["profiles"])
                check_type(argname="argument program_information", value=program_information, expected_type=type_hints["program_information"])
                check_type(argname="argument scte_dash", value=scte_dash, expected_type=type_hints["scte_dash"])
                check_type(argname="argument segment_template_format", value=segment_template_format, expected_type=type_hints["segment_template_format"])
                check_type(argname="argument subtitle_configuration", value=subtitle_configuration, expected_type=type_hints["subtitle_configuration"])
                check_type(argname="argument suggested_presentation_delay_seconds", value=suggested_presentation_delay_seconds, expected_type=type_hints["suggested_presentation_delay_seconds"])
                check_type(argname="argument utc_timing", value=utc_timing, expected_type=type_hints["utc_timing"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "manifest_name": manifest_name,
            }
            if base_urls is not None:
                self._values["base_urls"] = base_urls
            if compactness is not None:
                self._values["compactness"] = compactness
            if drm_signaling is not None:
                self._values["drm_signaling"] = drm_signaling
            if dvb_settings is not None:
                self._values["dvb_settings"] = dvb_settings
            if filter_configuration is not None:
                self._values["filter_configuration"] = filter_configuration
            if manifest_window_seconds is not None:
                self._values["manifest_window_seconds"] = manifest_window_seconds
            if min_buffer_time_seconds is not None:
                self._values["min_buffer_time_seconds"] = min_buffer_time_seconds
            if min_update_period_seconds is not None:
                self._values["min_update_period_seconds"] = min_update_period_seconds
            if period_triggers is not None:
                self._values["period_triggers"] = period_triggers
            if profiles is not None:
                self._values["profiles"] = profiles
            if program_information is not None:
                self._values["program_information"] = program_information
            if scte_dash is not None:
                self._values["scte_dash"] = scte_dash
            if segment_template_format is not None:
                self._values["segment_template_format"] = segment_template_format
            if subtitle_configuration is not None:
                self._values["subtitle_configuration"] = subtitle_configuration
            if suggested_presentation_delay_seconds is not None:
                self._values["suggested_presentation_delay_seconds"] = suggested_presentation_delay_seconds
            if utc_timing is not None:
                self._values["utc_timing"] = utc_timing

        @builtins.property
        def manifest_name(self) -> builtins.str:
            '''A short string that's appended to the endpoint URL.

            The child manifest name creates a unique path to this endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-manifestname
            '''
            result = self._values.get("manifest_name")
            assert result is not None, "Required property 'manifest_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def base_urls(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashBaseUrlProperty"]]]]:
            '''The base URLs to use for retrieving segments.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-baseurls
            '''
            result = self._values.get("base_urls")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashBaseUrlProperty"]]]], result)

        @builtins.property
        def compactness(self) -> typing.Optional[builtins.str]:
            '''The layout of the DASH manifest that MediaPackage produces.

            ``STANDARD`` indicates a default manifest, which is compacted. ``NONE`` indicates a full manifest.

            For information about compactness, see `DASH manifest compactness <https://docs.aws.amazon.com/mediapackage/latest/userguide/compacted.html>`_ in the *AWS Elemental MediaPackage v2 User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-compactness
            '''
            result = self._values.get("compactness")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def drm_signaling(self) -> typing.Optional[builtins.str]:
            '''Determines how the DASH manifest signals the DRM content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-drmsignaling
            '''
            result = self._values.get("drm_signaling")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dvb_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashDvbSettingsProperty"]]:
            '''For endpoints that use the DVB-DASH profile only.

            The font download and error reporting information that you want MediaPackage to pass through to the manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-dvbsettings
            '''
            result = self._values.get("dvb_settings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashDvbSettingsProperty"]], result)

        @builtins.property
        def filter_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.FilterConfigurationProperty"]]:
            '''Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-filterconfiguration
            '''
            result = self._values.get("filter_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.FilterConfigurationProperty"]], result)

        @builtins.property
        def manifest_window_seconds(self) -> typing.Optional[jsii.Number]:
            '''The total duration (in seconds) of the manifest's content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-manifestwindowseconds
            '''
            result = self._values.get("manifest_window_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_buffer_time_seconds(self) -> typing.Optional[jsii.Number]:
            '''Minimum amount of content (in seconds) that a player must keep available in the buffer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-minbuffertimeseconds
            '''
            result = self._values.get("min_buffer_time_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_update_period_seconds(self) -> typing.Optional[jsii.Number]:
            '''Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-minupdateperiodseconds
            '''
            result = self._values.get("min_update_period_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def period_triggers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of triggers that controls when AWS Elemental MediaPackage separates the MPEG-DASH manifest into multiple periods.

            Type ``ADS`` to indicate that AWS Elemental MediaPackage must create periods in the output manifest that correspond to SCTE-35 ad markers in the input source. Leave this value empty to indicate that the manifest is contained all in one period. For more information about periods in the DASH manifest, see `Multi-period DASH in AWS Elemental MediaPackage <https://docs.aws.amazon.com/mediapackage/latest/userguide/multi-period.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-periodtriggers
            '''
            result = self._values.get("period_triggers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def profiles(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The profile that the output is compliant with.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-profiles
            '''
            result = self._values.get("profiles")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def program_information(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashProgramInformationProperty"]]:
            '''Details about the content that you want MediaPackage to pass through in the manifest to the playback device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-programinformation
            '''
            result = self._values.get("program_information")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashProgramInformationProperty"]], result)

        @builtins.property
        def scte_dash(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.ScteDashProperty"]]:
            '''The SCTE configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-sctedash
            '''
            result = self._values.get("scte_dash")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.ScteDashProperty"]], result)

        @builtins.property
        def segment_template_format(self) -> typing.Optional[builtins.str]:
            '''Determines the type of variable used in the ``media`` URL of the ``SegmentTemplate`` tag in the manifest.

            Also specifies if segment timeline information is included in ``SegmentTimeline`` or ``SegmentTemplate`` .

            Value description:

            - ``NUMBER_WITH_TIMELINE`` - The ``$Number$`` variable is used in the ``media`` URL. The value of this variable is the sequential number of the segment. A full ``SegmentTimeline`` object is presented in each ``SegmentTemplate`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-segmenttemplateformat
            '''
            result = self._values.get("segment_template_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def subtitle_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashSubtitleConfigurationProperty"]]:
            '''The configuration for DASH subtitles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-subtitleconfiguration
            '''
            result = self._values.get("subtitle_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashSubtitleConfigurationProperty"]], result)

        @builtins.property
        def suggested_presentation_delay_seconds(self) -> typing.Optional[jsii.Number]:
            '''The amount of time (in seconds) that the player should be from the end of the manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-suggestedpresentationdelayseconds
            '''
            result = self._values.get("suggested_presentation_delay_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def utc_timing(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashUtcTimingProperty"]]:
            '''Determines the type of UTC timing included in the DASH Media Presentation Description (MPD).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-dashmanifestconfiguration-utctiming
            '''
            result = self._values.get("utc_timing")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashUtcTimingProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashManifestConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.DashProgramInformationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "copyright": "copyright",
            "language_code": "languageCode",
            "more_information_url": "moreInformationUrl",
            "source": "source",
            "title": "title",
        },
    )
    class DashProgramInformationProperty:
        def __init__(
            self,
            *,
            copyright: typing.Optional[builtins.str] = None,
            language_code: typing.Optional[builtins.str] = None,
            more_information_url: typing.Optional[builtins.str] = None,
            source: typing.Optional[builtins.str] = None,
            title: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Details about the content that you want MediaPackage to pass through in the manifest to the playback device.

            :param copyright: A copyright statement about the content.
            :param language_code: The language code for this manifest.
            :param more_information_url: An absolute URL that contains more information about this content.
            :param source: Information about the content provider.
            :param title: The title for the manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashprograminformation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                dash_program_information_property = mediapackagev2.CfnOriginEndpoint.DashProgramInformationProperty(
                    copyright="copyright",
                    language_code="languageCode",
                    more_information_url="moreInformationUrl",
                    source="source",
                    title="title"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5b0c2b5b70e24041767a172f1ebbd9317cd4ce50194b747d40b0c075a554bb92)
                check_type(argname="argument copyright", value=copyright, expected_type=type_hints["copyright"])
                check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
                check_type(argname="argument more_information_url", value=more_information_url, expected_type=type_hints["more_information_url"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
                check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if copyright is not None:
                self._values["copyright"] = copyright
            if language_code is not None:
                self._values["language_code"] = language_code
            if more_information_url is not None:
                self._values["more_information_url"] = more_information_url
            if source is not None:
                self._values["source"] = source
            if title is not None:
                self._values["title"] = title

        @builtins.property
        def copyright(self) -> typing.Optional[builtins.str]:
            '''A copyright statement about the content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashprograminformation.html#cfn-mediapackagev2-originendpoint-dashprograminformation-copyright
            '''
            result = self._values.get("copyright")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def language_code(self) -> typing.Optional[builtins.str]:
            '''The language code for this manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashprograminformation.html#cfn-mediapackagev2-originendpoint-dashprograminformation-languagecode
            '''
            result = self._values.get("language_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def more_information_url(self) -> typing.Optional[builtins.str]:
            '''An absolute URL that contains more information about this content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashprograminformation.html#cfn-mediapackagev2-originendpoint-dashprograminformation-moreinformationurl
            '''
            result = self._values.get("more_information_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''Information about the content provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashprograminformation.html#cfn-mediapackagev2-originendpoint-dashprograminformation-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def title(self) -> typing.Optional[builtins.str]:
            '''The title for the manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashprograminformation.html#cfn-mediapackagev2-originendpoint-dashprograminformation-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashProgramInformationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.DashSubtitleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"ttml_configuration": "ttmlConfiguration"},
    )
    class DashSubtitleConfigurationProperty:
        def __init__(
            self,
            *,
            ttml_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.DashTtmlConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration for DASH subtitles.

            :param ttml_configuration: Settings for TTML subtitles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashsubtitleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                dash_subtitle_configuration_property = mediapackagev2.CfnOriginEndpoint.DashSubtitleConfigurationProperty(
                    ttml_configuration=mediapackagev2.CfnOriginEndpoint.DashTtmlConfigurationProperty(
                        ttml_profile="ttmlProfile"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aa51912df0060cf290274ace134d0cb16e34e1de7ea689b411eeae296d9a8155)
                check_type(argname="argument ttml_configuration", value=ttml_configuration, expected_type=type_hints["ttml_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ttml_configuration is not None:
                self._values["ttml_configuration"] = ttml_configuration

        @builtins.property
        def ttml_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashTtmlConfigurationProperty"]]:
            '''Settings for TTML subtitles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashsubtitleconfiguration.html#cfn-mediapackagev2-originendpoint-dashsubtitleconfiguration-ttmlconfiguration
            '''
            result = self._values.get("ttml_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashTtmlConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashSubtitleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.DashTtmlConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"ttml_profile": "ttmlProfile"},
    )
    class DashTtmlConfigurationProperty:
        def __init__(self, *, ttml_profile: builtins.str) -> None:
            '''The settings for TTML subtitles.

            :param ttml_profile: The profile that MediaPackage uses when signaling subtitles in the manifest. ``IMSC`` is the default profile. ``EBU-TT-D`` produces subtitles that are compliant with the EBU-TT-D TTML profile. MediaPackage passes through subtitle styles to the manifest. For more information about EBU-TT-D subtitles, see `EBU-TT-D Subtitling Distribution Format <https://docs.aws.amazon.com/https://tech.ebu.ch/publications/tech3380>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashttmlconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                dash_ttml_configuration_property = mediapackagev2.CfnOriginEndpoint.DashTtmlConfigurationProperty(
                    ttml_profile="ttmlProfile"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bba187ab72699f6dc21195cb98838c8f292af76576ca0254079260c1346c116d)
                check_type(argname="argument ttml_profile", value=ttml_profile, expected_type=type_hints["ttml_profile"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "ttml_profile": ttml_profile,
            }

        @builtins.property
        def ttml_profile(self) -> builtins.str:
            '''The profile that MediaPackage uses when signaling subtitles in the manifest.

            ``IMSC`` is the default profile. ``EBU-TT-D`` produces subtitles that are compliant with the EBU-TT-D TTML profile. MediaPackage passes through subtitle styles to the manifest. For more information about EBU-TT-D subtitles, see `EBU-TT-D Subtitling Distribution Format <https://docs.aws.amazon.com/https://tech.ebu.ch/publications/tech3380>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashttmlconfiguration.html#cfn-mediapackagev2-originendpoint-dashttmlconfiguration-ttmlprofile
            '''
            result = self._values.get("ttml_profile")
            assert result is not None, "Required property 'ttml_profile' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashTtmlConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.DashUtcTimingProperty",
        jsii_struct_bases=[],
        name_mapping={"timing_mode": "timingMode", "timing_source": "timingSource"},
    )
    class DashUtcTimingProperty:
        def __init__(
            self,
            *,
            timing_mode: typing.Optional[builtins.str] = None,
            timing_source: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Determines the type of UTC timing included in the DASH Media Presentation Description (MPD).

            :param timing_mode: The UTC timing mode.
            :param timing_source: The the method that the player uses to synchronize to coordinated universal time (UTC) wall clock time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashutctiming.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                dash_utc_timing_property = mediapackagev2.CfnOriginEndpoint.DashUtcTimingProperty(
                    timing_mode="timingMode",
                    timing_source="timingSource"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__09bad37e3e4d3382385a9f8aab252d146616b680c49d6ef16671c82ef1248794)
                check_type(argname="argument timing_mode", value=timing_mode, expected_type=type_hints["timing_mode"])
                check_type(argname="argument timing_source", value=timing_source, expected_type=type_hints["timing_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if timing_mode is not None:
                self._values["timing_mode"] = timing_mode
            if timing_source is not None:
                self._values["timing_source"] = timing_source

        @builtins.property
        def timing_mode(self) -> typing.Optional[builtins.str]:
            '''The UTC timing mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashutctiming.html#cfn-mediapackagev2-originendpoint-dashutctiming-timingmode
            '''
            result = self._values.get("timing_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timing_source(self) -> typing.Optional[builtins.str]:
            '''The the method that the player uses to synchronize to coordinated universal time (UTC) wall clock time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-dashutctiming.html#cfn-mediapackagev2-originendpoint-dashutctiming-timingsource
            '''
            result = self._values.get("timing_source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashUtcTimingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.EncryptionContractConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "preset_speke20_audio": "presetSpeke20Audio",
            "preset_speke20_video": "presetSpeke20Video",
        },
    )
    class EncryptionContractConfigurationProperty:
        def __init__(
            self,
            *,
            preset_speke20_audio: builtins.str,
            preset_speke20_video: builtins.str,
        ) -> None:
            '''Use ``encryptionContractConfiguration`` to configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use.

            :param preset_speke20_audio: A collection of audio encryption presets. Value description: - ``PRESET-AUDIO-1`` - Use one content key to encrypt all of the audio tracks in your stream. - ``PRESET-AUDIO-2`` - Use one content key to encrypt all of the stereo audio tracks and one content key to encrypt all of the multichannel audio tracks. - ``PRESET-AUDIO-3`` - Use one content key to encrypt all of the stereo audio tracks, one content key to encrypt all of the multichannel audio tracks with 3 to 6 channels, and one content key to encrypt all of the multichannel audio tracks with more than 6 channels. - ``SHARED`` - Use the same content key for all of the audio and video tracks in your stream. - ``UNENCRYPTED`` - Don't encrypt any of the audio tracks in your stream.
            :param preset_speke20_video: The SPEKE Version 2.0 preset video associated with the encryption contract configuration of the origin endpoint. A collection of video encryption presets. Value description: - ``PRESET-VIDEO-1`` - Use one content key to encrypt all of the video tracks in your stream. - ``PRESET-VIDEO-2`` - Use one content key to encrypt all of the SD video tracks and one content key for all HD and higher resolutions video tracks. - ``PRESET-VIDEO-3`` - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks and one content key for all UHD video tracks. - ``PRESET-VIDEO-4`` - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks. - ``PRESET-VIDEO-5`` - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks. - ``PRESET-VIDEO-6`` - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks. - ``PRESET-VIDEO-7`` - Use one content key to encrypt all of the SD+HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks. - ``PRESET-VIDEO-8`` - Use one content key to encrypt all of the SD+HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks. - ``SHARED`` - Use the same content key for all of the video and audio tracks in your stream. - ``UNENCRYPTED`` - Don't encrypt any of the video tracks in your stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryptioncontractconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                encryption_contract_configuration_property = mediapackagev2.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                    preset_speke20_audio="presetSpeke20Audio",
                    preset_speke20_video="presetSpeke20Video"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5bec1eea406d4bb796486d5773d483a771df06a4cb391f44e1755e98877b7f22)
                check_type(argname="argument preset_speke20_audio", value=preset_speke20_audio, expected_type=type_hints["preset_speke20_audio"])
                check_type(argname="argument preset_speke20_video", value=preset_speke20_video, expected_type=type_hints["preset_speke20_video"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "preset_speke20_audio": preset_speke20_audio,
                "preset_speke20_video": preset_speke20_video,
            }

        @builtins.property
        def preset_speke20_audio(self) -> builtins.str:
            '''A collection of audio encryption presets.

            Value description:

            - ``PRESET-AUDIO-1`` - Use one content key to encrypt all of the audio tracks in your stream.
            - ``PRESET-AUDIO-2`` - Use one content key to encrypt all of the stereo audio tracks and one content key to encrypt all of the multichannel audio tracks.
            - ``PRESET-AUDIO-3`` - Use one content key to encrypt all of the stereo audio tracks, one content key to encrypt all of the multichannel audio tracks with 3 to 6 channels, and one content key to encrypt all of the multichannel audio tracks with more than 6 channels.
            - ``SHARED`` - Use the same content key for all of the audio and video tracks in your stream.
            - ``UNENCRYPTED`` - Don't encrypt any of the audio tracks in your stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryptioncontractconfiguration.html#cfn-mediapackagev2-originendpoint-encryptioncontractconfiguration-presetspeke20audio
            '''
            result = self._values.get("preset_speke20_audio")
            assert result is not None, "Required property 'preset_speke20_audio' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def preset_speke20_video(self) -> builtins.str:
            '''The SPEKE Version 2.0 preset video associated with the encryption contract configuration of the origin endpoint.

            A collection of video encryption presets.

            Value description:

            - ``PRESET-VIDEO-1`` - Use one content key to encrypt all of the video tracks in your stream.
            - ``PRESET-VIDEO-2`` - Use one content key to encrypt all of the SD video tracks and one content key for all HD and higher resolutions video tracks.
            - ``PRESET-VIDEO-3`` - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks and one content key for all UHD video tracks.
            - ``PRESET-VIDEO-4`` - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
            - ``PRESET-VIDEO-5`` - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
            - ``PRESET-VIDEO-6`` - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks.
            - ``PRESET-VIDEO-7`` - Use one content key to encrypt all of the SD+HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks.
            - ``PRESET-VIDEO-8`` - Use one content key to encrypt all of the SD+HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
            - ``SHARED`` - Use the same content key for all of the video and audio tracks in your stream.
            - ``UNENCRYPTED`` - Don't encrypt any of the video tracks in your stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryptioncontractconfiguration.html#cfn-mediapackagev2-originendpoint-encryptioncontractconfiguration-presetspeke20video
            '''
            result = self._values.get("preset_speke20_video")
            assert result is not None, "Required property 'preset_speke20_video' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionContractConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.EncryptionMethodProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cmaf_encryption_method": "cmafEncryptionMethod",
            "ts_encryption_method": "tsEncryptionMethod",
        },
    )
    class EncryptionMethodProperty:
        def __init__(
            self,
            *,
            cmaf_encryption_method: typing.Optional[builtins.str] = None,
            ts_encryption_method: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The encryption method associated with the origin endpoint.

            :param cmaf_encryption_method: The encryption method to use.
            :param ts_encryption_method: The encryption method to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryptionmethod.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                encryption_method_property = mediapackagev2.CfnOriginEndpoint.EncryptionMethodProperty(
                    cmaf_encryption_method="cmafEncryptionMethod",
                    ts_encryption_method="tsEncryptionMethod"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__abdd735051ce598919313a259e3efc1aa635283b073d78fb9c4e876eef4ca8b8)
                check_type(argname="argument cmaf_encryption_method", value=cmaf_encryption_method, expected_type=type_hints["cmaf_encryption_method"])
                check_type(argname="argument ts_encryption_method", value=ts_encryption_method, expected_type=type_hints["ts_encryption_method"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cmaf_encryption_method is not None:
                self._values["cmaf_encryption_method"] = cmaf_encryption_method
            if ts_encryption_method is not None:
                self._values["ts_encryption_method"] = ts_encryption_method

        @builtins.property
        def cmaf_encryption_method(self) -> typing.Optional[builtins.str]:
            '''The encryption method to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryptionmethod.html#cfn-mediapackagev2-originendpoint-encryptionmethod-cmafencryptionmethod
            '''
            result = self._values.get("cmaf_encryption_method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ts_encryption_method(self) -> typing.Optional[builtins.str]:
            '''The encryption method to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryptionmethod.html#cfn-mediapackagev2-originendpoint-encryptionmethod-tsencryptionmethod
            '''
            result = self._values.get("ts_encryption_method")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionMethodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.EncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_method": "encryptionMethod",
            "speke_key_provider": "spekeKeyProvider",
            "cmaf_exclude_segment_drm_metadata": "cmafExcludeSegmentDrmMetadata",
            "constant_initialization_vector": "constantInitializationVector",
            "key_rotation_interval_seconds": "keyRotationIntervalSeconds",
        },
    )
    class EncryptionProperty:
        def __init__(
            self,
            *,
            encryption_method: typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.EncryptionMethodProperty", typing.Dict[builtins.str, typing.Any]]],
            speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.SpekeKeyProviderProperty", typing.Dict[builtins.str, typing.Any]]],
            cmaf_exclude_segment_drm_metadata: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            constant_initialization_vector: typing.Optional[builtins.str] = None,
            key_rotation_interval_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The parameters for encrypting content.

            :param encryption_method: The encryption method to use.
            :param speke_key_provider: The SPEKE key provider to use for encryption.
            :param cmaf_exclude_segment_drm_metadata: Excludes SEIG and SGPD boxes from segment metadata in CMAF containers. When set to ``true`` , MediaPackage omits these DRM metadata boxes from CMAF segments, which can improve compatibility with certain devices and players that don't support these boxes. Important considerations: - This setting only affects CMAF container formats - Key rotation can still be handled through media playlist signaling - PSSH and TENC boxes remain unaffected - Default behavior is preserved when this setting is disabled Valid values: ``true`` | ``false`` Default: ``false``
            :param constant_initialization_vector: A 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting content. If you don't specify a value, then MediaPackage creates the constant initialization vector (IV).
            :param key_rotation_interval_seconds: The interval, in seconds, to rotate encryption keys for the origin endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                encryption_property = mediapackagev2.CfnOriginEndpoint.EncryptionProperty(
                    encryption_method=mediapackagev2.CfnOriginEndpoint.EncryptionMethodProperty(
                        cmaf_encryption_method="cmafEncryptionMethod",
                        ts_encryption_method="tsEncryptionMethod"
                    ),
                    speke_key_provider=mediapackagev2.CfnOriginEndpoint.SpekeKeyProviderProperty(
                        drm_systems=["drmSystems"],
                        encryption_contract_configuration=mediapackagev2.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        ),
                        resource_id="resourceId",
                        role_arn="roleArn",
                        url="url"
                    ),
                
                    # the properties below are optional
                    cmaf_exclude_segment_drm_metadata=False,
                    constant_initialization_vector="constantInitializationVector",
                    key_rotation_interval_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ba68bba2e5edd62f12d66393f036d9e0dc8f60c4705d328714b3a2f959ba4a07)
                check_type(argname="argument encryption_method", value=encryption_method, expected_type=type_hints["encryption_method"])
                check_type(argname="argument speke_key_provider", value=speke_key_provider, expected_type=type_hints["speke_key_provider"])
                check_type(argname="argument cmaf_exclude_segment_drm_metadata", value=cmaf_exclude_segment_drm_metadata, expected_type=type_hints["cmaf_exclude_segment_drm_metadata"])
                check_type(argname="argument constant_initialization_vector", value=constant_initialization_vector, expected_type=type_hints["constant_initialization_vector"])
                check_type(argname="argument key_rotation_interval_seconds", value=key_rotation_interval_seconds, expected_type=type_hints["key_rotation_interval_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_method": encryption_method,
                "speke_key_provider": speke_key_provider,
            }
            if cmaf_exclude_segment_drm_metadata is not None:
                self._values["cmaf_exclude_segment_drm_metadata"] = cmaf_exclude_segment_drm_metadata
            if constant_initialization_vector is not None:
                self._values["constant_initialization_vector"] = constant_initialization_vector
            if key_rotation_interval_seconds is not None:
                self._values["key_rotation_interval_seconds"] = key_rotation_interval_seconds

        @builtins.property
        def encryption_method(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.EncryptionMethodProperty"]:
            '''The encryption method to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryption.html#cfn-mediapackagev2-originendpoint-encryption-encryptionmethod
            '''
            result = self._values.get("encryption_method")
            assert result is not None, "Required property 'encryption_method' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.EncryptionMethodProperty"], result)

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.SpekeKeyProviderProperty"]:
            '''The SPEKE key provider to use for encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryption.html#cfn-mediapackagev2-originendpoint-encryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.SpekeKeyProviderProperty"], result)

        @builtins.property
        def cmaf_exclude_segment_drm_metadata(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Excludes SEIG and SGPD boxes from segment metadata in CMAF containers.

            When set to ``true`` , MediaPackage omits these DRM metadata boxes from CMAF segments, which can improve compatibility with certain devices and players that don't support these boxes.

            Important considerations:

            - This setting only affects CMAF container formats
            - Key rotation can still be handled through media playlist signaling
            - PSSH and TENC boxes remain unaffected
            - Default behavior is preserved when this setting is disabled

            Valid values: ``true`` | ``false``

            Default: ``false``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryption.html#cfn-mediapackagev2-originendpoint-encryption-cmafexcludesegmentdrmmetadata
            '''
            result = self._values.get("cmaf_exclude_segment_drm_metadata")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def constant_initialization_vector(self) -> typing.Optional[builtins.str]:
            '''A 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting content.

            If you don't specify a value, then MediaPackage creates the constant initialization vector (IV).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryption.html#cfn-mediapackagev2-originendpoint-encryption-constantinitializationvector
            '''
            result = self._values.get("constant_initialization_vector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_rotation_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''The interval, in seconds, to rotate encryption keys for the origin endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryption.html#cfn-mediapackagev2-originendpoint-encryption-keyrotationintervalseconds
            '''
            result = self._values.get("key_rotation_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.FilterConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "clip_start_time": "clipStartTime",
            "end": "end",
            "manifest_filter": "manifestFilter",
            "start": "start",
            "time_delay_seconds": "timeDelaySeconds",
        },
    )
    class FilterConfigurationProperty:
        def __init__(
            self,
            *,
            clip_start_time: typing.Optional[builtins.str] = None,
            end: typing.Optional[builtins.str] = None,
            manifest_filter: typing.Optional[builtins.str] = None,
            start: typing.Optional[builtins.str] = None,
            time_delay_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.

            :param clip_start_time: Optionally specify the clip start time for all of your manifest egress requests. When you include clip start time, note that you cannot use clip start time query parameters for this manifest's endpoint URL.
            :param end: Optionally specify the end time for all of your manifest egress requests. When you include end time, note that you cannot use end time query parameters for this manifest's endpoint URL.
            :param manifest_filter: Optionally specify one or more manifest filters for all of your manifest egress requests. When you include a manifest filter, note that you cannot use an identical manifest filter query parameter for this manifest's endpoint URL.
            :param start: Optionally specify the start time for all of your manifest egress requests. When you include start time, note that you cannot use start time query parameters for this manifest's endpoint URL.
            :param time_delay_seconds: Optionally specify the time delay for all of your manifest egress requests. Enter a value that is smaller than your endpoint's startover window. When you include time delay, note that you cannot use time delay query parameters for this manifest's endpoint URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-filterconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                filter_configuration_property = mediapackagev2.CfnOriginEndpoint.FilterConfigurationProperty(
                    clip_start_time="clipStartTime",
                    end="end",
                    manifest_filter="manifestFilter",
                    start="start",
                    time_delay_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cd4523035a4ce6e5ff7d759a2d3d8f5fc12e2c0c96ad04c9ef1b884c6334f16c)
                check_type(argname="argument clip_start_time", value=clip_start_time, expected_type=type_hints["clip_start_time"])
                check_type(argname="argument end", value=end, expected_type=type_hints["end"])
                check_type(argname="argument manifest_filter", value=manifest_filter, expected_type=type_hints["manifest_filter"])
                check_type(argname="argument start", value=start, expected_type=type_hints["start"])
                check_type(argname="argument time_delay_seconds", value=time_delay_seconds, expected_type=type_hints["time_delay_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if clip_start_time is not None:
                self._values["clip_start_time"] = clip_start_time
            if end is not None:
                self._values["end"] = end
            if manifest_filter is not None:
                self._values["manifest_filter"] = manifest_filter
            if start is not None:
                self._values["start"] = start
            if time_delay_seconds is not None:
                self._values["time_delay_seconds"] = time_delay_seconds

        @builtins.property
        def clip_start_time(self) -> typing.Optional[builtins.str]:
            '''Optionally specify the clip start time for all of your manifest egress requests.

            When you include clip start time, note that you cannot use clip start time query parameters for this manifest's endpoint URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-filterconfiguration.html#cfn-mediapackagev2-originendpoint-filterconfiguration-clipstarttime
            '''
            result = self._values.get("clip_start_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def end(self) -> typing.Optional[builtins.str]:
            '''Optionally specify the end time for all of your manifest egress requests.

            When you include end time, note that you cannot use end time query parameters for this manifest's endpoint URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-filterconfiguration.html#cfn-mediapackagev2-originendpoint-filterconfiguration-end
            '''
            result = self._values.get("end")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def manifest_filter(self) -> typing.Optional[builtins.str]:
            '''Optionally specify one or more manifest filters for all of your manifest egress requests.

            When you include a manifest filter, note that you cannot use an identical manifest filter query parameter for this manifest's endpoint URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-filterconfiguration.html#cfn-mediapackagev2-originendpoint-filterconfiguration-manifestfilter
            '''
            result = self._values.get("manifest_filter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start(self) -> typing.Optional[builtins.str]:
            '''Optionally specify the start time for all of your manifest egress requests.

            When you include start time, note that you cannot use start time query parameters for this manifest's endpoint URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-filterconfiguration.html#cfn-mediapackagev2-originendpoint-filterconfiguration-start
            '''
            result = self._values.get("start")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def time_delay_seconds(self) -> typing.Optional[jsii.Number]:
            '''Optionally specify the time delay for all of your manifest egress requests.

            Enter a value that is smaller than your endpoint's startover window. When you include time delay, note that you cannot use time delay query parameters for this manifest's endpoint URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-filterconfiguration.html#cfn-mediapackagev2-originendpoint-filterconfiguration-timedelayseconds
            '''
            result = self._values.get("time_delay_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.ForceEndpointErrorConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint_error_conditions": "endpointErrorConditions"},
    )
    class ForceEndpointErrorConfigurationProperty:
        def __init__(
            self,
            *,
            endpoint_error_conditions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The failover settings for the endpoint.

            :param endpoint_error_conditions: The failover conditions for the endpoint. The options are:. - ``STALE_MANIFEST`` - The manifest stalled and there are no new segments or parts. - ``INCOMPLETE_MANIFEST`` - There is a gap in the manifest. - ``MISSING_DRM_KEY`` - Key rotation is enabled but we're unable to fetch the key for the current key period. - ``SLATE_INPUT`` - The segments which contain slate content are considered to be missing content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-forceendpointerrorconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                force_endpoint_error_configuration_property = mediapackagev2.CfnOriginEndpoint.ForceEndpointErrorConfigurationProperty(
                    endpoint_error_conditions=["endpointErrorConditions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c775185d7f0f530d0727569d624c7700267dcbd432d6270153826a314b2e766e)
                check_type(argname="argument endpoint_error_conditions", value=endpoint_error_conditions, expected_type=type_hints["endpoint_error_conditions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if endpoint_error_conditions is not None:
                self._values["endpoint_error_conditions"] = endpoint_error_conditions

        @builtins.property
        def endpoint_error_conditions(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The failover conditions for the endpoint. The options are:.

            - ``STALE_MANIFEST`` - The manifest stalled and there are no new segments or parts.
            - ``INCOMPLETE_MANIFEST`` - There is a gap in the manifest.
            - ``MISSING_DRM_KEY`` - Key rotation is enabled but we're unable to fetch the key for the current key period.
            - ``SLATE_INPUT`` - The segments which contain slate content are considered to be missing content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-forceendpointerrorconfiguration.html#cfn-mediapackagev2-originendpoint-forceendpointerrorconfiguration-endpointerrorconditions
            '''
            result = self._values.get("endpoint_error_conditions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ForceEndpointErrorConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.HlsManifestConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "manifest_name": "manifestName",
            "child_manifest_name": "childManifestName",
            "filter_configuration": "filterConfiguration",
            "manifest_window_seconds": "manifestWindowSeconds",
            "program_date_time_interval_seconds": "programDateTimeIntervalSeconds",
            "scte_hls": "scteHls",
            "start_tag": "startTag",
            "url": "url",
            "url_encode_child_manifest": "urlEncodeChildManifest",
        },
    )
    class HlsManifestConfigurationProperty:
        def __init__(
            self,
            *,
            manifest_name: builtins.str,
            child_manifest_name: typing.Optional[builtins.str] = None,
            filter_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.FilterConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            manifest_window_seconds: typing.Optional[jsii.Number] = None,
            program_date_time_interval_seconds: typing.Optional[jsii.Number] = None,
            scte_hls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.ScteHlsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            start_tag: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.StartTagProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            url: typing.Optional[builtins.str] = None,
            url_encode_child_manifest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The HLS manifest configuration associated with the origin endpoint.

            :param manifest_name: The name of the manifest associated with the HLS manifest configuration.
            :param child_manifest_name: The name of the child manifest associated with the HLS manifest configuration.
            :param filter_configuration: Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.
            :param manifest_window_seconds: The duration of the manifest window, in seconds, for the HLS manifest configuration.
            :param program_date_time_interval_seconds: The ``EXT-X-PROGRAM-DATE-TIME`` interval, in seconds, associated with the HLS manifest configuration.
            :param scte_hls: THE SCTE-35 HLS configuration associated with the HLS manifest configuration.
            :param start_tag: To insert an EXT-X-START tag in your HLS playlist, specify a StartTag configuration object with a valid TimeOffset. When you do, you can also optionally specify whether to include a PRECISE value in the EXT-X-START tag.
            :param url: The URL of the HLS manifest configuration.
            :param url_encode_child_manifest: When enabled, MediaPackage URL-encodes the query string for API requests for HLS child manifests to comply with AWS Signature Version 4 (SigV4) signature signing protocol. For more information, see `AWS Signature Version 4 for API requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html>`_ in *AWS Identity and Access Management User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                hls_manifest_configuration_property = mediapackagev2.CfnOriginEndpoint.HlsManifestConfigurationProperty(
                    manifest_name="manifestName",
                
                    # the properties below are optional
                    child_manifest_name="childManifestName",
                    filter_configuration=mediapackagev2.CfnOriginEndpoint.FilterConfigurationProperty(
                        clip_start_time="clipStartTime",
                        end="end",
                        manifest_filter="manifestFilter",
                        start="start",
                        time_delay_seconds=123
                    ),
                    manifest_window_seconds=123,
                    program_date_time_interval_seconds=123,
                    scte_hls=mediapackagev2.CfnOriginEndpoint.ScteHlsProperty(
                        ad_marker_hls="adMarkerHls"
                    ),
                    start_tag=mediapackagev2.CfnOriginEndpoint.StartTagProperty(
                        time_offset=123,
                
                        # the properties below are optional
                        precise=False
                    ),
                    url="url",
                    url_encode_child_manifest=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b59520e6fbce62f410265deeb9cc043e1cf408c2c3cc498907eb73fcc18458d8)
                check_type(argname="argument manifest_name", value=manifest_name, expected_type=type_hints["manifest_name"])
                check_type(argname="argument child_manifest_name", value=child_manifest_name, expected_type=type_hints["child_manifest_name"])
                check_type(argname="argument filter_configuration", value=filter_configuration, expected_type=type_hints["filter_configuration"])
                check_type(argname="argument manifest_window_seconds", value=manifest_window_seconds, expected_type=type_hints["manifest_window_seconds"])
                check_type(argname="argument program_date_time_interval_seconds", value=program_date_time_interval_seconds, expected_type=type_hints["program_date_time_interval_seconds"])
                check_type(argname="argument scte_hls", value=scte_hls, expected_type=type_hints["scte_hls"])
                check_type(argname="argument start_tag", value=start_tag, expected_type=type_hints["start_tag"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument url_encode_child_manifest", value=url_encode_child_manifest, expected_type=type_hints["url_encode_child_manifest"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "manifest_name": manifest_name,
            }
            if child_manifest_name is not None:
                self._values["child_manifest_name"] = child_manifest_name
            if filter_configuration is not None:
                self._values["filter_configuration"] = filter_configuration
            if manifest_window_seconds is not None:
                self._values["manifest_window_seconds"] = manifest_window_seconds
            if program_date_time_interval_seconds is not None:
                self._values["program_date_time_interval_seconds"] = program_date_time_interval_seconds
            if scte_hls is not None:
                self._values["scte_hls"] = scte_hls
            if start_tag is not None:
                self._values["start_tag"] = start_tag
            if url is not None:
                self._values["url"] = url
            if url_encode_child_manifest is not None:
                self._values["url_encode_child_manifest"] = url_encode_child_manifest

        @builtins.property
        def manifest_name(self) -> builtins.str:
            '''The name of the manifest associated with the HLS manifest configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-manifestname
            '''
            result = self._values.get("manifest_name")
            assert result is not None, "Required property 'manifest_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def child_manifest_name(self) -> typing.Optional[builtins.str]:
            '''The name of the child manifest associated with the HLS manifest configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-childmanifestname
            '''
            result = self._values.get("child_manifest_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def filter_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.FilterConfigurationProperty"]]:
            '''Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-filterconfiguration
            '''
            result = self._values.get("filter_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.FilterConfigurationProperty"]], result)

        @builtins.property
        def manifest_window_seconds(self) -> typing.Optional[jsii.Number]:
            '''The duration of the manifest window, in seconds, for the HLS manifest configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-manifestwindowseconds
            '''
            result = self._values.get("manifest_window_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def program_date_time_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''The ``EXT-X-PROGRAM-DATE-TIME`` interval, in seconds, associated with the HLS manifest configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-programdatetimeintervalseconds
            '''
            result = self._values.get("program_date_time_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def scte_hls(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.ScteHlsProperty"]]:
            '''THE SCTE-35 HLS configuration associated with the HLS manifest configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-sctehls
            '''
            result = self._values.get("scte_hls")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.ScteHlsProperty"]], result)

        @builtins.property
        def start_tag(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.StartTagProperty"]]:
            '''To insert an EXT-X-START tag in your HLS playlist, specify a StartTag configuration object with a valid TimeOffset.

            When you do, you can also optionally specify whether to include a PRECISE value in the EXT-X-START tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-starttag
            '''
            result = self._values.get("start_tag")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.StartTagProperty"]], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The URL of the HLS manifest configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url_encode_child_manifest(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When enabled, MediaPackage URL-encodes the query string for API requests for HLS child manifests to comply with AWS Signature Version 4 (SigV4) signature signing protocol.

            For more information, see `AWS Signature Version 4 for API requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html>`_ in *AWS Identity and Access Management User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-urlencodechildmanifest
            '''
            result = self._values.get("url_encode_child_manifest")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsManifestConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.LowLatencyHlsManifestConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "manifest_name": "manifestName",
            "child_manifest_name": "childManifestName",
            "filter_configuration": "filterConfiguration",
            "manifest_window_seconds": "manifestWindowSeconds",
            "program_date_time_interval_seconds": "programDateTimeIntervalSeconds",
            "scte_hls": "scteHls",
            "start_tag": "startTag",
            "url": "url",
            "url_encode_child_manifest": "urlEncodeChildManifest",
        },
    )
    class LowLatencyHlsManifestConfigurationProperty:
        def __init__(
            self,
            *,
            manifest_name: builtins.str,
            child_manifest_name: typing.Optional[builtins.str] = None,
            filter_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.FilterConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            manifest_window_seconds: typing.Optional[jsii.Number] = None,
            program_date_time_interval_seconds: typing.Optional[jsii.Number] = None,
            scte_hls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.ScteHlsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            start_tag: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.StartTagProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            url: typing.Optional[builtins.str] = None,
            url_encode_child_manifest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Specify a low-latency HTTP live streaming (LL-HLS) manifest configuration.

            :param manifest_name: A short string that's appended to the endpoint URL. The manifest name creates a unique path to this endpoint. If you don't enter a value, MediaPackage uses the default manifest name, ``index`` . MediaPackage automatically inserts the format extension, such as ``.m3u8`` . You can't use the same manifest name if you use HLS manifest and low-latency HLS manifest. The ``manifestName`` on the ``HLSManifest`` object overrides the ``manifestName`` you provided on the ``originEndpoint`` object.
            :param child_manifest_name: The name of the child manifest associated with the low-latency HLS (LL-HLS) manifest configuration of the origin endpoint.
            :param filter_configuration: Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.
            :param manifest_window_seconds: The total duration (in seconds) of the manifest's content.
            :param program_date_time_interval_seconds: Inserts ``EXT-X-PROGRAM-DATE-TIME`` tags in the output manifest at the interval that you specify. If you don't enter an interval, ``EXT-X-PROGRAM-DATE-TIME`` tags aren't included in the manifest. The tags sync the stream to the wall clock so that viewers can seek to a specific time in the playback timeline on the player. Irrespective of this parameter, if any ``ID3Timed`` metadata is in the HLS input, MediaPackage passes through that metadata to the HLS output.
            :param scte_hls: The SCTE-35 HLS configuration associated with the low-latency HLS (LL-HLS) manifest configuration of the origin endpoint.
            :param start_tag: To insert an EXT-X-START tag in your HLS playlist, specify a StartTag configuration object with a valid TimeOffset. When you do, you can also optionally specify whether to include a PRECISE value in the EXT-X-START tag.
            :param url: The URL of the low-latency HLS (LL-HLS) manifest configuration of the origin endpoint.
            :param url_encode_child_manifest: When enabled, MediaPackage URL-encodes the query string for API requests for LL-HLS child manifests to comply with AWS Signature Version 4 (SigV4) signature signing protocol. For more information, see `AWS Signature Version 4 for API requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html>`_ in *AWS Identity and Access Management User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                low_latency_hls_manifest_configuration_property = mediapackagev2.CfnOriginEndpoint.LowLatencyHlsManifestConfigurationProperty(
                    manifest_name="manifestName",
                
                    # the properties below are optional
                    child_manifest_name="childManifestName",
                    filter_configuration=mediapackagev2.CfnOriginEndpoint.FilterConfigurationProperty(
                        clip_start_time="clipStartTime",
                        end="end",
                        manifest_filter="manifestFilter",
                        start="start",
                        time_delay_seconds=123
                    ),
                    manifest_window_seconds=123,
                    program_date_time_interval_seconds=123,
                    scte_hls=mediapackagev2.CfnOriginEndpoint.ScteHlsProperty(
                        ad_marker_hls="adMarkerHls"
                    ),
                    start_tag=mediapackagev2.CfnOriginEndpoint.StartTagProperty(
                        time_offset=123,
                
                        # the properties below are optional
                        precise=False
                    ),
                    url="url",
                    url_encode_child_manifest=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7ba3db62514b88b8da1b21ec0b9459116f857508c0670adb698a120b326fed5e)
                check_type(argname="argument manifest_name", value=manifest_name, expected_type=type_hints["manifest_name"])
                check_type(argname="argument child_manifest_name", value=child_manifest_name, expected_type=type_hints["child_manifest_name"])
                check_type(argname="argument filter_configuration", value=filter_configuration, expected_type=type_hints["filter_configuration"])
                check_type(argname="argument manifest_window_seconds", value=manifest_window_seconds, expected_type=type_hints["manifest_window_seconds"])
                check_type(argname="argument program_date_time_interval_seconds", value=program_date_time_interval_seconds, expected_type=type_hints["program_date_time_interval_seconds"])
                check_type(argname="argument scte_hls", value=scte_hls, expected_type=type_hints["scte_hls"])
                check_type(argname="argument start_tag", value=start_tag, expected_type=type_hints["start_tag"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument url_encode_child_manifest", value=url_encode_child_manifest, expected_type=type_hints["url_encode_child_manifest"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "manifest_name": manifest_name,
            }
            if child_manifest_name is not None:
                self._values["child_manifest_name"] = child_manifest_name
            if filter_configuration is not None:
                self._values["filter_configuration"] = filter_configuration
            if manifest_window_seconds is not None:
                self._values["manifest_window_seconds"] = manifest_window_seconds
            if program_date_time_interval_seconds is not None:
                self._values["program_date_time_interval_seconds"] = program_date_time_interval_seconds
            if scte_hls is not None:
                self._values["scte_hls"] = scte_hls
            if start_tag is not None:
                self._values["start_tag"] = start_tag
            if url is not None:
                self._values["url"] = url
            if url_encode_child_manifest is not None:
                self._values["url_encode_child_manifest"] = url_encode_child_manifest

        @builtins.property
        def manifest_name(self) -> builtins.str:
            '''A short string that's appended to the endpoint URL.

            The manifest name creates a unique path to this endpoint. If you don't enter a value, MediaPackage uses the default manifest name, ``index`` . MediaPackage automatically inserts the format extension, such as ``.m3u8`` . You can't use the same manifest name if you use HLS manifest and low-latency HLS manifest. The ``manifestName`` on the ``HLSManifest`` object overrides the ``manifestName`` you provided on the ``originEndpoint`` object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration-manifestname
            '''
            result = self._values.get("manifest_name")
            assert result is not None, "Required property 'manifest_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def child_manifest_name(self) -> typing.Optional[builtins.str]:
            '''The name of the child manifest associated with the low-latency HLS (LL-HLS) manifest configuration of the origin endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration-childmanifestname
            '''
            result = self._values.get("child_manifest_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def filter_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.FilterConfigurationProperty"]]:
            '''Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration-filterconfiguration
            '''
            result = self._values.get("filter_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.FilterConfigurationProperty"]], result)

        @builtins.property
        def manifest_window_seconds(self) -> typing.Optional[jsii.Number]:
            '''The total duration (in seconds) of the manifest's content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration-manifestwindowseconds
            '''
            result = self._values.get("manifest_window_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def program_date_time_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''Inserts ``EXT-X-PROGRAM-DATE-TIME`` tags in the output manifest at the interval that you specify.

            If you don't enter an interval, ``EXT-X-PROGRAM-DATE-TIME`` tags aren't included in the manifest. The tags sync the stream to the wall clock so that viewers can seek to a specific time in the playback timeline on the player.

            Irrespective of this parameter, if any ``ID3Timed`` metadata is in the HLS input, MediaPackage passes through that metadata to the HLS output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration-programdatetimeintervalseconds
            '''
            result = self._values.get("program_date_time_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def scte_hls(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.ScteHlsProperty"]]:
            '''The SCTE-35 HLS configuration associated with the low-latency HLS (LL-HLS) manifest configuration of the origin endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration-sctehls
            '''
            result = self._values.get("scte_hls")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.ScteHlsProperty"]], result)

        @builtins.property
        def start_tag(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.StartTagProperty"]]:
            '''To insert an EXT-X-START tag in your HLS playlist, specify a StartTag configuration object with a valid TimeOffset.

            When you do, you can also optionally specify whether to include a PRECISE value in the EXT-X-START tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration-starttag
            '''
            result = self._values.get("start_tag")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.StartTagProperty"]], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The URL of the low-latency HLS (LL-HLS) manifest configuration of the origin endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url_encode_child_manifest(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When enabled, MediaPackage URL-encodes the query string for API requests for LL-HLS child manifests to comply with AWS Signature Version 4 (SigV4) signature signing protocol.

            For more information, see `AWS Signature Version 4 for API requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html>`_ in *AWS Identity and Access Management User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration-urlencodechildmanifest
            '''
            result = self._values.get("url_encode_child_manifest")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LowLatencyHlsManifestConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.ScteDashProperty",
        jsii_struct_bases=[],
        name_mapping={"ad_marker_dash": "adMarkerDash"},
    )
    class ScteDashProperty:
        def __init__(
            self,
            *,
            ad_marker_dash: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The SCTE configuration.

            :param ad_marker_dash: Choose how ad markers are included in the packaged content. If you include ad markers in the content stream in your upstream encoders, then you need to inform MediaPackage what to do with the ad markers in the output. Value description: - ``Binary`` - The SCTE-35 marker is expressed as a hex-string (Base64 string) rather than full XML. - ``XML`` - The SCTE marker is expressed fully in XML.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-sctedash.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                scte_dash_property = mediapackagev2.CfnOriginEndpoint.ScteDashProperty(
                    ad_marker_dash="adMarkerDash"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__13ac94f52ccc71367f414c5388529d309fac2b39d9caa3e0e662dc2cfae97455)
                check_type(argname="argument ad_marker_dash", value=ad_marker_dash, expected_type=type_hints["ad_marker_dash"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ad_marker_dash is not None:
                self._values["ad_marker_dash"] = ad_marker_dash

        @builtins.property
        def ad_marker_dash(self) -> typing.Optional[builtins.str]:
            '''Choose how ad markers are included in the packaged content.

            If you include ad markers in the content stream in your upstream encoders, then you need to inform MediaPackage what to do with the ad markers in the output.

            Value description:

            - ``Binary`` - The SCTE-35 marker is expressed as a hex-string (Base64 string) rather than full XML.
            - ``XML`` - The SCTE marker is expressed fully in XML.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-sctedash.html#cfn-mediapackagev2-originendpoint-sctedash-admarkerdash
            '''
            result = self._values.get("ad_marker_dash")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScteDashProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.ScteHlsProperty",
        jsii_struct_bases=[],
        name_mapping={"ad_marker_hls": "adMarkerHls"},
    )
    class ScteHlsProperty:
        def __init__(
            self,
            *,
            ad_marker_hls: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The SCTE-35 HLS configuration associated with the origin endpoint.

            :param ad_marker_hls: The SCTE-35 HLS ad-marker configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-sctehls.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                scte_hls_property = mediapackagev2.CfnOriginEndpoint.ScteHlsProperty(
                    ad_marker_hls="adMarkerHls"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8d4f889b0a331f5c9a9819d549afcb4b4239d6f7040f9146668998df9485e7ea)
                check_type(argname="argument ad_marker_hls", value=ad_marker_hls, expected_type=type_hints["ad_marker_hls"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ad_marker_hls is not None:
                self._values["ad_marker_hls"] = ad_marker_hls

        @builtins.property
        def ad_marker_hls(self) -> typing.Optional[builtins.str]:
            '''The SCTE-35 HLS ad-marker configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-sctehls.html#cfn-mediapackagev2-originendpoint-sctehls-admarkerhls
            '''
            result = self._values.get("ad_marker_hls")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScteHlsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.ScteProperty",
        jsii_struct_bases=[],
        name_mapping={"scte_filter": "scteFilter"},
    )
    class ScteProperty:
        def __init__(
            self,
            *,
            scte_filter: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The SCTE-35 configuration associated with the origin endpoint.

            :param scte_filter: The filter associated with the SCTE-35 configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-scte.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                scte_property = mediapackagev2.CfnOriginEndpoint.ScteProperty(
                    scte_filter=["scteFilter"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ef2f402f6bd5f38be28bfd79b40a3e8bf701cd6b9384547f9b36a386a6075a98)
                check_type(argname="argument scte_filter", value=scte_filter, expected_type=type_hints["scte_filter"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if scte_filter is not None:
                self._values["scte_filter"] = scte_filter

        @builtins.property
        def scte_filter(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The filter associated with the SCTE-35 configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-scte.html#cfn-mediapackagev2-originendpoint-scte-sctefilter
            '''
            result = self._values.get("scte_filter")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.SegmentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption": "encryption",
            "include_iframe_only_streams": "includeIframeOnlyStreams",
            "scte": "scte",
            "segment_duration_seconds": "segmentDurationSeconds",
            "segment_name": "segmentName",
            "ts_include_dvb_subtitles": "tsIncludeDvbSubtitles",
            "ts_use_audio_rendition_group": "tsUseAudioRenditionGroup",
        },
    )
    class SegmentProperty:
        def __init__(
            self,
            *,
            encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.EncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            include_iframe_only_streams: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            scte: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.ScteProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
            segment_name: typing.Optional[builtins.str] = None,
            ts_include_dvb_subtitles: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            ts_use_audio_rendition_group: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The segment configuration, including the segment name, duration, and other configuration values.

            :param encryption: Whether to use encryption for the segment.
            :param include_iframe_only_streams: Whether the segment includes I-frame-only streams.
            :param scte: The SCTE-35 configuration associated with the segment.
            :param segment_duration_seconds: The duration of the segment, in seconds.
            :param segment_name: The name of the segment associated with the origin endpoint.
            :param ts_include_dvb_subtitles: Whether the segment includes DVB subtitles.
            :param ts_use_audio_rendition_group: Whether the segment is an audio rendition group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-segment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                segment_property = mediapackagev2.CfnOriginEndpoint.SegmentProperty(
                    encryption=mediapackagev2.CfnOriginEndpoint.EncryptionProperty(
                        encryption_method=mediapackagev2.CfnOriginEndpoint.EncryptionMethodProperty(
                            cmaf_encryption_method="cmafEncryptionMethod",
                            ts_encryption_method="tsEncryptionMethod"
                        ),
                        speke_key_provider=mediapackagev2.CfnOriginEndpoint.SpekeKeyProviderProperty(
                            drm_systems=["drmSystems"],
                            encryption_contract_configuration=mediapackagev2.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            ),
                            resource_id="resourceId",
                            role_arn="roleArn",
                            url="url"
                        ),
                
                        # the properties below are optional
                        cmaf_exclude_segment_drm_metadata=False,
                        constant_initialization_vector="constantInitializationVector",
                        key_rotation_interval_seconds=123
                    ),
                    include_iframe_only_streams=False,
                    scte=mediapackagev2.CfnOriginEndpoint.ScteProperty(
                        scte_filter=["scteFilter"]
                    ),
                    segment_duration_seconds=123,
                    segment_name="segmentName",
                    ts_include_dvb_subtitles=False,
                    ts_use_audio_rendition_group=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__99efb585c0a363a79f96102145e602f3f91887f61fac7a746b16b243ae503d48)
                check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
                check_type(argname="argument include_iframe_only_streams", value=include_iframe_only_streams, expected_type=type_hints["include_iframe_only_streams"])
                check_type(argname="argument scte", value=scte, expected_type=type_hints["scte"])
                check_type(argname="argument segment_duration_seconds", value=segment_duration_seconds, expected_type=type_hints["segment_duration_seconds"])
                check_type(argname="argument segment_name", value=segment_name, expected_type=type_hints["segment_name"])
                check_type(argname="argument ts_include_dvb_subtitles", value=ts_include_dvb_subtitles, expected_type=type_hints["ts_include_dvb_subtitles"])
                check_type(argname="argument ts_use_audio_rendition_group", value=ts_use_audio_rendition_group, expected_type=type_hints["ts_use_audio_rendition_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if encryption is not None:
                self._values["encryption"] = encryption
            if include_iframe_only_streams is not None:
                self._values["include_iframe_only_streams"] = include_iframe_only_streams
            if scte is not None:
                self._values["scte"] = scte
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds
            if segment_name is not None:
                self._values["segment_name"] = segment_name
            if ts_include_dvb_subtitles is not None:
                self._values["ts_include_dvb_subtitles"] = ts_include_dvb_subtitles
            if ts_use_audio_rendition_group is not None:
                self._values["ts_use_audio_rendition_group"] = ts_use_audio_rendition_group

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.EncryptionProperty"]]:
            '''Whether to use encryption for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-segment.html#cfn-mediapackagev2-originendpoint-segment-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.EncryptionProperty"]], result)

        @builtins.property
        def include_iframe_only_streams(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether the segment includes I-frame-only streams.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-segment.html#cfn-mediapackagev2-originendpoint-segment-includeiframeonlystreams
            '''
            result = self._values.get("include_iframe_only_streams")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def scte(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.ScteProperty"]]:
            '''The SCTE-35 configuration associated with the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-segment.html#cfn-mediapackagev2-originendpoint-segment-scte
            '''
            result = self._values.get("scte")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.ScteProperty"]], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''The duration of the segment, in seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-segment.html#cfn-mediapackagev2-originendpoint-segment-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segment_name(self) -> typing.Optional[builtins.str]:
            '''The name of the segment associated with the origin endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-segment.html#cfn-mediapackagev2-originendpoint-segment-segmentname
            '''
            result = self._values.get("segment_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ts_include_dvb_subtitles(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether the segment includes DVB subtitles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-segment.html#cfn-mediapackagev2-originendpoint-segment-tsincludedvbsubtitles
            '''
            result = self._values.get("ts_include_dvb_subtitles")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def ts_use_audio_rendition_group(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether the segment is an audio rendition group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-segment.html#cfn-mediapackagev2-originendpoint-segment-tsuseaudiorenditiongroup
            '''
            result = self._values.get("ts_use_audio_rendition_group")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SegmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.SpekeKeyProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "drm_systems": "drmSystems",
            "encryption_contract_configuration": "encryptionContractConfiguration",
            "resource_id": "resourceId",
            "role_arn": "roleArn",
            "url": "url",
        },
    )
    class SpekeKeyProviderProperty:
        def __init__(
            self,
            *,
            drm_systems: typing.Sequence[builtins.str],
            encryption_contract_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.EncryptionContractConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            resource_id: builtins.str,
            role_arn: builtins.str,
            url: builtins.str,
        ) -> None:
            '''The parameters for the SPEKE key provider.

            :param drm_systems: The DRM solution provider you're using to protect your content during distribution.
            :param encryption_contract_configuration: The encryption contract configuration associated with the SPEKE key provider.
            :param resource_id: The unique identifier for the content. The service sends this identifier to the key server to identify the current endpoint. How unique you make this identifier depends on how fine-grained you want access controls to be. The service does not permit you to use the same ID for two simultaneous encryption processes. The resource ID is also known as the content ID. The following example shows a resource ID: ``MovieNight20171126093045``
            :param role_arn: The ARN for the IAM role granted by the key provider that provides access to the key provider API. This role must have a trust policy that allows MediaPackage to assume the role, and it must have a sufficient permissions policy to allow access to the specific key retrieval URL. Get this from your DRM solution provider. Valid format: ``arn:aws:iam::{accountID}:role/{name}`` . The following example shows a role ARN: ``arn:aws:iam::444455556666:role/SpekeAccess``
            :param url: The URL of the SPEKE key provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-spekekeyprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                speke_key_provider_property = mediapackagev2.CfnOriginEndpoint.SpekeKeyProviderProperty(
                    drm_systems=["drmSystems"],
                    encryption_contract_configuration=mediapackagev2.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                        preset_speke20_audio="presetSpeke20Audio",
                        preset_speke20_video="presetSpeke20Video"
                    ),
                    resource_id="resourceId",
                    role_arn="roleArn",
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e4c003b5dabc0ccf6e42c45fb4504036521870f7799525c5b18f42c7c618d131)
                check_type(argname="argument drm_systems", value=drm_systems, expected_type=type_hints["drm_systems"])
                check_type(argname="argument encryption_contract_configuration", value=encryption_contract_configuration, expected_type=type_hints["encryption_contract_configuration"])
                check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "drm_systems": drm_systems,
                "encryption_contract_configuration": encryption_contract_configuration,
                "resource_id": resource_id,
                "role_arn": role_arn,
                "url": url,
            }

        @builtins.property
        def drm_systems(self) -> typing.List[builtins.str]:
            '''The DRM solution provider you're using to protect your content during distribution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-spekekeyprovider.html#cfn-mediapackagev2-originendpoint-spekekeyprovider-drmsystems
            '''
            result = self._values.get("drm_systems")
            assert result is not None, "Required property 'drm_systems' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def encryption_contract_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.EncryptionContractConfigurationProperty"]:
            '''The encryption contract configuration associated with the SPEKE key provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-spekekeyprovider.html#cfn-mediapackagev2-originendpoint-spekekeyprovider-encryptioncontractconfiguration
            '''
            result = self._values.get("encryption_contract_configuration")
            assert result is not None, "Required property 'encryption_contract_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.EncryptionContractConfigurationProperty"], result)

        @builtins.property
        def resource_id(self) -> builtins.str:
            '''The unique identifier for the content.

            The service sends this identifier to the key server to identify the current endpoint. How unique you make this identifier depends on how fine-grained you want access controls to be. The service does not permit you to use the same ID for two simultaneous encryption processes. The resource ID is also known as the content ID.

            The following example shows a resource ID: ``MovieNight20171126093045``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-spekekeyprovider.html#cfn-mediapackagev2-originendpoint-spekekeyprovider-resourceid
            '''
            result = self._values.get("resource_id")
            assert result is not None, "Required property 'resource_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN for the IAM role granted by the key provider that provides access to the key provider API.

            This role must have a trust policy that allows MediaPackage to assume the role, and it must have a sufficient permissions policy to allow access to the specific key retrieval URL. Get this from your DRM solution provider.

            Valid format: ``arn:aws:iam::{accountID}:role/{name}`` . The following example shows a role ARN: ``arn:aws:iam::444455556666:role/SpekeAccess``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-spekekeyprovider.html#cfn-mediapackagev2-originendpoint-spekekeyprovider-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def url(self) -> builtins.str:
            '''The URL of the SPEKE key provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-spekekeyprovider.html#cfn-mediapackagev2-originendpoint-spekekeyprovider-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SpekeKeyProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpoint.StartTagProperty",
        jsii_struct_bases=[],
        name_mapping={"time_offset": "timeOffset", "precise": "precise"},
    )
    class StartTagProperty:
        def __init__(
            self,
            *,
            time_offset: jsii.Number,
            precise: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''To insert an EXT-X-START tag in your HLS playlist, specify a StartTag configuration object with a valid TimeOffset.

            When you do, you can also optionally specify whether to include a PRECISE value in the EXT-X-START tag.

            :param time_offset: Specify the value for TIME-OFFSET within your EXT-X-START tag. Enter a signed floating point value which, if positive, must be less than the configured manifest duration minus three times the configured segment target duration. If negative, the absolute value must be larger than three times the configured segment target duration, and the absolute value must be smaller than the configured manifest duration.
            :param precise: Specify the value for PRECISE within your EXT-X-START tag. Leave blank, or choose false, to use the default value NO. Choose yes to use the value YES.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-starttag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                start_tag_property = mediapackagev2.CfnOriginEndpoint.StartTagProperty(
                    time_offset=123,
                
                    # the properties below are optional
                    precise=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__638acac01659df889e5cbdebcde00e01e52315bf2fdb140c76d10ea5a120c30a)
                check_type(argname="argument time_offset", value=time_offset, expected_type=type_hints["time_offset"])
                check_type(argname="argument precise", value=precise, expected_type=type_hints["precise"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "time_offset": time_offset,
            }
            if precise is not None:
                self._values["precise"] = precise

        @builtins.property
        def time_offset(self) -> jsii.Number:
            '''Specify the value for TIME-OFFSET within your EXT-X-START tag.

            Enter a signed floating point value which, if positive, must be less than the configured manifest duration minus three times the configured segment target duration. If negative, the absolute value must be larger than three times the configured segment target duration, and the absolute value must be smaller than the configured manifest duration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-starttag.html#cfn-mediapackagev2-originendpoint-starttag-timeoffset
            '''
            result = self._values.get("time_offset")
            assert result is not None, "Required property 'time_offset' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def precise(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specify the value for PRECISE within your EXT-X-START tag.

            Leave blank, or choose false, to use the default value NO. Choose yes to use the value YES.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-starttag.html#cfn-mediapackagev2-originendpoint-starttag-precise
            '''
            result = self._values.get("precise")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StartTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnOriginEndpointPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpointPolicy",
):
    '''Specifies the configuration parameters of a policy associated with a MediaPackage V2 origin endpoint.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpointpolicy.html
    :cloudformationResource: AWS::MediaPackageV2::OriginEndpointPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediapackagev2 as mediapackagev2
        
        # policy: Any
        
        cfn_origin_endpoint_policy = mediapackagev2.CfnOriginEndpointPolicy(self, "MyCfnOriginEndpointPolicy",
            channel_group_name="channelGroupName",
            channel_name="channelName",
            origin_endpoint_name="originEndpointName",
            policy=policy,
        
            # the properties below are optional
            cdn_auth_configuration=mediapackagev2.CfnOriginEndpointPolicy.CdnAuthConfigurationProperty(
                cdn_identifier_secret_arns=["cdnIdentifierSecretArns"],
                secrets_role_arn="secretsRoleArn"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        channel_group_name: builtins.str,
        channel_name: builtins.str,
        origin_endpoint_name: builtins.str,
        policy: typing.Any,
        cdn_auth_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpointPolicy.CdnAuthConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param channel_group_name: The name of the channel group associated with the origin endpoint policy.
        :param channel_name: The channel name associated with the origin endpoint policy.
        :param origin_endpoint_name: The name of the origin endpoint associated with the origin endpoint policy.
        :param policy: The policy associated with the origin endpoint.
        :param cdn_auth_configuration: The settings to enable CDN authorization headers in MediaPackage.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aac7ba5cbcac1c12933a477adf316805431ea433d0ce36ca80901377b6745377)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOriginEndpointPolicyProps(
            channel_group_name=channel_group_name,
            channel_name=channel_name,
            origin_endpoint_name=origin_endpoint_name,
            policy=policy,
            cdn_auth_configuration=cdn_auth_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74da85e5d1f694f56bc39f3c1d3745b511f779f8f4ad4d052b2b985b19780fcd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9132218ebec80b439a7e6308166a5da9778046634a6a905cd5b91648837863cc)
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
    @jsii.member(jsii_name="channelGroupName")
    def channel_group_name(self) -> builtins.str:
        '''The name of the channel group associated with the origin endpoint policy.'''
        return typing.cast(builtins.str, jsii.get(self, "channelGroupName"))

    @channel_group_name.setter
    def channel_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ece6fe1f3215cf8ea357ac0ae337fd3ee216bd554b13e1ed66f380a551871cf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelGroupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="channelName")
    def channel_name(self) -> builtins.str:
        '''The channel name associated with the origin endpoint policy.'''
        return typing.cast(builtins.str, jsii.get(self, "channelName"))

    @channel_name.setter
    def channel_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__061507a42f38505f6e3060097229ce610dd50d3f6f96ac0cdbd883d1e13cad8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="originEndpointName")
    def origin_endpoint_name(self) -> builtins.str:
        '''The name of the origin endpoint associated with the origin endpoint policy.'''
        return typing.cast(builtins.str, jsii.get(self, "originEndpointName"))

    @origin_endpoint_name.setter
    def origin_endpoint_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a22e35010e441892b8eae01173c80ff68e7e2c1da6f52737a724971f5555743)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originEndpointName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Any:
        '''The policy associated with the origin endpoint.'''
        return typing.cast(typing.Any, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03b8094def1eae0770367451a814cb41dcad8e59ef89ff30e7423278b23af07b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cdnAuthConfiguration")
    def cdn_auth_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpointPolicy.CdnAuthConfigurationProperty"]]:
        '''The settings to enable CDN authorization headers in MediaPackage.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpointPolicy.CdnAuthConfigurationProperty"]], jsii.get(self, "cdnAuthConfiguration"))

    @cdn_auth_configuration.setter
    def cdn_auth_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpointPolicy.CdnAuthConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb5c350a2cc1621e0ea6d63c230deab544127f834aa0418f2d3ec475c6dfc3d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdnAuthConfiguration", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpointPolicy.CdnAuthConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cdn_identifier_secret_arns": "cdnIdentifierSecretArns",
            "secrets_role_arn": "secretsRoleArn",
        },
    )
    class CdnAuthConfigurationProperty:
        def __init__(
            self,
            *,
            cdn_identifier_secret_arns: typing.Sequence[builtins.str],
            secrets_role_arn: builtins.str,
        ) -> None:
            '''The settings to enable CDN authorization headers in MediaPackage.

            :param cdn_identifier_secret_arns: The ARN for the secret in Secrets Manager that your CDN uses for authorization to access the endpoint.
            :param secrets_role_arn: The ARN for the IAM role that gives MediaPackage read access to Secrets Manager and AWS KMS for CDN authorization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpointpolicy-cdnauthconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackagev2 as mediapackagev2
                
                cdn_auth_configuration_property = mediapackagev2.CfnOriginEndpointPolicy.CdnAuthConfigurationProperty(
                    cdn_identifier_secret_arns=["cdnIdentifierSecretArns"],
                    secrets_role_arn="secretsRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2efc99cbc23753feeba6e611700f7b275a0d9dbb8667ffa3a69bd76404c7768b)
                check_type(argname="argument cdn_identifier_secret_arns", value=cdn_identifier_secret_arns, expected_type=type_hints["cdn_identifier_secret_arns"])
                check_type(argname="argument secrets_role_arn", value=secrets_role_arn, expected_type=type_hints["secrets_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cdn_identifier_secret_arns": cdn_identifier_secret_arns,
                "secrets_role_arn": secrets_role_arn,
            }

        @builtins.property
        def cdn_identifier_secret_arns(self) -> typing.List[builtins.str]:
            '''The ARN for the secret in Secrets Manager that your CDN uses for authorization to access the endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpointpolicy-cdnauthconfiguration.html#cfn-mediapackagev2-originendpointpolicy-cdnauthconfiguration-cdnidentifiersecretarns
            '''
            result = self._values.get("cdn_identifier_secret_arns")
            assert result is not None, "Required property 'cdn_identifier_secret_arns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def secrets_role_arn(self) -> builtins.str:
            '''The ARN for the IAM role that gives MediaPackage read access to Secrets Manager and AWS KMS for CDN authorization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpointpolicy-cdnauthconfiguration.html#cfn-mediapackagev2-originendpointpolicy-cdnauthconfiguration-secretsrolearn
            '''
            result = self._values.get("secrets_role_arn")
            assert result is not None, "Required property 'secrets_role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CdnAuthConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpointPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_group_name": "channelGroupName",
        "channel_name": "channelName",
        "origin_endpoint_name": "originEndpointName",
        "policy": "policy",
        "cdn_auth_configuration": "cdnAuthConfiguration",
    },
)
class CfnOriginEndpointPolicyProps:
    def __init__(
        self,
        *,
        channel_group_name: builtins.str,
        channel_name: builtins.str,
        origin_endpoint_name: builtins.str,
        policy: typing.Any,
        cdn_auth_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpointPolicy.CdnAuthConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOriginEndpointPolicy``.

        :param channel_group_name: The name of the channel group associated with the origin endpoint policy.
        :param channel_name: The channel name associated with the origin endpoint policy.
        :param origin_endpoint_name: The name of the origin endpoint associated with the origin endpoint policy.
        :param policy: The policy associated with the origin endpoint.
        :param cdn_auth_configuration: The settings to enable CDN authorization headers in MediaPackage.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpointpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediapackagev2 as mediapackagev2
            
            # policy: Any
            
            cfn_origin_endpoint_policy_props = mediapackagev2.CfnOriginEndpointPolicyProps(
                channel_group_name="channelGroupName",
                channel_name="channelName",
                origin_endpoint_name="originEndpointName",
                policy=policy,
            
                # the properties below are optional
                cdn_auth_configuration=mediapackagev2.CfnOriginEndpointPolicy.CdnAuthConfigurationProperty(
                    cdn_identifier_secret_arns=["cdnIdentifierSecretArns"],
                    secrets_role_arn="secretsRoleArn"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f894be53e4aa1a8dbf54a25d139b2ffb41422bce69404dd7f536c4f418ceaa35)
            check_type(argname="argument channel_group_name", value=channel_group_name, expected_type=type_hints["channel_group_name"])
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            check_type(argname="argument origin_endpoint_name", value=origin_endpoint_name, expected_type=type_hints["origin_endpoint_name"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument cdn_auth_configuration", value=cdn_auth_configuration, expected_type=type_hints["cdn_auth_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
            "origin_endpoint_name": origin_endpoint_name,
            "policy": policy,
        }
        if cdn_auth_configuration is not None:
            self._values["cdn_auth_configuration"] = cdn_auth_configuration

    @builtins.property
    def channel_group_name(self) -> builtins.str:
        '''The name of the channel group associated with the origin endpoint policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpointpolicy.html#cfn-mediapackagev2-originendpointpolicy-channelgroupname
        '''
        result = self._values.get("channel_group_name")
        assert result is not None, "Required property 'channel_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_name(self) -> builtins.str:
        '''The channel name associated with the origin endpoint policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpointpolicy.html#cfn-mediapackagev2-originendpointpolicy-channelname
        '''
        result = self._values.get("channel_name")
        assert result is not None, "Required property 'channel_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def origin_endpoint_name(self) -> builtins.str:
        '''The name of the origin endpoint associated with the origin endpoint policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpointpolicy.html#cfn-mediapackagev2-originendpointpolicy-originendpointname
        '''
        result = self._values.get("origin_endpoint_name")
        assert result is not None, "Required property 'origin_endpoint_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy(self) -> typing.Any:
        '''The policy associated with the origin endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpointpolicy.html#cfn-mediapackagev2-originendpointpolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def cdn_auth_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpointPolicy.CdnAuthConfigurationProperty]]:
        '''The settings to enable CDN authorization headers in MediaPackage.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpointpolicy.html#cfn-mediapackagev2-originendpointpolicy-cdnauthconfiguration
        '''
        result = self._values.get("cdn_auth_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpointPolicy.CdnAuthConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOriginEndpointPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediapackagev2.CfnOriginEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_group_name": "channelGroupName",
        "channel_name": "channelName",
        "container_type": "containerType",
        "origin_endpoint_name": "originEndpointName",
        "dash_manifests": "dashManifests",
        "description": "description",
        "force_endpoint_error_configuration": "forceEndpointErrorConfiguration",
        "hls_manifests": "hlsManifests",
        "low_latency_hls_manifests": "lowLatencyHlsManifests",
        "segment": "segment",
        "startover_window_seconds": "startoverWindowSeconds",
        "tags": "tags",
    },
)
class CfnOriginEndpointProps:
    def __init__(
        self,
        *,
        channel_group_name: builtins.str,
        channel_name: builtins.str,
        container_type: builtins.str,
        origin_endpoint_name: builtins.str,
        dash_manifests: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.DashManifestConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        force_endpoint_error_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.ForceEndpointErrorConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        hls_manifests: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.HlsManifestConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        low_latency_hls_manifests: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.LowLatencyHlsManifestConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        segment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.SegmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        startover_window_seconds: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOriginEndpoint``.

        :param channel_group_name: The name of the channel group associated with the origin endpoint configuration.
        :param channel_name: The channel name associated with the origin endpoint.
        :param container_type: The container type associated with the origin endpoint configuration.
        :param origin_endpoint_name: The name of the origin endpoint associated with the origin endpoint configuration.
        :param dash_manifests: A DASH manifest configuration.
        :param description: The description associated with the origin endpoint.
        :param force_endpoint_error_configuration: The failover settings for the endpoint.
        :param hls_manifests: The HLS manifests associated with the origin endpoint configuration.
        :param low_latency_hls_manifests: The low-latency HLS (LL-HLS) manifests associated with the origin endpoint.
        :param segment: The segment associated with the origin endpoint.
        :param startover_window_seconds: The size of the window (in seconds) to specify a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window.
        :param tags: The tags associated with the origin endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediapackagev2 as mediapackagev2
            
            cfn_origin_endpoint_props = mediapackagev2.CfnOriginEndpointProps(
                channel_group_name="channelGroupName",
                channel_name="channelName",
                container_type="containerType",
                origin_endpoint_name="originEndpointName",
            
                # the properties below are optional
                dash_manifests=[mediapackagev2.CfnOriginEndpoint.DashManifestConfigurationProperty(
                    manifest_name="manifestName",
            
                    # the properties below are optional
                    base_urls=[mediapackagev2.CfnOriginEndpoint.DashBaseUrlProperty(
                        url="url",
            
                        # the properties below are optional
                        dvb_priority=123,
                        dvb_weight=123,
                        service_location="serviceLocation"
                    )],
                    compactness="compactness",
                    drm_signaling="drmSignaling",
                    dvb_settings=mediapackagev2.CfnOriginEndpoint.DashDvbSettingsProperty(
                        error_metrics=[mediapackagev2.CfnOriginEndpoint.DashDvbMetricsReportingProperty(
                            reporting_url="reportingUrl",
            
                            # the properties below are optional
                            probability=123
                        )],
                        font_download=mediapackagev2.CfnOriginEndpoint.DashDvbFontDownloadProperty(
                            font_family="fontFamily",
                            mime_type="mimeType",
                            url="url"
                        )
                    ),
                    filter_configuration=mediapackagev2.CfnOriginEndpoint.FilterConfigurationProperty(
                        clip_start_time="clipStartTime",
                        end="end",
                        manifest_filter="manifestFilter",
                        start="start",
                        time_delay_seconds=123
                    ),
                    manifest_window_seconds=123,
                    min_buffer_time_seconds=123,
                    min_update_period_seconds=123,
                    period_triggers=["periodTriggers"],
                    profiles=["profiles"],
                    program_information=mediapackagev2.CfnOriginEndpoint.DashProgramInformationProperty(
                        copyright="copyright",
                        language_code="languageCode",
                        more_information_url="moreInformationUrl",
                        source="source",
                        title="title"
                    ),
                    scte_dash=mediapackagev2.CfnOriginEndpoint.ScteDashProperty(
                        ad_marker_dash="adMarkerDash"
                    ),
                    segment_template_format="segmentTemplateFormat",
                    subtitle_configuration=mediapackagev2.CfnOriginEndpoint.DashSubtitleConfigurationProperty(
                        ttml_configuration=mediapackagev2.CfnOriginEndpoint.DashTtmlConfigurationProperty(
                            ttml_profile="ttmlProfile"
                        )
                    ),
                    suggested_presentation_delay_seconds=123,
                    utc_timing=mediapackagev2.CfnOriginEndpoint.DashUtcTimingProperty(
                        timing_mode="timingMode",
                        timing_source="timingSource"
                    )
                )],
                description="description",
                force_endpoint_error_configuration=mediapackagev2.CfnOriginEndpoint.ForceEndpointErrorConfigurationProperty(
                    endpoint_error_conditions=["endpointErrorConditions"]
                ),
                hls_manifests=[mediapackagev2.CfnOriginEndpoint.HlsManifestConfigurationProperty(
                    manifest_name="manifestName",
            
                    # the properties below are optional
                    child_manifest_name="childManifestName",
                    filter_configuration=mediapackagev2.CfnOriginEndpoint.FilterConfigurationProperty(
                        clip_start_time="clipStartTime",
                        end="end",
                        manifest_filter="manifestFilter",
                        start="start",
                        time_delay_seconds=123
                    ),
                    manifest_window_seconds=123,
                    program_date_time_interval_seconds=123,
                    scte_hls=mediapackagev2.CfnOriginEndpoint.ScteHlsProperty(
                        ad_marker_hls="adMarkerHls"
                    ),
                    start_tag=mediapackagev2.CfnOriginEndpoint.StartTagProperty(
                        time_offset=123,
            
                        # the properties below are optional
                        precise=False
                    ),
                    url="url",
                    url_encode_child_manifest=False
                )],
                low_latency_hls_manifests=[mediapackagev2.CfnOriginEndpoint.LowLatencyHlsManifestConfigurationProperty(
                    manifest_name="manifestName",
            
                    # the properties below are optional
                    child_manifest_name="childManifestName",
                    filter_configuration=mediapackagev2.CfnOriginEndpoint.FilterConfigurationProperty(
                        clip_start_time="clipStartTime",
                        end="end",
                        manifest_filter="manifestFilter",
                        start="start",
                        time_delay_seconds=123
                    ),
                    manifest_window_seconds=123,
                    program_date_time_interval_seconds=123,
                    scte_hls=mediapackagev2.CfnOriginEndpoint.ScteHlsProperty(
                        ad_marker_hls="adMarkerHls"
                    ),
                    start_tag=mediapackagev2.CfnOriginEndpoint.StartTagProperty(
                        time_offset=123,
            
                        # the properties below are optional
                        precise=False
                    ),
                    url="url",
                    url_encode_child_manifest=False
                )],
                segment=mediapackagev2.CfnOriginEndpoint.SegmentProperty(
                    encryption=mediapackagev2.CfnOriginEndpoint.EncryptionProperty(
                        encryption_method=mediapackagev2.CfnOriginEndpoint.EncryptionMethodProperty(
                            cmaf_encryption_method="cmafEncryptionMethod",
                            ts_encryption_method="tsEncryptionMethod"
                        ),
                        speke_key_provider=mediapackagev2.CfnOriginEndpoint.SpekeKeyProviderProperty(
                            drm_systems=["drmSystems"],
                            encryption_contract_configuration=mediapackagev2.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            ),
                            resource_id="resourceId",
                            role_arn="roleArn",
                            url="url"
                        ),
            
                        # the properties below are optional
                        cmaf_exclude_segment_drm_metadata=False,
                        constant_initialization_vector="constantInitializationVector",
                        key_rotation_interval_seconds=123
                    ),
                    include_iframe_only_streams=False,
                    scte=mediapackagev2.CfnOriginEndpoint.ScteProperty(
                        scte_filter=["scteFilter"]
                    ),
                    segment_duration_seconds=123,
                    segment_name="segmentName",
                    ts_include_dvb_subtitles=False,
                    ts_use_audio_rendition_group=False
                ),
                startover_window_seconds=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d261c9ffb32b381ea679962b9a614498343af1f15dd4bdfdbf788de765f62402)
            check_type(argname="argument channel_group_name", value=channel_group_name, expected_type=type_hints["channel_group_name"])
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            check_type(argname="argument container_type", value=container_type, expected_type=type_hints["container_type"])
            check_type(argname="argument origin_endpoint_name", value=origin_endpoint_name, expected_type=type_hints["origin_endpoint_name"])
            check_type(argname="argument dash_manifests", value=dash_manifests, expected_type=type_hints["dash_manifests"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument force_endpoint_error_configuration", value=force_endpoint_error_configuration, expected_type=type_hints["force_endpoint_error_configuration"])
            check_type(argname="argument hls_manifests", value=hls_manifests, expected_type=type_hints["hls_manifests"])
            check_type(argname="argument low_latency_hls_manifests", value=low_latency_hls_manifests, expected_type=type_hints["low_latency_hls_manifests"])
            check_type(argname="argument segment", value=segment, expected_type=type_hints["segment"])
            check_type(argname="argument startover_window_seconds", value=startover_window_seconds, expected_type=type_hints["startover_window_seconds"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
            "container_type": container_type,
            "origin_endpoint_name": origin_endpoint_name,
        }
        if dash_manifests is not None:
            self._values["dash_manifests"] = dash_manifests
        if description is not None:
            self._values["description"] = description
        if force_endpoint_error_configuration is not None:
            self._values["force_endpoint_error_configuration"] = force_endpoint_error_configuration
        if hls_manifests is not None:
            self._values["hls_manifests"] = hls_manifests
        if low_latency_hls_manifests is not None:
            self._values["low_latency_hls_manifests"] = low_latency_hls_manifests
        if segment is not None:
            self._values["segment"] = segment
        if startover_window_seconds is not None:
            self._values["startover_window_seconds"] = startover_window_seconds
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def channel_group_name(self) -> builtins.str:
        '''The name of the channel group associated with the origin endpoint configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-channelgroupname
        '''
        result = self._values.get("channel_group_name")
        assert result is not None, "Required property 'channel_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_name(self) -> builtins.str:
        '''The channel name associated with the origin endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-channelname
        '''
        result = self._values.get("channel_name")
        assert result is not None, "Required property 'channel_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_type(self) -> builtins.str:
        '''The container type associated with the origin endpoint configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-containertype
        '''
        result = self._values.get("container_type")
        assert result is not None, "Required property 'container_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def origin_endpoint_name(self) -> builtins.str:
        '''The name of the origin endpoint associated with the origin endpoint configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-originendpointname
        '''
        result = self._values.get("origin_endpoint_name")
        assert result is not None, "Required property 'origin_endpoint_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dash_manifests(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.DashManifestConfigurationProperty]]]]:
        '''A DASH manifest configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-dashmanifests
        '''
        result = self._values.get("dash_manifests")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.DashManifestConfigurationProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description associated with the origin endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_endpoint_error_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.ForceEndpointErrorConfigurationProperty]]:
        '''The failover settings for the endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-forceendpointerrorconfiguration
        '''
        result = self._values.get("force_endpoint_error_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.ForceEndpointErrorConfigurationProperty]], result)

    @builtins.property
    def hls_manifests(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.HlsManifestConfigurationProperty]]]]:
        '''The HLS manifests associated with the origin endpoint configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-hlsmanifests
        '''
        result = self._values.get("hls_manifests")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.HlsManifestConfigurationProperty]]]], result)

    @builtins.property
    def low_latency_hls_manifests(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.LowLatencyHlsManifestConfigurationProperty]]]]:
        '''The low-latency HLS (LL-HLS) manifests associated with the origin endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifests
        '''
        result = self._values.get("low_latency_hls_manifests")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.LowLatencyHlsManifestConfigurationProperty]]]], result)

    @builtins.property
    def segment(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.SegmentProperty]]:
        '''The segment associated with the origin endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-segment
        '''
        result = self._values.get("segment")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.SegmentProperty]], result)

    @builtins.property
    def startover_window_seconds(self) -> typing.Optional[jsii.Number]:
        '''The size of the window (in seconds) to specify a window of the live stream that's available for on-demand viewing.

        Viewers can start-over or catch-up on content that falls within the window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-startoverwindowseconds
        '''
        result = self._values.get("startover_window_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags associated with the origin endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOriginEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnChannel",
    "CfnChannelGroup",
    "CfnChannelGroupProps",
    "CfnChannelPolicy",
    "CfnChannelPolicyProps",
    "CfnChannelProps",
    "CfnOriginEndpoint",
    "CfnOriginEndpointPolicy",
    "CfnOriginEndpointPolicyProps",
    "CfnOriginEndpointProps",
]

publication.publish()

def _typecheckingstub__f5f12d43fb05232f03795c27e5dde1f408f5762e93edacb27e01efb9e0e3c7c1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    channel_group_name: builtins.str,
    channel_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    input_switch_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.InputSwitchConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    input_type: typing.Optional[builtins.str] = None,
    output_header_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.OutputHeaderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e420705ca6e035f67df6dc549d10387c546517b6ba6c086e3e8a2aa9d31185d9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__151c82108a0a47810b493e5e882a8c1cee0d53d834da01c686f370947109f4b2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9226145b09f87b401f2f5e357dafd5cd14b0b6a288f53bb6f985030a67a2ac8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1e91bde8ef4635665f6fef9c2cf22478a1d6e8a29ee675d883277fd4eb950f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee07183524d44b124938ad354f47b29384e1ea3a14ba4e7fa739d6847d2cdf12(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3390ae8163479dfdbac5df53086ecff4210fbf97553d12d70faac0b628fe5c00(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.InputSwitchConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fd45bf182a4bcd922fc7964817a4166c9d667e78eb548b915896743cf024664(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cd874b506cfe4b7e50b6cfa6b36888413d69d5ce0a7f4649d690587ed70c417(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.OutputHeaderConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61a8d14ccc4954881d5a995d8d9c088f4870a4a3a28d0b44314514a2fbb02a01(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52a72049adc4af63f65ccfb6f3c098cecb2b442bbe00bad4a877f2099a4bea86(
    *,
    id: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__116c8177c767f1c1239016dd387671ce140ac29b5e59b8e19832080acf68bef5(
    *,
    mqcs_input_switching: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    preferred_input: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__173b31e2a58ec560b57e45f11a2ad4c62727971f6e225559d90b8cf278b9f4f8(
    *,
    publish_mqcs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d830ced0539d40633bba571496a990f327b96c8fb475a589dba800d21ebab93(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    channel_group_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85339d527078ada2373603756ae52ddf1f0419ece647a7ea7d90b5a88cd80494(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15b97c97551c59b98a88e9243bce42e0880ba6021ce928c5162f4d188e32c3d0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab608f9f2545c6bf246db306be81d4790f5052ef181c364ada9dfba9527799b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7398d92754f71ac10dc5aea2094dad8322025c79ae1302b6a69e6216e4e16144(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07fbb1a31d1fae7c89e591bbcc359f5dc55386649647301df2f2e0b4e9727f81(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c53e8c32bcc3339086fcebea2b9a32198690f58e488775d546eac1d98ce6635e(
    *,
    channel_group_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3bd3df241e2da49b066856cd5205c086667bdeae2c7accc2fb87dc6c27afcca(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    channel_group_name: builtins.str,
    channel_name: builtins.str,
    policy: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__876e67bc0ac491acabfef846d2cb0a4a12c7db69dc9b8510736610ce77094825(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__428a901c1d832a1ec31a5a15117cbe43d42edeb32192ef35e21682ad7114f777(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb6da332e5cbe78bc72a7af1de80f930372aa6490fa2d573b540c4b4050a16b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffc77e98d707d0206432d1f5669baff83936b87558c5f6b3966d25c6d2682bcb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f9e54d124a239f2e45623971b96e9da027d679f90368ed2a8e63d67a707784f(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b390a62609d42c685f94c0572af995fa58a878e57dc79822886178cfbe0a33f(
    *,
    channel_group_name: builtins.str,
    channel_name: builtins.str,
    policy: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb84231dfbf08cdefe6ca207d49155a084aa492947c635c5e9ba404f1b3b987f(
    *,
    channel_group_name: builtins.str,
    channel_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    input_switch_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.InputSwitchConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    input_type: typing.Optional[builtins.str] = None,
    output_header_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.OutputHeaderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dba3dfc2892c78e53aee7675a7a24aa25c0b29481aca92446e31a0d8e885454(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    channel_group_name: builtins.str,
    channel_name: builtins.str,
    container_type: builtins.str,
    origin_endpoint_name: builtins.str,
    dash_manifests: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.DashManifestConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    force_endpoint_error_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.ForceEndpointErrorConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hls_manifests: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.HlsManifestConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    low_latency_hls_manifests: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.LowLatencyHlsManifestConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    segment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.SegmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    startover_window_seconds: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e7f9bba2cb8ce16d2850e4d29968cd8a850c920cb1e5d66b966cd309dd0e90f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bffcdef090bba09d673a36358d5eb3ba86b040c5c727f2f4cc117a5fab72df6f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7078125edd1beb221f7e3a35a200ce058d31cb41756eb7b1dca1af5dfe90c96f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__300d202906247d29b698e05c2891ad6a3e8f72748a5cb046f44ee1cde390954a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ded0ec9a4a78b0a13f4013526976d3ef27bae8928fb665d57679f95325a85b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b645ac54fdc447a14891e1f23268d3a802e1d51ab06333dab9a1ae79ae88fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__316fdfa36cde837c49bfecdf48716a30e11db3879a7276c8207beeff9aff9317(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.DashManifestConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d2dcbe74f178ed4fd2315de3210f8a81e6084e3e73f7337556d68a41cc54333(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bd0bc6ee367a0d016a630be9b91f1bbb3565f44feb4d59db2010dbadda4a8a7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.ForceEndpointErrorConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de310c90fc64be46bd788fedd55681eba63f450cc4f6537fe91890137af54019(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.HlsManifestConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ab0da83ecaf5e8b2eb477e1a7bb2f955c99813829faeb44ce46e408a3739304(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.LowLatencyHlsManifestConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__761931cab894d0c1a04fe9fe8aad0785de043e26b7f476c427bb231ae9fc1eeb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.SegmentProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__285ecfef5a8ec9ebb3f1c4d2193922e98318f11cce543c9b9c4221cfee42fc11(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65cc25545f38d01b8ccc61c9494f0994747ef22d12fc3c94c71cb091aff2f324(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be1d880fe401caed5e0186c4f4a6b76f8d63f2e78cf2fcbb490b66d185d4af29(
    *,
    url: builtins.str,
    dvb_priority: typing.Optional[jsii.Number] = None,
    dvb_weight: typing.Optional[jsii.Number] = None,
    service_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81c2694b55243cfd80ec8b5b8d807b1d991f3ae38973b41f6fb77d9d5ea24965(
    *,
    font_family: typing.Optional[builtins.str] = None,
    mime_type: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fadf127f9f82d1f5f09e73b8a4d72d5685c1236b84cdaa5c6132a7ab4774e495(
    *,
    reporting_url: builtins.str,
    probability: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__280a149dc1f481cd4b69b2b250e75d424c71bee34e699369b2294841b0aed7d8(
    *,
    error_metrics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.DashDvbMetricsReportingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    font_download: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.DashDvbFontDownloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20e3bfad4ae40517c778173bab356d7bd208497ee33a09fdc9e380135384dfc6(
    *,
    manifest_name: builtins.str,
    base_urls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.DashBaseUrlProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    compactness: typing.Optional[builtins.str] = None,
    drm_signaling: typing.Optional[builtins.str] = None,
    dvb_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.DashDvbSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    filter_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.FilterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    manifest_window_seconds: typing.Optional[jsii.Number] = None,
    min_buffer_time_seconds: typing.Optional[jsii.Number] = None,
    min_update_period_seconds: typing.Optional[jsii.Number] = None,
    period_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
    profiles: typing.Optional[typing.Sequence[builtins.str]] = None,
    program_information: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.DashProgramInformationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scte_dash: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.ScteDashProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    segment_template_format: typing.Optional[builtins.str] = None,
    subtitle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.DashSubtitleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    suggested_presentation_delay_seconds: typing.Optional[jsii.Number] = None,
    utc_timing: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.DashUtcTimingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b0c2b5b70e24041767a172f1ebbd9317cd4ce50194b747d40b0c075a554bb92(
    *,
    copyright: typing.Optional[builtins.str] = None,
    language_code: typing.Optional[builtins.str] = None,
    more_information_url: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa51912df0060cf290274ace134d0cb16e34e1de7ea689b411eeae296d9a8155(
    *,
    ttml_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.DashTtmlConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bba187ab72699f6dc21195cb98838c8f292af76576ca0254079260c1346c116d(
    *,
    ttml_profile: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09bad37e3e4d3382385a9f8aab252d146616b680c49d6ef16671c82ef1248794(
    *,
    timing_mode: typing.Optional[builtins.str] = None,
    timing_source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bec1eea406d4bb796486d5773d483a771df06a4cb391f44e1755e98877b7f22(
    *,
    preset_speke20_audio: builtins.str,
    preset_speke20_video: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abdd735051ce598919313a259e3efc1aa635283b073d78fb9c4e876eef4ca8b8(
    *,
    cmaf_encryption_method: typing.Optional[builtins.str] = None,
    ts_encryption_method: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba68bba2e5edd62f12d66393f036d9e0dc8f60c4705d328714b3a2f959ba4a07(
    *,
    encryption_method: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.EncryptionMethodProperty, typing.Dict[builtins.str, typing.Any]]],
    speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.SpekeKeyProviderProperty, typing.Dict[builtins.str, typing.Any]]],
    cmaf_exclude_segment_drm_metadata: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    constant_initialization_vector: typing.Optional[builtins.str] = None,
    key_rotation_interval_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd4523035a4ce6e5ff7d759a2d3d8f5fc12e2c0c96ad04c9ef1b884c6334f16c(
    *,
    clip_start_time: typing.Optional[builtins.str] = None,
    end: typing.Optional[builtins.str] = None,
    manifest_filter: typing.Optional[builtins.str] = None,
    start: typing.Optional[builtins.str] = None,
    time_delay_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c775185d7f0f530d0727569d624c7700267dcbd432d6270153826a314b2e766e(
    *,
    endpoint_error_conditions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b59520e6fbce62f410265deeb9cc043e1cf408c2c3cc498907eb73fcc18458d8(
    *,
    manifest_name: builtins.str,
    child_manifest_name: typing.Optional[builtins.str] = None,
    filter_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.FilterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    manifest_window_seconds: typing.Optional[jsii.Number] = None,
    program_date_time_interval_seconds: typing.Optional[jsii.Number] = None,
    scte_hls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.ScteHlsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    start_tag: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.StartTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    url: typing.Optional[builtins.str] = None,
    url_encode_child_manifest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ba3db62514b88b8da1b21ec0b9459116f857508c0670adb698a120b326fed5e(
    *,
    manifest_name: builtins.str,
    child_manifest_name: typing.Optional[builtins.str] = None,
    filter_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.FilterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    manifest_window_seconds: typing.Optional[jsii.Number] = None,
    program_date_time_interval_seconds: typing.Optional[jsii.Number] = None,
    scte_hls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.ScteHlsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    start_tag: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.StartTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    url: typing.Optional[builtins.str] = None,
    url_encode_child_manifest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13ac94f52ccc71367f414c5388529d309fac2b39d9caa3e0e662dc2cfae97455(
    *,
    ad_marker_dash: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d4f889b0a331f5c9a9819d549afcb4b4239d6f7040f9146668998df9485e7ea(
    *,
    ad_marker_hls: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef2f402f6bd5f38be28bfd79b40a3e8bf701cd6b9384547f9b36a386a6075a98(
    *,
    scte_filter: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99efb585c0a363a79f96102145e602f3f91887f61fac7a746b16b243ae503d48(
    *,
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    include_iframe_only_streams: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    scte: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.ScteProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    segment_duration_seconds: typing.Optional[jsii.Number] = None,
    segment_name: typing.Optional[builtins.str] = None,
    ts_include_dvb_subtitles: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ts_use_audio_rendition_group: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4c003b5dabc0ccf6e42c45fb4504036521870f7799525c5b18f42c7c618d131(
    *,
    drm_systems: typing.Sequence[builtins.str],
    encryption_contract_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.EncryptionContractConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    resource_id: builtins.str,
    role_arn: builtins.str,
    url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__638acac01659df889e5cbdebcde00e01e52315bf2fdb140c76d10ea5a120c30a(
    *,
    time_offset: jsii.Number,
    precise: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aac7ba5cbcac1c12933a477adf316805431ea433d0ce36ca80901377b6745377(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    channel_group_name: builtins.str,
    channel_name: builtins.str,
    origin_endpoint_name: builtins.str,
    policy: typing.Any,
    cdn_auth_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpointPolicy.CdnAuthConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74da85e5d1f694f56bc39f3c1d3745b511f779f8f4ad4d052b2b985b19780fcd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9132218ebec80b439a7e6308166a5da9778046634a6a905cd5b91648837863cc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ece6fe1f3215cf8ea357ac0ae337fd3ee216bd554b13e1ed66f380a551871cf8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__061507a42f38505f6e3060097229ce610dd50d3f6f96ac0cdbd883d1e13cad8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a22e35010e441892b8eae01173c80ff68e7e2c1da6f52737a724971f5555743(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03b8094def1eae0770367451a814cb41dcad8e59ef89ff30e7423278b23af07b(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb5c350a2cc1621e0ea6d63c230deab544127f834aa0418f2d3ec475c6dfc3d3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpointPolicy.CdnAuthConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2efc99cbc23753feeba6e611700f7b275a0d9dbb8667ffa3a69bd76404c7768b(
    *,
    cdn_identifier_secret_arns: typing.Sequence[builtins.str],
    secrets_role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f894be53e4aa1a8dbf54a25d139b2ffb41422bce69404dd7f536c4f418ceaa35(
    *,
    channel_group_name: builtins.str,
    channel_name: builtins.str,
    origin_endpoint_name: builtins.str,
    policy: typing.Any,
    cdn_auth_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpointPolicy.CdnAuthConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d261c9ffb32b381ea679962b9a614498343af1f15dd4bdfdbf788de765f62402(
    *,
    channel_group_name: builtins.str,
    channel_name: builtins.str,
    container_type: builtins.str,
    origin_endpoint_name: builtins.str,
    dash_manifests: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.DashManifestConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    force_endpoint_error_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.ForceEndpointErrorConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hls_manifests: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.HlsManifestConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    low_latency_hls_manifests: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.LowLatencyHlsManifestConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    segment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.SegmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    startover_window_seconds: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
