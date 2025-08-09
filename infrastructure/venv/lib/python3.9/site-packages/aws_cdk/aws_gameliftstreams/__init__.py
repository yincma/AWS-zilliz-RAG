r'''
# AWS::GameLiftStreams Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_gameliftstreams as gameliftstreams
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for GameLiftStreams construct libraries](https://constructs.dev/search?q=gameliftstreams)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::GameLiftStreams resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GameLiftStreams.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::GameLiftStreams](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GameLiftStreams.html).

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
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gameliftstreams.CfnApplication",
):
    '''The ``AWS::GameLiftStreams::Application`` resource defines an Amazon GameLift Streams application.

    An application specifies the content that you want to stream, such as a game or other software, and its runtime environment (Microsoft Windows, Ubuntu, or Proton).

    Before you create an Amazon GameLift Streams application, upload your *uncompressed* game files to an Amazon Simple Storage Service (Amazon S3) bucket.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gameliftstreams-application.html
    :cloudformationResource: AWS::GameLiftStreams::Application
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gameliftstreams as gameliftstreams
        
        cfn_application = gameliftstreams.CfnApplication(self, "MyCfnApplication",
            application_source_uri="applicationSourceUri",
            description="description",
            executable_path="executablePath",
            runtime_environment=gameliftstreams.CfnApplication.RuntimeEnvironmentProperty(
                type="type",
                version="version"
            ),
        
            # the properties below are optional
            application_log_output_uri="applicationLogOutputUri",
            application_log_paths=["applicationLogPaths"],
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
        application_source_uri: builtins.str,
        description: builtins.str,
        executable_path: builtins.str,
        runtime_environment: typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.RuntimeEnvironmentProperty", typing.Dict[builtins.str, typing.Any]]],
        application_log_output_uri: typing.Optional[builtins.str] = None,
        application_log_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_source_uri: The location of the content that you want to stream. Enter an Amazon S3 URI to a bucket that contains your game or other application. The location can have a multi-level prefix structure, but it must include all the files needed to run the content. Amazon GameLift Streams copies everything under the specified location. This value is immutable. To designate a different content location, create a new application. .. epigraph:: The Amazon S3 bucket and the Amazon GameLift Streams application must be in the same AWS Region.
        :param description: A human-readable label for the application. You can update this value later.
        :param executable_path: The path and file name of the executable file that launches the content for streaming. Enter a path value that is relative to the location set in ``ApplicationSourceUri`` .
        :param runtime_environment: A set of configuration settings to run the application on a stream group. This configures the operating system, and can include compatibility layers and other drivers.
        :param application_log_output_uri: An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more ``ApplicationLogPaths`` .
        :param application_log_paths: Locations of log files that your content generates during a stream session. Enter path values that are relative to the ``ApplicationSourceUri`` location. You can specify up to 10 log paths. Amazon GameLift Streams uploads designated log files to the Amazon S3 bucket that you specify in ``ApplicationLogOutputUri`` at the end of a stream session. To retrieve stored log files, call `GetStreamSession <https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html>`_ and get the ``LogFileLocationUri`` .
        :param tags: A list of labels to assign to the new application resource. Tags are developer-defined key-value pairs. Tagging AWS resources is useful for resource management, access management and cost allocation. See `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98acfa7b89cf716a7d04ae3a442e9ce27afcc5fb822ef47ddf9f1d824dffcb57)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            application_source_uri=application_source_uri,
            description=description,
            executable_path=executable_path,
            runtime_environment=runtime_environment,
            application_log_output_uri=application_log_output_uri,
            application_log_paths=application_log_paths,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d76bc5828ad9405857a447dd5e09d353f094e8dace57a54f0cf310c8491cdf2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__50c31bcf353c2c84c0618a01ad12939bc1543325af7012c982b33b3805174c1c)
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
        '''An `Amazon Resource Name (ARN) <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html>`_ that uniquely identifies the application resource across all AWS Regions. For example:.

        ``arn:aws:gameliftstreams:us-west-2:123456789012:application/a-9ZY8X7Wv6`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''An ID that uniquely identifies the application resource.

        For example: ``a-9ZY8X7Wv6`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="applicationSourceUri")
    def application_source_uri(self) -> builtins.str:
        '''The location of the content that you want to stream.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationSourceUri"))

    @application_source_uri.setter
    def application_source_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1879374230d6341862d7d814f31258e5fa681d1bb031c6cda6c5b47607c67d17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationSourceUri", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''A human-readable label for the application.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8714b4b46e3aca8a02e428c362995e23942e3b680d88f693386d95f4351f36e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="executablePath")
    def executable_path(self) -> builtins.str:
        '''The path and file name of the executable file that launches the content for streaming.'''
        return typing.cast(builtins.str, jsii.get(self, "executablePath"))

    @executable_path.setter
    def executable_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31e9a9acdd861e63cdd99c001364a9e3ba706bbf503797c4fd9ac585c1f76a0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executablePath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="runtimeEnvironment")
    def runtime_environment(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnApplication.RuntimeEnvironmentProperty"]:
        '''A set of configuration settings to run the application on a stream group.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnApplication.RuntimeEnvironmentProperty"], jsii.get(self, "runtimeEnvironment"))

    @runtime_environment.setter
    def runtime_environment(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnApplication.RuntimeEnvironmentProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99f6582f76f3c6a11837e068e6e72ca864955b2789dca17c695fab2bad3ca516)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeEnvironment", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="applicationLogOutputUri")
    def application_log_output_uri(self) -> typing.Optional[builtins.str]:
        '''An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationLogOutputUri"))

    @application_log_output_uri.setter
    def application_log_output_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fd55d29c5f92dec6b4e922ca4c78d4fbe17f68d92c455f0fe391ec69b4687c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationLogOutputUri", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="applicationLogPaths")
    def application_log_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Locations of log files that your content generates during a stream session.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "applicationLogPaths"))

    @application_log_paths.setter
    def application_log_paths(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b132398da4b4570c9a85ae72bf79d405aa40a1c75f2961f628de9d9b1224e0eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationLogPaths", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of labels to assign to the new application resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7a1896b47cdd07eb41b16d50651877cd16a2b19eb7ee93b0abc4e48422f849f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gameliftstreams.CfnApplication.RuntimeEnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "version": "version"},
    )
    class RuntimeEnvironmentProperty:
        def __init__(self, *, type: builtins.str, version: builtins.str) -> None:
            '''Configuration settings that identify the operating system for an application resource.

            This can also include a compatibility layer and other drivers.

            A runtime environment can be one of the following:

            - For Linux applications
            - Ubuntu 22.04 LTS ( ``Type=UBUNTU, Version=22_04_LTS`` )
            - For Windows applications
            - Microsoft Windows Server 2022 Base ( ``Type=WINDOWS, Version=2022`` )
            - Proton 8.0-5 ( ``Type=PROTON, Version=20241007`` )
            - Proton 8.0-2c ( ``Type=PROTON, Version=20230704`` )

            :param type: The operating system and other drivers. For Proton, this also includes the Proton compatibility layer.
            :param version: Versioned container environment for the application operating system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gameliftstreams-application-runtimeenvironment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gameliftstreams as gameliftstreams
                
                runtime_environment_property = gameliftstreams.CfnApplication.RuntimeEnvironmentProperty(
                    type="type",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__36db25239f5829e6be78b8afc94eb689056b154e144d17ae679806f522900e44)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
                "version": version,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''The operating system and other drivers.

            For Proton, this also includes the Proton compatibility layer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gameliftstreams-application-runtimeenvironment.html#cfn-gameliftstreams-application-runtimeenvironment-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> builtins.str:
            '''Versioned container environment for the application operating system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gameliftstreams-application-runtimeenvironment.html#cfn-gameliftstreams-application-runtimeenvironment-version
            '''
            result = self._values.get("version")
            assert result is not None, "Required property 'version' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuntimeEnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gameliftstreams.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_source_uri": "applicationSourceUri",
        "description": "description",
        "executable_path": "executablePath",
        "runtime_environment": "runtimeEnvironment",
        "application_log_output_uri": "applicationLogOutputUri",
        "application_log_paths": "applicationLogPaths",
        "tags": "tags",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        application_source_uri: builtins.str,
        description: builtins.str,
        executable_path: builtins.str,
        runtime_environment: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.RuntimeEnvironmentProperty, typing.Dict[builtins.str, typing.Any]]],
        application_log_output_uri: typing.Optional[builtins.str] = None,
        application_log_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param application_source_uri: The location of the content that you want to stream. Enter an Amazon S3 URI to a bucket that contains your game or other application. The location can have a multi-level prefix structure, but it must include all the files needed to run the content. Amazon GameLift Streams copies everything under the specified location. This value is immutable. To designate a different content location, create a new application. .. epigraph:: The Amazon S3 bucket and the Amazon GameLift Streams application must be in the same AWS Region.
        :param description: A human-readable label for the application. You can update this value later.
        :param executable_path: The path and file name of the executable file that launches the content for streaming. Enter a path value that is relative to the location set in ``ApplicationSourceUri`` .
        :param runtime_environment: A set of configuration settings to run the application on a stream group. This configures the operating system, and can include compatibility layers and other drivers.
        :param application_log_output_uri: An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more ``ApplicationLogPaths`` .
        :param application_log_paths: Locations of log files that your content generates during a stream session. Enter path values that are relative to the ``ApplicationSourceUri`` location. You can specify up to 10 log paths. Amazon GameLift Streams uploads designated log files to the Amazon S3 bucket that you specify in ``ApplicationLogOutputUri`` at the end of a stream session. To retrieve stored log files, call `GetStreamSession <https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html>`_ and get the ``LogFileLocationUri`` .
        :param tags: A list of labels to assign to the new application resource. Tags are developer-defined key-value pairs. Tagging AWS resources is useful for resource management, access management and cost allocation. See `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gameliftstreams-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gameliftstreams as gameliftstreams
            
            cfn_application_props = gameliftstreams.CfnApplicationProps(
                application_source_uri="applicationSourceUri",
                description="description",
                executable_path="executablePath",
                runtime_environment=gameliftstreams.CfnApplication.RuntimeEnvironmentProperty(
                    type="type",
                    version="version"
                ),
            
                # the properties below are optional
                application_log_output_uri="applicationLogOutputUri",
                application_log_paths=["applicationLogPaths"],
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf559d648da5bcc6d426f2fa9d64617eba1c68df0cd94a3f9e4e8e5996e805e4)
            check_type(argname="argument application_source_uri", value=application_source_uri, expected_type=type_hints["application_source_uri"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument executable_path", value=executable_path, expected_type=type_hints["executable_path"])
            check_type(argname="argument runtime_environment", value=runtime_environment, expected_type=type_hints["runtime_environment"])
            check_type(argname="argument application_log_output_uri", value=application_log_output_uri, expected_type=type_hints["application_log_output_uri"])
            check_type(argname="argument application_log_paths", value=application_log_paths, expected_type=type_hints["application_log_paths"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_source_uri": application_source_uri,
            "description": description,
            "executable_path": executable_path,
            "runtime_environment": runtime_environment,
        }
        if application_log_output_uri is not None:
            self._values["application_log_output_uri"] = application_log_output_uri
        if application_log_paths is not None:
            self._values["application_log_paths"] = application_log_paths
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def application_source_uri(self) -> builtins.str:
        '''The location of the content that you want to stream.

        Enter an Amazon S3 URI to a bucket that contains your game or other application. The location can have a multi-level prefix structure, but it must include all the files needed to run the content. Amazon GameLift Streams copies everything under the specified location.

        This value is immutable. To designate a different content location, create a new application.
        .. epigraph::

           The Amazon S3 bucket and the Amazon GameLift Streams application must be in the same AWS Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gameliftstreams-application.html#cfn-gameliftstreams-application-applicationsourceuri
        '''
        result = self._values.get("application_source_uri")
        assert result is not None, "Required property 'application_source_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> builtins.str:
        '''A human-readable label for the application.

        You can update this value later.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gameliftstreams-application.html#cfn-gameliftstreams-application-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def executable_path(self) -> builtins.str:
        '''The path and file name of the executable file that launches the content for streaming.

        Enter a path value that is relative to the location set in ``ApplicationSourceUri`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gameliftstreams-application.html#cfn-gameliftstreams-application-executablepath
        '''
        result = self._values.get("executable_path")
        assert result is not None, "Required property 'executable_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runtime_environment(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnApplication.RuntimeEnvironmentProperty]:
        '''A set of configuration settings to run the application on a stream group.

        This configures the operating system, and can include compatibility layers and other drivers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gameliftstreams-application.html#cfn-gameliftstreams-application-runtimeenvironment
        '''
        result = self._values.get("runtime_environment")
        assert result is not None, "Required property 'runtime_environment' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnApplication.RuntimeEnvironmentProperty], result)

    @builtins.property
    def application_log_output_uri(self) -> typing.Optional[builtins.str]:
        '''An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs.

        Required if you specify one or more ``ApplicationLogPaths`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gameliftstreams-application.html#cfn-gameliftstreams-application-applicationlogoutputuri
        '''
        result = self._values.get("application_log_output_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_log_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Locations of log files that your content generates during a stream session.

        Enter path values that are relative to the ``ApplicationSourceUri`` location. You can specify up to 10 log paths. Amazon GameLift Streams uploads designated log files to the Amazon S3 bucket that you specify in ``ApplicationLogOutputUri`` at the end of a stream session. To retrieve stored log files, call `GetStreamSession <https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html>`_ and get the ``LogFileLocationUri`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gameliftstreams-application.html#cfn-gameliftstreams-application-applicationlogpaths
        '''
        result = self._values.get("application_log_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of labels to assign to the new application resource.

        Tags are developer-defined key-value pairs. Tagging AWS resources is useful for resource management, access management and cost allocation. See `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gameliftstreams-application.html#cfn-gameliftstreams-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnStreamGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gameliftstreams.CfnStreamGroup",
):
    '''The ``AWS::GameLiftStreams::StreamGroup`` resource defines a group of compute resources that will be running and streaming your game.

    When you create a stream group, you specify the hardware configuration (CPU, GPU, RAM) that will run your game (known as the *stream class* ), the geographical locations where your game can run, and the number of streams that can run simultaneously in each location (known as *stream capacity* ). Stream groups manage how Amazon GameLift Streams allocates resources and handles concurrent streams, allowing you to effectively manage capacity and costs.

    There are two types of stream capacity: always-on and on-demand.

    - *Always-on* : The streaming capacity that is allocated and ready to handle stream requests without delay. You pay for this capacity whether it's in use or not. Best for quickest time from streaming request to streaming session.
    - *On-demand* : The streaming capacity that Amazon GameLift Streams can allocate in response to stream requests, and then de-allocate when the session has terminated. This offers a cost control measure at the expense of a greater startup time (typically under 5 minutes).

    .. epigraph::

       Application association is not currently supported in AWS CloudFormation . To link additional applications to a stream group, use the Amazon GameLift Streams console or the AWS CLI .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gameliftstreams-streamgroup.html
    :cloudformationResource: AWS::GameLiftStreams::StreamGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gameliftstreams as gameliftstreams
        
        cfn_stream_group = gameliftstreams.CfnStreamGroup(self, "MyCfnStreamGroup",
            description="description",
            location_configurations=[gameliftstreams.CfnStreamGroup.LocationConfigurationProperty(
                location_name="locationName",
        
                # the properties below are optional
                always_on_capacity=123,
                on_demand_capacity=123
            )],
            stream_class="streamClass",
        
            # the properties below are optional
            default_application=gameliftstreams.CfnStreamGroup.DefaultApplicationProperty(
                arn="arn",
                id="id"
            ),
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
        description: builtins.str,
        location_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStreamGroup.LocationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        stream_class: builtins.str,
        default_application: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStreamGroup.DefaultApplicationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: A descriptive label for the stream group.
        :param location_configurations: A set of one or more locations and the streaming capacity for each location. One of the locations MUST be your primary location, which is the AWS Region where you are specifying this resource.
        :param stream_class: The target stream quality for sessions that are hosted in this stream group. Set a stream class that is appropriate to the type of content that you're streaming. Stream class determines the type of computing resources Amazon GameLift Streams uses and impacts the cost of streaming. The following options are available: A stream class can be one of the following: - *``gen5n_win2022`` (NVIDIA, ultra)* Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.4, 32 and 64-bit applications, and anti-cheat technology. Uses NVIDIA A10G Tensor GPU. - Reference resolution: 1080p - Reference frame rate: 60 fps - Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM - Tenancy: Supports 1 concurrent stream session - *``gen5n_high`` (NVIDIA, high)* Supports applications with moderate to high 3D scene complexity. Uses NVIDIA A10G Tensor GPU. - Reference resolution: 1080p - Reference frame rate: 60 fps - Workload specifications: 4 vCPUs, 16 GB RAM, 12 GB VRAM - Tenancy: Supports up to 2 concurrent stream sessions - *``gen5n_ultra`` (NVIDIA, ultra)* Supports applications with extremely high 3D scene complexity. Uses dedicated NVIDIA A10G Tensor GPU. - Reference resolution: 1080p - Reference frame rate: 60 fps - Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM - Tenancy: Supports 1 concurrent stream session - *``gen4n_win2022`` (NVIDIA, ultra)* Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.4, 32 and 64-bit applications, and anti-cheat technology. Uses NVIDIA T4 Tensor GPU. - Reference resolution: 1080p - Reference frame rate: 60 fps - Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM - Tenancy: Supports 1 concurrent stream session - *``gen4n_high`` (NVIDIA, high)* Supports applications with moderate to high 3D scene complexity. Uses NVIDIA T4 Tensor GPU. - Reference resolution: 1080p - Reference frame rate: 60 fps - Workload specifications: 4 vCPUs, 16 GB RAM, 8 GB VRAM - Tenancy: Supports up to 2 concurrent stream sessions - *``gen4n_ultra`` (NVIDIA, ultra)* Supports applications with high 3D scene complexity. Uses dedicated NVIDIA T4 Tensor GPU. - Reference resolution: 1080p - Reference frame rate: 60 fps - Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM - Tenancy: Supports 1 concurrent stream session
        :param default_application: Object that identifies the Amazon GameLift Streams application to stream with this stream group.
        :param tags: A list of labels to assign to the new stream group resource. Tags are developer-defined key-value pairs. Tagging AWS resources is useful for resource management, access management and cost allocation. See `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79f0f973b06de7ae1a48df1df69579c9c8dfd0885945a959686fdddf31cc2674)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStreamGroupProps(
            description=description,
            location_configurations=location_configurations,
            stream_class=stream_class,
            default_application=default_application,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb56536ce44817c859b61b163e409d7355fcd5587161451f9e349b151919e117)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e452216970f4fb3ed8f8671a8e3d85dc54c1eb595b151c7880df187fd3ffc5e1)
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
        '''An `Amazon Resource Name (ARN) <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html>`_ that uniquely identifies the stream group resource. For example: ``arn:aws:gameliftstreams:us-west-2:123456789012:streamgroup/sg-1AB2C3De4`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''An ID that uniquely identifies the stream group resource.

        For example: ``sg-1AB2C3De4`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''A descriptive label for the stream group.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be883277b66b56e75f860926d2ccdff02bbe3ad4484bdf975afaa283e57056d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="locationConfigurations")
    def location_configurations(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStreamGroup.LocationConfigurationProperty"]]]:
        '''A set of one or more locations and the streaming capacity for each location.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStreamGroup.LocationConfigurationProperty"]]], jsii.get(self, "locationConfigurations"))

    @location_configurations.setter
    def location_configurations(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStreamGroup.LocationConfigurationProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dce7069bc18c5adbe92459796919490fb80e38f9a3fe455b779e19b0b30da98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationConfigurations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="streamClass")
    def stream_class(self) -> builtins.str:
        '''The target stream quality for sessions that are hosted in this stream group.'''
        return typing.cast(builtins.str, jsii.get(self, "streamClass"))

    @stream_class.setter
    def stream_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__936ee9ce8407944010c50c15e2b4554c116b1f3d52c2407d116cc9635a8f1cef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamClass", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultApplication")
    def default_application(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamGroup.DefaultApplicationProperty"]]:
        '''Object that identifies the Amazon GameLift Streams application to stream with this stream group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamGroup.DefaultApplicationProperty"]], jsii.get(self, "defaultApplication"))

    @default_application.setter
    def default_application(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamGroup.DefaultApplicationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4aa4ce53af802ec6bb329423326bcefed0b20e44bbe786ff2d23e1de4a242ec9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultApplication", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of labels to assign to the new stream group resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__491f8e30ff0958f00c4865b688648d82e82269ac2cd26ab478fe4579914e9c64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gameliftstreams.CfnStreamGroup.DefaultApplicationProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "id": "id"},
    )
    class DefaultApplicationProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents the default Amazon GameLift Streams application that a stream group hosts.

            :param arn: An `Amazon Resource Name (ARN) <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html>`_ that uniquely identifies the application resource. Example ARN: ``arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`` .
            :param id: An ID that uniquely identifies the application resource. Example ID: ``a-9ZY8X7Wv6`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gameliftstreams-streamgroup-defaultapplication.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gameliftstreams as gameliftstreams
                
                default_application_property = gameliftstreams.CfnStreamGroup.DefaultApplicationProperty(
                    arn="arn",
                    id="id"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c9b2ab7b0a09f30591f6dfe285dd0f1f30dec2efec3678c3961dddd6549f7a49)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if id is not None:
                self._values["id"] = id

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''An `Amazon Resource Name (ARN) <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html>`_ that uniquely identifies the application resource. Example ARN: ``arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gameliftstreams-streamgroup-defaultapplication.html#cfn-gameliftstreams-streamgroup-defaultapplication-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''An ID that uniquely identifies the application resource.

            Example ID: ``a-9ZY8X7Wv6`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gameliftstreams-streamgroup-defaultapplication.html#cfn-gameliftstreams-streamgroup-defaultapplication-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefaultApplicationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gameliftstreams.CfnStreamGroup.LocationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "location_name": "locationName",
            "always_on_capacity": "alwaysOnCapacity",
            "on_demand_capacity": "onDemandCapacity",
        },
    )
    class LocationConfigurationProperty:
        def __init__(
            self,
            *,
            location_name: builtins.str,
            always_on_capacity: typing.Optional[jsii.Number] = None,
            on_demand_capacity: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configuration settings that define a stream group's stream capacity for a location.

            When configuring a location for the first time, you must specify a numeric value for at least one of the two capacity types.

            :param location_name: A location's name. For example, ``us-east-1`` . For a complete list of locations that Amazon GameLift Streams supports, refer to `Regions, quotas, and limitations <https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html>`_ in the *Amazon GameLift Streams Developer Guide* .
            :param always_on_capacity: The streaming capacity that is allocated and ready to handle stream requests without delay. You pay for this capacity whether it's in use or not. Best for quickest time from streaming request to streaming session.
            :param on_demand_capacity: The streaming capacity that Amazon GameLift Streams can allocate in response to stream requests, and then de-allocate when the session has terminated. This offers a cost control measure at the expense of a greater startup time (typically under 5 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gameliftstreams-streamgroup-locationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gameliftstreams as gameliftstreams
                
                location_configuration_property = gameliftstreams.CfnStreamGroup.LocationConfigurationProperty(
                    location_name="locationName",
                
                    # the properties below are optional
                    always_on_capacity=123,
                    on_demand_capacity=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4c32e96242e189f6a75d890a7316a655383684ce9337b4906f2e3b49bec9a86e)
                check_type(argname="argument location_name", value=location_name, expected_type=type_hints["location_name"])
                check_type(argname="argument always_on_capacity", value=always_on_capacity, expected_type=type_hints["always_on_capacity"])
                check_type(argname="argument on_demand_capacity", value=on_demand_capacity, expected_type=type_hints["on_demand_capacity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "location_name": location_name,
            }
            if always_on_capacity is not None:
                self._values["always_on_capacity"] = always_on_capacity
            if on_demand_capacity is not None:
                self._values["on_demand_capacity"] = on_demand_capacity

        @builtins.property
        def location_name(self) -> builtins.str:
            '''A location's name.

            For example, ``us-east-1`` . For a complete list of locations that Amazon GameLift Streams supports, refer to `Regions, quotas, and limitations <https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html>`_ in the *Amazon GameLift Streams Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gameliftstreams-streamgroup-locationconfiguration.html#cfn-gameliftstreams-streamgroup-locationconfiguration-locationname
            '''
            result = self._values.get("location_name")
            assert result is not None, "Required property 'location_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def always_on_capacity(self) -> typing.Optional[jsii.Number]:
            '''The streaming capacity that is allocated and ready to handle stream requests without delay.

            You pay for this capacity whether it's in use or not. Best for quickest time from streaming request to streaming session.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gameliftstreams-streamgroup-locationconfiguration.html#cfn-gameliftstreams-streamgroup-locationconfiguration-alwaysoncapacity
            '''
            result = self._values.get("always_on_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def on_demand_capacity(self) -> typing.Optional[jsii.Number]:
            '''The streaming capacity that Amazon GameLift Streams can allocate in response to stream requests, and then de-allocate when the session has terminated.

            This offers a cost control measure at the expense of a greater startup time (typically under 5 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gameliftstreams-streamgroup-locationconfiguration.html#cfn-gameliftstreams-streamgroup-locationconfiguration-ondemandcapacity
            '''
            result = self._values.get("on_demand_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gameliftstreams.CfnStreamGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "location_configurations": "locationConfigurations",
        "stream_class": "streamClass",
        "default_application": "defaultApplication",
        "tags": "tags",
    },
)
class CfnStreamGroupProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        location_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamGroup.LocationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
        stream_class: builtins.str,
        default_application: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamGroup.DefaultApplicationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStreamGroup``.

        :param description: A descriptive label for the stream group.
        :param location_configurations: A set of one or more locations and the streaming capacity for each location. One of the locations MUST be your primary location, which is the AWS Region where you are specifying this resource.
        :param stream_class: The target stream quality for sessions that are hosted in this stream group. Set a stream class that is appropriate to the type of content that you're streaming. Stream class determines the type of computing resources Amazon GameLift Streams uses and impacts the cost of streaming. The following options are available: A stream class can be one of the following: - *``gen5n_win2022`` (NVIDIA, ultra)* Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.4, 32 and 64-bit applications, and anti-cheat technology. Uses NVIDIA A10G Tensor GPU. - Reference resolution: 1080p - Reference frame rate: 60 fps - Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM - Tenancy: Supports 1 concurrent stream session - *``gen5n_high`` (NVIDIA, high)* Supports applications with moderate to high 3D scene complexity. Uses NVIDIA A10G Tensor GPU. - Reference resolution: 1080p - Reference frame rate: 60 fps - Workload specifications: 4 vCPUs, 16 GB RAM, 12 GB VRAM - Tenancy: Supports up to 2 concurrent stream sessions - *``gen5n_ultra`` (NVIDIA, ultra)* Supports applications with extremely high 3D scene complexity. Uses dedicated NVIDIA A10G Tensor GPU. - Reference resolution: 1080p - Reference frame rate: 60 fps - Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM - Tenancy: Supports 1 concurrent stream session - *``gen4n_win2022`` (NVIDIA, ultra)* Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.4, 32 and 64-bit applications, and anti-cheat technology. Uses NVIDIA T4 Tensor GPU. - Reference resolution: 1080p - Reference frame rate: 60 fps - Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM - Tenancy: Supports 1 concurrent stream session - *``gen4n_high`` (NVIDIA, high)* Supports applications with moderate to high 3D scene complexity. Uses NVIDIA T4 Tensor GPU. - Reference resolution: 1080p - Reference frame rate: 60 fps - Workload specifications: 4 vCPUs, 16 GB RAM, 8 GB VRAM - Tenancy: Supports up to 2 concurrent stream sessions - *``gen4n_ultra`` (NVIDIA, ultra)* Supports applications with high 3D scene complexity. Uses dedicated NVIDIA T4 Tensor GPU. - Reference resolution: 1080p - Reference frame rate: 60 fps - Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM - Tenancy: Supports 1 concurrent stream session
        :param default_application: Object that identifies the Amazon GameLift Streams application to stream with this stream group.
        :param tags: A list of labels to assign to the new stream group resource. Tags are developer-defined key-value pairs. Tagging AWS resources is useful for resource management, access management and cost allocation. See `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gameliftstreams-streamgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gameliftstreams as gameliftstreams
            
            cfn_stream_group_props = gameliftstreams.CfnStreamGroupProps(
                description="description",
                location_configurations=[gameliftstreams.CfnStreamGroup.LocationConfigurationProperty(
                    location_name="locationName",
            
                    # the properties below are optional
                    always_on_capacity=123,
                    on_demand_capacity=123
                )],
                stream_class="streamClass",
            
                # the properties below are optional
                default_application=gameliftstreams.CfnStreamGroup.DefaultApplicationProperty(
                    arn="arn",
                    id="id"
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2997124a9d44ddc8951fa0effc557b193f10cbfb4e3867a8a2d79ba217b9edc8)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument location_configurations", value=location_configurations, expected_type=type_hints["location_configurations"])
            check_type(argname="argument stream_class", value=stream_class, expected_type=type_hints["stream_class"])
            check_type(argname="argument default_application", value=default_application, expected_type=type_hints["default_application"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "location_configurations": location_configurations,
            "stream_class": stream_class,
        }
        if default_application is not None:
            self._values["default_application"] = default_application
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> builtins.str:
        '''A descriptive label for the stream group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gameliftstreams-streamgroup.html#cfn-gameliftstreams-streamgroup-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location_configurations(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStreamGroup.LocationConfigurationProperty]]]:
        '''A set of one or more locations and the streaming capacity for each location.

        One of the locations MUST be your primary location, which is the AWS Region where you are specifying this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gameliftstreams-streamgroup.html#cfn-gameliftstreams-streamgroup-locationconfigurations
        '''
        result = self._values.get("location_configurations")
        assert result is not None, "Required property 'location_configurations' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStreamGroup.LocationConfigurationProperty]]], result)

    @builtins.property
    def stream_class(self) -> builtins.str:
        '''The target stream quality for sessions that are hosted in this stream group.

        Set a stream class that is appropriate to the type of content that you're streaming. Stream class determines the type of computing resources Amazon GameLift Streams uses and impacts the cost of streaming. The following options are available:

        A stream class can be one of the following:

        - *``gen5n_win2022`` (NVIDIA, ultra)* Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.4, 32 and 64-bit applications, and anti-cheat technology. Uses NVIDIA A10G Tensor GPU.
        - Reference resolution: 1080p
        - Reference frame rate: 60 fps
        - Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM
        - Tenancy: Supports 1 concurrent stream session
        - *``gen5n_high`` (NVIDIA, high)* Supports applications with moderate to high 3D scene complexity. Uses NVIDIA A10G Tensor GPU.
        - Reference resolution: 1080p
        - Reference frame rate: 60 fps
        - Workload specifications: 4 vCPUs, 16 GB RAM, 12 GB VRAM
        - Tenancy: Supports up to 2 concurrent stream sessions
        - *``gen5n_ultra`` (NVIDIA, ultra)* Supports applications with extremely high 3D scene complexity. Uses dedicated NVIDIA A10G Tensor GPU.
        - Reference resolution: 1080p
        - Reference frame rate: 60 fps
        - Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM
        - Tenancy: Supports 1 concurrent stream session
        - *``gen4n_win2022`` (NVIDIA, ultra)* Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.4, 32 and 64-bit applications, and anti-cheat technology. Uses NVIDIA T4 Tensor GPU.
        - Reference resolution: 1080p
        - Reference frame rate: 60 fps
        - Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM
        - Tenancy: Supports 1 concurrent stream session
        - *``gen4n_high`` (NVIDIA, high)* Supports applications with moderate to high 3D scene complexity. Uses NVIDIA T4 Tensor GPU.
        - Reference resolution: 1080p
        - Reference frame rate: 60 fps
        - Workload specifications: 4 vCPUs, 16 GB RAM, 8 GB VRAM
        - Tenancy: Supports up to 2 concurrent stream sessions
        - *``gen4n_ultra`` (NVIDIA, ultra)* Supports applications with high 3D scene complexity. Uses dedicated NVIDIA T4 Tensor GPU.
        - Reference resolution: 1080p
        - Reference frame rate: 60 fps
        - Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM
        - Tenancy: Supports 1 concurrent stream session

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gameliftstreams-streamgroup.html#cfn-gameliftstreams-streamgroup-streamclass
        '''
        result = self._values.get("stream_class")
        assert result is not None, "Required property 'stream_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_application(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamGroup.DefaultApplicationProperty]]:
        '''Object that identifies the Amazon GameLift Streams application to stream with this stream group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gameliftstreams-streamgroup.html#cfn-gameliftstreams-streamgroup-defaultapplication
        '''
        result = self._values.get("default_application")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamGroup.DefaultApplicationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of labels to assign to the new stream group resource.

        Tags are developer-defined key-value pairs. Tagging AWS resources is useful for resource management, access management and cost allocation. See `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gameliftstreams-streamgroup.html#cfn-gameliftstreams-streamgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStreamGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
    "CfnStreamGroup",
    "CfnStreamGroupProps",
]

publication.publish()

def _typecheckingstub__98acfa7b89cf716a7d04ae3a442e9ce27afcc5fb822ef47ddf9f1d824dffcb57(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_source_uri: builtins.str,
    description: builtins.str,
    executable_path: builtins.str,
    runtime_environment: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.RuntimeEnvironmentProperty, typing.Dict[builtins.str, typing.Any]]],
    application_log_output_uri: typing.Optional[builtins.str] = None,
    application_log_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d76bc5828ad9405857a447dd5e09d353f094e8dace57a54f0cf310c8491cdf2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50c31bcf353c2c84c0618a01ad12939bc1543325af7012c982b33b3805174c1c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1879374230d6341862d7d814f31258e5fa681d1bb031c6cda6c5b47607c67d17(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8714b4b46e3aca8a02e428c362995e23942e3b680d88f693386d95f4351f36e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31e9a9acdd861e63cdd99c001364a9e3ba706bbf503797c4fd9ac585c1f76a0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99f6582f76f3c6a11837e068e6e72ca864955b2789dca17c695fab2bad3ca516(
    value: typing.Union[_IResolvable_da3f097b, CfnApplication.RuntimeEnvironmentProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fd55d29c5f92dec6b4e922ca4c78d4fbe17f68d92c455f0fe391ec69b4687c9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b132398da4b4570c9a85ae72bf79d405aa40a1c75f2961f628de9d9b1224e0eb(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7a1896b47cdd07eb41b16d50651877cd16a2b19eb7ee93b0abc4e48422f849f(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36db25239f5829e6be78b8afc94eb689056b154e144d17ae679806f522900e44(
    *,
    type: builtins.str,
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf559d648da5bcc6d426f2fa9d64617eba1c68df0cd94a3f9e4e8e5996e805e4(
    *,
    application_source_uri: builtins.str,
    description: builtins.str,
    executable_path: builtins.str,
    runtime_environment: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.RuntimeEnvironmentProperty, typing.Dict[builtins.str, typing.Any]]],
    application_log_output_uri: typing.Optional[builtins.str] = None,
    application_log_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79f0f973b06de7ae1a48df1df69579c9c8dfd0885945a959686fdddf31cc2674(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: builtins.str,
    location_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamGroup.LocationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    stream_class: builtins.str,
    default_application: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamGroup.DefaultApplicationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb56536ce44817c859b61b163e409d7355fcd5587161451f9e349b151919e117(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e452216970f4fb3ed8f8671a8e3d85dc54c1eb595b151c7880df187fd3ffc5e1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be883277b66b56e75f860926d2ccdff02bbe3ad4484bdf975afaa283e57056d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dce7069bc18c5adbe92459796919490fb80e38f9a3fe455b779e19b0b30da98(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStreamGroup.LocationConfigurationProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__936ee9ce8407944010c50c15e2b4554c116b1f3d52c2407d116cc9635a8f1cef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aa4ce53af802ec6bb329423326bcefed0b20e44bbe786ff2d23e1de4a242ec9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamGroup.DefaultApplicationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__491f8e30ff0958f00c4865b688648d82e82269ac2cd26ab478fe4579914e9c64(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9b2ab7b0a09f30591f6dfe285dd0f1f30dec2efec3678c3961dddd6549f7a49(
    *,
    arn: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c32e96242e189f6a75d890a7316a655383684ce9337b4906f2e3b49bec9a86e(
    *,
    location_name: builtins.str,
    always_on_capacity: typing.Optional[jsii.Number] = None,
    on_demand_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2997124a9d44ddc8951fa0effc557b193f10cbfb4e3867a8a2d79ba217b9edc8(
    *,
    description: builtins.str,
    location_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamGroup.LocationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    stream_class: builtins.str,
    default_application: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamGroup.DefaultApplicationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
