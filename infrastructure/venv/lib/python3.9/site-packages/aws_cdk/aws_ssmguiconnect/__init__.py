r'''
# AWS::SSMGuiConnect Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_ssmguiconnect as ssmguiconnect
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SSMGuiConnect construct libraries](https://constructs.dev/search?q=ssmguiconnect)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SSMGuiConnect resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSMGuiConnect.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SSMGuiConnect](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSMGuiConnect.html).

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
class CfnPreferences(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssmguiconnect.CfnPreferences",
):
    '''Specify new or changed connection recording preferences for your AWS Systems Manager GUI Connect connections.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmguiconnect-preferences.html
    :cloudformationResource: AWS::SSMGuiConnect::Preferences
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssmguiconnect as ssmguiconnect
        
        cfn_preferences = ssmguiconnect.CfnPreferences(self, "MyCfnPreferences",
            connection_recording_preferences=ssmguiconnect.CfnPreferences.ConnectionRecordingPreferencesProperty(
                kms_key_arn="kmsKeyArn",
                recording_destinations=ssmguiconnect.CfnPreferences.RecordingDestinationsProperty(
                    s3_buckets=[ssmguiconnect.CfnPreferences.S3BucketProperty(
                        bucket_name="bucketName",
                        bucket_owner="bucketOwner"
                    )]
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        connection_recording_preferences: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPreferences.ConnectionRecordingPreferencesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param connection_recording_preferences: The set of preferences used for recording RDP connections in the requesting AWS account and AWS Region . This includes details such as which S3 bucket recordings are stored in.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__045e31f70bcabcaa4437ed6c7e11fb8462233ba15c60675b143088abfe090752)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPreferencesProps(
            connection_recording_preferences=connection_recording_preferences
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59c7a3e2f3cdd2e9d3e4372020a482f624a989ea6d129be44dbf7f070aacda70)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3749ba458af11bbb5fb93542c69a8b02362071d74426f5a7f030e9ea0836efac)
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
        '''The primary identifier for the AWS CloudFormation resource.

        :cloudformationAttribute: AccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccountId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="connectionRecordingPreferences")
    def connection_recording_preferences(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPreferences.ConnectionRecordingPreferencesProperty"]]:
        '''The set of preferences used for recording RDP connections in the requesting AWS account and AWS Region .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPreferences.ConnectionRecordingPreferencesProperty"]], jsii.get(self, "connectionRecordingPreferences"))

    @connection_recording_preferences.setter
    def connection_recording_preferences(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPreferences.ConnectionRecordingPreferencesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c66582ef0ec82c9acb896e156d048eb1944403cdb814f8c249895be7c4d8043)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionRecordingPreferences", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmguiconnect.CfnPreferences.ConnectionRecordingPreferencesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kms_key_arn": "kmsKeyArn",
            "recording_destinations": "recordingDestinations",
        },
    )
    class ConnectionRecordingPreferencesProperty:
        def __init__(
            self,
            *,
            kms_key_arn: builtins.str,
            recording_destinations: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPreferences.RecordingDestinationsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The set of preferences used for recording RDP connections in the requesting AWS account and AWS Region .

            This includes details such as which S3 bucket recordings are stored in.

            :param kms_key_arn: The ARN of a AWS KMS key that is used to encrypt data while it is being processed by the service. This key must exist in the same AWS Region as the node you start an RDP connection to.
            :param recording_destinations: Determines where recordings of RDP connections are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-connectionrecordingpreferences.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmguiconnect as ssmguiconnect
                
                connection_recording_preferences_property = ssmguiconnect.CfnPreferences.ConnectionRecordingPreferencesProperty(
                    kms_key_arn="kmsKeyArn",
                    recording_destinations=ssmguiconnect.CfnPreferences.RecordingDestinationsProperty(
                        s3_buckets=[ssmguiconnect.CfnPreferences.S3BucketProperty(
                            bucket_name="bucketName",
                            bucket_owner="bucketOwner"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9f83b9fd07eaf3bda97494ddce8a45cd58dcb54692ec0360bf9d23845c3be5f1)
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
                check_type(argname="argument recording_destinations", value=recording_destinations, expected_type=type_hints["recording_destinations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "kms_key_arn": kms_key_arn,
                "recording_destinations": recording_destinations,
            }

        @builtins.property
        def kms_key_arn(self) -> builtins.str:
            '''The ARN of a AWS KMS key that is used to encrypt data while it is being processed by the service.

            This key must exist in the same AWS Region as the node you start an RDP connection to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-connectionrecordingpreferences.html#cfn-ssmguiconnect-preferences-connectionrecordingpreferences-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            assert result is not None, "Required property 'kms_key_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def recording_destinations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnPreferences.RecordingDestinationsProperty"]:
            '''Determines where recordings of RDP connections are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-connectionrecordingpreferences.html#cfn-ssmguiconnect-preferences-connectionrecordingpreferences-recordingdestinations
            '''
            result = self._values.get("recording_destinations")
            assert result is not None, "Required property 'recording_destinations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPreferences.RecordingDestinationsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectionRecordingPreferencesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmguiconnect.CfnPreferences.RecordingDestinationsProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_buckets": "s3Buckets"},
    )
    class RecordingDestinationsProperty:
        def __init__(
            self,
            *,
            s3_buckets: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPreferences.S3BucketProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Determines where recordings of RDP connections are stored.

            :param s3_buckets: The S3 bucket where RDP connection recordings are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-recordingdestinations.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmguiconnect as ssmguiconnect
                
                recording_destinations_property = ssmguiconnect.CfnPreferences.RecordingDestinationsProperty(
                    s3_buckets=[ssmguiconnect.CfnPreferences.S3BucketProperty(
                        bucket_name="bucketName",
                        bucket_owner="bucketOwner"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__21f97360ac6f836d446e4669043ec91e366abd4faef63955c501e70a94faac1b)
                check_type(argname="argument s3_buckets", value=s3_buckets, expected_type=type_hints["s3_buckets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_buckets": s3_buckets,
            }

        @builtins.property
        def s3_buckets(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPreferences.S3BucketProperty"]]]:
            '''The S3 bucket where RDP connection recordings are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-recordingdestinations.html#cfn-ssmguiconnect-preferences-recordingdestinations-s3buckets
            '''
            result = self._values.get("s3_buckets")
            assert result is not None, "Required property 's3_buckets' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPreferences.S3BucketProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordingDestinationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmguiconnect.CfnPreferences.S3BucketProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName", "bucket_owner": "bucketOwner"},
    )
    class S3BucketProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            bucket_owner: builtins.str,
        ) -> None:
            '''The S3 bucket where RDP connection recordings are stored.

            :param bucket_name: The name of the S3 bucket where RDP connection recordings are stored.
            :param bucket_owner: The AWS account number that owns the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-s3bucket.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmguiconnect as ssmguiconnect
                
                s3_bucket_property = ssmguiconnect.CfnPreferences.S3BucketProperty(
                    bucket_name="bucketName",
                    bucket_owner="bucketOwner"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3939ea87d6ea5ac56e97e4118631928a1de532647a270d9cb345a6e1e23ad144)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument bucket_owner", value=bucket_owner, expected_type=type_hints["bucket_owner"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
                "bucket_owner": bucket_owner,
            }

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The name of the S3 bucket where RDP connection recordings are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-s3bucket.html#cfn-ssmguiconnect-preferences-s3bucket-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_owner(self) -> builtins.str:
            '''The AWS account number that owns the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmguiconnect-preferences-s3bucket.html#cfn-ssmguiconnect-preferences-s3bucket-bucketowner
            '''
            result = self._values.get("bucket_owner")
            assert result is not None, "Required property 'bucket_owner' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3BucketProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssmguiconnect.CfnPreferencesProps",
    jsii_struct_bases=[],
    name_mapping={
        "connection_recording_preferences": "connectionRecordingPreferences",
    },
)
class CfnPreferencesProps:
    def __init__(
        self,
        *,
        connection_recording_preferences: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPreferences.ConnectionRecordingPreferencesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPreferences``.

        :param connection_recording_preferences: The set of preferences used for recording RDP connections in the requesting AWS account and AWS Region . This includes details such as which S3 bucket recordings are stored in.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmguiconnect-preferences.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssmguiconnect as ssmguiconnect
            
            cfn_preferences_props = ssmguiconnect.CfnPreferencesProps(
                connection_recording_preferences=ssmguiconnect.CfnPreferences.ConnectionRecordingPreferencesProperty(
                    kms_key_arn="kmsKeyArn",
                    recording_destinations=ssmguiconnect.CfnPreferences.RecordingDestinationsProperty(
                        s3_buckets=[ssmguiconnect.CfnPreferences.S3BucketProperty(
                            bucket_name="bucketName",
                            bucket_owner="bucketOwner"
                        )]
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98cae01e7635c618ff7b373fa87c04c806f9ee04274631cc3ad753469d5b8661)
            check_type(argname="argument connection_recording_preferences", value=connection_recording_preferences, expected_type=type_hints["connection_recording_preferences"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_recording_preferences is not None:
            self._values["connection_recording_preferences"] = connection_recording_preferences

    @builtins.property
    def connection_recording_preferences(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPreferences.ConnectionRecordingPreferencesProperty]]:
        '''The set of preferences used for recording RDP connections in the requesting AWS account and AWS Region .

        This includes details such as which S3 bucket recordings are stored in.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmguiconnect-preferences.html#cfn-ssmguiconnect-preferences-connectionrecordingpreferences
        '''
        result = self._values.get("connection_recording_preferences")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPreferences.ConnectionRecordingPreferencesProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPreferencesProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnPreferences",
    "CfnPreferencesProps",
]

publication.publish()

def _typecheckingstub__045e31f70bcabcaa4437ed6c7e11fb8462233ba15c60675b143088abfe090752(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    connection_recording_preferences: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPreferences.ConnectionRecordingPreferencesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59c7a3e2f3cdd2e9d3e4372020a482f624a989ea6d129be44dbf7f070aacda70(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3749ba458af11bbb5fb93542c69a8b02362071d74426f5a7f030e9ea0836efac(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c66582ef0ec82c9acb896e156d048eb1944403cdb814f8c249895be7c4d8043(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPreferences.ConnectionRecordingPreferencesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f83b9fd07eaf3bda97494ddce8a45cd58dcb54692ec0360bf9d23845c3be5f1(
    *,
    kms_key_arn: builtins.str,
    recording_destinations: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPreferences.RecordingDestinationsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21f97360ac6f836d446e4669043ec91e366abd4faef63955c501e70a94faac1b(
    *,
    s3_buckets: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPreferences.S3BucketProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3939ea87d6ea5ac56e97e4118631928a1de532647a270d9cb345a6e1e23ad144(
    *,
    bucket_name: builtins.str,
    bucket_owner: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98cae01e7635c618ff7b373fa87c04c806f9ee04274631cc3ad753469d5b8661(
    *,
    connection_recording_preferences: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPreferences.ConnectionRecordingPreferencesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
