r'''
# AWS::DataZone Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_datazone as datazone
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DataZone construct libraries](https://constructs.dev/search?q=datazone)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DataZone resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DataZone.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DataZone](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DataZone.html).

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


@jsii.implements(_IInspectable_c2943556)
class CfnConnection(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnConnection",
):
    '''In Amazon DataZone, a connection enables you to connect your resources (domains, projects, and environments) to external resources and services.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-connection.html
    :cloudformationResource: AWS::DataZone::Connection
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_connection = datazone.CfnConnection(self, "MyCfnConnection",
            domain_identifier="domainIdentifier",
            environment_identifier="environmentIdentifier",
            name="name",
        
            # the properties below are optional
            aws_location=datazone.CfnConnection.AwsLocationProperty(
                access_role="accessRole",
                aws_account_id="awsAccountId",
                aws_region="awsRegion",
                iam_connection_id="iamConnectionId"
            ),
            description="description",
            props=datazone.CfnConnection.ConnectionPropertiesInputProperty(
                athena_properties=datazone.CfnConnection.AthenaPropertiesInputProperty(
                    workgroup_name="workgroupName"
                ),
                glue_properties=datazone.CfnConnection.GluePropertiesInputProperty(
                    glue_connection_input=datazone.CfnConnection.GlueConnectionInputProperty(
                        athena_properties={
                            "athena_properties_key": "athenaProperties"
                        },
                        authentication_configuration=datazone.CfnConnection.AuthenticationConfigurationInputProperty(
                            authentication_type="authenticationType",
                            basic_authentication_credentials=datazone.CfnConnection.BasicAuthenticationCredentialsProperty(
                                password="password",
                                user_name="userName"
                            ),
                            custom_authentication_credentials={
                                "custom_authentication_credentials_key": "customAuthenticationCredentials"
                            },
                            kms_key_arn="kmsKeyArn",
                            o_auth2_properties=datazone.CfnConnection.OAuth2PropertiesProperty(
                                authorization_code_properties=datazone.CfnConnection.AuthorizationCodePropertiesProperty(
                                    authorization_code="authorizationCode",
                                    redirect_uri="redirectUri"
                                ),
                                o_auth2_client_application=datazone.CfnConnection.OAuth2ClientApplicationProperty(
                                    aws_managed_client_application_reference="awsManagedClientApplicationReference",
                                    user_managed_client_application_client_id="userManagedClientApplicationClientId"
                                ),
                                o_auth2_credentials=datazone.CfnConnection.GlueOAuth2CredentialsProperty(
                                    access_token="accessToken",
                                    jwt_token="jwtToken",
                                    refresh_token="refreshToken",
                                    user_managed_client_application_client_secret="userManagedClientApplicationClientSecret"
                                ),
                                o_auth2_grant_type="oAuth2GrantType",
                                token_url="tokenUrl",
                                token_url_parameters_map={
                                    "token_url_parameters_map_key": "tokenUrlParametersMap"
                                }
                            ),
                            secret_arn="secretArn"
                        ),
                        connection_properties={
                            "connection_properties_key": "connectionProperties"
                        },
                        connection_type="connectionType",
                        description="description",
                        match_criteria="matchCriteria",
                        name="name",
                        physical_connection_requirements=datazone.CfnConnection.PhysicalConnectionRequirementsProperty(
                            availability_zone="availabilityZone",
                            security_group_id_list=["securityGroupIdList"],
                            subnet_id="subnetId",
                            subnet_id_list=["subnetIdList"]
                        ),
                        python_properties={
                            "python_properties_key": "pythonProperties"
                        },
                        spark_properties={
                            "spark_properties_key": "sparkProperties"
                        },
                        validate_credentials=False,
                        validate_for_compute_environments=["validateForComputeEnvironments"]
                    )
                ),
                hyper_pod_properties=datazone.CfnConnection.HyperPodPropertiesInputProperty(
                    cluster_name="clusterName"
                ),
                iam_properties=datazone.CfnConnection.IamPropertiesInputProperty(
                    glue_lineage_sync_enabled=False
                ),
                redshift_properties=datazone.CfnConnection.RedshiftPropertiesInputProperty(
                    credentials=datazone.CfnConnection.RedshiftCredentialsProperty(
                        secret_arn="secretArn",
                        username_password=datazone.CfnConnection.UsernamePasswordProperty(
                            password="password",
                            username="username"
                        )
                    ),
                    database_name="databaseName",
                    host="host",
                    lineage_sync=datazone.CfnConnection.RedshiftLineageSyncConfigurationInputProperty(
                        enabled=False,
                        schedule=datazone.CfnConnection.LineageSyncScheduleProperty(
                            schedule="schedule"
                        )
                    ),
                    port=123,
                    storage=datazone.CfnConnection.RedshiftStoragePropertiesProperty(
                        cluster_name="clusterName",
                        workgroup_name="workgroupName"
                    )
                ),
                spark_emr_properties=datazone.CfnConnection.SparkEmrPropertiesInputProperty(
                    compute_arn="computeArn",
                    instance_profile_arn="instanceProfileArn",
                    java_virtual_env="javaVirtualEnv",
                    log_uri="logUri",
                    python_virtual_env="pythonVirtualEnv",
                    runtime_role="runtimeRole",
                    trusted_certificates_s3_uri="trustedCertificatesS3Uri"
                ),
                spark_glue_properties=datazone.CfnConnection.SparkGluePropertiesInputProperty(
                    additional_args=datazone.CfnConnection.SparkGlueArgsProperty(
                        connection="connection"
                    ),
                    glue_connection_name="glueConnectionName",
                    glue_version="glueVersion",
                    idle_timeout=123,
                    java_virtual_env="javaVirtualEnv",
                    number_of_workers=123,
                    python_virtual_env="pythonVirtualEnv",
                    worker_type="workerType"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_identifier: builtins.str,
        environment_identifier: builtins.str,
        name: builtins.str,
        aws_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.AwsLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        props: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.ConnectionPropertiesInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_identifier: The ID of the domain where the connection is created.
        :param environment_identifier: The ID of the environment where the connection is created.
        :param name: The name of the connection.
        :param aws_location: The location where the connection is created.
        :param description: Connection description.
        :param props: Connection props.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68db6ef5de752113ca6cf32190e1173ded9b82274379374d5e16834f4fed2680)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props_ = CfnConnectionProps(
            domain_identifier=domain_identifier,
            environment_identifier=environment_identifier,
            name=name,
            aws_location=aws_location,
            description=description,
            props=props,
        )

        jsii.create(self.__class__, self, [scope, id, props_])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__398c2006651598ffb80d8dc727165745adb2a6958c75f5926b613ba3177e9d64)
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
            type_hints = typing.get_type_hints(_typecheckingstub__136bd666b9e38ddb69494b10631ff5d0eaef6cf06229255303630179d477d90f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectionId")
    def attr_connection_id(self) -> builtins.str:
        '''The ID of the connection.

        :cloudformationAttribute: ConnectionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectionId"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The domain ID of the connection.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainUnitId")
    def attr_domain_unit_id(self) -> builtins.str:
        '''The domain unit ID of the connection.

        :cloudformationAttribute: DomainUnitId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainUnitId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentId")
    def attr_environment_id(self) -> builtins.str:
        '''The ID of the environment.

        :cloudformationAttribute: EnvironmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentUserRole")
    def attr_environment_user_role(self) -> builtins.str:
        '''The environment user role.

        :cloudformationAttribute: EnvironmentUserRole
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentUserRole"))

    @builtins.property
    @jsii.member(jsii_name="attrProjectId")
    def attr_project_id(self) -> builtins.str:
        '''The ID of the project.

        :cloudformationAttribute: ProjectId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectId"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''The type of the connection.

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The ID of the domain where the connection is created.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f8e028075d374db4fd60d67eeb1b9ec1a7ba6de37d2ff5159166ef7a5c1b36b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentIdentifier")
    def environment_identifier(self) -> builtins.str:
        '''The ID of the environment where the connection is created.'''
        return typing.cast(builtins.str, jsii.get(self, "environmentIdentifier"))

    @environment_identifier.setter
    def environment_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b4cbfbd3c4ab850b86dca1cc1c0182806c09d658dbbad4aeefac22ff57e747f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the connection.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d602657575f2a77c389ea4e89f4d92dbe2bb3c30e0ccfc811aff15e122a98d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="awsLocation")
    def aws_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.AwsLocationProperty"]]:
        '''The location where the connection is created.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.AwsLocationProperty"]], jsii.get(self, "awsLocation"))

    @aws_location.setter
    def aws_location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.AwsLocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e0849d8ebdd0fce1643c3904bce5fd806bb233f7ff27eddb627fac859586e5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsLocation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Connection description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab8e0823bbef4ec627d5b737de745882d73474d54729e96b788a912f2dfe521c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.ConnectionPropertiesInputProperty"]]:
        '''Connection props.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.ConnectionPropertiesInputProperty"]], jsii.get(self, "props"))

    @props.setter
    def props(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.ConnectionPropertiesInputProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17a641eb769944a69ded6b3f471012669d56d0ff95b65a8c7c137bc906851136)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "props", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.AthenaPropertiesInputProperty",
        jsii_struct_bases=[],
        name_mapping={"workgroup_name": "workgroupName"},
    )
    class AthenaPropertiesInputProperty:
        def __init__(self, *, workgroup_name: builtins.str) -> None:
            '''The Amazon Athena properties of a connection.

            :param workgroup_name: The Amazon Athena workgroup name of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-athenapropertiesinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                athena_properties_input_property = datazone.CfnConnection.AthenaPropertiesInputProperty(
                    workgroup_name="workgroupName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6dc6a593151a7d129b46176dfadfaef1e3447a0d3883bc7e17f19c97bc36e3b3)
                check_type(argname="argument workgroup_name", value=workgroup_name, expected_type=type_hints["workgroup_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "workgroup_name": workgroup_name,
            }

        @builtins.property
        def workgroup_name(self) -> builtins.str:
            '''The Amazon Athena workgroup name of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-athenapropertiesinput.html#cfn-datazone-connection-athenapropertiesinput-workgroupname
            '''
            result = self._values.get("workgroup_name")
            assert result is not None, "Required property 'workgroup_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AthenaPropertiesInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.AuthenticationConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_type": "authenticationType",
            "basic_authentication_credentials": "basicAuthenticationCredentials",
            "custom_authentication_credentials": "customAuthenticationCredentials",
            "kms_key_arn": "kmsKeyArn",
            "o_auth2_properties": "oAuth2Properties",
            "secret_arn": "secretArn",
        },
    )
    class AuthenticationConfigurationInputProperty:
        def __init__(
            self,
            *,
            authentication_type: typing.Optional[builtins.str] = None,
            basic_authentication_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.BasicAuthenticationCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            custom_authentication_credentials: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            kms_key_arn: typing.Optional[builtins.str] = None,
            o_auth2_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.OAuth2PropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            secret_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The authentication configuration of a connection.

            :param authentication_type: The authentication type of a connection.
            :param basic_authentication_credentials: The basic authentication credentials of a connection.
            :param custom_authentication_credentials: The custom authentication credentials of a connection.
            :param kms_key_arn: The KMS key ARN of a connection.
            :param o_auth2_properties: The oAuth2 properties of a connection.
            :param secret_arn: The secret ARN of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-authenticationconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                authentication_configuration_input_property = datazone.CfnConnection.AuthenticationConfigurationInputProperty(
                    authentication_type="authenticationType",
                    basic_authentication_credentials=datazone.CfnConnection.BasicAuthenticationCredentialsProperty(
                        password="password",
                        user_name="userName"
                    ),
                    custom_authentication_credentials={
                        "custom_authentication_credentials_key": "customAuthenticationCredentials"
                    },
                    kms_key_arn="kmsKeyArn",
                    o_auth2_properties=datazone.CfnConnection.OAuth2PropertiesProperty(
                        authorization_code_properties=datazone.CfnConnection.AuthorizationCodePropertiesProperty(
                            authorization_code="authorizationCode",
                            redirect_uri="redirectUri"
                        ),
                        o_auth2_client_application=datazone.CfnConnection.OAuth2ClientApplicationProperty(
                            aws_managed_client_application_reference="awsManagedClientApplicationReference",
                            user_managed_client_application_client_id="userManagedClientApplicationClientId"
                        ),
                        o_auth2_credentials=datazone.CfnConnection.GlueOAuth2CredentialsProperty(
                            access_token="accessToken",
                            jwt_token="jwtToken",
                            refresh_token="refreshToken",
                            user_managed_client_application_client_secret="userManagedClientApplicationClientSecret"
                        ),
                        o_auth2_grant_type="oAuth2GrantType",
                        token_url="tokenUrl",
                        token_url_parameters_map={
                            "token_url_parameters_map_key": "tokenUrlParametersMap"
                        }
                    ),
                    secret_arn="secretArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bede0f21a390e4991cddbe5e8b7fc491f05c5af9d778e5f1ecb4a57c9c7144e9)
                check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
                check_type(argname="argument basic_authentication_credentials", value=basic_authentication_credentials, expected_type=type_hints["basic_authentication_credentials"])
                check_type(argname="argument custom_authentication_credentials", value=custom_authentication_credentials, expected_type=type_hints["custom_authentication_credentials"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
                check_type(argname="argument o_auth2_properties", value=o_auth2_properties, expected_type=type_hints["o_auth2_properties"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if authentication_type is not None:
                self._values["authentication_type"] = authentication_type
            if basic_authentication_credentials is not None:
                self._values["basic_authentication_credentials"] = basic_authentication_credentials
            if custom_authentication_credentials is not None:
                self._values["custom_authentication_credentials"] = custom_authentication_credentials
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn
            if o_auth2_properties is not None:
                self._values["o_auth2_properties"] = o_auth2_properties
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn

        @builtins.property
        def authentication_type(self) -> typing.Optional[builtins.str]:
            '''The authentication type of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-authenticationconfigurationinput.html#cfn-datazone-connection-authenticationconfigurationinput-authenticationtype
            '''
            result = self._values.get("authentication_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def basic_authentication_credentials(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.BasicAuthenticationCredentialsProperty"]]:
            '''The basic authentication credentials of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-authenticationconfigurationinput.html#cfn-datazone-connection-authenticationconfigurationinput-basicauthenticationcredentials
            '''
            result = self._values.get("basic_authentication_credentials")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.BasicAuthenticationCredentialsProperty"]], result)

        @builtins.property
        def custom_authentication_credentials(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The custom authentication credentials of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-authenticationconfigurationinput.html#cfn-datazone-connection-authenticationconfigurationinput-customauthenticationcredentials
            '''
            result = self._values.get("custom_authentication_credentials")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The KMS key ARN of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-authenticationconfigurationinput.html#cfn-datazone-connection-authenticationconfigurationinput-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def o_auth2_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.OAuth2PropertiesProperty"]]:
            '''The oAuth2 properties of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-authenticationconfigurationinput.html#cfn-datazone-connection-authenticationconfigurationinput-oauth2properties
            '''
            result = self._values.get("o_auth2_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.OAuth2PropertiesProperty"]], result)

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            '''The secret ARN of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-authenticationconfigurationinput.html#cfn-datazone-connection-authenticationconfigurationinput-secretarn
            '''
            result = self._values.get("secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthenticationConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.AuthorizationCodePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorization_code": "authorizationCode",
            "redirect_uri": "redirectUri",
        },
    )
    class AuthorizationCodePropertiesProperty:
        def __init__(
            self,
            *,
            authorization_code: typing.Optional[builtins.str] = None,
            redirect_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The authorization code properties of a connection.

            :param authorization_code: The authorization code of a connection.
            :param redirect_uri: The redirect URI of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-authorizationcodeproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                authorization_code_properties_property = datazone.CfnConnection.AuthorizationCodePropertiesProperty(
                    authorization_code="authorizationCode",
                    redirect_uri="redirectUri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__709c9a9c016d2e06938c1c1ea54063ae38a4addfc19c769dff4d0e585d8c7527)
                check_type(argname="argument authorization_code", value=authorization_code, expected_type=type_hints["authorization_code"])
                check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if authorization_code is not None:
                self._values["authorization_code"] = authorization_code
            if redirect_uri is not None:
                self._values["redirect_uri"] = redirect_uri

        @builtins.property
        def authorization_code(self) -> typing.Optional[builtins.str]:
            '''The authorization code of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-authorizationcodeproperties.html#cfn-datazone-connection-authorizationcodeproperties-authorizationcode
            '''
            result = self._values.get("authorization_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def redirect_uri(self) -> typing.Optional[builtins.str]:
            '''The redirect URI of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-authorizationcodeproperties.html#cfn-datazone-connection-authorizationcodeproperties-redirecturi
            '''
            result = self._values.get("redirect_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizationCodePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.AwsLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_role": "accessRole",
            "aws_account_id": "awsAccountId",
            "aws_region": "awsRegion",
            "iam_connection_id": "iamConnectionId",
        },
    )
    class AwsLocationProperty:
        def __init__(
            self,
            *,
            access_role: typing.Optional[builtins.str] = None,
            aws_account_id: typing.Optional[builtins.str] = None,
            aws_region: typing.Optional[builtins.str] = None,
            iam_connection_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The location of a project.

            :param access_role: The access role of a connection.
            :param aws_account_id: The account ID of a connection.
            :param aws_region: The Region of a connection.
            :param iam_connection_id: The IAM connection ID of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-awslocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                aws_location_property = datazone.CfnConnection.AwsLocationProperty(
                    access_role="accessRole",
                    aws_account_id="awsAccountId",
                    aws_region="awsRegion",
                    iam_connection_id="iamConnectionId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__298e27e7bc1a0b15a9b79d0ebf0e4abe337d89521ddfa348fac1a78cdda506e7)
                check_type(argname="argument access_role", value=access_role, expected_type=type_hints["access_role"])
                check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
                check_type(argname="argument iam_connection_id", value=iam_connection_id, expected_type=type_hints["iam_connection_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if access_role is not None:
                self._values["access_role"] = access_role
            if aws_account_id is not None:
                self._values["aws_account_id"] = aws_account_id
            if aws_region is not None:
                self._values["aws_region"] = aws_region
            if iam_connection_id is not None:
                self._values["iam_connection_id"] = iam_connection_id

        @builtins.property
        def access_role(self) -> typing.Optional[builtins.str]:
            '''The access role of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-awslocation.html#cfn-datazone-connection-awslocation-accessrole
            '''
            result = self._values.get("access_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def aws_account_id(self) -> typing.Optional[builtins.str]:
            '''The account ID of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-awslocation.html#cfn-datazone-connection-awslocation-awsaccountid
            '''
            result = self._values.get("aws_account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def aws_region(self) -> typing.Optional[builtins.str]:
            '''The Region of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-awslocation.html#cfn-datazone-connection-awslocation-awsregion
            '''
            result = self._values.get("aws_region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def iam_connection_id(self) -> typing.Optional[builtins.str]:
            '''The IAM connection ID of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-awslocation.html#cfn-datazone-connection-awslocation-iamconnectionid
            '''
            result = self._values.get("iam_connection_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.BasicAuthenticationCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={"password": "password", "user_name": "userName"},
    )
    class BasicAuthenticationCredentialsProperty:
        def __init__(
            self,
            *,
            password: typing.Optional[builtins.str] = None,
            user_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The basic authentication credentials of a connection.

            :param password: The password for a connection.
            :param user_name: The user name for the connecion.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-basicauthenticationcredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                basic_authentication_credentials_property = datazone.CfnConnection.BasicAuthenticationCredentialsProperty(
                    password="password",
                    user_name="userName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7ee4cc1ea0ba5d5144e8b2c837d252087208460444755cfb7f5128e742a104c3)
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if password is not None:
                self._values["password"] = password
            if user_name is not None:
                self._values["user_name"] = user_name

        @builtins.property
        def password(self) -> typing.Optional[builtins.str]:
            '''The password for a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-basicauthenticationcredentials.html#cfn-datazone-connection-basicauthenticationcredentials-password
            '''
            result = self._values.get("password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_name(self) -> typing.Optional[builtins.str]:
            '''The user name for the connecion.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-basicauthenticationcredentials.html#cfn-datazone-connection-basicauthenticationcredentials-username
            '''
            result = self._values.get("user_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BasicAuthenticationCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.ConnectionPropertiesInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "athena_properties": "athenaProperties",
            "glue_properties": "glueProperties",
            "hyper_pod_properties": "hyperPodProperties",
            "iam_properties": "iamProperties",
            "redshift_properties": "redshiftProperties",
            "spark_emr_properties": "sparkEmrProperties",
            "spark_glue_properties": "sparkGlueProperties",
        },
    )
    class ConnectionPropertiesInputProperty:
        def __init__(
            self,
            *,
            athena_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.AthenaPropertiesInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            glue_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.GluePropertiesInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            hyper_pod_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.HyperPodPropertiesInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            iam_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.IamPropertiesInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            redshift_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.RedshiftPropertiesInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            spark_emr_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.SparkEmrPropertiesInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            spark_glue_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.SparkGluePropertiesInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The properties of a connection.

            :param athena_properties: The Amazon Athena properties of a connection.
            :param glue_properties: The AWS Glue properties of a connection.
            :param hyper_pod_properties: The hyper pod properties of a connection.
            :param iam_properties: The IAM properties of a connection.
            :param redshift_properties: The Amazon Redshift properties of a connection.
            :param spark_emr_properties: The Spark EMR properties of a connection.
            :param spark_glue_properties: The Spark AWS Glue properties of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-connectionpropertiesinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                connection_properties_input_property = datazone.CfnConnection.ConnectionPropertiesInputProperty(
                    athena_properties=datazone.CfnConnection.AthenaPropertiesInputProperty(
                        workgroup_name="workgroupName"
                    ),
                    glue_properties=datazone.CfnConnection.GluePropertiesInputProperty(
                        glue_connection_input=datazone.CfnConnection.GlueConnectionInputProperty(
                            athena_properties={
                                "athena_properties_key": "athenaProperties"
                            },
                            authentication_configuration=datazone.CfnConnection.AuthenticationConfigurationInputProperty(
                                authentication_type="authenticationType",
                                basic_authentication_credentials=datazone.CfnConnection.BasicAuthenticationCredentialsProperty(
                                    password="password",
                                    user_name="userName"
                                ),
                                custom_authentication_credentials={
                                    "custom_authentication_credentials_key": "customAuthenticationCredentials"
                                },
                                kms_key_arn="kmsKeyArn",
                                o_auth2_properties=datazone.CfnConnection.OAuth2PropertiesProperty(
                                    authorization_code_properties=datazone.CfnConnection.AuthorizationCodePropertiesProperty(
                                        authorization_code="authorizationCode",
                                        redirect_uri="redirectUri"
                                    ),
                                    o_auth2_client_application=datazone.CfnConnection.OAuth2ClientApplicationProperty(
                                        aws_managed_client_application_reference="awsManagedClientApplicationReference",
                                        user_managed_client_application_client_id="userManagedClientApplicationClientId"
                                    ),
                                    o_auth2_credentials=datazone.CfnConnection.GlueOAuth2CredentialsProperty(
                                        access_token="accessToken",
                                        jwt_token="jwtToken",
                                        refresh_token="refreshToken",
                                        user_managed_client_application_client_secret="userManagedClientApplicationClientSecret"
                                    ),
                                    o_auth2_grant_type="oAuth2GrantType",
                                    token_url="tokenUrl",
                                    token_url_parameters_map={
                                        "token_url_parameters_map_key": "tokenUrlParametersMap"
                                    }
                                ),
                                secret_arn="secretArn"
                            ),
                            connection_properties={
                                "connection_properties_key": "connectionProperties"
                            },
                            connection_type="connectionType",
                            description="description",
                            match_criteria="matchCriteria",
                            name="name",
                            physical_connection_requirements=datazone.CfnConnection.PhysicalConnectionRequirementsProperty(
                                availability_zone="availabilityZone",
                                security_group_id_list=["securityGroupIdList"],
                                subnet_id="subnetId",
                                subnet_id_list=["subnetIdList"]
                            ),
                            python_properties={
                                "python_properties_key": "pythonProperties"
                            },
                            spark_properties={
                                "spark_properties_key": "sparkProperties"
                            },
                            validate_credentials=False,
                            validate_for_compute_environments=["validateForComputeEnvironments"]
                        )
                    ),
                    hyper_pod_properties=datazone.CfnConnection.HyperPodPropertiesInputProperty(
                        cluster_name="clusterName"
                    ),
                    iam_properties=datazone.CfnConnection.IamPropertiesInputProperty(
                        glue_lineage_sync_enabled=False
                    ),
                    redshift_properties=datazone.CfnConnection.RedshiftPropertiesInputProperty(
                        credentials=datazone.CfnConnection.RedshiftCredentialsProperty(
                            secret_arn="secretArn",
                            username_password=datazone.CfnConnection.UsernamePasswordProperty(
                                password="password",
                                username="username"
                            )
                        ),
                        database_name="databaseName",
                        host="host",
                        lineage_sync=datazone.CfnConnection.RedshiftLineageSyncConfigurationInputProperty(
                            enabled=False,
                            schedule=datazone.CfnConnection.LineageSyncScheduleProperty(
                                schedule="schedule"
                            )
                        ),
                        port=123,
                        storage=datazone.CfnConnection.RedshiftStoragePropertiesProperty(
                            cluster_name="clusterName",
                            workgroup_name="workgroupName"
                        )
                    ),
                    spark_emr_properties=datazone.CfnConnection.SparkEmrPropertiesInputProperty(
                        compute_arn="computeArn",
                        instance_profile_arn="instanceProfileArn",
                        java_virtual_env="javaVirtualEnv",
                        log_uri="logUri",
                        python_virtual_env="pythonVirtualEnv",
                        runtime_role="runtimeRole",
                        trusted_certificates_s3_uri="trustedCertificatesS3Uri"
                    ),
                    spark_glue_properties=datazone.CfnConnection.SparkGluePropertiesInputProperty(
                        additional_args=datazone.CfnConnection.SparkGlueArgsProperty(
                            connection="connection"
                        ),
                        glue_connection_name="glueConnectionName",
                        glue_version="glueVersion",
                        idle_timeout=123,
                        java_virtual_env="javaVirtualEnv",
                        number_of_workers=123,
                        python_virtual_env="pythonVirtualEnv",
                        worker_type="workerType"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__afac89e500a9d5f348ce1c21e174ddef9825d543c744b00c3ff73a0c8dba8f38)
                check_type(argname="argument athena_properties", value=athena_properties, expected_type=type_hints["athena_properties"])
                check_type(argname="argument glue_properties", value=glue_properties, expected_type=type_hints["glue_properties"])
                check_type(argname="argument hyper_pod_properties", value=hyper_pod_properties, expected_type=type_hints["hyper_pod_properties"])
                check_type(argname="argument iam_properties", value=iam_properties, expected_type=type_hints["iam_properties"])
                check_type(argname="argument redshift_properties", value=redshift_properties, expected_type=type_hints["redshift_properties"])
                check_type(argname="argument spark_emr_properties", value=spark_emr_properties, expected_type=type_hints["spark_emr_properties"])
                check_type(argname="argument spark_glue_properties", value=spark_glue_properties, expected_type=type_hints["spark_glue_properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if athena_properties is not None:
                self._values["athena_properties"] = athena_properties
            if glue_properties is not None:
                self._values["glue_properties"] = glue_properties
            if hyper_pod_properties is not None:
                self._values["hyper_pod_properties"] = hyper_pod_properties
            if iam_properties is not None:
                self._values["iam_properties"] = iam_properties
            if redshift_properties is not None:
                self._values["redshift_properties"] = redshift_properties
            if spark_emr_properties is not None:
                self._values["spark_emr_properties"] = spark_emr_properties
            if spark_glue_properties is not None:
                self._values["spark_glue_properties"] = spark_glue_properties

        @builtins.property
        def athena_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.AthenaPropertiesInputProperty"]]:
            '''The Amazon Athena properties of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-connectionpropertiesinput.html#cfn-datazone-connection-connectionpropertiesinput-athenaproperties
            '''
            result = self._values.get("athena_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.AthenaPropertiesInputProperty"]], result)

        @builtins.property
        def glue_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.GluePropertiesInputProperty"]]:
            '''The AWS Glue properties of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-connectionpropertiesinput.html#cfn-datazone-connection-connectionpropertiesinput-glueproperties
            '''
            result = self._values.get("glue_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.GluePropertiesInputProperty"]], result)

        @builtins.property
        def hyper_pod_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.HyperPodPropertiesInputProperty"]]:
            '''The hyper pod properties of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-connectionpropertiesinput.html#cfn-datazone-connection-connectionpropertiesinput-hyperpodproperties
            '''
            result = self._values.get("hyper_pod_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.HyperPodPropertiesInputProperty"]], result)

        @builtins.property
        def iam_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.IamPropertiesInputProperty"]]:
            '''The IAM properties of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-connectionpropertiesinput.html#cfn-datazone-connection-connectionpropertiesinput-iamproperties
            '''
            result = self._values.get("iam_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.IamPropertiesInputProperty"]], result)

        @builtins.property
        def redshift_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.RedshiftPropertiesInputProperty"]]:
            '''The Amazon Redshift properties of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-connectionpropertiesinput.html#cfn-datazone-connection-connectionpropertiesinput-redshiftproperties
            '''
            result = self._values.get("redshift_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.RedshiftPropertiesInputProperty"]], result)

        @builtins.property
        def spark_emr_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.SparkEmrPropertiesInputProperty"]]:
            '''The Spark EMR properties of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-connectionpropertiesinput.html#cfn-datazone-connection-connectionpropertiesinput-sparkemrproperties
            '''
            result = self._values.get("spark_emr_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.SparkEmrPropertiesInputProperty"]], result)

        @builtins.property
        def spark_glue_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.SparkGluePropertiesInputProperty"]]:
            '''The Spark AWS Glue properties of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-connectionpropertiesinput.html#cfn-datazone-connection-connectionpropertiesinput-sparkglueproperties
            '''
            result = self._values.get("spark_glue_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.SparkGluePropertiesInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectionPropertiesInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.GlueConnectionInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "athena_properties": "athenaProperties",
            "authentication_configuration": "authenticationConfiguration",
            "connection_properties": "connectionProperties",
            "connection_type": "connectionType",
            "description": "description",
            "match_criteria": "matchCriteria",
            "name": "name",
            "physical_connection_requirements": "physicalConnectionRequirements",
            "python_properties": "pythonProperties",
            "spark_properties": "sparkProperties",
            "validate_credentials": "validateCredentials",
            "validate_for_compute_environments": "validateForComputeEnvironments",
        },
    )
    class GlueConnectionInputProperty:
        def __init__(
            self,
            *,
            athena_properties: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            authentication_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.AuthenticationConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            connection_properties: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            connection_type: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            match_criteria: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            physical_connection_requirements: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.PhysicalConnectionRequirementsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            python_properties: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            spark_properties: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            validate_credentials: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            validate_for_compute_environments: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The AWS Glue connecton input.

            :param athena_properties: The Amazon Athena properties of the AWS Glue connection.
            :param authentication_configuration: The authentication configuration of the AWS Glue connection.
            :param connection_properties: The connection properties of the AWS Glue connection.
            :param connection_type: The connection type of the AWS Glue connection.
            :param description: The description of the AWS Glue connection.
            :param match_criteria: The match criteria of the AWS Glue connection.
            :param name: The name of the AWS Glue connection.
            :param physical_connection_requirements: The physical connection requirements for the AWS Glue connection.
            :param python_properties: The Python properties of the AWS Glue connection.
            :param spark_properties: The Spark properties of the AWS Glue connection.
            :param validate_credentials: Speciefies whether to validate credentials of the AWS Glue connection.
            :param validate_for_compute_environments: Speciefies whether to validate for compute environments of the AWS Glue connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueconnectioninput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                glue_connection_input_property = datazone.CfnConnection.GlueConnectionInputProperty(
                    athena_properties={
                        "athena_properties_key": "athenaProperties"
                    },
                    authentication_configuration=datazone.CfnConnection.AuthenticationConfigurationInputProperty(
                        authentication_type="authenticationType",
                        basic_authentication_credentials=datazone.CfnConnection.BasicAuthenticationCredentialsProperty(
                            password="password",
                            user_name="userName"
                        ),
                        custom_authentication_credentials={
                            "custom_authentication_credentials_key": "customAuthenticationCredentials"
                        },
                        kms_key_arn="kmsKeyArn",
                        o_auth2_properties=datazone.CfnConnection.OAuth2PropertiesProperty(
                            authorization_code_properties=datazone.CfnConnection.AuthorizationCodePropertiesProperty(
                                authorization_code="authorizationCode",
                                redirect_uri="redirectUri"
                            ),
                            o_auth2_client_application=datazone.CfnConnection.OAuth2ClientApplicationProperty(
                                aws_managed_client_application_reference="awsManagedClientApplicationReference",
                                user_managed_client_application_client_id="userManagedClientApplicationClientId"
                            ),
                            o_auth2_credentials=datazone.CfnConnection.GlueOAuth2CredentialsProperty(
                                access_token="accessToken",
                                jwt_token="jwtToken",
                                refresh_token="refreshToken",
                                user_managed_client_application_client_secret="userManagedClientApplicationClientSecret"
                            ),
                            o_auth2_grant_type="oAuth2GrantType",
                            token_url="tokenUrl",
                            token_url_parameters_map={
                                "token_url_parameters_map_key": "tokenUrlParametersMap"
                            }
                        ),
                        secret_arn="secretArn"
                    ),
                    connection_properties={
                        "connection_properties_key": "connectionProperties"
                    },
                    connection_type="connectionType",
                    description="description",
                    match_criteria="matchCriteria",
                    name="name",
                    physical_connection_requirements=datazone.CfnConnection.PhysicalConnectionRequirementsProperty(
                        availability_zone="availabilityZone",
                        security_group_id_list=["securityGroupIdList"],
                        subnet_id="subnetId",
                        subnet_id_list=["subnetIdList"]
                    ),
                    python_properties={
                        "python_properties_key": "pythonProperties"
                    },
                    spark_properties={
                        "spark_properties_key": "sparkProperties"
                    },
                    validate_credentials=False,
                    validate_for_compute_environments=["validateForComputeEnvironments"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__647e7cf0ba0ee1ab7c75fea7d6b34c8a50c95526cd1ec69c86c54c920adef3a9)
                check_type(argname="argument athena_properties", value=athena_properties, expected_type=type_hints["athena_properties"])
                check_type(argname="argument authentication_configuration", value=authentication_configuration, expected_type=type_hints["authentication_configuration"])
                check_type(argname="argument connection_properties", value=connection_properties, expected_type=type_hints["connection_properties"])
                check_type(argname="argument connection_type", value=connection_type, expected_type=type_hints["connection_type"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument match_criteria", value=match_criteria, expected_type=type_hints["match_criteria"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument physical_connection_requirements", value=physical_connection_requirements, expected_type=type_hints["physical_connection_requirements"])
                check_type(argname="argument python_properties", value=python_properties, expected_type=type_hints["python_properties"])
                check_type(argname="argument spark_properties", value=spark_properties, expected_type=type_hints["spark_properties"])
                check_type(argname="argument validate_credentials", value=validate_credentials, expected_type=type_hints["validate_credentials"])
                check_type(argname="argument validate_for_compute_environments", value=validate_for_compute_environments, expected_type=type_hints["validate_for_compute_environments"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if athena_properties is not None:
                self._values["athena_properties"] = athena_properties
            if authentication_configuration is not None:
                self._values["authentication_configuration"] = authentication_configuration
            if connection_properties is not None:
                self._values["connection_properties"] = connection_properties
            if connection_type is not None:
                self._values["connection_type"] = connection_type
            if description is not None:
                self._values["description"] = description
            if match_criteria is not None:
                self._values["match_criteria"] = match_criteria
            if name is not None:
                self._values["name"] = name
            if physical_connection_requirements is not None:
                self._values["physical_connection_requirements"] = physical_connection_requirements
            if python_properties is not None:
                self._values["python_properties"] = python_properties
            if spark_properties is not None:
                self._values["spark_properties"] = spark_properties
            if validate_credentials is not None:
                self._values["validate_credentials"] = validate_credentials
            if validate_for_compute_environments is not None:
                self._values["validate_for_compute_environments"] = validate_for_compute_environments

        @builtins.property
        def athena_properties(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The Amazon Athena properties of the AWS Glue connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueconnectioninput.html#cfn-datazone-connection-glueconnectioninput-athenaproperties
            '''
            result = self._values.get("athena_properties")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def authentication_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.AuthenticationConfigurationInputProperty"]]:
            '''The authentication configuration of the AWS Glue connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueconnectioninput.html#cfn-datazone-connection-glueconnectioninput-authenticationconfiguration
            '''
            result = self._values.get("authentication_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.AuthenticationConfigurationInputProperty"]], result)

        @builtins.property
        def connection_properties(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The connection properties of the AWS Glue connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueconnectioninput.html#cfn-datazone-connection-glueconnectioninput-connectionproperties
            '''
            result = self._values.get("connection_properties")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def connection_type(self) -> typing.Optional[builtins.str]:
            '''The connection type of the AWS Glue connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueconnectioninput.html#cfn-datazone-connection-glueconnectioninput-connectiontype
            '''
            result = self._values.get("connection_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the AWS Glue connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueconnectioninput.html#cfn-datazone-connection-glueconnectioninput-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def match_criteria(self) -> typing.Optional[builtins.str]:
            '''The match criteria of the AWS Glue connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueconnectioninput.html#cfn-datazone-connection-glueconnectioninput-matchcriteria
            '''
            result = self._values.get("match_criteria")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the AWS Glue connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueconnectioninput.html#cfn-datazone-connection-glueconnectioninput-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def physical_connection_requirements(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.PhysicalConnectionRequirementsProperty"]]:
            '''The physical connection requirements for the AWS Glue connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueconnectioninput.html#cfn-datazone-connection-glueconnectioninput-physicalconnectionrequirements
            '''
            result = self._values.get("physical_connection_requirements")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.PhysicalConnectionRequirementsProperty"]], result)

        @builtins.property
        def python_properties(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The Python properties of the AWS Glue connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueconnectioninput.html#cfn-datazone-connection-glueconnectioninput-pythonproperties
            '''
            result = self._values.get("python_properties")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def spark_properties(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The Spark properties of the AWS Glue connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueconnectioninput.html#cfn-datazone-connection-glueconnectioninput-sparkproperties
            '''
            result = self._values.get("spark_properties")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def validate_credentials(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Speciefies whether to validate credentials of the AWS Glue connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueconnectioninput.html#cfn-datazone-connection-glueconnectioninput-validatecredentials
            '''
            result = self._values.get("validate_credentials")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def validate_for_compute_environments(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''Speciefies whether to validate for compute environments of the AWS Glue connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueconnectioninput.html#cfn-datazone-connection-glueconnectioninput-validateforcomputeenvironments
            '''
            result = self._values.get("validate_for_compute_environments")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlueConnectionInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.GlueOAuth2CredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_token": "accessToken",
            "jwt_token": "jwtToken",
            "refresh_token": "refreshToken",
            "user_managed_client_application_client_secret": "userManagedClientApplicationClientSecret",
        },
    )
    class GlueOAuth2CredentialsProperty:
        def __init__(
            self,
            *,
            access_token: typing.Optional[builtins.str] = None,
            jwt_token: typing.Optional[builtins.str] = None,
            refresh_token: typing.Optional[builtins.str] = None,
            user_managed_client_application_client_secret: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The GlueOAuth2 credentials of a connection.

            :param access_token: The access token of a connection.
            :param jwt_token: The jwt token of the connection.
            :param refresh_token: The refresh token of the connection.
            :param user_managed_client_application_client_secret: The user managed client application client secret of the connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueoauth2credentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                glue_oAuth2_credentials_property = datazone.CfnConnection.GlueOAuth2CredentialsProperty(
                    access_token="accessToken",
                    jwt_token="jwtToken",
                    refresh_token="refreshToken",
                    user_managed_client_application_client_secret="userManagedClientApplicationClientSecret"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d948c343e2b90a8893463e22eaab4033317f5a056da9d7e7559e3285f2c7ff17)
                check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
                check_type(argname="argument jwt_token", value=jwt_token, expected_type=type_hints["jwt_token"])
                check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
                check_type(argname="argument user_managed_client_application_client_secret", value=user_managed_client_application_client_secret, expected_type=type_hints["user_managed_client_application_client_secret"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if access_token is not None:
                self._values["access_token"] = access_token
            if jwt_token is not None:
                self._values["jwt_token"] = jwt_token
            if refresh_token is not None:
                self._values["refresh_token"] = refresh_token
            if user_managed_client_application_client_secret is not None:
                self._values["user_managed_client_application_client_secret"] = user_managed_client_application_client_secret

        @builtins.property
        def access_token(self) -> typing.Optional[builtins.str]:
            '''The access token of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueoauth2credentials.html#cfn-datazone-connection-glueoauth2credentials-accesstoken
            '''
            result = self._values.get("access_token")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def jwt_token(self) -> typing.Optional[builtins.str]:
            '''The jwt token of the connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueoauth2credentials.html#cfn-datazone-connection-glueoauth2credentials-jwttoken
            '''
            result = self._values.get("jwt_token")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def refresh_token(self) -> typing.Optional[builtins.str]:
            '''The refresh token of the connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueoauth2credentials.html#cfn-datazone-connection-glueoauth2credentials-refreshtoken
            '''
            result = self._values.get("refresh_token")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_managed_client_application_client_secret(
            self,
        ) -> typing.Optional[builtins.str]:
            '''The user managed client application client secret of the connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-glueoauth2credentials.html#cfn-datazone-connection-glueoauth2credentials-usermanagedclientapplicationclientsecret
            '''
            result = self._values.get("user_managed_client_application_client_secret")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlueOAuth2CredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.GluePropertiesInputProperty",
        jsii_struct_bases=[],
        name_mapping={"glue_connection_input": "glueConnectionInput"},
    )
    class GluePropertiesInputProperty:
        def __init__(
            self,
            *,
            glue_connection_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.GlueConnectionInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The AWS Glue properties of a connection.

            :param glue_connection_input: The AWS Glue connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-gluepropertiesinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                glue_properties_input_property = datazone.CfnConnection.GluePropertiesInputProperty(
                    glue_connection_input=datazone.CfnConnection.GlueConnectionInputProperty(
                        athena_properties={
                            "athena_properties_key": "athenaProperties"
                        },
                        authentication_configuration=datazone.CfnConnection.AuthenticationConfigurationInputProperty(
                            authentication_type="authenticationType",
                            basic_authentication_credentials=datazone.CfnConnection.BasicAuthenticationCredentialsProperty(
                                password="password",
                                user_name="userName"
                            ),
                            custom_authentication_credentials={
                                "custom_authentication_credentials_key": "customAuthenticationCredentials"
                            },
                            kms_key_arn="kmsKeyArn",
                            o_auth2_properties=datazone.CfnConnection.OAuth2PropertiesProperty(
                                authorization_code_properties=datazone.CfnConnection.AuthorizationCodePropertiesProperty(
                                    authorization_code="authorizationCode",
                                    redirect_uri="redirectUri"
                                ),
                                o_auth2_client_application=datazone.CfnConnection.OAuth2ClientApplicationProperty(
                                    aws_managed_client_application_reference="awsManagedClientApplicationReference",
                                    user_managed_client_application_client_id="userManagedClientApplicationClientId"
                                ),
                                o_auth2_credentials=datazone.CfnConnection.GlueOAuth2CredentialsProperty(
                                    access_token="accessToken",
                                    jwt_token="jwtToken",
                                    refresh_token="refreshToken",
                                    user_managed_client_application_client_secret="userManagedClientApplicationClientSecret"
                                ),
                                o_auth2_grant_type="oAuth2GrantType",
                                token_url="tokenUrl",
                                token_url_parameters_map={
                                    "token_url_parameters_map_key": "tokenUrlParametersMap"
                                }
                            ),
                            secret_arn="secretArn"
                        ),
                        connection_properties={
                            "connection_properties_key": "connectionProperties"
                        },
                        connection_type="connectionType",
                        description="description",
                        match_criteria="matchCriteria",
                        name="name",
                        physical_connection_requirements=datazone.CfnConnection.PhysicalConnectionRequirementsProperty(
                            availability_zone="availabilityZone",
                            security_group_id_list=["securityGroupIdList"],
                            subnet_id="subnetId",
                            subnet_id_list=["subnetIdList"]
                        ),
                        python_properties={
                            "python_properties_key": "pythonProperties"
                        },
                        spark_properties={
                            "spark_properties_key": "sparkProperties"
                        },
                        validate_credentials=False,
                        validate_for_compute_environments=["validateForComputeEnvironments"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__07f6c7fa8f6b6af10d26eadc862dfc837c455b56372fa29947bd67161af5e5c7)
                check_type(argname="argument glue_connection_input", value=glue_connection_input, expected_type=type_hints["glue_connection_input"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if glue_connection_input is not None:
                self._values["glue_connection_input"] = glue_connection_input

        @builtins.property
        def glue_connection_input(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.GlueConnectionInputProperty"]]:
            '''The AWS Glue connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-gluepropertiesinput.html#cfn-datazone-connection-gluepropertiesinput-glueconnectioninput
            '''
            result = self._values.get("glue_connection_input")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.GlueConnectionInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GluePropertiesInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.HyperPodPropertiesInputProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_name": "clusterName"},
    )
    class HyperPodPropertiesInputProperty:
        def __init__(self, *, cluster_name: builtins.str) -> None:
            '''The hyper pod properties of a AWS Glue properties patch.

            :param cluster_name: The cluster name the hyper pod properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-hyperpodpropertiesinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                hyper_pod_properties_input_property = datazone.CfnConnection.HyperPodPropertiesInputProperty(
                    cluster_name="clusterName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b2574ba013a10f07b6e0a61c5559f70c13b2de025bb4b8d00be0efcd15f721fd)
                check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cluster_name": cluster_name,
            }

        @builtins.property
        def cluster_name(self) -> builtins.str:
            '''The cluster name the hyper pod properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-hyperpodpropertiesinput.html#cfn-datazone-connection-hyperpodpropertiesinput-clustername
            '''
            result = self._values.get("cluster_name")
            assert result is not None, "Required property 'cluster_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HyperPodPropertiesInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.IamPropertiesInputProperty",
        jsii_struct_bases=[],
        name_mapping={"glue_lineage_sync_enabled": "glueLineageSyncEnabled"},
    )
    class IamPropertiesInputProperty:
        def __init__(
            self,
            *,
            glue_lineage_sync_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The IAM properties of a connection.

            :param glue_lineage_sync_enabled: Specifies whether AWS Glue lineage sync is enabled for a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-iampropertiesinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                iam_properties_input_property = datazone.CfnConnection.IamPropertiesInputProperty(
                    glue_lineage_sync_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5fcef45bd8fc26fdf37a0281f7789bd6e0fc1105a24dd2b5148ec9b0e0c27b75)
                check_type(argname="argument glue_lineage_sync_enabled", value=glue_lineage_sync_enabled, expected_type=type_hints["glue_lineage_sync_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if glue_lineage_sync_enabled is not None:
                self._values["glue_lineage_sync_enabled"] = glue_lineage_sync_enabled

        @builtins.property
        def glue_lineage_sync_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether AWS Glue lineage sync is enabled for a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-iampropertiesinput.html#cfn-datazone-connection-iampropertiesinput-gluelineagesyncenabled
            '''
            result = self._values.get("glue_lineage_sync_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamPropertiesInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.LineageSyncScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={"schedule": "schedule"},
    )
    class LineageSyncScheduleProperty:
        def __init__(self, *, schedule: typing.Optional[builtins.str] = None) -> None:
            '''The lineage sync schedule.

            :param schedule: The lineage sync schedule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-lineagesyncschedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                lineage_sync_schedule_property = datazone.CfnConnection.LineageSyncScheduleProperty(
                    schedule="schedule"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__807712ef4f77e804709861b4d4515e24f1b5cb14208414a29172fa52c5a8622e)
                check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if schedule is not None:
                self._values["schedule"] = schedule

        @builtins.property
        def schedule(self) -> typing.Optional[builtins.str]:
            '''The lineage sync schedule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-lineagesyncschedule.html#cfn-datazone-connection-lineagesyncschedule-schedule
            '''
            result = self._values.get("schedule")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LineageSyncScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.OAuth2ClientApplicationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_managed_client_application_reference": "awsManagedClientApplicationReference",
            "user_managed_client_application_client_id": "userManagedClientApplicationClientId",
        },
    )
    class OAuth2ClientApplicationProperty:
        def __init__(
            self,
            *,
            aws_managed_client_application_reference: typing.Optional[builtins.str] = None,
            user_managed_client_application_client_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The OAuth2Client application.

            :param aws_managed_client_application_reference: The AWS managed client application reference in the OAuth2Client application.
            :param user_managed_client_application_client_id: The user managed client application client ID in the OAuth2Client application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-oauth2clientapplication.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                o_auth2_client_application_property = datazone.CfnConnection.OAuth2ClientApplicationProperty(
                    aws_managed_client_application_reference="awsManagedClientApplicationReference",
                    user_managed_client_application_client_id="userManagedClientApplicationClientId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__06033edd4e1d109e79d816fec5df671c9c991a52cf6e92d45aa0f6ca6cb72d98)
                check_type(argname="argument aws_managed_client_application_reference", value=aws_managed_client_application_reference, expected_type=type_hints["aws_managed_client_application_reference"])
                check_type(argname="argument user_managed_client_application_client_id", value=user_managed_client_application_client_id, expected_type=type_hints["user_managed_client_application_client_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aws_managed_client_application_reference is not None:
                self._values["aws_managed_client_application_reference"] = aws_managed_client_application_reference
            if user_managed_client_application_client_id is not None:
                self._values["user_managed_client_application_client_id"] = user_managed_client_application_client_id

        @builtins.property
        def aws_managed_client_application_reference(
            self,
        ) -> typing.Optional[builtins.str]:
            '''The AWS managed client application reference in the OAuth2Client application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-oauth2clientapplication.html#cfn-datazone-connection-oauth2clientapplication-awsmanagedclientapplicationreference
            '''
            result = self._values.get("aws_managed_client_application_reference")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_managed_client_application_client_id(
            self,
        ) -> typing.Optional[builtins.str]:
            '''The user managed client application client ID in the OAuth2Client application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-oauth2clientapplication.html#cfn-datazone-connection-oauth2clientapplication-usermanagedclientapplicationclientid
            '''
            result = self._values.get("user_managed_client_application_client_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OAuth2ClientApplicationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.OAuth2PropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorization_code_properties": "authorizationCodeProperties",
            "o_auth2_client_application": "oAuth2ClientApplication",
            "o_auth2_credentials": "oAuth2Credentials",
            "o_auth2_grant_type": "oAuth2GrantType",
            "token_url": "tokenUrl",
            "token_url_parameters_map": "tokenUrlParametersMap",
        },
    )
    class OAuth2PropertiesProperty:
        def __init__(
            self,
            *,
            authorization_code_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.AuthorizationCodePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            o_auth2_client_application: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.OAuth2ClientApplicationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            o_auth2_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.GlueOAuth2CredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            o_auth2_grant_type: typing.Optional[builtins.str] = None,
            token_url: typing.Optional[builtins.str] = None,
            token_url_parameters_map: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The OAuth2 properties.

            :param authorization_code_properties: The authorization code properties of the OAuth2 properties.
            :param o_auth2_client_application: The OAuth2 client application of the OAuth2 properties.
            :param o_auth2_credentials: The OAuth2 credentials of the OAuth2 properties.
            :param o_auth2_grant_type: The OAuth2 grant type of the OAuth2 properties.
            :param token_url: The OAuth2 token URL of the OAuth2 properties.
            :param token_url_parameters_map: The OAuth2 token URL parameter map of the OAuth2 properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-oauth2properties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                o_auth2_properties_property = datazone.CfnConnection.OAuth2PropertiesProperty(
                    authorization_code_properties=datazone.CfnConnection.AuthorizationCodePropertiesProperty(
                        authorization_code="authorizationCode",
                        redirect_uri="redirectUri"
                    ),
                    o_auth2_client_application=datazone.CfnConnection.OAuth2ClientApplicationProperty(
                        aws_managed_client_application_reference="awsManagedClientApplicationReference",
                        user_managed_client_application_client_id="userManagedClientApplicationClientId"
                    ),
                    o_auth2_credentials=datazone.CfnConnection.GlueOAuth2CredentialsProperty(
                        access_token="accessToken",
                        jwt_token="jwtToken",
                        refresh_token="refreshToken",
                        user_managed_client_application_client_secret="userManagedClientApplicationClientSecret"
                    ),
                    o_auth2_grant_type="oAuth2GrantType",
                    token_url="tokenUrl",
                    token_url_parameters_map={
                        "token_url_parameters_map_key": "tokenUrlParametersMap"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4cba63b68fdb8bbf2e7a537a629e7f6c6d51267f6c2af7395b1464f0ecb29b7d)
                check_type(argname="argument authorization_code_properties", value=authorization_code_properties, expected_type=type_hints["authorization_code_properties"])
                check_type(argname="argument o_auth2_client_application", value=o_auth2_client_application, expected_type=type_hints["o_auth2_client_application"])
                check_type(argname="argument o_auth2_credentials", value=o_auth2_credentials, expected_type=type_hints["o_auth2_credentials"])
                check_type(argname="argument o_auth2_grant_type", value=o_auth2_grant_type, expected_type=type_hints["o_auth2_grant_type"])
                check_type(argname="argument token_url", value=token_url, expected_type=type_hints["token_url"])
                check_type(argname="argument token_url_parameters_map", value=token_url_parameters_map, expected_type=type_hints["token_url_parameters_map"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if authorization_code_properties is not None:
                self._values["authorization_code_properties"] = authorization_code_properties
            if o_auth2_client_application is not None:
                self._values["o_auth2_client_application"] = o_auth2_client_application
            if o_auth2_credentials is not None:
                self._values["o_auth2_credentials"] = o_auth2_credentials
            if o_auth2_grant_type is not None:
                self._values["o_auth2_grant_type"] = o_auth2_grant_type
            if token_url is not None:
                self._values["token_url"] = token_url
            if token_url_parameters_map is not None:
                self._values["token_url_parameters_map"] = token_url_parameters_map

        @builtins.property
        def authorization_code_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.AuthorizationCodePropertiesProperty"]]:
            '''The authorization code properties of the OAuth2 properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-oauth2properties.html#cfn-datazone-connection-oauth2properties-authorizationcodeproperties
            '''
            result = self._values.get("authorization_code_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.AuthorizationCodePropertiesProperty"]], result)

        @builtins.property
        def o_auth2_client_application(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.OAuth2ClientApplicationProperty"]]:
            '''The OAuth2 client application of the OAuth2 properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-oauth2properties.html#cfn-datazone-connection-oauth2properties-oauth2clientapplication
            '''
            result = self._values.get("o_auth2_client_application")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.OAuth2ClientApplicationProperty"]], result)

        @builtins.property
        def o_auth2_credentials(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.GlueOAuth2CredentialsProperty"]]:
            '''The OAuth2 credentials of the OAuth2 properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-oauth2properties.html#cfn-datazone-connection-oauth2properties-oauth2credentials
            '''
            result = self._values.get("o_auth2_credentials")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.GlueOAuth2CredentialsProperty"]], result)

        @builtins.property
        def o_auth2_grant_type(self) -> typing.Optional[builtins.str]:
            '''The OAuth2 grant type of the OAuth2 properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-oauth2properties.html#cfn-datazone-connection-oauth2properties-oauth2granttype
            '''
            result = self._values.get("o_auth2_grant_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def token_url(self) -> typing.Optional[builtins.str]:
            '''The OAuth2 token URL of the OAuth2 properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-oauth2properties.html#cfn-datazone-connection-oauth2properties-tokenurl
            '''
            result = self._values.get("token_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def token_url_parameters_map(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The OAuth2 token URL parameter map of the OAuth2 properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-oauth2properties.html#cfn-datazone-connection-oauth2properties-tokenurlparametersmap
            '''
            result = self._values.get("token_url_parameters_map")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OAuth2PropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.PhysicalConnectionRequirementsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "availability_zone": "availabilityZone",
            "security_group_id_list": "securityGroupIdList",
            "subnet_id": "subnetId",
            "subnet_id_list": "subnetIdList",
        },
    )
    class PhysicalConnectionRequirementsProperty:
        def __init__(
            self,
            *,
            availability_zone: typing.Optional[builtins.str] = None,
            security_group_id_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_id: typing.Optional[builtins.str] = None,
            subnet_id_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Physical connection requirements of a connection.

            :param availability_zone: The availability zone of the physical connection requirements of a connection.
            :param security_group_id_list: The group ID list of the physical connection requirements of a connection.
            :param subnet_id: The subnet ID of the physical connection requirements of a connection.
            :param subnet_id_list: The subnet ID list of the physical connection requirements of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-physicalconnectionrequirements.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                physical_connection_requirements_property = datazone.CfnConnection.PhysicalConnectionRequirementsProperty(
                    availability_zone="availabilityZone",
                    security_group_id_list=["securityGroupIdList"],
                    subnet_id="subnetId",
                    subnet_id_list=["subnetIdList"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__33253a54618916e3372650927015127ea603d71a4c9363ab9570cdaaa038b28b)
                check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
                check_type(argname="argument security_group_id_list", value=security_group_id_list, expected_type=type_hints["security_group_id_list"])
                check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
                check_type(argname="argument subnet_id_list", value=subnet_id_list, expected_type=type_hints["subnet_id_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if availability_zone is not None:
                self._values["availability_zone"] = availability_zone
            if security_group_id_list is not None:
                self._values["security_group_id_list"] = security_group_id_list
            if subnet_id is not None:
                self._values["subnet_id"] = subnet_id
            if subnet_id_list is not None:
                self._values["subnet_id_list"] = subnet_id_list

        @builtins.property
        def availability_zone(self) -> typing.Optional[builtins.str]:
            '''The availability zone of the physical connection requirements of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-physicalconnectionrequirements.html#cfn-datazone-connection-physicalconnectionrequirements-availabilityzone
            '''
            result = self._values.get("availability_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_group_id_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The group ID list of the physical connection requirements of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-physicalconnectionrequirements.html#cfn-datazone-connection-physicalconnectionrequirements-securitygroupidlist
            '''
            result = self._values.get("security_group_id_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_id(self) -> typing.Optional[builtins.str]:
            '''The subnet ID of the physical connection requirements of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-physicalconnectionrequirements.html#cfn-datazone-connection-physicalconnectionrequirements-subnetid
            '''
            result = self._values.get("subnet_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def subnet_id_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The subnet ID list of the physical connection requirements of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-physicalconnectionrequirements.html#cfn-datazone-connection-physicalconnectionrequirements-subnetidlist
            '''
            result = self._values.get("subnet_id_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PhysicalConnectionRequirementsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.RedshiftCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "secret_arn": "secretArn",
            "username_password": "usernamePassword",
        },
    )
    class RedshiftCredentialsProperty:
        def __init__(
            self,
            *,
            secret_arn: typing.Optional[builtins.str] = None,
            username_password: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.UsernamePasswordProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Amazon Redshift credentials of a connection.

            :param secret_arn: The secret ARN of the Amazon Redshift credentials of a connection.
            :param username_password: The username and password of the Amazon Redshift credentials of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-redshiftcredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                redshift_credentials_property = datazone.CfnConnection.RedshiftCredentialsProperty(
                    secret_arn="secretArn",
                    username_password=datazone.CfnConnection.UsernamePasswordProperty(
                        password="password",
                        username="username"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__573044a4537dd6f740734285ebbb2dcd69d20a0dc8c1a613d8498d6a3bcb9504)
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument username_password", value=username_password, expected_type=type_hints["username_password"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn
            if username_password is not None:
                self._values["username_password"] = username_password

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            '''The secret ARN of the Amazon Redshift credentials of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-redshiftcredentials.html#cfn-datazone-connection-redshiftcredentials-secretarn
            '''
            result = self._values.get("secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username_password(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.UsernamePasswordProperty"]]:
            '''The username and password of the Amazon Redshift credentials of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-redshiftcredentials.html#cfn-datazone-connection-redshiftcredentials-usernamepassword
            '''
            result = self._values.get("username_password")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.UsernamePasswordProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.RedshiftLineageSyncConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "schedule": "schedule"},
    )
    class RedshiftLineageSyncConfigurationInputProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.LineageSyncScheduleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The Amaon Redshift lineage sync configuration.

            :param enabled: Specifies whether the Amaon Redshift lineage sync configuration is enabled.
            :param schedule: The schedule of the Amaon Redshift lineage sync configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-redshiftlineagesyncconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                redshift_lineage_sync_configuration_input_property = datazone.CfnConnection.RedshiftLineageSyncConfigurationInputProperty(
                    enabled=False,
                    schedule=datazone.CfnConnection.LineageSyncScheduleProperty(
                        schedule="schedule"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__86e732877333e36da3944ac0771866cd4ef9ef230040330b2a710ca0eba2f6f7)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if schedule is not None:
                self._values["schedule"] = schedule

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the Amaon Redshift lineage sync configuration is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-redshiftlineagesyncconfigurationinput.html#cfn-datazone-connection-redshiftlineagesyncconfigurationinput-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def schedule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.LineageSyncScheduleProperty"]]:
            '''The schedule of the Amaon Redshift lineage sync configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-redshiftlineagesyncconfigurationinput.html#cfn-datazone-connection-redshiftlineagesyncconfigurationinput-schedule
            '''
            result = self._values.get("schedule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.LineageSyncScheduleProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftLineageSyncConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.RedshiftPropertiesInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "credentials": "credentials",
            "database_name": "databaseName",
            "host": "host",
            "lineage_sync": "lineageSync",
            "port": "port",
            "storage": "storage",
        },
    )
    class RedshiftPropertiesInputProperty:
        def __init__(
            self,
            *,
            credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.RedshiftCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            database_name: typing.Optional[builtins.str] = None,
            host: typing.Optional[builtins.str] = None,
            lineage_sync: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.RedshiftLineageSyncConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            port: typing.Optional[jsii.Number] = None,
            storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.RedshiftStoragePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The Amazon Redshift properties.

            :param credentials: The Amaon Redshift credentials.
            :param database_name: The Amazon Redshift database name.
            :param host: The Amazon Redshift host.
            :param lineage_sync: The lineage sync of the Amazon Redshift.
            :param port: The Amaon Redshift port.
            :param storage: The Amazon Redshift storage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-redshiftpropertiesinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                redshift_properties_input_property = datazone.CfnConnection.RedshiftPropertiesInputProperty(
                    credentials=datazone.CfnConnection.RedshiftCredentialsProperty(
                        secret_arn="secretArn",
                        username_password=datazone.CfnConnection.UsernamePasswordProperty(
                            password="password",
                            username="username"
                        )
                    ),
                    database_name="databaseName",
                    host="host",
                    lineage_sync=datazone.CfnConnection.RedshiftLineageSyncConfigurationInputProperty(
                        enabled=False,
                        schedule=datazone.CfnConnection.LineageSyncScheduleProperty(
                            schedule="schedule"
                        )
                    ),
                    port=123,
                    storage=datazone.CfnConnection.RedshiftStoragePropertiesProperty(
                        cluster_name="clusterName",
                        workgroup_name="workgroupName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6bad9bb99ea9342d656480e79701348e43bbb8385f639af2c2e92651653e3bb4)
                check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument host", value=host, expected_type=type_hints["host"])
                check_type(argname="argument lineage_sync", value=lineage_sync, expected_type=type_hints["lineage_sync"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if credentials is not None:
                self._values["credentials"] = credentials
            if database_name is not None:
                self._values["database_name"] = database_name
            if host is not None:
                self._values["host"] = host
            if lineage_sync is not None:
                self._values["lineage_sync"] = lineage_sync
            if port is not None:
                self._values["port"] = port
            if storage is not None:
                self._values["storage"] = storage

        @builtins.property
        def credentials(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.RedshiftCredentialsProperty"]]:
            '''The Amaon Redshift credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-redshiftpropertiesinput.html#cfn-datazone-connection-redshiftpropertiesinput-credentials
            '''
            result = self._values.get("credentials")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.RedshiftCredentialsProperty"]], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The Amazon Redshift database name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-redshiftpropertiesinput.html#cfn-datazone-connection-redshiftpropertiesinput-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def host(self) -> typing.Optional[builtins.str]:
            '''The Amazon Redshift host.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-redshiftpropertiesinput.html#cfn-datazone-connection-redshiftpropertiesinput-host
            '''
            result = self._values.get("host")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def lineage_sync(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.RedshiftLineageSyncConfigurationInputProperty"]]:
            '''The lineage sync of the Amazon Redshift.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-redshiftpropertiesinput.html#cfn-datazone-connection-redshiftpropertiesinput-lineagesync
            '''
            result = self._values.get("lineage_sync")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.RedshiftLineageSyncConfigurationInputProperty"]], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''The Amaon Redshift port.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-redshiftpropertiesinput.html#cfn-datazone-connection-redshiftpropertiesinput-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def storage(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.RedshiftStoragePropertiesProperty"]]:
            '''The Amazon Redshift storage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-redshiftpropertiesinput.html#cfn-datazone-connection-redshiftpropertiesinput-storage
            '''
            result = self._values.get("storage")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.RedshiftStoragePropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftPropertiesInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.RedshiftStoragePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cluster_name": "clusterName",
            "workgroup_name": "workgroupName",
        },
    )
    class RedshiftStoragePropertiesProperty:
        def __init__(
            self,
            *,
            cluster_name: typing.Optional[builtins.str] = None,
            workgroup_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Amazon Redshift storage properties.

            :param cluster_name: The cluster name in the Amazon Redshift storage properties.
            :param workgroup_name: The workgroup name in the Amazon Redshift storage properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-redshiftstorageproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                redshift_storage_properties_property = datazone.CfnConnection.RedshiftStoragePropertiesProperty(
                    cluster_name="clusterName",
                    workgroup_name="workgroupName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b195696e44f8816ec97423896e5a52b6ee46aa7c4c9e0e33aa0ac4a92900d2ea)
                check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
                check_type(argname="argument workgroup_name", value=workgroup_name, expected_type=type_hints["workgroup_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cluster_name is not None:
                self._values["cluster_name"] = cluster_name
            if workgroup_name is not None:
                self._values["workgroup_name"] = workgroup_name

        @builtins.property
        def cluster_name(self) -> typing.Optional[builtins.str]:
            '''The cluster name in the Amazon Redshift storage properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-redshiftstorageproperties.html#cfn-datazone-connection-redshiftstorageproperties-clustername
            '''
            result = self._values.get("cluster_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def workgroup_name(self) -> typing.Optional[builtins.str]:
            '''The workgroup name in the Amazon Redshift storage properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-redshiftstorageproperties.html#cfn-datazone-connection-redshiftstorageproperties-workgroupname
            '''
            result = self._values.get("workgroup_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftStoragePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.SparkEmrPropertiesInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "compute_arn": "computeArn",
            "instance_profile_arn": "instanceProfileArn",
            "java_virtual_env": "javaVirtualEnv",
            "log_uri": "logUri",
            "python_virtual_env": "pythonVirtualEnv",
            "runtime_role": "runtimeRole",
            "trusted_certificates_s3_uri": "trustedCertificatesS3Uri",
        },
    )
    class SparkEmrPropertiesInputProperty:
        def __init__(
            self,
            *,
            compute_arn: typing.Optional[builtins.str] = None,
            instance_profile_arn: typing.Optional[builtins.str] = None,
            java_virtual_env: typing.Optional[builtins.str] = None,
            log_uri: typing.Optional[builtins.str] = None,
            python_virtual_env: typing.Optional[builtins.str] = None,
            runtime_role: typing.Optional[builtins.str] = None,
            trusted_certificates_s3_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Spark EMR properties.

            :param compute_arn: The compute ARN of Spark EMR.
            :param instance_profile_arn: The instance profile ARN of Spark EMR.
            :param java_virtual_env: The java virtual env of the Spark EMR.
            :param log_uri: The log URI of the Spark EMR.
            :param python_virtual_env: The Python virtual env of the Spark EMR.
            :param runtime_role: The runtime role of the Spark EMR.
            :param trusted_certificates_s3_uri: The certificates S3 URI of the Spark EMR.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkemrpropertiesinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                spark_emr_properties_input_property = datazone.CfnConnection.SparkEmrPropertiesInputProperty(
                    compute_arn="computeArn",
                    instance_profile_arn="instanceProfileArn",
                    java_virtual_env="javaVirtualEnv",
                    log_uri="logUri",
                    python_virtual_env="pythonVirtualEnv",
                    runtime_role="runtimeRole",
                    trusted_certificates_s3_uri="trustedCertificatesS3Uri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__94fbdb6dfc5f26da94f6f165997647170dbb3404b50c6d28eef32f77d6fcd395)
                check_type(argname="argument compute_arn", value=compute_arn, expected_type=type_hints["compute_arn"])
                check_type(argname="argument instance_profile_arn", value=instance_profile_arn, expected_type=type_hints["instance_profile_arn"])
                check_type(argname="argument java_virtual_env", value=java_virtual_env, expected_type=type_hints["java_virtual_env"])
                check_type(argname="argument log_uri", value=log_uri, expected_type=type_hints["log_uri"])
                check_type(argname="argument python_virtual_env", value=python_virtual_env, expected_type=type_hints["python_virtual_env"])
                check_type(argname="argument runtime_role", value=runtime_role, expected_type=type_hints["runtime_role"])
                check_type(argname="argument trusted_certificates_s3_uri", value=trusted_certificates_s3_uri, expected_type=type_hints["trusted_certificates_s3_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if compute_arn is not None:
                self._values["compute_arn"] = compute_arn
            if instance_profile_arn is not None:
                self._values["instance_profile_arn"] = instance_profile_arn
            if java_virtual_env is not None:
                self._values["java_virtual_env"] = java_virtual_env
            if log_uri is not None:
                self._values["log_uri"] = log_uri
            if python_virtual_env is not None:
                self._values["python_virtual_env"] = python_virtual_env
            if runtime_role is not None:
                self._values["runtime_role"] = runtime_role
            if trusted_certificates_s3_uri is not None:
                self._values["trusted_certificates_s3_uri"] = trusted_certificates_s3_uri

        @builtins.property
        def compute_arn(self) -> typing.Optional[builtins.str]:
            '''The compute ARN of Spark EMR.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkemrpropertiesinput.html#cfn-datazone-connection-sparkemrpropertiesinput-computearn
            '''
            result = self._values.get("compute_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def instance_profile_arn(self) -> typing.Optional[builtins.str]:
            '''The instance profile ARN of Spark EMR.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkemrpropertiesinput.html#cfn-datazone-connection-sparkemrpropertiesinput-instanceprofilearn
            '''
            result = self._values.get("instance_profile_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def java_virtual_env(self) -> typing.Optional[builtins.str]:
            '''The java virtual env of the Spark EMR.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkemrpropertiesinput.html#cfn-datazone-connection-sparkemrpropertiesinput-javavirtualenv
            '''
            result = self._values.get("java_virtual_env")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_uri(self) -> typing.Optional[builtins.str]:
            '''The log URI of the Spark EMR.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkemrpropertiesinput.html#cfn-datazone-connection-sparkemrpropertiesinput-loguri
            '''
            result = self._values.get("log_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def python_virtual_env(self) -> typing.Optional[builtins.str]:
            '''The Python virtual env of the Spark EMR.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkemrpropertiesinput.html#cfn-datazone-connection-sparkemrpropertiesinput-pythonvirtualenv
            '''
            result = self._values.get("python_virtual_env")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def runtime_role(self) -> typing.Optional[builtins.str]:
            '''The runtime role of the Spark EMR.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkemrpropertiesinput.html#cfn-datazone-connection-sparkemrpropertiesinput-runtimerole
            '''
            result = self._values.get("runtime_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def trusted_certificates_s3_uri(self) -> typing.Optional[builtins.str]:
            '''The certificates S3 URI of the Spark EMR.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkemrpropertiesinput.html#cfn-datazone-connection-sparkemrpropertiesinput-trustedcertificatess3uri
            '''
            result = self._values.get("trusted_certificates_s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SparkEmrPropertiesInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.SparkGlueArgsProperty",
        jsii_struct_bases=[],
        name_mapping={"connection": "connection"},
    )
    class SparkGlueArgsProperty:
        def __init__(self, *, connection: typing.Optional[builtins.str] = None) -> None:
            '''The Spark AWS Glue args.

            :param connection: The connection in the Spark AWS Glue args.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkglueargs.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                spark_glue_args_property = datazone.CfnConnection.SparkGlueArgsProperty(
                    connection="connection"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fc6a385f982dd6f3097586513e776c152b3210e81a751a74ccdf596b24edf2ba)
                check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if connection is not None:
                self._values["connection"] = connection

        @builtins.property
        def connection(self) -> typing.Optional[builtins.str]:
            '''The connection in the Spark AWS Glue args.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkglueargs.html#cfn-datazone-connection-sparkglueargs-connection
            '''
            result = self._values.get("connection")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SparkGlueArgsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.SparkGluePropertiesInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "additional_args": "additionalArgs",
            "glue_connection_name": "glueConnectionName",
            "glue_version": "glueVersion",
            "idle_timeout": "idleTimeout",
            "java_virtual_env": "javaVirtualEnv",
            "number_of_workers": "numberOfWorkers",
            "python_virtual_env": "pythonVirtualEnv",
            "worker_type": "workerType",
        },
    )
    class SparkGluePropertiesInputProperty:
        def __init__(
            self,
            *,
            additional_args: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.SparkGlueArgsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            glue_connection_name: typing.Optional[builtins.str] = None,
            glue_version: typing.Optional[builtins.str] = None,
            idle_timeout: typing.Optional[jsii.Number] = None,
            java_virtual_env: typing.Optional[builtins.str] = None,
            number_of_workers: typing.Optional[jsii.Number] = None,
            python_virtual_env: typing.Optional[builtins.str] = None,
            worker_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Spark AWS Glue properties.

            :param additional_args: The additional args in the Spark AWS Glue properties.
            :param glue_connection_name: The AWS Glue connection name in the Spark AWS Glue properties.
            :param glue_version: The AWS Glue version in the Spark AWS Glue properties.
            :param idle_timeout: The idle timeout in the Spark AWS Glue properties.
            :param java_virtual_env: The Java virtual env in the Spark AWS Glue properties.
            :param number_of_workers: The number of workers in the Spark AWS Glue properties.
            :param python_virtual_env: The Python virtual env in the Spark AWS Glue properties.
            :param worker_type: The worker type in the Spark AWS Glue properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkgluepropertiesinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                spark_glue_properties_input_property = datazone.CfnConnection.SparkGluePropertiesInputProperty(
                    additional_args=datazone.CfnConnection.SparkGlueArgsProperty(
                        connection="connection"
                    ),
                    glue_connection_name="glueConnectionName",
                    glue_version="glueVersion",
                    idle_timeout=123,
                    java_virtual_env="javaVirtualEnv",
                    number_of_workers=123,
                    python_virtual_env="pythonVirtualEnv",
                    worker_type="workerType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__44d0d0a8466990262ea9a97c7791e494a3b6f38cf1968ce4fcff9de3fc1a9c77)
                check_type(argname="argument additional_args", value=additional_args, expected_type=type_hints["additional_args"])
                check_type(argname="argument glue_connection_name", value=glue_connection_name, expected_type=type_hints["glue_connection_name"])
                check_type(argname="argument glue_version", value=glue_version, expected_type=type_hints["glue_version"])
                check_type(argname="argument idle_timeout", value=idle_timeout, expected_type=type_hints["idle_timeout"])
                check_type(argname="argument java_virtual_env", value=java_virtual_env, expected_type=type_hints["java_virtual_env"])
                check_type(argname="argument number_of_workers", value=number_of_workers, expected_type=type_hints["number_of_workers"])
                check_type(argname="argument python_virtual_env", value=python_virtual_env, expected_type=type_hints["python_virtual_env"])
                check_type(argname="argument worker_type", value=worker_type, expected_type=type_hints["worker_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if additional_args is not None:
                self._values["additional_args"] = additional_args
            if glue_connection_name is not None:
                self._values["glue_connection_name"] = glue_connection_name
            if glue_version is not None:
                self._values["glue_version"] = glue_version
            if idle_timeout is not None:
                self._values["idle_timeout"] = idle_timeout
            if java_virtual_env is not None:
                self._values["java_virtual_env"] = java_virtual_env
            if number_of_workers is not None:
                self._values["number_of_workers"] = number_of_workers
            if python_virtual_env is not None:
                self._values["python_virtual_env"] = python_virtual_env
            if worker_type is not None:
                self._values["worker_type"] = worker_type

        @builtins.property
        def additional_args(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.SparkGlueArgsProperty"]]:
            '''The additional args in the Spark AWS Glue properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkgluepropertiesinput.html#cfn-datazone-connection-sparkgluepropertiesinput-additionalargs
            '''
            result = self._values.get("additional_args")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.SparkGlueArgsProperty"]], result)

        @builtins.property
        def glue_connection_name(self) -> typing.Optional[builtins.str]:
            '''The AWS Glue connection name in the Spark AWS Glue properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkgluepropertiesinput.html#cfn-datazone-connection-sparkgluepropertiesinput-glueconnectionname
            '''
            result = self._values.get("glue_connection_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def glue_version(self) -> typing.Optional[builtins.str]:
            '''The AWS Glue version in the Spark AWS Glue properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkgluepropertiesinput.html#cfn-datazone-connection-sparkgluepropertiesinput-glueversion
            '''
            result = self._values.get("glue_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def idle_timeout(self) -> typing.Optional[jsii.Number]:
            '''The idle timeout in the Spark AWS Glue properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkgluepropertiesinput.html#cfn-datazone-connection-sparkgluepropertiesinput-idletimeout
            '''
            result = self._values.get("idle_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def java_virtual_env(self) -> typing.Optional[builtins.str]:
            '''The Java virtual env in the Spark AWS Glue properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkgluepropertiesinput.html#cfn-datazone-connection-sparkgluepropertiesinput-javavirtualenv
            '''
            result = self._values.get("java_virtual_env")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def number_of_workers(self) -> typing.Optional[jsii.Number]:
            '''The number of workers in the Spark AWS Glue properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkgluepropertiesinput.html#cfn-datazone-connection-sparkgluepropertiesinput-numberofworkers
            '''
            result = self._values.get("number_of_workers")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def python_virtual_env(self) -> typing.Optional[builtins.str]:
            '''The Python virtual env in the Spark AWS Glue properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkgluepropertiesinput.html#cfn-datazone-connection-sparkgluepropertiesinput-pythonvirtualenv
            '''
            result = self._values.get("python_virtual_env")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def worker_type(self) -> typing.Optional[builtins.str]:
            '''The worker type in the Spark AWS Glue properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-sparkgluepropertiesinput.html#cfn-datazone-connection-sparkgluepropertiesinput-workertype
            '''
            result = self._values.get("worker_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SparkGluePropertiesInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnConnection.UsernamePasswordProperty",
        jsii_struct_bases=[],
        name_mapping={"password": "password", "username": "username"},
    )
    class UsernamePasswordProperty:
        def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
            '''The username and password of a connection.

            :param password: The password of a connection.
            :param username: The username of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-usernamepassword.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                username_password_property = datazone.CfnConnection.UsernamePasswordProperty(
                    password="password",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__09aad17749e39aa1e36aa16e65e288bbdbfd74b1ed996ed966f666f40ce8c31d)
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "password": password,
                "username": username,
            }

        @builtins.property
        def password(self) -> builtins.str:
            '''The password of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-usernamepassword.html#cfn-datazone-connection-usernamepassword-password
            '''
            result = self._values.get("password")
            assert result is not None, "Required property 'password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def username(self) -> builtins.str:
            '''The username of a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-connection-usernamepassword.html#cfn-datazone-connection-usernamepassword-username
            '''
            result = self._values.get("username")
            assert result is not None, "Required property 'username' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UsernamePasswordProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnConnectionProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "environment_identifier": "environmentIdentifier",
        "name": "name",
        "aws_location": "awsLocation",
        "description": "description",
        "props": "props",
    },
)
class CfnConnectionProps:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        environment_identifier: builtins.str,
        name: builtins.str,
        aws_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.AwsLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        props: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.ConnectionPropertiesInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnection``.

        :param domain_identifier: The ID of the domain where the connection is created.
        :param environment_identifier: The ID of the environment where the connection is created.
        :param name: The name of the connection.
        :param aws_location: The location where the connection is created.
        :param description: Connection description.
        :param props: Connection props.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-connection.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_connection_props = datazone.CfnConnectionProps(
                domain_identifier="domainIdentifier",
                environment_identifier="environmentIdentifier",
                name="name",
            
                # the properties below are optional
                aws_location=datazone.CfnConnection.AwsLocationProperty(
                    access_role="accessRole",
                    aws_account_id="awsAccountId",
                    aws_region="awsRegion",
                    iam_connection_id="iamConnectionId"
                ),
                description="description",
                props=datazone.CfnConnection.ConnectionPropertiesInputProperty(
                    athena_properties=datazone.CfnConnection.AthenaPropertiesInputProperty(
                        workgroup_name="workgroupName"
                    ),
                    glue_properties=datazone.CfnConnection.GluePropertiesInputProperty(
                        glue_connection_input=datazone.CfnConnection.GlueConnectionInputProperty(
                            athena_properties={
                                "athena_properties_key": "athenaProperties"
                            },
                            authentication_configuration=datazone.CfnConnection.AuthenticationConfigurationInputProperty(
                                authentication_type="authenticationType",
                                basic_authentication_credentials=datazone.CfnConnection.BasicAuthenticationCredentialsProperty(
                                    password="password",
                                    user_name="userName"
                                ),
                                custom_authentication_credentials={
                                    "custom_authentication_credentials_key": "customAuthenticationCredentials"
                                },
                                kms_key_arn="kmsKeyArn",
                                o_auth2_properties=datazone.CfnConnection.OAuth2PropertiesProperty(
                                    authorization_code_properties=datazone.CfnConnection.AuthorizationCodePropertiesProperty(
                                        authorization_code="authorizationCode",
                                        redirect_uri="redirectUri"
                                    ),
                                    o_auth2_client_application=datazone.CfnConnection.OAuth2ClientApplicationProperty(
                                        aws_managed_client_application_reference="awsManagedClientApplicationReference",
                                        user_managed_client_application_client_id="userManagedClientApplicationClientId"
                                    ),
                                    o_auth2_credentials=datazone.CfnConnection.GlueOAuth2CredentialsProperty(
                                        access_token="accessToken",
                                        jwt_token="jwtToken",
                                        refresh_token="refreshToken",
                                        user_managed_client_application_client_secret="userManagedClientApplicationClientSecret"
                                    ),
                                    o_auth2_grant_type="oAuth2GrantType",
                                    token_url="tokenUrl",
                                    token_url_parameters_map={
                                        "token_url_parameters_map_key": "tokenUrlParametersMap"
                                    }
                                ),
                                secret_arn="secretArn"
                            ),
                            connection_properties={
                                "connection_properties_key": "connectionProperties"
                            },
                            connection_type="connectionType",
                            description="description",
                            match_criteria="matchCriteria",
                            name="name",
                            physical_connection_requirements=datazone.CfnConnection.PhysicalConnectionRequirementsProperty(
                                availability_zone="availabilityZone",
                                security_group_id_list=["securityGroupIdList"],
                                subnet_id="subnetId",
                                subnet_id_list=["subnetIdList"]
                            ),
                            python_properties={
                                "python_properties_key": "pythonProperties"
                            },
                            spark_properties={
                                "spark_properties_key": "sparkProperties"
                            },
                            validate_credentials=False,
                            validate_for_compute_environments=["validateForComputeEnvironments"]
                        )
                    ),
                    hyper_pod_properties=datazone.CfnConnection.HyperPodPropertiesInputProperty(
                        cluster_name="clusterName"
                    ),
                    iam_properties=datazone.CfnConnection.IamPropertiesInputProperty(
                        glue_lineage_sync_enabled=False
                    ),
                    redshift_properties=datazone.CfnConnection.RedshiftPropertiesInputProperty(
                        credentials=datazone.CfnConnection.RedshiftCredentialsProperty(
                            secret_arn="secretArn",
                            username_password=datazone.CfnConnection.UsernamePasswordProperty(
                                password="password",
                                username="username"
                            )
                        ),
                        database_name="databaseName",
                        host="host",
                        lineage_sync=datazone.CfnConnection.RedshiftLineageSyncConfigurationInputProperty(
                            enabled=False,
                            schedule=datazone.CfnConnection.LineageSyncScheduleProperty(
                                schedule="schedule"
                            )
                        ),
                        port=123,
                        storage=datazone.CfnConnection.RedshiftStoragePropertiesProperty(
                            cluster_name="clusterName",
                            workgroup_name="workgroupName"
                        )
                    ),
                    spark_emr_properties=datazone.CfnConnection.SparkEmrPropertiesInputProperty(
                        compute_arn="computeArn",
                        instance_profile_arn="instanceProfileArn",
                        java_virtual_env="javaVirtualEnv",
                        log_uri="logUri",
                        python_virtual_env="pythonVirtualEnv",
                        runtime_role="runtimeRole",
                        trusted_certificates_s3_uri="trustedCertificatesS3Uri"
                    ),
                    spark_glue_properties=datazone.CfnConnection.SparkGluePropertiesInputProperty(
                        additional_args=datazone.CfnConnection.SparkGlueArgsProperty(
                            connection="connection"
                        ),
                        glue_connection_name="glueConnectionName",
                        glue_version="glueVersion",
                        idle_timeout=123,
                        java_virtual_env="javaVirtualEnv",
                        number_of_workers=123,
                        python_virtual_env="pythonVirtualEnv",
                        worker_type="workerType"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8797ba459ed68920849c7b460987b708539d45c9d479ab52091ec466aebc8432)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument environment_identifier", value=environment_identifier, expected_type=type_hints["environment_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument aws_location", value=aws_location, expected_type=type_hints["aws_location"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
            "name": name,
        }
        if aws_location is not None:
            self._values["aws_location"] = aws_location
        if description is not None:
            self._values["description"] = description
        if props is not None:
            self._values["props"] = props

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The ID of the domain where the connection is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-connection.html#cfn-datazone-connection-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_identifier(self) -> builtins.str:
        '''The ID of the environment where the connection is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-connection.html#cfn-datazone-connection-environmentidentifier
        '''
        result = self._values.get("environment_identifier")
        assert result is not None, "Required property 'environment_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-connection.html#cfn-datazone-connection-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnection.AwsLocationProperty]]:
        '''The location where the connection is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-connection.html#cfn-datazone-connection-awslocation
        '''
        result = self._values.get("aws_location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnection.AwsLocationProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Connection description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-connection.html#cfn-datazone-connection-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def props(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnection.ConnectionPropertiesInputProperty]]:
        '''Connection props.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-connection.html#cfn-datazone-connection-props
        '''
        result = self._values.get("props")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnection.ConnectionPropertiesInputProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDataSource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource",
):
    '''The ``AWS::DataZone::DataSource`` resource specifies an Amazon DataZone data source that is used to import technical metadata of assets (data) from the source databases or data warehouses into Amazon DataZone.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html
    :cloudformationResource: AWS::DataZone::DataSource
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_data_source = datazone.CfnDataSource(self, "MyCfnDataSource",
            domain_identifier="domainIdentifier",
            name="name",
            project_identifier="projectIdentifier",
            type="type",
        
            # the properties below are optional
            asset_forms_input=[datazone.CfnDataSource.FormInputProperty(
                form_name="formName",
        
                # the properties below are optional
                content="content",
                type_identifier="typeIdentifier",
                type_revision="typeRevision"
            )],
            configuration=datazone.CfnDataSource.DataSourceConfigurationInputProperty(
                glue_run_configuration=datazone.CfnDataSource.GlueRunConfigurationInputProperty(
                    relational_filter_configurations=[datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                        database_name="databaseName",
        
                        # the properties below are optional
                        filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                            expression="expression",
                            type="type"
                        )],
                        schema_name="schemaName"
                    )],
        
                    # the properties below are optional
                    auto_import_data_quality_result=False,
                    catalog_name="catalogName",
                    data_access_role="dataAccessRole"
                ),
                redshift_run_configuration=datazone.CfnDataSource.RedshiftRunConfigurationInputProperty(
                    relational_filter_configurations=[datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                        database_name="databaseName",
        
                        # the properties below are optional
                        filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                            expression="expression",
                            type="type"
                        )],
                        schema_name="schemaName"
                    )],
        
                    # the properties below are optional
                    data_access_role="dataAccessRole",
                    redshift_credential_configuration=datazone.CfnDataSource.RedshiftCredentialConfigurationProperty(
                        secret_manager_arn="secretManagerArn"
                    ),
                    redshift_storage=datazone.CfnDataSource.RedshiftStorageProperty(
                        redshift_cluster_source=datazone.CfnDataSource.RedshiftClusterStorageProperty(
                            cluster_name="clusterName"
                        ),
                        redshift_serverless_source=datazone.CfnDataSource.RedshiftServerlessStorageProperty(
                            workgroup_name="workgroupName"
                        )
                    )
                ),
                sage_maker_run_configuration=datazone.CfnDataSource.SageMakerRunConfigurationInputProperty(
                    tracking_assets={
                        "tracking_assets_key": ["trackingAssets"]
                    }
                )
            ),
            connection_identifier="connectionIdentifier",
            description="description",
            enable_setting="enableSetting",
            environment_identifier="environmentIdentifier",
            publish_on_import=False,
            recommendation=datazone.CfnDataSource.RecommendationConfigurationProperty(
                enable_business_name_generation=False
            ),
            schedule=datazone.CfnDataSource.ScheduleConfigurationProperty(
                schedule="schedule",
                timezone="timezone"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_identifier: builtins.str,
        name: builtins.str,
        project_identifier: builtins.str,
        type: builtins.str,
        asset_forms_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.FormInputProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.DataSourceConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        connection_identifier: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        enable_setting: typing.Optional[builtins.str] = None,
        environment_identifier: typing.Optional[builtins.str] = None,
        publish_on_import: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        recommendation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RecommendationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.ScheduleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_identifier: The ID of the Amazon DataZone domain where the data source is created.
        :param name: The name of the data source.
        :param project_identifier: The identifier of the Amazon DataZone project in which you want to add this data source.
        :param type: The type of the data source. In Amazon DataZone, you can use data sources to import technical metadata of assets (data) from the source databases or data warehouses into Amazon DataZone. In the current release of Amazon DataZone, you can create and run data sources for AWS Glue and Amazon Redshift.
        :param asset_forms_input: The metadata forms attached to the assets that the data source works with.
        :param configuration: The configuration of the data source.
        :param connection_identifier: The unique identifier of a connection used to fetch relevant parameters from connection during Datasource run.
        :param description: The description of the data source.
        :param enable_setting: Specifies whether the data source is enabled.
        :param environment_identifier: The unique identifier of the Amazon DataZone environment to which the data source publishes assets.
        :param publish_on_import: Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.
        :param recommendation: Specifies whether the business name generation is to be enabled for this data source.
        :param schedule: The schedule of the data source runs.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b74a6ac4c3e98c769e70eb9dc6e8b5f1e8f347a3615d992ea7f1c0d421505732)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataSourceProps(
            domain_identifier=domain_identifier,
            name=name,
            project_identifier=project_identifier,
            type=type,
            asset_forms_input=asset_forms_input,
            configuration=configuration,
            connection_identifier=connection_identifier,
            description=description,
            enable_setting=enable_setting,
            environment_identifier=environment_identifier,
            publish_on_import=publish_on_import,
            recommendation=recommendation,
            schedule=schedule,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33bcdad9dc3f66143343138916ff460345630898241997119efe034ff66c6a2d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__514e677208a85632dfb8a4fcf6a71bea051c78567845845ff000fb632aab7b5e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectionId")
    def attr_connection_id(self) -> builtins.str:
        '''The connection ID that's part of the data source summary.

        :cloudformationAttribute: ConnectionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectionId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when the data source was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The ID of the Amazon DataZone domain in which the data source exists.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentId")
    def attr_environment_id(self) -> builtins.str:
        '''The ID of the environment in which the data source exists.

        :cloudformationAttribute: EnvironmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The identifier of the data source run.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastRunAssetCount")
    def attr_last_run_asset_count(self) -> _IResolvable_da3f097b:
        '''The count of the assets created during the last data source run.

        :cloudformationAttribute: LastRunAssetCount
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrLastRunAssetCount"))

    @builtins.property
    @jsii.member(jsii_name="attrLastRunAt")
    def attr_last_run_at(self) -> builtins.str:
        '''The timestamp of when the data source run was last performed.

        :cloudformationAttribute: LastRunAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastRunAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastRunStatus")
    def attr_last_run_status(self) -> builtins.str:
        '''The status of the last data source run.

        :cloudformationAttribute: LastRunStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastRunStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrProjectId")
    def attr_project_id(self) -> builtins.str:
        '''The project ID included in the data source run activity.

        :cloudformationAttribute: ProjectId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the data source.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp of when the data source was updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The ID of the Amazon DataZone domain where the data source is created.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a7af31e6c5b528548b0d530d4c772805fb61420d812ed44382c7c390086f11a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the data source.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2821916d0fb71bfe9878d75d49136fb173b8984bb70e31a4a9720eebf6db3ab3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="projectIdentifier")
    def project_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone project in which you want to add this data source.'''
        return typing.cast(builtins.str, jsii.get(self, "projectIdentifier"))

    @project_identifier.setter
    def project_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__132e7e2cf26f81c0a6085283f4e8d4d9f57da8d3612dd55ee6749c192a2d2d48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the data source.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d073c13da920100b2d471eb086a45db9d741e4fba0dc8a0677ffe38913dffe2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assetFormsInput")
    def asset_forms_input(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.FormInputProperty"]]]]:
        '''The metadata forms attached to the assets that the data source works with.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.FormInputProperty"]]]], jsii.get(self, "assetFormsInput"))

    @asset_forms_input.setter
    def asset_forms_input(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.FormInputProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd33f5216eca4a4d866e941b183a5ef445088a5e6ecec69e2fbc695f6b40c3c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetFormsInput", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DataSourceConfigurationInputProperty"]]:
        '''The configuration of the data source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DataSourceConfigurationInputProperty"]], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DataSourceConfigurationInputProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89afb772730c8209e27316b8af14ef1a6fce9f26db9f31432460eff964f55b9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="connectionIdentifier")
    def connection_identifier(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of a connection used to fetch relevant parameters from connection during Datasource run.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionIdentifier"))

    @connection_identifier.setter
    def connection_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caff1a5a915d2678ed1266a9c2f82efe4b3b9c3fcccd444c54fd11e49a43068e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the data source.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7e5b5e600ceeed0171e7700fd1bb1de08837412c76a72396b54b2ddfcd29970)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enableSetting")
    def enable_setting(self) -> typing.Optional[builtins.str]:
        '''Specifies whether the data source is enabled.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enableSetting"))

    @enable_setting.setter
    def enable_setting(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c4b8af5e1647731587c5aaa0ac03d7e6980729c429135de819a778bb0e7a2eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSetting", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentIdentifier")
    def environment_identifier(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the Amazon DataZone environment to which the data source publishes assets.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentIdentifier"))

    @environment_identifier.setter
    def environment_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ed64595e5e156084952dfe11e1e064218cba6affcb8bf2736d3e0a177b08bea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publishOnImport")
    def publish_on_import(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "publishOnImport"))

    @publish_on_import.setter
    def publish_on_import(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b8ce503c85a6ffdd243c0997e3ddab5dbbb39fc65cc2c74982964209c9e4eaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publishOnImport", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="recommendation")
    def recommendation(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RecommendationConfigurationProperty"]]:
        '''Specifies whether the business name generation is to be enabled for this data source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RecommendationConfigurationProperty"]], jsii.get(self, "recommendation"))

    @recommendation.setter
    def recommendation(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RecommendationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__213e25d07ce5c23cedc981ed540f97a1577533cd3dab4f6e0a08f166e38cfb49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recommendation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.ScheduleConfigurationProperty"]]:
        '''The schedule of the data source runs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.ScheduleConfigurationProperty"]], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.ScheduleConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__693f7d02be84739f3d95375e94a3b4c964749b34e7dbf67ac0aa2b011ca3f625)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.DataSourceConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "glue_run_configuration": "glueRunConfiguration",
            "redshift_run_configuration": "redshiftRunConfiguration",
            "sage_maker_run_configuration": "sageMakerRunConfiguration",
        },
    )
    class DataSourceConfigurationInputProperty:
        def __init__(
            self,
            *,
            glue_run_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.GlueRunConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            redshift_run_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RedshiftRunConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sage_maker_run_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.SageMakerRunConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration of the data source.

            :param glue_run_configuration: The configuration of the AWS Glue data source.
            :param redshift_run_configuration: The configuration of the Amazon Redshift data source.
            :param sage_maker_run_configuration: The configuration details of the Amazon SageMaker data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-datasourceconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                data_source_configuration_input_property = datazone.CfnDataSource.DataSourceConfigurationInputProperty(
                    glue_run_configuration=datazone.CfnDataSource.GlueRunConfigurationInputProperty(
                        relational_filter_configurations=[datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                            database_name="databaseName",
                
                            # the properties below are optional
                            filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                                expression="expression",
                                type="type"
                            )],
                            schema_name="schemaName"
                        )],
                
                        # the properties below are optional
                        auto_import_data_quality_result=False,
                        catalog_name="catalogName",
                        data_access_role="dataAccessRole"
                    ),
                    redshift_run_configuration=datazone.CfnDataSource.RedshiftRunConfigurationInputProperty(
                        relational_filter_configurations=[datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                            database_name="databaseName",
                
                            # the properties below are optional
                            filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                                expression="expression",
                                type="type"
                            )],
                            schema_name="schemaName"
                        )],
                
                        # the properties below are optional
                        data_access_role="dataAccessRole",
                        redshift_credential_configuration=datazone.CfnDataSource.RedshiftCredentialConfigurationProperty(
                            secret_manager_arn="secretManagerArn"
                        ),
                        redshift_storage=datazone.CfnDataSource.RedshiftStorageProperty(
                            redshift_cluster_source=datazone.CfnDataSource.RedshiftClusterStorageProperty(
                                cluster_name="clusterName"
                            ),
                            redshift_serverless_source=datazone.CfnDataSource.RedshiftServerlessStorageProperty(
                                workgroup_name="workgroupName"
                            )
                        )
                    ),
                    sage_maker_run_configuration=datazone.CfnDataSource.SageMakerRunConfigurationInputProperty(
                        tracking_assets={
                            "tracking_assets_key": ["trackingAssets"]
                        }
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e9bda82e8d6905101b134276b283067e9b4fc8445ba4e98917ea7cd2937c5828)
                check_type(argname="argument glue_run_configuration", value=glue_run_configuration, expected_type=type_hints["glue_run_configuration"])
                check_type(argname="argument redshift_run_configuration", value=redshift_run_configuration, expected_type=type_hints["redshift_run_configuration"])
                check_type(argname="argument sage_maker_run_configuration", value=sage_maker_run_configuration, expected_type=type_hints["sage_maker_run_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if glue_run_configuration is not None:
                self._values["glue_run_configuration"] = glue_run_configuration
            if redshift_run_configuration is not None:
                self._values["redshift_run_configuration"] = redshift_run_configuration
            if sage_maker_run_configuration is not None:
                self._values["sage_maker_run_configuration"] = sage_maker_run_configuration

        @builtins.property
        def glue_run_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.GlueRunConfigurationInputProperty"]]:
            '''The configuration of the AWS Glue data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-datasourceconfigurationinput.html#cfn-datazone-datasource-datasourceconfigurationinput-gluerunconfiguration
            '''
            result = self._values.get("glue_run_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.GlueRunConfigurationInputProperty"]], result)

        @builtins.property
        def redshift_run_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftRunConfigurationInputProperty"]]:
            '''The configuration of the Amazon Redshift data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-datasourceconfigurationinput.html#cfn-datazone-datasource-datasourceconfigurationinput-redshiftrunconfiguration
            '''
            result = self._values.get("redshift_run_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftRunConfigurationInputProperty"]], result)

        @builtins.property
        def sage_maker_run_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.SageMakerRunConfigurationInputProperty"]]:
            '''The configuration details of the Amazon SageMaker data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-datasourceconfigurationinput.html#cfn-datazone-datasource-datasourceconfigurationinput-sagemakerrunconfiguration
            '''
            result = self._values.get("sage_maker_run_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.SageMakerRunConfigurationInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.FilterExpressionProperty",
        jsii_struct_bases=[],
        name_mapping={"expression": "expression", "type": "type"},
    )
    class FilterExpressionProperty:
        def __init__(self, *, expression: builtins.str, type: builtins.str) -> None:
            '''A filter expression in Amazon DataZone.

            :param expression: The search filter expression.
            :param type: The search filter explresison type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-filterexpression.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                filter_expression_property = datazone.CfnDataSource.FilterExpressionProperty(
                    expression="expression",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb2b40bf6229fe763c7c585fa978f99e3900fbd6916fc58d9065ddc99d90df18)
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "expression": expression,
                "type": type,
            }

        @builtins.property
        def expression(self) -> builtins.str:
            '''The search filter expression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-filterexpression.html#cfn-datazone-datasource-filterexpression-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The search filter explresison type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-filterexpression.html#cfn-datazone-datasource-filterexpression-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterExpressionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.FormInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "form_name": "formName",
            "content": "content",
            "type_identifier": "typeIdentifier",
            "type_revision": "typeRevision",
        },
    )
    class FormInputProperty:
        def __init__(
            self,
            *,
            form_name: builtins.str,
            content: typing.Optional[builtins.str] = None,
            type_identifier: typing.Optional[builtins.str] = None,
            type_revision: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The details of a metadata form.

            :param form_name: The name of the metadata form.
            :param content: The content of the metadata form.
            :param type_identifier: The ID of the metadata form type.
            :param type_revision: The revision of the metadata form type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-forminput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                form_input_property = datazone.CfnDataSource.FormInputProperty(
                    form_name="formName",
                
                    # the properties below are optional
                    content="content",
                    type_identifier="typeIdentifier",
                    type_revision="typeRevision"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e39737bda51e6e9e0b04ce2c0598b00c495cf2dad8f53d4761c7a31ecf92227e)
                check_type(argname="argument form_name", value=form_name, expected_type=type_hints["form_name"])
                check_type(argname="argument content", value=content, expected_type=type_hints["content"])
                check_type(argname="argument type_identifier", value=type_identifier, expected_type=type_hints["type_identifier"])
                check_type(argname="argument type_revision", value=type_revision, expected_type=type_hints["type_revision"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "form_name": form_name,
            }
            if content is not None:
                self._values["content"] = content
            if type_identifier is not None:
                self._values["type_identifier"] = type_identifier
            if type_revision is not None:
                self._values["type_revision"] = type_revision

        @builtins.property
        def form_name(self) -> builtins.str:
            '''The name of the metadata form.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-forminput.html#cfn-datazone-datasource-forminput-formname
            '''
            result = self._values.get("form_name")
            assert result is not None, "Required property 'form_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def content(self) -> typing.Optional[builtins.str]:
            '''The content of the metadata form.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-forminput.html#cfn-datazone-datasource-forminput-content
            '''
            result = self._values.get("content")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type_identifier(self) -> typing.Optional[builtins.str]:
            '''The ID of the metadata form type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-forminput.html#cfn-datazone-datasource-forminput-typeidentifier
            '''
            result = self._values.get("type_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type_revision(self) -> typing.Optional[builtins.str]:
            '''The revision of the metadata form type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-forminput.html#cfn-datazone-datasource-forminput-typerevision
            '''
            result = self._values.get("type_revision")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FormInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.GlueRunConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "relational_filter_configurations": "relationalFilterConfigurations",
            "auto_import_data_quality_result": "autoImportDataQualityResult",
            "catalog_name": "catalogName",
            "data_access_role": "dataAccessRole",
        },
    )
    class GlueRunConfigurationInputProperty:
        def __init__(
            self,
            *,
            relational_filter_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RelationalFilterConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
            auto_import_data_quality_result: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            catalog_name: typing.Optional[builtins.str] = None,
            data_access_role: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration details of the AWS Glue data source.

            :param relational_filter_configurations: The relational filter configurations included in the configuration details of the AWS Glue data source.
            :param auto_import_data_quality_result: Specifies whether to automatically import data quality metrics as part of the data source run.
            :param catalog_name: The catalog name in the AWS Glue run configuration.
            :param data_access_role: The data access role included in the configuration details of the AWS Glue data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-gluerunconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                glue_run_configuration_input_property = datazone.CfnDataSource.GlueRunConfigurationInputProperty(
                    relational_filter_configurations=[datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                        database_name="databaseName",
                
                        # the properties below are optional
                        filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                            expression="expression",
                            type="type"
                        )],
                        schema_name="schemaName"
                    )],
                
                    # the properties below are optional
                    auto_import_data_quality_result=False,
                    catalog_name="catalogName",
                    data_access_role="dataAccessRole"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ad6a5a243d0193849a3ba940cfbd956439268966f2ff08bff1fbcf5af20fe953)
                check_type(argname="argument relational_filter_configurations", value=relational_filter_configurations, expected_type=type_hints["relational_filter_configurations"])
                check_type(argname="argument auto_import_data_quality_result", value=auto_import_data_quality_result, expected_type=type_hints["auto_import_data_quality_result"])
                check_type(argname="argument catalog_name", value=catalog_name, expected_type=type_hints["catalog_name"])
                check_type(argname="argument data_access_role", value=data_access_role, expected_type=type_hints["data_access_role"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "relational_filter_configurations": relational_filter_configurations,
            }
            if auto_import_data_quality_result is not None:
                self._values["auto_import_data_quality_result"] = auto_import_data_quality_result
            if catalog_name is not None:
                self._values["catalog_name"] = catalog_name
            if data_access_role is not None:
                self._values["data_access_role"] = data_access_role

        @builtins.property
        def relational_filter_configurations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RelationalFilterConfigurationProperty"]]]:
            '''The relational filter configurations included in the configuration details of the AWS Glue data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-gluerunconfigurationinput.html#cfn-datazone-datasource-gluerunconfigurationinput-relationalfilterconfigurations
            '''
            result = self._values.get("relational_filter_configurations")
            assert result is not None, "Required property 'relational_filter_configurations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RelationalFilterConfigurationProperty"]]], result)

        @builtins.property
        def auto_import_data_quality_result(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether to automatically import data quality metrics as part of the data source run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-gluerunconfigurationinput.html#cfn-datazone-datasource-gluerunconfigurationinput-autoimportdataqualityresult
            '''
            result = self._values.get("auto_import_data_quality_result")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def catalog_name(self) -> typing.Optional[builtins.str]:
            '''The catalog name in the AWS Glue run configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-gluerunconfigurationinput.html#cfn-datazone-datasource-gluerunconfigurationinput-catalogname
            '''
            result = self._values.get("catalog_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_access_role(self) -> typing.Optional[builtins.str]:
            '''The data access role included in the configuration details of the AWS Glue data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-gluerunconfigurationinput.html#cfn-datazone-datasource-gluerunconfigurationinput-dataaccessrole
            '''
            result = self._values.get("data_access_role")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlueRunConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.RecommendationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_business_name_generation": "enableBusinessNameGeneration",
        },
    )
    class RecommendationConfigurationProperty:
        def __init__(
            self,
            *,
            enable_business_name_generation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The recommendation configuration for the data source.

            :param enable_business_name_generation: Specifies whether automatic business name generation is to be enabled or not as part of the recommendation configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-recommendationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                recommendation_configuration_property = datazone.CfnDataSource.RecommendationConfigurationProperty(
                    enable_business_name_generation=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b892cb470f7ea420aeb56956a5375b815b6b2a91d0e3d5aaa0a3461f5924b22)
                check_type(argname="argument enable_business_name_generation", value=enable_business_name_generation, expected_type=type_hints["enable_business_name_generation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enable_business_name_generation is not None:
                self._values["enable_business_name_generation"] = enable_business_name_generation

        @builtins.property
        def enable_business_name_generation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether automatic business name generation is to be enabled or not as part of the recommendation configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-recommendationconfiguration.html#cfn-datazone-datasource-recommendationconfiguration-enablebusinessnamegeneration
            '''
            result = self._values.get("enable_business_name_generation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecommendationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.RedshiftClusterStorageProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_name": "clusterName"},
    )
    class RedshiftClusterStorageProperty:
        def __init__(self, *, cluster_name: builtins.str) -> None:
            '''The details of the Amazon Redshift cluster storage.

            :param cluster_name: The name of an Amazon Redshift cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftclusterstorage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                redshift_cluster_storage_property = datazone.CfnDataSource.RedshiftClusterStorageProperty(
                    cluster_name="clusterName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cf5e238c98cd0e25a8234c800e1db4699c482f8c18eb4b1a30bdf8afd3ca2718)
                check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cluster_name": cluster_name,
            }

        @builtins.property
        def cluster_name(self) -> builtins.str:
            '''The name of an Amazon Redshift cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftclusterstorage.html#cfn-datazone-datasource-redshiftclusterstorage-clustername
            '''
            result = self._values.get("cluster_name")
            assert result is not None, "Required property 'cluster_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftClusterStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.RedshiftCredentialConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"secret_manager_arn": "secretManagerArn"},
    )
    class RedshiftCredentialConfigurationProperty:
        def __init__(self, *, secret_manager_arn: builtins.str) -> None:
            '''The details of the credentials required to access an Amazon Redshift cluster.

            :param secret_manager_arn: The ARN of a secret manager for an Amazon Redshift cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftcredentialconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                redshift_credential_configuration_property = datazone.CfnDataSource.RedshiftCredentialConfigurationProperty(
                    secret_manager_arn="secretManagerArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1df8fcf30634f3b35250f98172cf307551610fbd637ef517691ae5581ccb5f66)
                check_type(argname="argument secret_manager_arn", value=secret_manager_arn, expected_type=type_hints["secret_manager_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "secret_manager_arn": secret_manager_arn,
            }

        @builtins.property
        def secret_manager_arn(self) -> builtins.str:
            '''The ARN of a secret manager for an Amazon Redshift cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftcredentialconfiguration.html#cfn-datazone-datasource-redshiftcredentialconfiguration-secretmanagerarn
            '''
            result = self._values.get("secret_manager_arn")
            assert result is not None, "Required property 'secret_manager_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftCredentialConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.RedshiftRunConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "relational_filter_configurations": "relationalFilterConfigurations",
            "data_access_role": "dataAccessRole",
            "redshift_credential_configuration": "redshiftCredentialConfiguration",
            "redshift_storage": "redshiftStorage",
        },
    )
    class RedshiftRunConfigurationInputProperty:
        def __init__(
            self,
            *,
            relational_filter_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RelationalFilterConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
            data_access_role: typing.Optional[builtins.str] = None,
            redshift_credential_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RedshiftCredentialConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            redshift_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RedshiftStorageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The relational filter configurations included in the configuration details of the Amazon Redshift data source.

            :param relational_filter_configurations: The relational filter configurations included in the configuration details of the AWS Glue data source.
            :param data_access_role: The data access role included in the configuration details of the Amazon Redshift data source.
            :param redshift_credential_configuration: The details of the credentials required to access an Amazon Redshift cluster.
            :param redshift_storage: The details of the Amazon Redshift storage as part of the configuration of an Amazon Redshift data source run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftrunconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                redshift_run_configuration_input_property = datazone.CfnDataSource.RedshiftRunConfigurationInputProperty(
                    relational_filter_configurations=[datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                        database_name="databaseName",
                
                        # the properties below are optional
                        filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                            expression="expression",
                            type="type"
                        )],
                        schema_name="schemaName"
                    )],
                
                    # the properties below are optional
                    data_access_role="dataAccessRole",
                    redshift_credential_configuration=datazone.CfnDataSource.RedshiftCredentialConfigurationProperty(
                        secret_manager_arn="secretManagerArn"
                    ),
                    redshift_storage=datazone.CfnDataSource.RedshiftStorageProperty(
                        redshift_cluster_source=datazone.CfnDataSource.RedshiftClusterStorageProperty(
                            cluster_name="clusterName"
                        ),
                        redshift_serverless_source=datazone.CfnDataSource.RedshiftServerlessStorageProperty(
                            workgroup_name="workgroupName"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5dd4c8b6216739fc8295ada55b58407d555982639c53118e9be94f72b8eb8e7c)
                check_type(argname="argument relational_filter_configurations", value=relational_filter_configurations, expected_type=type_hints["relational_filter_configurations"])
                check_type(argname="argument data_access_role", value=data_access_role, expected_type=type_hints["data_access_role"])
                check_type(argname="argument redshift_credential_configuration", value=redshift_credential_configuration, expected_type=type_hints["redshift_credential_configuration"])
                check_type(argname="argument redshift_storage", value=redshift_storage, expected_type=type_hints["redshift_storage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "relational_filter_configurations": relational_filter_configurations,
            }
            if data_access_role is not None:
                self._values["data_access_role"] = data_access_role
            if redshift_credential_configuration is not None:
                self._values["redshift_credential_configuration"] = redshift_credential_configuration
            if redshift_storage is not None:
                self._values["redshift_storage"] = redshift_storage

        @builtins.property
        def relational_filter_configurations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RelationalFilterConfigurationProperty"]]]:
            '''The relational filter configurations included in the configuration details of the AWS Glue data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftrunconfigurationinput.html#cfn-datazone-datasource-redshiftrunconfigurationinput-relationalfilterconfigurations
            '''
            result = self._values.get("relational_filter_configurations")
            assert result is not None, "Required property 'relational_filter_configurations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RelationalFilterConfigurationProperty"]]], result)

        @builtins.property
        def data_access_role(self) -> typing.Optional[builtins.str]:
            '''The data access role included in the configuration details of the Amazon Redshift data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftrunconfigurationinput.html#cfn-datazone-datasource-redshiftrunconfigurationinput-dataaccessrole
            '''
            result = self._values.get("data_access_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def redshift_credential_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftCredentialConfigurationProperty"]]:
            '''The details of the credentials required to access an Amazon Redshift cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftrunconfigurationinput.html#cfn-datazone-datasource-redshiftrunconfigurationinput-redshiftcredentialconfiguration
            '''
            result = self._values.get("redshift_credential_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftCredentialConfigurationProperty"]], result)

        @builtins.property
        def redshift_storage(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftStorageProperty"]]:
            '''The details of the Amazon Redshift storage as part of the configuration of an Amazon Redshift data source run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftrunconfigurationinput.html#cfn-datazone-datasource-redshiftrunconfigurationinput-redshiftstorage
            '''
            result = self._values.get("redshift_storage")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftStorageProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftRunConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.RedshiftServerlessStorageProperty",
        jsii_struct_bases=[],
        name_mapping={"workgroup_name": "workgroupName"},
    )
    class RedshiftServerlessStorageProperty:
        def __init__(self, *, workgroup_name: builtins.str) -> None:
            '''The details of the Amazon Redshift Serverless workgroup storage.

            :param workgroup_name: The name of the Amazon Redshift Serverless workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftserverlessstorage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                redshift_serverless_storage_property = datazone.CfnDataSource.RedshiftServerlessStorageProperty(
                    workgroup_name="workgroupName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c58e081ae0c5b103243a5fb5e44d072e16021860d239dd719e8ecaa4696f2da8)
                check_type(argname="argument workgroup_name", value=workgroup_name, expected_type=type_hints["workgroup_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "workgroup_name": workgroup_name,
            }

        @builtins.property
        def workgroup_name(self) -> builtins.str:
            '''The name of the Amazon Redshift Serverless workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftserverlessstorage.html#cfn-datazone-datasource-redshiftserverlessstorage-workgroupname
            '''
            result = self._values.get("workgroup_name")
            assert result is not None, "Required property 'workgroup_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftServerlessStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.RedshiftStorageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "redshift_cluster_source": "redshiftClusterSource",
            "redshift_serverless_source": "redshiftServerlessSource",
        },
    )
    class RedshiftStorageProperty:
        def __init__(
            self,
            *,
            redshift_cluster_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RedshiftClusterStorageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            redshift_serverless_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RedshiftServerlessStorageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The details of the Amazon Redshift storage as part of the configuration of an Amazon Redshift data source run.

            :param redshift_cluster_source: The details of the Amazon Redshift cluster source.
            :param redshift_serverless_source: The details of the Amazon Redshift Serverless workgroup source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftstorage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                redshift_storage_property = datazone.CfnDataSource.RedshiftStorageProperty(
                    redshift_cluster_source=datazone.CfnDataSource.RedshiftClusterStorageProperty(
                        cluster_name="clusterName"
                    ),
                    redshift_serverless_source=datazone.CfnDataSource.RedshiftServerlessStorageProperty(
                        workgroup_name="workgroupName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6959cf31dac7c5d3c9ee4d255059c5f6007a01d1da657810b6e3e44f31806173)
                check_type(argname="argument redshift_cluster_source", value=redshift_cluster_source, expected_type=type_hints["redshift_cluster_source"])
                check_type(argname="argument redshift_serverless_source", value=redshift_serverless_source, expected_type=type_hints["redshift_serverless_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if redshift_cluster_source is not None:
                self._values["redshift_cluster_source"] = redshift_cluster_source
            if redshift_serverless_source is not None:
                self._values["redshift_serverless_source"] = redshift_serverless_source

        @builtins.property
        def redshift_cluster_source(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftClusterStorageProperty"]]:
            '''The details of the Amazon Redshift cluster source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftstorage.html#cfn-datazone-datasource-redshiftstorage-redshiftclustersource
            '''
            result = self._values.get("redshift_cluster_source")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftClusterStorageProperty"]], result)

        @builtins.property
        def redshift_serverless_source(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftServerlessStorageProperty"]]:
            '''The details of the Amazon Redshift Serverless workgroup source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftstorage.html#cfn-datazone-datasource-redshiftstorage-redshiftserverlesssource
            '''
            result = self._values.get("redshift_serverless_source")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftServerlessStorageProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.RelationalFilterConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_name": "databaseName",
            "filter_expressions": "filterExpressions",
            "schema_name": "schemaName",
        },
    )
    class RelationalFilterConfigurationProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            filter_expressions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.FilterExpressionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            schema_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The relational filter configuration for the data source.

            :param database_name: The database name specified in the relational filter configuration for the data source.
            :param filter_expressions: The filter expressions specified in the relational filter configuration for the data source.
            :param schema_name: The schema name specified in the relational filter configuration for the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-relationalfilterconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                relational_filter_configuration_property = datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                    database_name="databaseName",
                
                    # the properties below are optional
                    filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                        expression="expression",
                        type="type"
                    )],
                    schema_name="schemaName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b69950b3dd7224f1119f8c5e6a2c8675594377bc1e5845a101f3b5f210681258)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument filter_expressions", value=filter_expressions, expected_type=type_hints["filter_expressions"])
                check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "database_name": database_name,
            }
            if filter_expressions is not None:
                self._values["filter_expressions"] = filter_expressions
            if schema_name is not None:
                self._values["schema_name"] = schema_name

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The database name specified in the relational filter configuration for the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-relationalfilterconfiguration.html#cfn-datazone-datasource-relationalfilterconfiguration-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def filter_expressions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.FilterExpressionProperty"]]]]:
            '''The filter expressions specified in the relational filter configuration for the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-relationalfilterconfiguration.html#cfn-datazone-datasource-relationalfilterconfiguration-filterexpressions
            '''
            result = self._values.get("filter_expressions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.FilterExpressionProperty"]]]], result)

        @builtins.property
        def schema_name(self) -> typing.Optional[builtins.str]:
            '''The schema name specified in the relational filter configuration for the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-relationalfilterconfiguration.html#cfn-datazone-datasource-relationalfilterconfiguration-schemaname
            '''
            result = self._values.get("schema_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RelationalFilterConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.SageMakerRunConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"tracking_assets": "trackingAssets"},
    )
    class SageMakerRunConfigurationInputProperty:
        def __init__(
            self,
            *,
            tracking_assets: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Sequence[builtins.str]]],
        ) -> None:
            '''The configuration details of the Amazon SageMaker data source.

            :param tracking_assets: The tracking assets of the Amazon SageMaker run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-sagemakerrunconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                sage_maker_run_configuration_input_property = datazone.CfnDataSource.SageMakerRunConfigurationInputProperty(
                    tracking_assets={
                        "tracking_assets_key": ["trackingAssets"]
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__28babf5c4c5363adc4e0e12e10b52800bdefbc80558e5eb5e050bd3e2c484591)
                check_type(argname="argument tracking_assets", value=tracking_assets, expected_type=type_hints["tracking_assets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "tracking_assets": tracking_assets,
            }

        @builtins.property
        def tracking_assets(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.List[builtins.str]]]:
            '''The tracking assets of the Amazon SageMaker run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-sagemakerrunconfigurationinput.html#cfn-datazone-datasource-sagemakerrunconfigurationinput-trackingassets
            '''
            result = self._values.get("tracking_assets")
            assert result is not None, "Required property 'tracking_assets' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.List[builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SageMakerRunConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.ScheduleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"schedule": "schedule", "timezone": "timezone"},
    )
    class ScheduleConfigurationProperty:
        def __init__(
            self,
            *,
            schedule: typing.Optional[builtins.str] = None,
            timezone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The details of the schedule of the data source runs.

            :param schedule: The schedule of the data source runs.
            :param timezone: The timezone of the data source run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-scheduleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                schedule_configuration_property = datazone.CfnDataSource.ScheduleConfigurationProperty(
                    schedule="schedule",
                    timezone="timezone"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9fc1ad55dd2850c09e234b6cbea1fb383c32658a6b0f4b3e6c9ec1d67d8ae10c)
                check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
                check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if schedule is not None:
                self._values["schedule"] = schedule
            if timezone is not None:
                self._values["timezone"] = timezone

        @builtins.property
        def schedule(self) -> typing.Optional[builtins.str]:
            '''The schedule of the data source runs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-scheduleconfiguration.html#cfn-datazone-datasource-scheduleconfiguration-schedule
            '''
            result = self._values.get("schedule")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timezone(self) -> typing.Optional[builtins.str]:
            '''The timezone of the data source run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-scheduleconfiguration.html#cfn-datazone-datasource-scheduleconfiguration-timezone
            '''
            result = self._values.get("timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "name": "name",
        "project_identifier": "projectIdentifier",
        "type": "type",
        "asset_forms_input": "assetFormsInput",
        "configuration": "configuration",
        "connection_identifier": "connectionIdentifier",
        "description": "description",
        "enable_setting": "enableSetting",
        "environment_identifier": "environmentIdentifier",
        "publish_on_import": "publishOnImport",
        "recommendation": "recommendation",
        "schedule": "schedule",
    },
)
class CfnDataSourceProps:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        name: builtins.str,
        project_identifier: builtins.str,
        type: builtins.str,
        asset_forms_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.FormInputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DataSourceConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        connection_identifier: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        enable_setting: typing.Optional[builtins.str] = None,
        environment_identifier: typing.Optional[builtins.str] = None,
        publish_on_import: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        recommendation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RecommendationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.ScheduleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataSource``.

        :param domain_identifier: The ID of the Amazon DataZone domain where the data source is created.
        :param name: The name of the data source.
        :param project_identifier: The identifier of the Amazon DataZone project in which you want to add this data source.
        :param type: The type of the data source. In Amazon DataZone, you can use data sources to import technical metadata of assets (data) from the source databases or data warehouses into Amazon DataZone. In the current release of Amazon DataZone, you can create and run data sources for AWS Glue and Amazon Redshift.
        :param asset_forms_input: The metadata forms attached to the assets that the data source works with.
        :param configuration: The configuration of the data source.
        :param connection_identifier: The unique identifier of a connection used to fetch relevant parameters from connection during Datasource run.
        :param description: The description of the data source.
        :param enable_setting: Specifies whether the data source is enabled.
        :param environment_identifier: The unique identifier of the Amazon DataZone environment to which the data source publishes assets.
        :param publish_on_import: Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.
        :param recommendation: Specifies whether the business name generation is to be enabled for this data source.
        :param schedule: The schedule of the data source runs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_data_source_props = datazone.CfnDataSourceProps(
                domain_identifier="domainIdentifier",
                name="name",
                project_identifier="projectIdentifier",
                type="type",
            
                # the properties below are optional
                asset_forms_input=[datazone.CfnDataSource.FormInputProperty(
                    form_name="formName",
            
                    # the properties below are optional
                    content="content",
                    type_identifier="typeIdentifier",
                    type_revision="typeRevision"
                )],
                configuration=datazone.CfnDataSource.DataSourceConfigurationInputProperty(
                    glue_run_configuration=datazone.CfnDataSource.GlueRunConfigurationInputProperty(
                        relational_filter_configurations=[datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                            database_name="databaseName",
            
                            # the properties below are optional
                            filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                                expression="expression",
                                type="type"
                            )],
                            schema_name="schemaName"
                        )],
            
                        # the properties below are optional
                        auto_import_data_quality_result=False,
                        catalog_name="catalogName",
                        data_access_role="dataAccessRole"
                    ),
                    redshift_run_configuration=datazone.CfnDataSource.RedshiftRunConfigurationInputProperty(
                        relational_filter_configurations=[datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                            database_name="databaseName",
            
                            # the properties below are optional
                            filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                                expression="expression",
                                type="type"
                            )],
                            schema_name="schemaName"
                        )],
            
                        # the properties below are optional
                        data_access_role="dataAccessRole",
                        redshift_credential_configuration=datazone.CfnDataSource.RedshiftCredentialConfigurationProperty(
                            secret_manager_arn="secretManagerArn"
                        ),
                        redshift_storage=datazone.CfnDataSource.RedshiftStorageProperty(
                            redshift_cluster_source=datazone.CfnDataSource.RedshiftClusterStorageProperty(
                                cluster_name="clusterName"
                            ),
                            redshift_serverless_source=datazone.CfnDataSource.RedshiftServerlessStorageProperty(
                                workgroup_name="workgroupName"
                            )
                        )
                    ),
                    sage_maker_run_configuration=datazone.CfnDataSource.SageMakerRunConfigurationInputProperty(
                        tracking_assets={
                            "tracking_assets_key": ["trackingAssets"]
                        }
                    )
                ),
                connection_identifier="connectionIdentifier",
                description="description",
                enable_setting="enableSetting",
                environment_identifier="environmentIdentifier",
                publish_on_import=False,
                recommendation=datazone.CfnDataSource.RecommendationConfigurationProperty(
                    enable_business_name_generation=False
                ),
                schedule=datazone.CfnDataSource.ScheduleConfigurationProperty(
                    schedule="schedule",
                    timezone="timezone"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc5ec98207dd171531ba923ab77ceb4e9c095a2ac7eb083b5faef7393c183f86)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project_identifier", value=project_identifier, expected_type=type_hints["project_identifier"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument asset_forms_input", value=asset_forms_input, expected_type=type_hints["asset_forms_input"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument connection_identifier", value=connection_identifier, expected_type=type_hints["connection_identifier"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enable_setting", value=enable_setting, expected_type=type_hints["enable_setting"])
            check_type(argname="argument environment_identifier", value=environment_identifier, expected_type=type_hints["environment_identifier"])
            check_type(argname="argument publish_on_import", value=publish_on_import, expected_type=type_hints["publish_on_import"])
            check_type(argname="argument recommendation", value=recommendation, expected_type=type_hints["recommendation"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "name": name,
            "project_identifier": project_identifier,
            "type": type,
        }
        if asset_forms_input is not None:
            self._values["asset_forms_input"] = asset_forms_input
        if configuration is not None:
            self._values["configuration"] = configuration
        if connection_identifier is not None:
            self._values["connection_identifier"] = connection_identifier
        if description is not None:
            self._values["description"] = description
        if enable_setting is not None:
            self._values["enable_setting"] = enable_setting
        if environment_identifier is not None:
            self._values["environment_identifier"] = environment_identifier
        if publish_on_import is not None:
            self._values["publish_on_import"] = publish_on_import
        if recommendation is not None:
            self._values["recommendation"] = recommendation
        if schedule is not None:
            self._values["schedule"] = schedule

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The ID of the Amazon DataZone domain where the data source is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone project in which you want to add this data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-projectidentifier
        '''
        result = self._values.get("project_identifier")
        assert result is not None, "Required property 'project_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the data source.

        In Amazon DataZone, you can use data sources to import technical metadata of assets (data) from the source databases or data warehouses into Amazon DataZone. In the current release of Amazon DataZone, you can create and run data sources for AWS Glue and Amazon Redshift.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_forms_input(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataSource.FormInputProperty]]]]:
        '''The metadata forms attached to the assets that the data source works with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-assetformsinput
        '''
        result = self._values.get("asset_forms_input")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataSource.FormInputProperty]]]], result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DataSourceConfigurationInputProperty]]:
        '''The configuration of the data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-configuration
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DataSourceConfigurationInputProperty]], result)

    @builtins.property
    def connection_identifier(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of a connection used to fetch relevant parameters from connection during Datasource run.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-connectionidentifier
        '''
        result = self._values.get("connection_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_setting(self) -> typing.Optional[builtins.str]:
        '''Specifies whether the data source is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-enablesetting
        '''
        result = self._values.get("enable_setting")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_identifier(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the Amazon DataZone environment to which the data source publishes assets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-environmentidentifier
        '''
        result = self._values.get("environment_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publish_on_import(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-publishonimport
        '''
        result = self._values.get("publish_on_import")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def recommendation(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.RecommendationConfigurationProperty]]:
        '''Specifies whether the business name generation is to be enabled for this data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-recommendation
        '''
        result = self._values.get("recommendation")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.RecommendationConfigurationProperty]], result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.ScheduleConfigurationProperty]]:
        '''The schedule of the data source runs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.ScheduleConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnDomain(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnDomain",
):
    '''The ``AWS::DataZone::Domain`` resource specifies an Amazon DataZone domain.

    You can use domains to organize your assets, users, and their projects.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html
    :cloudformationResource: AWS::DataZone::Domain
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_domain = datazone.CfnDomain(self, "MyCfnDomain",
            domain_execution_role="domainExecutionRole",
            name="name",
        
            # the properties below are optional
            description="description",
            domain_version="domainVersion",
            kms_key_identifier="kmsKeyIdentifier",
            service_role="serviceRole",
            single_sign_on=datazone.CfnDomain.SingleSignOnProperty(
                idc_instance_arn="idcInstanceArn",
                type="type",
                user_assignment="userAssignment"
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
        domain_execution_role: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        domain_version: typing.Optional[builtins.str] = None,
        kms_key_identifier: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[builtins.str] = None,
        single_sign_on: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.SingleSignOnProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_execution_role: The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the AWS account that houses the Amazon DataZone domain.
        :param name: The name of the Amazon DataZone domain.
        :param description: The description of the Amazon DataZone domain.
        :param domain_version: The domain version.
        :param kms_key_identifier: The identifier of the AWS Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.
        :param service_role: The service role of the domain.
        :param single_sign_on: The single sign-on details in Amazon DataZone.
        :param tags: The tags specified for the Amazon DataZone domain.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__047efef40bc572d080b2e64b8f32c1db40e40ba16fc7d29d887073e9c6b44c3f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainProps(
            domain_execution_role=domain_execution_role,
            name=name,
            description=description,
            domain_version=domain_version,
            kms_key_identifier=kms_key_identifier,
            service_role=service_role,
            single_sign_on=single_sign_on,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44ac286b6a265a7b8c549e9f75d607cdf3e71f300523940763c96adb368c15ac)
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
            type_hints = typing.get_type_hints(_typecheckingstub__595689c850e768a74bf0e3147031e1acd033e20ab08856209edf9954aa010432)
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
        '''The ARN of the Amazon DataZone domain.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''A timestamp of when a Amazon DataZone domain was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the Amazon DataZone domain.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''A timestamp of when a Amazon DataZone domain was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrManagedAccountId")
    def attr_managed_account_id(self) -> builtins.str:
        '''The identifier of the AWS account that manages the domain.

        :cloudformationAttribute: ManagedAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrManagedAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrPortalUrl")
    def attr_portal_url(self) -> builtins.str:
        '''The data portal URL for the Amazon DataZone domain.

        :cloudformationAttribute: PortalUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPortalUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrRootDomainUnitId")
    def attr_root_domain_unit_id(self) -> builtins.str:
        '''The ID of the root domain unit.

        :cloudformationAttribute: RootDomainUnitId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRootDomainUnitId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the Amazon DataZone domain.

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
    @jsii.member(jsii_name="domainExecutionRole")
    def domain_execution_role(self) -> builtins.str:
        '''The domain execution role that is created when an Amazon DataZone domain is created.'''
        return typing.cast(builtins.str, jsii.get(self, "domainExecutionRole"))

    @domain_execution_role.setter
    def domain_execution_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f0f91db144dcd37dc91c4f005e5e179143c7d40165baf625ef7e284af70358e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainExecutionRole", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the Amazon DataZone domain.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb44fad9b00c8b94e0193e65a7d6e38fbf79595a0c367032211eb3ddcec54145)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the Amazon DataZone domain.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfb0d62a189dbc4d1b327c1e7f651b95f580a2f6196abce203f4709bcca75c7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainVersion")
    def domain_version(self) -> typing.Optional[builtins.str]:
        '''The domain version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainVersion"))

    @domain_version.setter
    def domain_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01acac61c7163cf6379c6cbe162a62434376eca50700d6cfaaea6008ea3ec333)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainVersion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the AWS Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdentifier"))

    @kms_key_identifier.setter
    def kms_key_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49d22f79e701c8bd8ae540b270f397204f2285f1dc76ab7d1556d659a050f38b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> typing.Optional[builtins.str]:
        '''The service role of the domain.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fd383448cae4473b200d8583b604eef942f85827467ce9f6bf4b1fc6f61390c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRole", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="singleSignOn")
    def single_sign_on(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.SingleSignOnProperty"]]:
        '''The single sign-on details in Amazon DataZone.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.SingleSignOnProperty"]], jsii.get(self, "singleSignOn"))

    @single_sign_on.setter
    def single_sign_on(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.SingleSignOnProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee4595d765303396b66c3b59368637f839b950667fb4c707c509ac63e084f20b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singleSignOn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags specified for the Amazon DataZone domain.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d899e2a4a220703956ab7f56e7c810107ec736f8c6281bedb3bc027e6ddb2ba4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDomain.SingleSignOnProperty",
        jsii_struct_bases=[],
        name_mapping={
            "idc_instance_arn": "idcInstanceArn",
            "type": "type",
            "user_assignment": "userAssignment",
        },
    )
    class SingleSignOnProperty:
        def __init__(
            self,
            *,
            idc_instance_arn: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            user_assignment: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The single sign-on details in Amazon DataZone.

            :param idc_instance_arn: The ARN of the IDC instance.
            :param type: The type of single sign-on in Amazon DataZone.
            :param user_assignment: The single sign-on user assignment in Amazon DataZone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-domain-singlesignon.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                single_sign_on_property = datazone.CfnDomain.SingleSignOnProperty(
                    idc_instance_arn="idcInstanceArn",
                    type="type",
                    user_assignment="userAssignment"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7f4cd03b79bceb07fb9f1366c739ee9cc49b8cbf6b9077a564689e81698df16)
                check_type(argname="argument idc_instance_arn", value=idc_instance_arn, expected_type=type_hints["idc_instance_arn"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument user_assignment", value=user_assignment, expected_type=type_hints["user_assignment"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if idc_instance_arn is not None:
                self._values["idc_instance_arn"] = idc_instance_arn
            if type is not None:
                self._values["type"] = type
            if user_assignment is not None:
                self._values["user_assignment"] = user_assignment

        @builtins.property
        def idc_instance_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the IDC instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-domain-singlesignon.html#cfn-datazone-domain-singlesignon-idcinstancearn
            '''
            result = self._values.get("idc_instance_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of single sign-on in Amazon DataZone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-domain-singlesignon.html#cfn-datazone-domain-singlesignon-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_assignment(self) -> typing.Optional[builtins.str]:
            '''The single sign-on user assignment in Amazon DataZone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-domain-singlesignon.html#cfn-datazone-domain-singlesignon-userassignment
            '''
            result = self._values.get("user_assignment")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SingleSignOnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnDomainProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_execution_role": "domainExecutionRole",
        "name": "name",
        "description": "description",
        "domain_version": "domainVersion",
        "kms_key_identifier": "kmsKeyIdentifier",
        "service_role": "serviceRole",
        "single_sign_on": "singleSignOn",
        "tags": "tags",
    },
)
class CfnDomainProps:
    def __init__(
        self,
        *,
        domain_execution_role: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        domain_version: typing.Optional[builtins.str] = None,
        kms_key_identifier: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[builtins.str] = None,
        single_sign_on: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SingleSignOnProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDomain``.

        :param domain_execution_role: The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the AWS account that houses the Amazon DataZone domain.
        :param name: The name of the Amazon DataZone domain.
        :param description: The description of the Amazon DataZone domain.
        :param domain_version: The domain version.
        :param kms_key_identifier: The identifier of the AWS Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.
        :param service_role: The service role of the domain.
        :param single_sign_on: The single sign-on details in Amazon DataZone.
        :param tags: The tags specified for the Amazon DataZone domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_domain_props = datazone.CfnDomainProps(
                domain_execution_role="domainExecutionRole",
                name="name",
            
                # the properties below are optional
                description="description",
                domain_version="domainVersion",
                kms_key_identifier="kmsKeyIdentifier",
                service_role="serviceRole",
                single_sign_on=datazone.CfnDomain.SingleSignOnProperty(
                    idc_instance_arn="idcInstanceArn",
                    type="type",
                    user_assignment="userAssignment"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d98e07f58a8aeb53fe8b36894639594f83be43ac8d182e1c384572cf0038d27)
            check_type(argname="argument domain_execution_role", value=domain_execution_role, expected_type=type_hints["domain_execution_role"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument domain_version", value=domain_version, expected_type=type_hints["domain_version"])
            check_type(argname="argument kms_key_identifier", value=kms_key_identifier, expected_type=type_hints["kms_key_identifier"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument single_sign_on", value=single_sign_on, expected_type=type_hints["single_sign_on"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_execution_role": domain_execution_role,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if domain_version is not None:
            self._values["domain_version"] = domain_version
        if kms_key_identifier is not None:
            self._values["kms_key_identifier"] = kms_key_identifier
        if service_role is not None:
            self._values["service_role"] = service_role
        if single_sign_on is not None:
            self._values["single_sign_on"] = single_sign_on
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def domain_execution_role(self) -> builtins.str:
        '''The domain execution role that is created when an Amazon DataZone domain is created.

        The domain execution role is created in the AWS account that houses the Amazon DataZone domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html#cfn-datazone-domain-domainexecutionrole
        '''
        result = self._values.get("domain_execution_role")
        assert result is not None, "Required property 'domain_execution_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the Amazon DataZone domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html#cfn-datazone-domain-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the Amazon DataZone domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html#cfn-datazone-domain-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_version(self) -> typing.Optional[builtins.str]:
        '''The domain version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html#cfn-datazone-domain-domainversion
        '''
        result = self._values.get("domain_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the AWS Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html#cfn-datazone-domain-kmskeyidentifier
        '''
        result = self._values.get("kms_key_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role(self) -> typing.Optional[builtins.str]:
        '''The service role of the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html#cfn-datazone-domain-servicerole
        '''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_sign_on(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.SingleSignOnProperty]]:
        '''The single sign-on details in Amazon DataZone.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html#cfn-datazone-domain-singlesignon
        '''
        result = self._values.get("single_sign_on")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.SingleSignOnProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags specified for the Amazon DataZone domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html#cfn-datazone-domain-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDomainUnit(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnDomainUnit",
):
    '''The summary of the domain unit.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domainunit.html
    :cloudformationResource: AWS::DataZone::DomainUnit
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_domain_unit = datazone.CfnDomainUnit(self, "MyCfnDomainUnit",
            domain_identifier="domainIdentifier",
            name="name",
            parent_domain_unit_identifier="parentDomainUnitIdentifier",
        
            # the properties below are optional
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_identifier: builtins.str,
        name: builtins.str,
        parent_domain_unit_identifier: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_identifier: The ID of the domain where you want to crate a domain unit.
        :param name: The name of the domain unit.
        :param parent_domain_unit_identifier: The ID of the parent domain unit.
        :param description: The description of the domain unit.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1700595f9c5a7d1c2312abf9e8d15687f79d83e5ead5d4136afe1d562d212c38)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainUnitProps(
            domain_identifier=domain_identifier,
            name=name,
            parent_domain_unit_identifier=parent_domain_unit_identifier,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__253603c22b8126a36f68fce57f93a169ab3bae1eea3f4a0ed84da859e1a38444)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a243fcb8e7ead0c756ca762c1cdda3fa9d1e09b6cc2627c55905a3ba1c13d46a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time stamp at which the domain unit was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The ID of the domain in which the domain unit lives.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the domain unit.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentifier")
    def attr_identifier(self) -> builtins.str:
        '''The identifier of the domain unit that you want to get.

        :cloudformationAttribute: Identifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The timestamp at which the domain unit was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrParentDomainUnitId")
    def attr_parent_domain_unit_id(self) -> builtins.str:
        '''The ID of the parent domain unit.

        :cloudformationAttribute: ParentDomainUnitId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrParentDomainUnitId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The ID of the domain where you want to crate a domain unit.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf72156aa725b96faaed85404e23d70dc267cd0abb5f25a82730b49e79db3da3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the domain unit.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e554b39a08bdebb47a996dd0ed4d2386500e1f97db8b2b102320bf4c229a429)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="parentDomainUnitIdentifier")
    def parent_domain_unit_identifier(self) -> builtins.str:
        '''The ID of the parent domain unit.'''
        return typing.cast(builtins.str, jsii.get(self, "parentDomainUnitIdentifier"))

    @parent_domain_unit_identifier.setter
    def parent_domain_unit_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fc10ab18c77014087fe1354e8f1063236b8830e559cbc2287ef325f51d1ab0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentDomainUnitIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the domain unit.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a999765de6c52fcb132be3cd0b216fc666c0809dfc86c99a02dfc71a5fff2974)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnDomainUnitProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "name": "name",
        "parent_domain_unit_identifier": "parentDomainUnitIdentifier",
        "description": "description",
    },
)
class CfnDomainUnitProps:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        name: builtins.str,
        parent_domain_unit_identifier: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDomainUnit``.

        :param domain_identifier: The ID of the domain where you want to crate a domain unit.
        :param name: The name of the domain unit.
        :param parent_domain_unit_identifier: The ID of the parent domain unit.
        :param description: The description of the domain unit.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domainunit.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_domain_unit_props = datazone.CfnDomainUnitProps(
                domain_identifier="domainIdentifier",
                name="name",
                parent_domain_unit_identifier="parentDomainUnitIdentifier",
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__740935adbb77d29725778a65030d855aa614e033e09a756660d6c3eef6160bd9)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parent_domain_unit_identifier", value=parent_domain_unit_identifier, expected_type=type_hints["parent_domain_unit_identifier"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "name": name,
            "parent_domain_unit_identifier": parent_domain_unit_identifier,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The ID of the domain where you want to crate a domain unit.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domainunit.html#cfn-datazone-domainunit-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the domain unit.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domainunit.html#cfn-datazone-domainunit-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent_domain_unit_identifier(self) -> builtins.str:
        '''The ID of the parent domain unit.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domainunit.html#cfn-datazone-domainunit-parentdomainunitidentifier
        '''
        result = self._values.get("parent_domain_unit_identifier")
        assert result is not None, "Required property 'parent_domain_unit_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the domain unit.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domainunit.html#cfn-datazone-domainunit-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainUnitProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEnvironment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironment",
):
    '''The ``AWS::DataZone::Environment`` resource specifies an Amazon DataZone environment, which is a collection of zero or more configured resources with a given set of IAM principals who can operate on those resources.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html
    :cloudformationResource: AWS::DataZone::Environment
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_environment = datazone.CfnEnvironment(self, "MyCfnEnvironment",
            domain_identifier="domainIdentifier",
            name="name",
            project_identifier="projectIdentifier",
        
            # the properties below are optional
            description="description",
            environment_account_identifier="environmentAccountIdentifier",
            environment_account_region="environmentAccountRegion",
            environment_profile_identifier="environmentProfileIdentifier",
            environment_role_arn="environmentRoleArn",
            glossary_terms=["glossaryTerms"],
            user_parameters=[datazone.CfnEnvironment.EnvironmentParameterProperty(
                name="name",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_identifier: builtins.str,
        name: builtins.str,
        project_identifier: builtins.str,
        description: typing.Optional[builtins.str] = None,
        environment_account_identifier: typing.Optional[builtins.str] = None,
        environment_account_region: typing.Optional[builtins.str] = None,
        environment_profile_identifier: typing.Optional[builtins.str] = None,
        environment_role_arn: typing.Optional[builtins.str] = None,
        glossary_terms: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.EnvironmentParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_identifier: The identifier of the Amazon DataZone domain in which the environment is created.
        :param name: The name of the Amazon DataZone environment.
        :param project_identifier: The identifier of the Amazon DataZone project in which this environment is created.
        :param description: The description of the environment.
        :param environment_account_identifier: The identifier of the AWS account in which an environment exists.
        :param environment_account_region: The AWS Region in which an environment exists.
        :param environment_profile_identifier: The identifier of the environment profile that is used to create this Amazon DataZone environment.
        :param environment_role_arn: The ARN of the environment role.
        :param glossary_terms: The glossary terms that can be used in this Amazon DataZone environment.
        :param user_parameters: The user parameters of this Amazon DataZone environment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9dbab782927b08354bbafa4881abe3f775c9141395be836e6450777f8729b9b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentProps(
            domain_identifier=domain_identifier,
            name=name,
            project_identifier=project_identifier,
            description=description,
            environment_account_identifier=environment_account_identifier,
            environment_account_region=environment_account_region,
            environment_profile_identifier=environment_profile_identifier,
            environment_role_arn=environment_role_arn,
            glossary_terms=glossary_terms,
            user_parameters=user_parameters,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a28a39a0c7ba040029b6d28481def84a1131453e9259d7f220a8d8f9a9562fcf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7a663cc771f3c58655975db4a99b46784c16b0b96c4bb006217531f931854d1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAwsAccountId")
    def attr_aws_account_id(self) -> builtins.str:
        '''The identifier of the AWS account in which an environment exists.

        :cloudformationAttribute: AwsAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAwsAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrAwsAccountRegion")
    def attr_aws_account_region(self) -> builtins.str:
        '''The AWS Region in which an environment exists.

        :cloudformationAttribute: AwsAccountRegion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAwsAccountRegion"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when the environment was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedBy")
    def attr_created_by(self) -> builtins.str:
        '''The Amazon DataZone user who created the environment.

        :cloudformationAttribute: CreatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the environment exists.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentBlueprintId")
    def attr_environment_blueprint_id(self) -> builtins.str:
        '''The identifier of a blueprint with which an environment profile is created.

        :cloudformationAttribute: EnvironmentBlueprintId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentBlueprintId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentProfileId")
    def attr_environment_profile_id(self) -> builtins.str:
        '''The identifier of the environment profile with which the environment was created.

        :cloudformationAttribute: EnvironmentProfileId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentProfileId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The identifier of the environment.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrProjectId")
    def attr_project_id(self) -> builtins.str:
        '''The identifier of the project in which the environment exists.

        :cloudformationAttribute: ProjectId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectId"))

    @builtins.property
    @jsii.member(jsii_name="attrProvider")
    def attr_provider(self) -> builtins.str:
        '''The provider of the environment.

        :cloudformationAttribute: Provider
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProvider"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the environment.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp of when the environment was updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the environment is created.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b36a4aa57667467b8bda95ca761a942a6f67e34e8549cd2dccc7a61d8399e9b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the Amazon DataZone environment.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4376356ce7178baaec6de65e59f567c3496e08605a27833ed8e83bfe0ff4be4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="projectIdentifier")
    def project_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone project in which this environment is created.'''
        return typing.cast(builtins.str, jsii.get(self, "projectIdentifier"))

    @project_identifier.setter
    def project_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baefbe7e97d72065b3b2c6be4e97a54bf9298376bb60dcac92eb7191397e306b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00e90ff4028654f7f45c97804aa061515407ac2ce2e55a21a1a4e4ff76fefd60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentAccountIdentifier")
    def environment_account_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the AWS account in which an environment exists.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentAccountIdentifier"))

    @environment_account_identifier.setter
    def environment_account_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43f5514f896b52007434785f6106a995073e27bf964e663b740911090d537bf3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentAccountIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentAccountRegion")
    def environment_account_region(self) -> typing.Optional[builtins.str]:
        '''The AWS Region in which an environment exists.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentAccountRegion"))

    @environment_account_region.setter
    def environment_account_region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c559df95e35a94ccf1ae460803faf8ff00fc715c3ad0b7cfafb1b92c2258564)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentAccountRegion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentProfileIdentifier")
    def environment_profile_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the environment profile that is used to create this Amazon DataZone environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentProfileIdentifier"))

    @environment_profile_identifier.setter
    def environment_profile_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__123d0e6b3ed252019ec79f09a380206e446d8155ba73fc8e7518fbd3dbac8c2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentProfileIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentRoleArn")
    def environment_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the environment role.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentRoleArn"))

    @environment_role_arn.setter
    def environment_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b4153aa4bfc638db19251feaaf147e1376f5797ff9dd67109f2a7bf538d8a17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="glossaryTerms")
    def glossary_terms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The glossary terms that can be used in this Amazon DataZone environment.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "glossaryTerms"))

    @glossary_terms.setter
    def glossary_terms(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d52d21b9ab0852f8793f985e6f12ccea104ddc7e138f30b744d739af3c46b742)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "glossaryTerms", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="userParameters")
    def user_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.EnvironmentParameterProperty"]]]]:
        '''The user parameters of this Amazon DataZone environment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.EnvironmentParameterProperty"]]]], jsii.get(self, "userParameters"))

    @user_parameters.setter
    def user_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.EnvironmentParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d345163e4f1ef89a409f470c896454213d0735fe6e5011e7ec6df4ead799556d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userParameters", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironment.EnvironmentParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class EnvironmentParameterProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The parameter details of the environment.

            :param name: The name of the environment parameter.
            :param value: The value of the environment parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environment-environmentparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                environment_parameter_property = datazone.CfnEnvironment.EnvironmentParameterProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d32a764f93482ecbfe18350874389b17ae96f3d5f78686bae5b55a2dcdfc012b)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the environment parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environment-environmentparameter.html#cfn-datazone-environment-environmentparameter-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of the environment parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environment-environmentparameter.html#cfn-datazone-environment-environmentparameter-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnEnvironmentActions(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentActions",
):
    '''The details about the specified action configured for an environment.

    For example, the details of the specified console links for an analytics tool that is available in this environment.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentactions.html
    :cloudformationResource: AWS::DataZone::EnvironmentActions
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_environment_actions = datazone.CfnEnvironmentActions(self, "MyCfnEnvironmentActions",
            name="name",
        
            # the properties below are optional
            description="description",
            domain_identifier="domainIdentifier",
            environment_identifier="environmentIdentifier",
            identifier="identifier",
            parameters=datazone.CfnEnvironmentActions.AwsConsoleLinkParametersProperty(
                uri="uri"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        domain_identifier: typing.Optional[builtins.str] = None,
        environment_identifier: typing.Optional[builtins.str] = None,
        identifier: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironmentActions.AwsConsoleLinkParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the environment action.
        :param description: The environment action description.
        :param domain_identifier: The Amazon DataZone domain ID of the environment action.
        :param environment_identifier: The environment ID of the environment action.
        :param identifier: The ID of the environment action.
        :param parameters: The parameters of the environment action.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23d8a73d028f6e855c2cc806cf34d881ee774001b5faf55329f1186898cd5d1c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentActionsProps(
            name=name,
            description=description,
            domain_identifier=domain_identifier,
            environment_identifier=environment_identifier,
            identifier=identifier,
            parameters=parameters,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5619cfe3b3ca5963d029c87191973ca35ac3bb01102c8e807502ada262fedcc7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__be72805e85c16a3d6d6a9862f3a07226b330cf4b3b110b5775de9db3c6d64dd2)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The Amazon DataZone domain ID of the environment action.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentId")
    def attr_environment_id(self) -> builtins.str:
        '''The environment ID of the environment action.

        :cloudformationAttribute: EnvironmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the environment action.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the environment action.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af36c191170daaf1b24eec04f527e30281e32ee3f3f75aaacbd67e64aca1b10b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The environment action description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55c22815170a2513147f4e74885cc8ca51917b6ec8c0644bc9c6d05b0fa2f41d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> typing.Optional[builtins.str]:
        '''The Amazon DataZone domain ID of the environment action.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa29021d0052df07430696eb45141a3ff12c83aa11f3fe5291138364d64bfe49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentIdentifier")
    def environment_identifier(self) -> typing.Optional[builtins.str]:
        '''The environment ID of the environment action.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentIdentifier"))

    @environment_identifier.setter
    def environment_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__224d8bbf6ba3a5a13d6893687689bb34a69380029d8d4fe281607965ccb59065)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="identifier")
    def identifier(self) -> typing.Optional[builtins.str]:
        '''The ID of the environment action.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identifier"))

    @identifier.setter
    def identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b0cf584a76af6d608e499b80f7ae532dcfdbe54a0d8d961ad67e4b52052f530)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentActions.AwsConsoleLinkParametersProperty"]]:
        '''The parameters of the environment action.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentActions.AwsConsoleLinkParametersProperty"]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentActions.AwsConsoleLinkParametersProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d7a1e83f2300dd2bce221749201b3aef3859d465ce9d2e72bb7161776120da2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentActions.AwsConsoleLinkParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"uri": "uri"},
    )
    class AwsConsoleLinkParametersProperty:
        def __init__(self, *, uri: typing.Optional[builtins.str] = None) -> None:
            '''The parameters of the console link specified as part of the environment action.

            :param uri: The URI of the console link specified as part of the environment action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentactions-awsconsolelinkparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                aws_console_link_parameters_property = datazone.CfnEnvironmentActions.AwsConsoleLinkParametersProperty(
                    uri="uri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a66aef49f4cbb5c05c7c82600d65a4b555f3e4321747102f3fc890d8498bac56)
                check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if uri is not None:
                self._values["uri"] = uri

        @builtins.property
        def uri(self) -> typing.Optional[builtins.str]:
            '''The URI of the console link specified as part of the environment action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentactions-awsconsolelinkparameters.html#cfn-datazone-environmentactions-awsconsolelinkparameters-uri
            '''
            result = self._values.get("uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsConsoleLinkParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentActionsProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "domain_identifier": "domainIdentifier",
        "environment_identifier": "environmentIdentifier",
        "identifier": "identifier",
        "parameters": "parameters",
    },
)
class CfnEnvironmentActionsProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        domain_identifier: typing.Optional[builtins.str] = None,
        environment_identifier: typing.Optional[builtins.str] = None,
        identifier: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentActions.AwsConsoleLinkParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironmentActions``.

        :param name: The name of the environment action.
        :param description: The environment action description.
        :param domain_identifier: The Amazon DataZone domain ID of the environment action.
        :param environment_identifier: The environment ID of the environment action.
        :param identifier: The ID of the environment action.
        :param parameters: The parameters of the environment action.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentactions.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_environment_actions_props = datazone.CfnEnvironmentActionsProps(
                name="name",
            
                # the properties below are optional
                description="description",
                domain_identifier="domainIdentifier",
                environment_identifier="environmentIdentifier",
                identifier="identifier",
                parameters=datazone.CfnEnvironmentActions.AwsConsoleLinkParametersProperty(
                    uri="uri"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c38a51ef4e52ffbf8312da8137617dd0e35055ad7636f23de55e829eae23750)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument environment_identifier", value=environment_identifier, expected_type=type_hints["environment_identifier"])
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if domain_identifier is not None:
            self._values["domain_identifier"] = domain_identifier
        if environment_identifier is not None:
            self._values["environment_identifier"] = environment_identifier
        if identifier is not None:
            self._values["identifier"] = identifier
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the environment action.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentactions.html#cfn-datazone-environmentactions-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The environment action description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentactions.html#cfn-datazone-environmentactions-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_identifier(self) -> typing.Optional[builtins.str]:
        '''The Amazon DataZone domain ID of the environment action.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentactions.html#cfn-datazone-environmentactions-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_identifier(self) -> typing.Optional[builtins.str]:
        '''The environment ID of the environment action.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentactions.html#cfn-datazone-environmentactions-environmentidentifier
        '''
        result = self._values.get("environment_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identifier(self) -> typing.Optional[builtins.str]:
        '''The ID of the environment action.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentactions.html#cfn-datazone-environmentactions-identifier
        '''
        result = self._values.get("identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironmentActions.AwsConsoleLinkParametersProperty]]:
        '''The parameters of the environment action.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentactions.html#cfn-datazone-environmentactions-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironmentActions.AwsConsoleLinkParametersProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentActionsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEnvironmentBlueprintConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentBlueprintConfiguration",
):
    '''The configuration details of an environment blueprint.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html
    :cloudformationResource: AWS::DataZone::EnvironmentBlueprintConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_environment_blueprint_configuration = datazone.CfnEnvironmentBlueprintConfiguration(self, "MyCfnEnvironmentBlueprintConfiguration",
            domain_identifier="domainIdentifier",
            enabled_regions=["enabledRegions"],
            environment_blueprint_identifier="environmentBlueprintIdentifier",
        
            # the properties below are optional
            environment_role_permission_boundary="environmentRolePermissionBoundary",
            manage_access_role_arn="manageAccessRoleArn",
            provisioning_configurations=[datazone.CfnEnvironmentBlueprintConfiguration.ProvisioningConfigurationProperty(
                lake_formation_configuration=datazone.CfnEnvironmentBlueprintConfiguration.LakeFormationConfigurationProperty(
                    location_registration_exclude_s3_locations=["locationRegistrationExcludeS3Locations"],
                    location_registration_role="locationRegistrationRole"
                )
            )],
            provisioning_role_arn="provisioningRoleArn",
            regional_parameters=[datazone.CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty(
                parameters={
                    "parameters_key": "parameters"
                },
                region="region"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_identifier: builtins.str,
        enabled_regions: typing.Sequence[builtins.str],
        environment_blueprint_identifier: builtins.str,
        environment_role_permission_boundary: typing.Optional[builtins.str] = None,
        manage_access_role_arn: typing.Optional[builtins.str] = None,
        provisioning_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironmentBlueprintConfiguration.ProvisioningConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        provisioning_role_arn: typing.Optional[builtins.str] = None,
        regional_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_identifier: The identifier of the Amazon DataZone domain in which an environment blueprint exists.
        :param enabled_regions: The enabled AWS Regions specified in a blueprint configuration.
        :param environment_blueprint_identifier: The identifier of the environment blueprint. In the current release, only the following values are supported: ``DefaultDataLake`` and ``DefaultDataWarehouse`` .
        :param environment_role_permission_boundary: The environment role permission boundary.
        :param manage_access_role_arn: The ARN of the manage access role.
        :param provisioning_configurations: The provisioning configuration of a blueprint.
        :param provisioning_role_arn: The ARN of the provisioning role.
        :param regional_parameters: The regional parameters of the environment blueprint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48d8677ae22ff2da132402ace39f998c6b914f7464ce38abe9373fdbc550c445)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentBlueprintConfigurationProps(
            domain_identifier=domain_identifier,
            enabled_regions=enabled_regions,
            environment_blueprint_identifier=environment_blueprint_identifier,
            environment_role_permission_boundary=environment_role_permission_boundary,
            manage_access_role_arn=manage_access_role_arn,
            provisioning_configurations=provisioning_configurations,
            provisioning_role_arn=provisioning_role_arn,
            regional_parameters=regional_parameters,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeb5ba3f6738d175b0ca7714e77b6af191ccad2c9967480252920cb95dc6cb8f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__86364c1d7caa870da909a60996d646dde31c0e41cb594d0e952262cd925d5bdf)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when an environment blueprint was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which an environment blueprint exists.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentBlueprintId")
    def attr_environment_blueprint_id(self) -> builtins.str:
        '''The identifier of the environment blueprint.

        This identifier should be used when creating environment profiles.

        :cloudformationAttribute: EnvironmentBlueprintId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentBlueprintId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp of when the environment blueprint was updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which an environment blueprint exists.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e6a26e61dc0bca0a16da5100bf8f8cfcb05985dcd52fd83afd7818c62445836)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enabledRegions")
    def enabled_regions(self) -> typing.List[builtins.str]:
        '''The enabled AWS Regions specified in a blueprint configuration.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "enabledRegions"))

    @enabled_regions.setter
    def enabled_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9064df9af275b8a17afb82a8fc271f7b6e0ab19cdf01da41f144bac4832180e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledRegions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentBlueprintIdentifier")
    def environment_blueprint_identifier(self) -> builtins.str:
        '''The identifier of the environment blueprint.'''
        return typing.cast(builtins.str, jsii.get(self, "environmentBlueprintIdentifier"))

    @environment_blueprint_identifier.setter
    def environment_blueprint_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db2bf9c4c7f25403fe2aa03be854b8b8b1f530f8d53a317f87b2fb9470d906a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentBlueprintIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentRolePermissionBoundary")
    def environment_role_permission_boundary(self) -> typing.Optional[builtins.str]:
        '''The environment role permission boundary.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentRolePermissionBoundary"))

    @environment_role_permission_boundary.setter
    def environment_role_permission_boundary(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0142557047b6391f0c0d7425b73085935e7a1d5e07139d87dcb9c9ab709bd4ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentRolePermissionBoundary", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="manageAccessRoleArn")
    def manage_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the manage access role.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "manageAccessRoleArn"))

    @manage_access_role_arn.setter
    def manage_access_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13a80be3403ea5113203d40c0843c4e4965600487d58b5f1e83bf1b8a9fc3d11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manageAccessRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="provisioningConfigurations")
    def provisioning_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentBlueprintConfiguration.ProvisioningConfigurationProperty"]]]]:
        '''The provisioning configuration of a blueprint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentBlueprintConfiguration.ProvisioningConfigurationProperty"]]]], jsii.get(self, "provisioningConfigurations"))

    @provisioning_configurations.setter
    def provisioning_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentBlueprintConfiguration.ProvisioningConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f945458658c5114bd92815174ffa8cabc189cbb27ef04cd8ca8a0ca6b933ad77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisioningConfigurations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="provisioningRoleArn")
    def provisioning_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the provisioning role.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "provisioningRoleArn"))

    @provisioning_role_arn.setter
    def provisioning_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09c1e18144766c7e8d72f080dbe9de88dc085cfbdaa47a10b50cf7e235be8d65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisioningRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="regionalParameters")
    def regional_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty"]]]]:
        '''The regional parameters of the environment blueprint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty"]]]], jsii.get(self, "regionalParameters"))

    @regional_parameters.setter
    def regional_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93fe5a214b768cb7201e2f47a6073bdec0303c4cda4d1d0b739b124ba7858574)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionalParameters", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentBlueprintConfiguration.LakeFormationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "location_registration_exclude_s3_locations": "locationRegistrationExcludeS3Locations",
            "location_registration_role": "locationRegistrationRole",
        },
    )
    class LakeFormationConfigurationProperty:
        def __init__(
            self,
            *,
            location_registration_exclude_s3_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
            location_registration_role: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Lake Formation configuration of the Data Lake blueprint.

            :param location_registration_exclude_s3_locations: Specifies certain Amazon S3 locations if you do not want Amazon DataZone to automatically register them in hybrid mode.
            :param location_registration_role: The role that is used to manage read/write access to the chosen Amazon S3 bucket(s) for Data Lake using AWS Lake Formation hybrid access mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentblueprintconfiguration-lakeformationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                lake_formation_configuration_property = datazone.CfnEnvironmentBlueprintConfiguration.LakeFormationConfigurationProperty(
                    location_registration_exclude_s3_locations=["locationRegistrationExcludeS3Locations"],
                    location_registration_role="locationRegistrationRole"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5b34e7436c5711c0e3c03f2d39f197fd5268605136341c021dfdb2f9be036a01)
                check_type(argname="argument location_registration_exclude_s3_locations", value=location_registration_exclude_s3_locations, expected_type=type_hints["location_registration_exclude_s3_locations"])
                check_type(argname="argument location_registration_role", value=location_registration_role, expected_type=type_hints["location_registration_role"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if location_registration_exclude_s3_locations is not None:
                self._values["location_registration_exclude_s3_locations"] = location_registration_exclude_s3_locations
            if location_registration_role is not None:
                self._values["location_registration_role"] = location_registration_role

        @builtins.property
        def location_registration_exclude_s3_locations(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies certain Amazon S3 locations if you do not want Amazon DataZone to automatically register them in hybrid mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentblueprintconfiguration-lakeformationconfiguration.html#cfn-datazone-environmentblueprintconfiguration-lakeformationconfiguration-locationregistrationexcludes3locations
            '''
            result = self._values.get("location_registration_exclude_s3_locations")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def location_registration_role(self) -> typing.Optional[builtins.str]:
            '''The role that is used to manage read/write access to the chosen Amazon S3 bucket(s) for Data Lake using AWS Lake Formation hybrid access mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentblueprintconfiguration-lakeformationconfiguration.html#cfn-datazone-environmentblueprintconfiguration-lakeformationconfiguration-locationregistrationrole
            '''
            result = self._values.get("location_registration_role")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LakeFormationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentBlueprintConfiguration.ProvisioningConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"lake_formation_configuration": "lakeFormationConfiguration"},
    )
    class ProvisioningConfigurationProperty:
        def __init__(
            self,
            *,
            lake_formation_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironmentBlueprintConfiguration.LakeFormationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The provisioning configuration of the blueprint.

            :param lake_formation_configuration: The Lake Formation configuration of the Data Lake blueprint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentblueprintconfiguration-provisioningconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                provisioning_configuration_property = datazone.CfnEnvironmentBlueprintConfiguration.ProvisioningConfigurationProperty(
                    lake_formation_configuration=datazone.CfnEnvironmentBlueprintConfiguration.LakeFormationConfigurationProperty(
                        location_registration_exclude_s3_locations=["locationRegistrationExcludeS3Locations"],
                        location_registration_role="locationRegistrationRole"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__29b5e41d02462ac9818fbf0e54d1556527c5ab2ab685686237dee244c941e9bd)
                check_type(argname="argument lake_formation_configuration", value=lake_formation_configuration, expected_type=type_hints["lake_formation_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lake_formation_configuration": lake_formation_configuration,
            }

        @builtins.property
        def lake_formation_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnEnvironmentBlueprintConfiguration.LakeFormationConfigurationProperty"]:
            '''The Lake Formation configuration of the Data Lake blueprint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentblueprintconfiguration-provisioningconfiguration.html#cfn-datazone-environmentblueprintconfiguration-provisioningconfiguration-lakeformationconfiguration
            '''
            result = self._values.get("lake_formation_configuration")
            assert result is not None, "Required property 'lake_formation_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEnvironmentBlueprintConfiguration.LakeFormationConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisioningConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"parameters": "parameters", "region": "region"},
    )
    class RegionalParameterProperty:
        def __init__(
            self,
            *,
            parameters: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The regional parameters in the environment blueprint.

            :param parameters: A string to string map containing parameters for the region.
            :param region: The region specified in the environment parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentblueprintconfiguration-regionalparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                regional_parameter_property = datazone.CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty(
                    parameters={
                        "parameters_key": "parameters"
                    },
                    region="region"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__563b6d6aa110d6b77fcca8e42c3020852fa0c12036e1ba7f6ee62b2ce30826ff)
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if parameters is not None:
                self._values["parameters"] = parameters
            if region is not None:
                self._values["region"] = region

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''A string to string map containing parameters for the region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentblueprintconfiguration-regionalparameter.html#cfn-datazone-environmentblueprintconfiguration-regionalparameter-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''The region specified in the environment parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentblueprintconfiguration-regionalparameter.html#cfn-datazone-environmentblueprintconfiguration-regionalparameter-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegionalParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentBlueprintConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "enabled_regions": "enabledRegions",
        "environment_blueprint_identifier": "environmentBlueprintIdentifier",
        "environment_role_permission_boundary": "environmentRolePermissionBoundary",
        "manage_access_role_arn": "manageAccessRoleArn",
        "provisioning_configurations": "provisioningConfigurations",
        "provisioning_role_arn": "provisioningRoleArn",
        "regional_parameters": "regionalParameters",
    },
)
class CfnEnvironmentBlueprintConfigurationProps:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        enabled_regions: typing.Sequence[builtins.str],
        environment_blueprint_identifier: builtins.str,
        environment_role_permission_boundary: typing.Optional[builtins.str] = None,
        manage_access_role_arn: typing.Optional[builtins.str] = None,
        provisioning_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentBlueprintConfiguration.ProvisioningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        provisioning_role_arn: typing.Optional[builtins.str] = None,
        regional_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironmentBlueprintConfiguration``.

        :param domain_identifier: The identifier of the Amazon DataZone domain in which an environment blueprint exists.
        :param enabled_regions: The enabled AWS Regions specified in a blueprint configuration.
        :param environment_blueprint_identifier: The identifier of the environment blueprint. In the current release, only the following values are supported: ``DefaultDataLake`` and ``DefaultDataWarehouse`` .
        :param environment_role_permission_boundary: The environment role permission boundary.
        :param manage_access_role_arn: The ARN of the manage access role.
        :param provisioning_configurations: The provisioning configuration of a blueprint.
        :param provisioning_role_arn: The ARN of the provisioning role.
        :param regional_parameters: The regional parameters of the environment blueprint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_environment_blueprint_configuration_props = datazone.CfnEnvironmentBlueprintConfigurationProps(
                domain_identifier="domainIdentifier",
                enabled_regions=["enabledRegions"],
                environment_blueprint_identifier="environmentBlueprintIdentifier",
            
                # the properties below are optional
                environment_role_permission_boundary="environmentRolePermissionBoundary",
                manage_access_role_arn="manageAccessRoleArn",
                provisioning_configurations=[datazone.CfnEnvironmentBlueprintConfiguration.ProvisioningConfigurationProperty(
                    lake_formation_configuration=datazone.CfnEnvironmentBlueprintConfiguration.LakeFormationConfigurationProperty(
                        location_registration_exclude_s3_locations=["locationRegistrationExcludeS3Locations"],
                        location_registration_role="locationRegistrationRole"
                    )
                )],
                provisioning_role_arn="provisioningRoleArn",
                regional_parameters=[datazone.CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty(
                    parameters={
                        "parameters_key": "parameters"
                    },
                    region="region"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca96f6fc24dc164f6fafb08d94645f48f6b4fc5c0a2ad8a3b95e170935e7353a)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument enabled_regions", value=enabled_regions, expected_type=type_hints["enabled_regions"])
            check_type(argname="argument environment_blueprint_identifier", value=environment_blueprint_identifier, expected_type=type_hints["environment_blueprint_identifier"])
            check_type(argname="argument environment_role_permission_boundary", value=environment_role_permission_boundary, expected_type=type_hints["environment_role_permission_boundary"])
            check_type(argname="argument manage_access_role_arn", value=manage_access_role_arn, expected_type=type_hints["manage_access_role_arn"])
            check_type(argname="argument provisioning_configurations", value=provisioning_configurations, expected_type=type_hints["provisioning_configurations"])
            check_type(argname="argument provisioning_role_arn", value=provisioning_role_arn, expected_type=type_hints["provisioning_role_arn"])
            check_type(argname="argument regional_parameters", value=regional_parameters, expected_type=type_hints["regional_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "enabled_regions": enabled_regions,
            "environment_blueprint_identifier": environment_blueprint_identifier,
        }
        if environment_role_permission_boundary is not None:
            self._values["environment_role_permission_boundary"] = environment_role_permission_boundary
        if manage_access_role_arn is not None:
            self._values["manage_access_role_arn"] = manage_access_role_arn
        if provisioning_configurations is not None:
            self._values["provisioning_configurations"] = provisioning_configurations
        if provisioning_role_arn is not None:
            self._values["provisioning_role_arn"] = provisioning_role_arn
        if regional_parameters is not None:
            self._values["regional_parameters"] = regional_parameters

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which an environment blueprint exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html#cfn-datazone-environmentblueprintconfiguration-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled_regions(self) -> typing.List[builtins.str]:
        '''The enabled AWS Regions specified in a blueprint configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html#cfn-datazone-environmentblueprintconfiguration-enabledregions
        '''
        result = self._values.get("enabled_regions")
        assert result is not None, "Required property 'enabled_regions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def environment_blueprint_identifier(self) -> builtins.str:
        '''The identifier of the environment blueprint.

        In the current release, only the following values are supported: ``DefaultDataLake`` and ``DefaultDataWarehouse`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html#cfn-datazone-environmentblueprintconfiguration-environmentblueprintidentifier
        '''
        result = self._values.get("environment_blueprint_identifier")
        assert result is not None, "Required property 'environment_blueprint_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_role_permission_boundary(self) -> typing.Optional[builtins.str]:
        '''The environment role permission boundary.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html#cfn-datazone-environmentblueprintconfiguration-environmentrolepermissionboundary
        '''
        result = self._values.get("environment_role_permission_boundary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def manage_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the manage access role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html#cfn-datazone-environmentblueprintconfiguration-manageaccessrolearn
        '''
        result = self._values.get("manage_access_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provisioning_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentBlueprintConfiguration.ProvisioningConfigurationProperty]]]]:
        '''The provisioning configuration of a blueprint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html#cfn-datazone-environmentblueprintconfiguration-provisioningconfigurations
        '''
        result = self._values.get("provisioning_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentBlueprintConfiguration.ProvisioningConfigurationProperty]]]], result)

    @builtins.property
    def provisioning_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the provisioning role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html#cfn-datazone-environmentblueprintconfiguration-provisioningrolearn
        '''
        result = self._values.get("provisioning_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regional_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty]]]]:
        '''The regional parameters of the environment blueprint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html#cfn-datazone-environmentblueprintconfiguration-regionalparameters
        '''
        result = self._values.get("regional_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentBlueprintConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEnvironmentProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentProfile",
):
    '''The details of an environment profile.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html
    :cloudformationResource: AWS::DataZone::EnvironmentProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_environment_profile = datazone.CfnEnvironmentProfile(self, "MyCfnEnvironmentProfile",
            aws_account_id="awsAccountId",
            aws_account_region="awsAccountRegion",
            domain_identifier="domainIdentifier",
            environment_blueprint_identifier="environmentBlueprintIdentifier",
            name="name",
            project_identifier="projectIdentifier",
        
            # the properties below are optional
            description="description",
            user_parameters=[datazone.CfnEnvironmentProfile.EnvironmentParameterProperty(
                name="name",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        aws_account_id: builtins.str,
        aws_account_region: builtins.str,
        domain_identifier: builtins.str,
        environment_blueprint_identifier: builtins.str,
        name: builtins.str,
        project_identifier: builtins.str,
        description: typing.Optional[builtins.str] = None,
        user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironmentProfile.EnvironmentParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param aws_account_id: The identifier of an AWS account in which an environment profile exists.
        :param aws_account_region: The AWS Region in which an environment profile exists.
        :param domain_identifier: The identifier of the Amazon DataZone domain in which the environment profile exists.
        :param environment_blueprint_identifier: The identifier of a blueprint with which an environment profile is created.
        :param name: The name of the environment profile.
        :param project_identifier: The identifier of a project in which an environment profile exists.
        :param description: The description of the environment profile.
        :param user_parameters: The user parameters of this Amazon DataZone environment profile.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a22dac59a328e3776825e07c2891d034e7e205eeeb00866d9086cf2f1dceb4f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentProfileProps(
            aws_account_id=aws_account_id,
            aws_account_region=aws_account_region,
            domain_identifier=domain_identifier,
            environment_blueprint_identifier=environment_blueprint_identifier,
            name=name,
            project_identifier=project_identifier,
            description=description,
            user_parameters=user_parameters,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b72ea9dd66a1ceac9aed426988a2df917e784879f21b1f6f0c19ca29b30b31b0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d250e5f9b10cd5d865865b560ea448ee7860153a35651b00d758f6634aba260)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when an environment profile was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedBy")
    def attr_created_by(self) -> builtins.str:
        '''The Amazon DataZone user who created the environment profile.

        :cloudformationAttribute: CreatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the environment profile exists.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentBlueprintId")
    def attr_environment_blueprint_id(self) -> builtins.str:
        '''The identifier of a blueprint with which an environment profile is created.

        :cloudformationAttribute: EnvironmentBlueprintId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentBlueprintId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The identifier of the environment profile.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrProjectId")
    def attr_project_id(self) -> builtins.str:
        '''The identifier of a project in which an environment profile exists.

        :cloudformationAttribute: ProjectId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp of when the environment profile was updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> builtins.str:
        '''The identifier of an AWS account in which an environment profile exists.'''
        return typing.cast(builtins.str, jsii.get(self, "awsAccountId"))

    @aws_account_id.setter
    def aws_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de45320506b6ea6065d4e8de40a649bf205ae44ef01638670599709d45fde670)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsAccountId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="awsAccountRegion")
    def aws_account_region(self) -> builtins.str:
        '''The AWS Region in which an environment profile exists.'''
        return typing.cast(builtins.str, jsii.get(self, "awsAccountRegion"))

    @aws_account_region.setter
    def aws_account_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__929764ebd8bf0a538d63bf5bea864a4c6a1f1fa57874f35c72ee4cb0c977cdf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsAccountRegion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the environment profile exists.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9311c317e06fadb8c96c0e621239f5e4ce23903cdc1515f8f48973321817bc6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentBlueprintIdentifier")
    def environment_blueprint_identifier(self) -> builtins.str:
        '''The identifier of a blueprint with which an environment profile is created.'''
        return typing.cast(builtins.str, jsii.get(self, "environmentBlueprintIdentifier"))

    @environment_blueprint_identifier.setter
    def environment_blueprint_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40d0761ec5bd844c4a1859c609961ac63da5ca2a42154f19f8cdf0482693545f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentBlueprintIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the environment profile.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__894c00430dd4f51ab95f6ed5db99418bdfe03c4cd5e70df92930998dc03b23e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="projectIdentifier")
    def project_identifier(self) -> builtins.str:
        '''The identifier of a project in which an environment profile exists.'''
        return typing.cast(builtins.str, jsii.get(self, "projectIdentifier"))

    @project_identifier.setter
    def project_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32f0a4cae84b8e4e478646d80c611ae0d63fbea35bd054197eaeb64b33b624c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the environment profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__537f0658d3e004344b5e150e1c4182f64abe6101e2d21aaf1644347b19d27116)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="userParameters")
    def user_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentProfile.EnvironmentParameterProperty"]]]]:
        '''The user parameters of this Amazon DataZone environment profile.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentProfile.EnvironmentParameterProperty"]]]], jsii.get(self, "userParameters"))

    @user_parameters.setter
    def user_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentProfile.EnvironmentParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f091fadf5731901077c11ba7bce182eb007b6bd8b291bb6a4676fd3fa8e0e689)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userParameters", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentProfile.EnvironmentParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class EnvironmentParameterProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The parameter details of an environment profile.

            :param name: The name specified in the environment parameter.
            :param value: The value of the environment profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentprofile-environmentparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                environment_parameter_property = datazone.CfnEnvironmentProfile.EnvironmentParameterProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7d9a0947f6555aed5fe498e71fb0065f6dff69f004c35341f60523d1de281e5f)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name specified in the environment parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentprofile-environmentparameter.html#cfn-datazone-environmentprofile-environmentparameter-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of the environment profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentprofile-environmentparameter.html#cfn-datazone-environmentprofile-environmentparameter-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "aws_account_region": "awsAccountRegion",
        "domain_identifier": "domainIdentifier",
        "environment_blueprint_identifier": "environmentBlueprintIdentifier",
        "name": "name",
        "project_identifier": "projectIdentifier",
        "description": "description",
        "user_parameters": "userParameters",
    },
)
class CfnEnvironmentProfileProps:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        aws_account_region: builtins.str,
        domain_identifier: builtins.str,
        environment_blueprint_identifier: builtins.str,
        name: builtins.str,
        project_identifier: builtins.str,
        description: typing.Optional[builtins.str] = None,
        user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentProfile.EnvironmentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironmentProfile``.

        :param aws_account_id: The identifier of an AWS account in which an environment profile exists.
        :param aws_account_region: The AWS Region in which an environment profile exists.
        :param domain_identifier: The identifier of the Amazon DataZone domain in which the environment profile exists.
        :param environment_blueprint_identifier: The identifier of a blueprint with which an environment profile is created.
        :param name: The name of the environment profile.
        :param project_identifier: The identifier of a project in which an environment profile exists.
        :param description: The description of the environment profile.
        :param user_parameters: The user parameters of this Amazon DataZone environment profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_environment_profile_props = datazone.CfnEnvironmentProfileProps(
                aws_account_id="awsAccountId",
                aws_account_region="awsAccountRegion",
                domain_identifier="domainIdentifier",
                environment_blueprint_identifier="environmentBlueprintIdentifier",
                name="name",
                project_identifier="projectIdentifier",
            
                # the properties below are optional
                description="description",
                user_parameters=[datazone.CfnEnvironmentProfile.EnvironmentParameterProperty(
                    name="name",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24d37d0c5f53a77c5e5be4ffa574af7dd3da85d8b5eb31bff30362d6c63ac36b)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument aws_account_region", value=aws_account_region, expected_type=type_hints["aws_account_region"])
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument environment_blueprint_identifier", value=environment_blueprint_identifier, expected_type=type_hints["environment_blueprint_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project_identifier", value=project_identifier, expected_type=type_hints["project_identifier"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument user_parameters", value=user_parameters, expected_type=type_hints["user_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "aws_account_region": aws_account_region,
            "domain_identifier": domain_identifier,
            "environment_blueprint_identifier": environment_blueprint_identifier,
            "name": name,
            "project_identifier": project_identifier,
        }
        if description is not None:
            self._values["description"] = description
        if user_parameters is not None:
            self._values["user_parameters"] = user_parameters

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The identifier of an AWS account in which an environment profile exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html#cfn-datazone-environmentprofile-awsaccountid
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_region(self) -> builtins.str:
        '''The AWS Region in which an environment profile exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html#cfn-datazone-environmentprofile-awsaccountregion
        '''
        result = self._values.get("aws_account_region")
        assert result is not None, "Required property 'aws_account_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the environment profile exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html#cfn-datazone-environmentprofile-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_blueprint_identifier(self) -> builtins.str:
        '''The identifier of a blueprint with which an environment profile is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html#cfn-datazone-environmentprofile-environmentblueprintidentifier
        '''
        result = self._values.get("environment_blueprint_identifier")
        assert result is not None, "Required property 'environment_blueprint_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the environment profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html#cfn-datazone-environmentprofile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_identifier(self) -> builtins.str:
        '''The identifier of a project in which an environment profile exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html#cfn-datazone-environmentprofile-projectidentifier
        '''
        result = self._values.get("project_identifier")
        assert result is not None, "Required property 'project_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the environment profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html#cfn-datazone-environmentprofile-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentProfile.EnvironmentParameterProperty]]]]:
        '''The user parameters of this Amazon DataZone environment profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html#cfn-datazone-environmentprofile-userparameters
        '''
        result = self._values.get("user_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentProfile.EnvironmentParameterProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "name": "name",
        "project_identifier": "projectIdentifier",
        "description": "description",
        "environment_account_identifier": "environmentAccountIdentifier",
        "environment_account_region": "environmentAccountRegion",
        "environment_profile_identifier": "environmentProfileIdentifier",
        "environment_role_arn": "environmentRoleArn",
        "glossary_terms": "glossaryTerms",
        "user_parameters": "userParameters",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        name: builtins.str,
        project_identifier: builtins.str,
        description: typing.Optional[builtins.str] = None,
        environment_account_identifier: typing.Optional[builtins.str] = None,
        environment_account_region: typing.Optional[builtins.str] = None,
        environment_profile_identifier: typing.Optional[builtins.str] = None,
        environment_role_arn: typing.Optional[builtins.str] = None,
        glossary_terms: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.EnvironmentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironment``.

        :param domain_identifier: The identifier of the Amazon DataZone domain in which the environment is created.
        :param name: The name of the Amazon DataZone environment.
        :param project_identifier: The identifier of the Amazon DataZone project in which this environment is created.
        :param description: The description of the environment.
        :param environment_account_identifier: The identifier of the AWS account in which an environment exists.
        :param environment_account_region: The AWS Region in which an environment exists.
        :param environment_profile_identifier: The identifier of the environment profile that is used to create this Amazon DataZone environment.
        :param environment_role_arn: The ARN of the environment role.
        :param glossary_terms: The glossary terms that can be used in this Amazon DataZone environment.
        :param user_parameters: The user parameters of this Amazon DataZone environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_environment_props = datazone.CfnEnvironmentProps(
                domain_identifier="domainIdentifier",
                name="name",
                project_identifier="projectIdentifier",
            
                # the properties below are optional
                description="description",
                environment_account_identifier="environmentAccountIdentifier",
                environment_account_region="environmentAccountRegion",
                environment_profile_identifier="environmentProfileIdentifier",
                environment_role_arn="environmentRoleArn",
                glossary_terms=["glossaryTerms"],
                user_parameters=[datazone.CfnEnvironment.EnvironmentParameterProperty(
                    name="name",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52cb17aae6cf0b0cbeef010a71f7f53573517f0a8e973b5881ae34c1691d672b)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project_identifier", value=project_identifier, expected_type=type_hints["project_identifier"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment_account_identifier", value=environment_account_identifier, expected_type=type_hints["environment_account_identifier"])
            check_type(argname="argument environment_account_region", value=environment_account_region, expected_type=type_hints["environment_account_region"])
            check_type(argname="argument environment_profile_identifier", value=environment_profile_identifier, expected_type=type_hints["environment_profile_identifier"])
            check_type(argname="argument environment_role_arn", value=environment_role_arn, expected_type=type_hints["environment_role_arn"])
            check_type(argname="argument glossary_terms", value=glossary_terms, expected_type=type_hints["glossary_terms"])
            check_type(argname="argument user_parameters", value=user_parameters, expected_type=type_hints["user_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "name": name,
            "project_identifier": project_identifier,
        }
        if description is not None:
            self._values["description"] = description
        if environment_account_identifier is not None:
            self._values["environment_account_identifier"] = environment_account_identifier
        if environment_account_region is not None:
            self._values["environment_account_region"] = environment_account_region
        if environment_profile_identifier is not None:
            self._values["environment_profile_identifier"] = environment_profile_identifier
        if environment_role_arn is not None:
            self._values["environment_role_arn"] = environment_role_arn
        if glossary_terms is not None:
            self._values["glossary_terms"] = glossary_terms
        if user_parameters is not None:
            self._values["user_parameters"] = user_parameters

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the environment is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the Amazon DataZone environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone project in which this environment is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-projectidentifier
        '''
        result = self._values.get("project_identifier")
        assert result is not None, "Required property 'project_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_account_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the AWS account in which an environment exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-environmentaccountidentifier
        '''
        result = self._values.get("environment_account_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_account_region(self) -> typing.Optional[builtins.str]:
        '''The AWS Region in which an environment exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-environmentaccountregion
        '''
        result = self._values.get("environment_account_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_profile_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the environment profile that is used to create this Amazon DataZone environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-environmentprofileidentifier
        '''
        result = self._values.get("environment_profile_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the environment role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-environmentrolearn
        '''
        result = self._values.get("environment_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def glossary_terms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The glossary terms that can be used in this Amazon DataZone environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-glossaryterms
        '''
        result = self._values.get("glossary_terms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def user_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.EnvironmentParameterProperty]]]]:
        '''The user parameters of this Amazon DataZone environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-userparameters
        '''
        result = self._values.get("user_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.EnvironmentParameterProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnGroupProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnGroupProfile",
):
    '''The details of a group profile in Amazon DataZone.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-groupprofile.html
    :cloudformationResource: AWS::DataZone::GroupProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_group_profile = datazone.CfnGroupProfile(self, "MyCfnGroupProfile",
            domain_identifier="domainIdentifier",
            group_identifier="groupIdentifier",
        
            # the properties below are optional
            status="status"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_identifier: builtins.str,
        group_identifier: builtins.str,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_identifier: The identifier of the Amazon DataZone domain in which a group profile exists.
        :param group_identifier: The ID of the group of a project member.
        :param status: The status of a group profile.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bccafb3ac5ccb0c73cc0aaea6cf365a78e841d8d731ffbfa84165d7f8100f7a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGroupProfileProps(
            domain_identifier=domain_identifier,
            group_identifier=group_identifier,
            status=status,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3064788268855f6623aaf3b52a7be17022b3d0c8d206428bb22e10d7bd9791de)
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
            type_hints = typing.get_type_hints(_typecheckingstub__66e617beac92ae83db2859cea30504a6e86d11714b8584d4212fe2f5634055e4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which a group profile exists.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrGroupName")
    def attr_group_name(self) -> builtins.str:
        '''The name of a group profile.

        :cloudformationAttribute: GroupName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGroupName"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of a group profile.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which a group profile exists.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bfce5f937e19aa12105a026759b48056e8cb9facac990d4a84ae9ebf754349a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="groupIdentifier")
    def group_identifier(self) -> builtins.str:
        '''The ID of the group of a project member.'''
        return typing.cast(builtins.str, jsii.get(self, "groupIdentifier"))

    @group_identifier.setter
    def group_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4cfe59401594c99ca6ed491e080ab3526afa6a5fbfa200d918455779f2c060f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of a group profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__489105c9239ff5a560f37a1c161dc9de12874e97ca98bb0ac4df8139e29b6727)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnGroupProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "group_identifier": "groupIdentifier",
        "status": "status",
    },
)
class CfnGroupProfileProps:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        group_identifier: builtins.str,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnGroupProfile``.

        :param domain_identifier: The identifier of the Amazon DataZone domain in which a group profile exists.
        :param group_identifier: The ID of the group of a project member.
        :param status: The status of a group profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-groupprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_group_profile_props = datazone.CfnGroupProfileProps(
                domain_identifier="domainIdentifier",
                group_identifier="groupIdentifier",
            
                # the properties below are optional
                status="status"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f4f2d05f4850cb07cd88e6e5af875d2c16fa3ae4bcbc384b9a51f7f0d0ca2e4)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument group_identifier", value=group_identifier, expected_type=type_hints["group_identifier"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "group_identifier": group_identifier,
        }
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which a group profile exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-groupprofile.html#cfn-datazone-groupprofile-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_identifier(self) -> builtins.str:
        '''The ID of the group of a project member.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-groupprofile.html#cfn-datazone-groupprofile-groupidentifier
        '''
        result = self._values.get("group_identifier")
        assert result is not None, "Required property 'group_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of a group profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-groupprofile.html#cfn-datazone-groupprofile-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnOwner(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnOwner",
):
    '''The owner that you want to add to the entity.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-owner.html
    :cloudformationResource: AWS::DataZone::Owner
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_owner = datazone.CfnOwner(self, "MyCfnOwner",
            domain_identifier="domainIdentifier",
            entity_identifier="entityIdentifier",
            entity_type="entityType",
            owner=datazone.CfnOwner.OwnerPropertiesProperty(
                group=datazone.CfnOwner.OwnerGroupPropertiesProperty(
                    group_identifier="groupIdentifier"
                ),
                user=datazone.CfnOwner.OwnerUserPropertiesProperty(
                    user_identifier="userIdentifier"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_identifier: builtins.str,
        entity_identifier: builtins.str,
        entity_type: builtins.str,
        owner: typing.Union[_IResolvable_da3f097b, typing.Union["CfnOwner.OwnerPropertiesProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_identifier: The ID of the domain in which you want to add the entity owner.
        :param entity_identifier: The ID of the entity to which you want to add an owner.
        :param entity_type: The type of an entity.
        :param owner: The owner that you want to add to the entity.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94bfd7733fd63571746923975807ae8f32ba35341a37f7148bb545b4e9847274)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOwnerProps(
            domain_identifier=domain_identifier,
            entity_identifier=entity_identifier,
            entity_type=entity_type,
            owner=owner,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa3b09221ad53f7b391234ed414a2caf5be239897130cb63a881be90fd3d5159)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7abc3e34a10e4f417d29d275feb8d0afab58fee4bf106d762ec5e892461eaa7)
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
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The ID of the domain in which you want to add the entity owner.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9073faa55a5b23ffa32de5b7b260a878507e76f90477bf1a9c90357c2872891)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="entityIdentifier")
    def entity_identifier(self) -> builtins.str:
        '''The ID of the entity to which you want to add an owner.'''
        return typing.cast(builtins.str, jsii.get(self, "entityIdentifier"))

    @entity_identifier.setter
    def entity_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__553cfea40a703af75f1688c6e78763ca8d67d1e10486295a4f15880e459e83ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="entityType")
    def entity_type(self) -> builtins.str:
        '''The type of an entity.'''
        return typing.cast(builtins.str, jsii.get(self, "entityType"))

    @entity_type.setter
    def entity_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59a8766cde46db5fea0cab80e368951dc950c0c18bbe166065a74941ff7268d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnOwner.OwnerPropertiesProperty"]:
        '''The owner that you want to add to the entity.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnOwner.OwnerPropertiesProperty"], jsii.get(self, "owner"))

    @owner.setter
    def owner(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnOwner.OwnerPropertiesProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9200651c9921dbe5e1d4780332c9e8f8b197d26e18954ed4949d2b2e1f42f642)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnOwner.OwnerGroupPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"group_identifier": "groupIdentifier"},
    )
    class OwnerGroupPropertiesProperty:
        def __init__(
            self,
            *,
            group_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The properties of the domain unit owners group.

            :param group_identifier: The ID of the domain unit owners group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-owner-ownergroupproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                owner_group_properties_property = datazone.CfnOwner.OwnerGroupPropertiesProperty(
                    group_identifier="groupIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ebdf17d77276482c77fb47efd9e4dbd02334583fe0ecbd40c08d7f701ee8d14b)
                check_type(argname="argument group_identifier", value=group_identifier, expected_type=type_hints["group_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if group_identifier is not None:
                self._values["group_identifier"] = group_identifier

        @builtins.property
        def group_identifier(self) -> typing.Optional[builtins.str]:
            '''The ID of the domain unit owners group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-owner-ownergroupproperties.html#cfn-datazone-owner-ownergroupproperties-groupidentifier
            '''
            result = self._values.get("group_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OwnerGroupPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnOwner.OwnerPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"group": "group", "user": "user"},
    )
    class OwnerPropertiesProperty:
        def __init__(
            self,
            *,
            group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOwner.OwnerGroupPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            user: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOwner.OwnerUserPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The properties of a domain unit's owner.

            :param group: Specifies that the domain unit owner is a group.
            :param user: Specifies that the domain unit owner is a user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-owner-ownerproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                owner_properties_property = datazone.CfnOwner.OwnerPropertiesProperty(
                    group=datazone.CfnOwner.OwnerGroupPropertiesProperty(
                        group_identifier="groupIdentifier"
                    ),
                    user=datazone.CfnOwner.OwnerUserPropertiesProperty(
                        user_identifier="userIdentifier"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5c101d7b0fa44737f68ea873c4543f1aaebe3e1acc72b89c5d6be7d3315a3f6a)
                check_type(argname="argument group", value=group, expected_type=type_hints["group"])
                check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if group is not None:
                self._values["group"] = group
            if user is not None:
                self._values["user"] = user

        @builtins.property
        def group(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOwner.OwnerGroupPropertiesProperty"]]:
            '''Specifies that the domain unit owner is a group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-owner-ownerproperties.html#cfn-datazone-owner-ownerproperties-group
            '''
            result = self._values.get("group")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOwner.OwnerGroupPropertiesProperty"]], result)

        @builtins.property
        def user(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOwner.OwnerUserPropertiesProperty"]]:
            '''Specifies that the domain unit owner is a user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-owner-ownerproperties.html#cfn-datazone-owner-ownerproperties-user
            '''
            result = self._values.get("user")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOwner.OwnerUserPropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OwnerPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnOwner.OwnerUserPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"user_identifier": "userIdentifier"},
    )
    class OwnerUserPropertiesProperty:
        def __init__(
            self,
            *,
            user_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The properties of the owner user.

            :param user_identifier: The ID of the owner user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-owner-owneruserproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                owner_user_properties_property = datazone.CfnOwner.OwnerUserPropertiesProperty(
                    user_identifier="userIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6ddd200ac00629d27d95838e6fe38733e398593324aa72df62d033667a13781d)
                check_type(argname="argument user_identifier", value=user_identifier, expected_type=type_hints["user_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if user_identifier is not None:
                self._values["user_identifier"] = user_identifier

        @builtins.property
        def user_identifier(self) -> typing.Optional[builtins.str]:
            '''The ID of the owner user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-owner-owneruserproperties.html#cfn-datazone-owner-owneruserproperties-useridentifier
            '''
            result = self._values.get("user_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OwnerUserPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnOwnerProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "entity_identifier": "entityIdentifier",
        "entity_type": "entityType",
        "owner": "owner",
    },
)
class CfnOwnerProps:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        entity_identifier: builtins.str,
        entity_type: builtins.str,
        owner: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOwner.OwnerPropertiesProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnOwner``.

        :param domain_identifier: The ID of the domain in which you want to add the entity owner.
        :param entity_identifier: The ID of the entity to which you want to add an owner.
        :param entity_type: The type of an entity.
        :param owner: The owner that you want to add to the entity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-owner.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_owner_props = datazone.CfnOwnerProps(
                domain_identifier="domainIdentifier",
                entity_identifier="entityIdentifier",
                entity_type="entityType",
                owner=datazone.CfnOwner.OwnerPropertiesProperty(
                    group=datazone.CfnOwner.OwnerGroupPropertiesProperty(
                        group_identifier="groupIdentifier"
                    ),
                    user=datazone.CfnOwner.OwnerUserPropertiesProperty(
                        user_identifier="userIdentifier"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d35804fdeb7af54df495ac452da3f154252f3e8b980bc354ae920748f4c8e46d)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument entity_identifier", value=entity_identifier, expected_type=type_hints["entity_identifier"])
            check_type(argname="argument entity_type", value=entity_type, expected_type=type_hints["entity_type"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "entity_identifier": entity_identifier,
            "entity_type": entity_type,
            "owner": owner,
        }

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The ID of the domain in which you want to add the entity owner.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-owner.html#cfn-datazone-owner-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def entity_identifier(self) -> builtins.str:
        '''The ID of the entity to which you want to add an owner.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-owner.html#cfn-datazone-owner-entityidentifier
        '''
        result = self._values.get("entity_identifier")
        assert result is not None, "Required property 'entity_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def entity_type(self) -> builtins.str:
        '''The type of an entity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-owner.html#cfn-datazone-owner-entitytype
        '''
        result = self._values.get("entity_type")
        assert result is not None, "Required property 'entity_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def owner(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnOwner.OwnerPropertiesProperty]:
        '''The owner that you want to add to the entity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-owner.html#cfn-datazone-owner-owner
        '''
        result = self._values.get("owner")
        assert result is not None, "Required property 'owner' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnOwner.OwnerPropertiesProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOwnerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnProject(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnProject",
):
    '''The ``AWS::DataZone::Project`` resource specifies an Amazon DataZone project.

    Projects enable a group of users to collaborate on various business use cases that involve publishing, discovering, subscribing to, and consuming data in the Amazon DataZone catalog. Project members consume assets from the Amazon DataZone catalog and produce new assets using one or more analytical workflows.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html
    :cloudformationResource: AWS::DataZone::Project
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_project = datazone.CfnProject(self, "MyCfnProject",
            domain_identifier="domainIdentifier",
            name="name",
        
            # the properties below are optional
            description="description",
            domain_unit_id="domainUnitId",
            glossary_terms=["glossaryTerms"],
            project_profile_id="projectProfileId",
            project_profile_version="projectProfileVersion",
            user_parameters=[datazone.CfnProject.EnvironmentConfigurationUserParameterProperty(
                environment_configuration_name="environmentConfigurationName",
                environment_id="environmentId",
                environment_parameters=[datazone.CfnProject.EnvironmentParameterProperty(
                    name="name",
                    value="value"
                )]
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_identifier: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        domain_unit_id: typing.Optional[builtins.str] = None,
        glossary_terms: typing.Optional[typing.Sequence[builtins.str]] = None,
        project_profile_id: typing.Optional[builtins.str] = None,
        project_profile_version: typing.Optional[builtins.str] = None,
        user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnProject.EnvironmentConfigurationUserParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_identifier: The identifier of a Amazon DataZone domain where the project exists.
        :param name: The name of a project.
        :param description: The description of a project.
        :param domain_unit_id: The ID of the domain unit. This parameter is not required and if it is not specified, then the project is created at the root domain unit level.
        :param glossary_terms: The glossary terms that can be used in this Amazon DataZone project.
        :param project_profile_id: The ID of the project profile.
        :param project_profile_version: The project profile version to which the project should be updated. You can only specify the following string for this parameter: ``latest`` .
        :param user_parameters: The user parameters of the project.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dd190e348e5421f499a11e44b2fb0c69295587e5e7717b13a56786a897efe7f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectProps(
            domain_identifier=domain_identifier,
            name=name,
            description=description,
            domain_unit_id=domain_unit_id,
            glossary_terms=glossary_terms,
            project_profile_id=project_profile_id,
            project_profile_version=project_profile_version,
            user_parameters=user_parameters,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dec99f127bfd691b7b1ab5260c233568e5b335a316a646dd759686435ab2eb32)
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
            type_hints = typing.get_type_hints(_typecheckingstub__81361e533bde98a7e424eedf14591a679c836493433a44301b63cbf3357e5369)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when a project was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedBy")
    def attr_created_by(self) -> builtins.str:
        '''The Amazon DataZone user who created the project.

        :cloudformationAttribute: CreatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The identifier of a Amazon DataZone domain where the project exists.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The identifier of a project.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The timestamp of when the project was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrProjectStatus")
    def attr_project_status(self) -> builtins.str:
        '''The status of the project.

        :cloudformationAttribute: ProjectStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The identifier of a Amazon DataZone domain where the project exists.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c4440504b53716f23143b92e80a5ea3dcfaddd707d93cad9b77c33e5e19e7a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of a project.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7972d56cc7ec2cdd1800b8f0d6a79f7b4ad88633cf64a2e04f072fab6c9454b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of a project.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbb0277c9bfd29282afdae45a284966770345575b2854ec5cd9e6c04dffbac96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainUnitId")
    def domain_unit_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the domain unit.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainUnitId"))

    @domain_unit_id.setter
    def domain_unit_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38159bc2eeb309ee419b2f700c1738155e88fd699cb77897bb1441e19caa9250)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainUnitId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="glossaryTerms")
    def glossary_terms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The glossary terms that can be used in this Amazon DataZone project.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "glossaryTerms"))

    @glossary_terms.setter
    def glossary_terms(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed99a8f1a094dd4883e961330ac91acc714a4a5fd200b2d53a52d4113d5a34f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "glossaryTerms", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="projectProfileId")
    def project_profile_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the project profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectProfileId"))

    @project_profile_id.setter
    def project_profile_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd4329ffc5180ec3c489a9b9628b37fda4e7e56daeff4465877926e7905d64d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectProfileId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="projectProfileVersion")
    def project_profile_version(self) -> typing.Optional[builtins.str]:
        '''The project profile version to which the project should be updated.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectProfileVersion"))

    @project_profile_version.setter
    def project_profile_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fea851298bf6dff2224e18bba1dcf8117578fd86b764925c8087d78e2917049)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectProfileVersion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="userParameters")
    def user_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProject.EnvironmentConfigurationUserParameterProperty"]]]]:
        '''The user parameters of the project.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProject.EnvironmentConfigurationUserParameterProperty"]]]], jsii.get(self, "userParameters"))

    @user_parameters.setter
    def user_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProject.EnvironmentConfigurationUserParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a8a1e223cb296d2e10e4a3c700e7f0c868d2c481c6f8c40ddf1c6a06e86a604)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userParameters", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnProject.EnvironmentConfigurationUserParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "environment_configuration_name": "environmentConfigurationName",
            "environment_id": "environmentId",
            "environment_parameters": "environmentParameters",
        },
    )
    class EnvironmentConfigurationUserParameterProperty:
        def __init__(
            self,
            *,
            environment_configuration_name: typing.Optional[builtins.str] = None,
            environment_id: typing.Optional[builtins.str] = None,
            environment_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnProject.EnvironmentParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The environment configuration user parameters.

            :param environment_configuration_name: The environment configuration name.
            :param environment_id: The ID of the environment.
            :param environment_parameters: The environment parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-project-environmentconfigurationuserparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                environment_configuration_user_parameter_property = datazone.CfnProject.EnvironmentConfigurationUserParameterProperty(
                    environment_configuration_name="environmentConfigurationName",
                    environment_id="environmentId",
                    environment_parameters=[datazone.CfnProject.EnvironmentParameterProperty(
                        name="name",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2e38660ae766630ccadf35e49b4f78a771668296fc64a72a9c1e9b3d3b1a16a1)
                check_type(argname="argument environment_configuration_name", value=environment_configuration_name, expected_type=type_hints["environment_configuration_name"])
                check_type(argname="argument environment_id", value=environment_id, expected_type=type_hints["environment_id"])
                check_type(argname="argument environment_parameters", value=environment_parameters, expected_type=type_hints["environment_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if environment_configuration_name is not None:
                self._values["environment_configuration_name"] = environment_configuration_name
            if environment_id is not None:
                self._values["environment_id"] = environment_id
            if environment_parameters is not None:
                self._values["environment_parameters"] = environment_parameters

        @builtins.property
        def environment_configuration_name(self) -> typing.Optional[builtins.str]:
            '''The environment configuration name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-project-environmentconfigurationuserparameter.html#cfn-datazone-project-environmentconfigurationuserparameter-environmentconfigurationname
            '''
            result = self._values.get("environment_configuration_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def environment_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-project-environmentconfigurationuserparameter.html#cfn-datazone-project-environmentconfigurationuserparameter-environmentid
            '''
            result = self._values.get("environment_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def environment_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProject.EnvironmentParameterProperty"]]]]:
            '''The environment parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-project-environmentconfigurationuserparameter.html#cfn-datazone-project-environmentconfigurationuserparameter-environmentparameters
            '''
            result = self._values.get("environment_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProject.EnvironmentParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentConfigurationUserParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnProject.EnvironmentParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class EnvironmentParameterProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The parameter details of an evironment profile.

            :param name: The name of an environment profile parameter.
            :param value: The value of an environment profile parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-project-environmentparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                environment_parameter_property = datazone.CfnProject.EnvironmentParameterProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4bfbfca939a617b6012dc8847e17b3567d673ec789228318c5d1c397165a7b9e)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of an environment profile parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-project-environmentparameter.html#cfn-datazone-project-environmentparameter-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of an environment profile parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-project-environmentparameter.html#cfn-datazone-project-environmentparameter-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnProjectMembership(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnProjectMembership",
):
    '''The ``AWS::DataZone::ProjectMembership`` resource adds a member to an Amazon DataZone project.

    Project members consume assets from the Amazon DataZone catalog and produce new assets using one or more analytical workflows.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectmembership.html
    :cloudformationResource: AWS::DataZone::ProjectMembership
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_project_membership = datazone.CfnProjectMembership(self, "MyCfnProjectMembership",
            designation="designation",
            domain_identifier="domainIdentifier",
            member=datazone.CfnProjectMembership.MemberProperty(
                group_identifier="groupIdentifier",
                user_identifier="userIdentifier"
            ),
            project_identifier="projectIdentifier"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        designation: builtins.str,
        domain_identifier: builtins.str,
        member: typing.Union[_IResolvable_da3f097b, typing.Union["CfnProjectMembership.MemberProperty", typing.Dict[builtins.str, typing.Any]]],
        project_identifier: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param designation: The designated role of a project member.
        :param domain_identifier: The ID of the Amazon DataZone domain in which project membership is created.
        :param member: The details about a project member.
        :param project_identifier: The ID of the project for which this project membership was created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__227cc3d5649ee98fd5579f9e1870652d6de5250e0390e91fec524565dc07c0b9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectMembershipProps(
            designation=designation,
            domain_identifier=domain_identifier,
            member=member,
            project_identifier=project_identifier,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e6a7791d79b9b8f15baba0f04bddbfa77afbfbdd8d2872a6e46acd2ccee79c4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e37a11438611477027ae5dde4a091dc361c7dc56ba7538221e222ef9083be907)
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
    @jsii.member(jsii_name="designation")
    def designation(self) -> builtins.str:
        '''The designated role of a project member.'''
        return typing.cast(builtins.str, jsii.get(self, "designation"))

    @designation.setter
    def designation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71ec417c1a2abac8b6037b5bfedeb8520a3be4a0844d46c1862cb259465e45f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "designation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The ID of the Amazon DataZone domain in which project membership is created.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66d809e4462dc85243bcc1ab3799cc4a5180f2f4119683718081fa5f79530ac7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="member")
    def member(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnProjectMembership.MemberProperty"]:
        '''The details about a project member.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnProjectMembership.MemberProperty"], jsii.get(self, "member"))

    @member.setter
    def member(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnProjectMembership.MemberProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50f6e6b64e6349a5c9d740955a9ccac88cf9da161bf02038bc9e12572958a93f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "member", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="projectIdentifier")
    def project_identifier(self) -> builtins.str:
        '''The ID of the project for which this project membership was created.'''
        return typing.cast(builtins.str, jsii.get(self, "projectIdentifier"))

    @project_identifier.setter
    def project_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da845d5c47de18f48a6a2e21aa5b41e5193d4b3faad962602fc4d3b98d677eb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectIdentifier", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnProjectMembership.MemberProperty",
        jsii_struct_bases=[],
        name_mapping={
            "group_identifier": "groupIdentifier",
            "user_identifier": "userIdentifier",
        },
    )
    class MemberProperty:
        def __init__(
            self,
            *,
            group_identifier: typing.Optional[builtins.str] = None,
            user_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The details about a project member.

            Important - this data type is a UNION, so only one of the following members can be specified when used or returned.

            :param group_identifier: The ID of the group of a project member.
            :param user_identifier: The user ID of a project member.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectmembership-member.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                member_property = datazone.CfnProjectMembership.MemberProperty(
                    group_identifier="groupIdentifier",
                    user_identifier="userIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2184a0c3aa18e8899e2cb70b944b79d781e689bd543ac2140e9176025c2fa864)
                check_type(argname="argument group_identifier", value=group_identifier, expected_type=type_hints["group_identifier"])
                check_type(argname="argument user_identifier", value=user_identifier, expected_type=type_hints["user_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if group_identifier is not None:
                self._values["group_identifier"] = group_identifier
            if user_identifier is not None:
                self._values["user_identifier"] = user_identifier

        @builtins.property
        def group_identifier(self) -> typing.Optional[builtins.str]:
            '''The ID of the group of a project member.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectmembership-member.html#cfn-datazone-projectmembership-member-groupidentifier
            '''
            result = self._values.get("group_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_identifier(self) -> typing.Optional[builtins.str]:
            '''The user ID of a project member.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectmembership-member.html#cfn-datazone-projectmembership-member-useridentifier
            '''
            result = self._values.get("user_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemberProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnProjectMembershipProps",
    jsii_struct_bases=[],
    name_mapping={
        "designation": "designation",
        "domain_identifier": "domainIdentifier",
        "member": "member",
        "project_identifier": "projectIdentifier",
    },
)
class CfnProjectMembershipProps:
    def __init__(
        self,
        *,
        designation: builtins.str,
        domain_identifier: builtins.str,
        member: typing.Union[_IResolvable_da3f097b, typing.Union[CfnProjectMembership.MemberProperty, typing.Dict[builtins.str, typing.Any]]],
        project_identifier: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnProjectMembership``.

        :param designation: The designated role of a project member.
        :param domain_identifier: The ID of the Amazon DataZone domain in which project membership is created.
        :param member: The details about a project member.
        :param project_identifier: The ID of the project for which this project membership was created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectmembership.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_project_membership_props = datazone.CfnProjectMembershipProps(
                designation="designation",
                domain_identifier="domainIdentifier",
                member=datazone.CfnProjectMembership.MemberProperty(
                    group_identifier="groupIdentifier",
                    user_identifier="userIdentifier"
                ),
                project_identifier="projectIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b25f4db16efa2b368a4cf197bdf102ccdf0c613db5654c1186f9404f9259e4d7)
            check_type(argname="argument designation", value=designation, expected_type=type_hints["designation"])
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument member", value=member, expected_type=type_hints["member"])
            check_type(argname="argument project_identifier", value=project_identifier, expected_type=type_hints["project_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "designation": designation,
            "domain_identifier": domain_identifier,
            "member": member,
            "project_identifier": project_identifier,
        }

    @builtins.property
    def designation(self) -> builtins.str:
        '''The designated role of a project member.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectmembership.html#cfn-datazone-projectmembership-designation
        '''
        result = self._values.get("designation")
        assert result is not None, "Required property 'designation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The ID of the Amazon DataZone domain in which project membership is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectmembership.html#cfn-datazone-projectmembership-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnProjectMembership.MemberProperty]:
        '''The details about a project member.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectmembership.html#cfn-datazone-projectmembership-member
        '''
        result = self._values.get("member")
        assert result is not None, "Required property 'member' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnProjectMembership.MemberProperty], result)

    @builtins.property
    def project_identifier(self) -> builtins.str:
        '''The ID of the project for which this project membership was created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectmembership.html#cfn-datazone-projectmembership-projectidentifier
        '''
        result = self._values.get("project_identifier")
        assert result is not None, "Required property 'project_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectMembershipProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnProjectProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnProjectProfile",
):
    '''The summary of a project profile.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectprofile.html
    :cloudformationResource: AWS::DataZone::ProjectProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_project_profile = datazone.CfnProjectProfile(self, "MyCfnProjectProfile",
            name="name",
        
            # the properties below are optional
            description="description",
            domain_identifier="domainIdentifier",
            domain_unit_identifier="domainUnitIdentifier",
            environment_configurations=[datazone.CfnProjectProfile.EnvironmentConfigurationProperty(
                aws_region=datazone.CfnProjectProfile.RegionProperty(
                    region_name="regionName"
                ),
                environment_blueprint_id="environmentBlueprintId",
                name="name",
        
                # the properties below are optional
                aws_account=datazone.CfnProjectProfile.AwsAccountProperty(
                    aws_account_id="awsAccountId"
                ),
                configuration_parameters=datazone.CfnProjectProfile.EnvironmentConfigurationParametersDetailsProperty(
                    parameter_overrides=[datazone.CfnProjectProfile.EnvironmentConfigurationParameterProperty(
                        is_editable=False,
                        name="name",
                        value="value"
                    )],
                    resolved_parameters=[datazone.CfnProjectProfile.EnvironmentConfigurationParameterProperty(
                        is_editable=False,
                        name="name",
                        value="value"
                    )],
                    ssm_path="ssmPath"
                ),
                deployment_mode="deploymentMode",
                deployment_order=123,
                description="description",
                id="id"
            )],
            status="status"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        domain_identifier: typing.Optional[builtins.str] = None,
        domain_unit_identifier: typing.Optional[builtins.str] = None,
        environment_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnProjectProfile.EnvironmentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of a project profile.
        :param description: The description of the project profile.
        :param domain_identifier: A domain ID of the project profile.
        :param domain_unit_identifier: A domain unit ID of the project profile.
        :param environment_configurations: Environment configurations of a project profile.
        :param status: The status of a project profile.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be64eda6c4825457191dba5045e07eaa3e14f5b1d6605cefc1c291b8f70eb5b2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectProfileProps(
            name=name,
            description=description,
            domain_identifier=domain_identifier,
            domain_unit_identifier=domain_unit_identifier,
            environment_configurations=environment_configurations,
            status=status,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b4346bd08f5dc87b3a8b49fbf28cae8774624d1da19c5d260d4fbdf104d531f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__85b771eebccea5f26f952595144e99a6c3ff8b1d0cce9803511978dff3785a2a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when the project profile was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedBy")
    def attr_created_by(self) -> builtins.str:
        '''The user who created the project profile.

        :cloudformationAttribute: CreatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The domain ID of the project profile.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainUnitId")
    def attr_domain_unit_id(self) -> builtins.str:
        '''The domain unit ID of the project profile.

        :cloudformationAttribute: DomainUnitId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainUnitId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the project profile.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentifier")
    def attr_identifier(self) -> builtins.str:
        '''Project profile ID.

        :cloudformationAttribute: Identifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The timestamp at which a project profile was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of a project profile.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5acf0d662fb5f406ca391f15c3cadba1d68d0dc161876b2305e495701c03968)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the project profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3e1ff90e5fbfc5a555174f254ce075a9c3654511436a8acf04928992020df04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> typing.Optional[builtins.str]:
        '''A domain ID of the project profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__872e790316704042dc15857aaaff7b99878b643ac02f9de929f704cf6ca6762a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainUnitIdentifier")
    def domain_unit_identifier(self) -> typing.Optional[builtins.str]:
        '''A domain unit ID of the project profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainUnitIdentifier"))

    @domain_unit_identifier.setter
    def domain_unit_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b87add426c25b8a2eafdfd51a8707432f3ee35363162b07265e414b1d427ff1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainUnitIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentConfigurations")
    def environment_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProjectProfile.EnvironmentConfigurationProperty"]]]]:
        '''Environment configurations of a project profile.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProjectProfile.EnvironmentConfigurationProperty"]]]], jsii.get(self, "environmentConfigurations"))

    @environment_configurations.setter
    def environment_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProjectProfile.EnvironmentConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11d2d41d817a0c6b3e1fb33f36874d8544dda639fa89db0b3de59a24198ab098)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentConfigurations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of a project profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22f2f0484438c03962ae71a7a8c680afa1c54e8a672160956c3951d55a32ae02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnProjectProfile.AwsAccountProperty",
        jsii_struct_bases=[],
        name_mapping={"aws_account_id": "awsAccountId"},
    )
    class AwsAccountProperty:
        def __init__(self, *, aws_account_id: builtins.str) -> None:
            '''The AWS account of the environment.

            :param aws_account_id: The account ID of a project.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-awsaccount.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                aws_account_property = datazone.CfnProjectProfile.AwsAccountProperty(
                    aws_account_id="awsAccountId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7fcf2ee1bc8e5e84878993902463e74d2e0d59a5486d29b3270a330e403a11e1)
                check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "aws_account_id": aws_account_id,
            }

        @builtins.property
        def aws_account_id(self) -> builtins.str:
            '''The account ID of a project.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-awsaccount.html#cfn-datazone-projectprofile-awsaccount-awsaccountid
            '''
            result = self._values.get("aws_account_id")
            assert result is not None, "Required property 'aws_account_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsAccountProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnProjectProfile.EnvironmentConfigurationParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"is_editable": "isEditable", "name": "name", "value": "value"},
    )
    class EnvironmentConfigurationParameterProperty:
        def __init__(
            self,
            *,
            is_editable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The environment configuration parameter.

            :param is_editable: Specifies whether the environment parameter is editable.
            :param name: The name of the environment configuration parameter.
            :param value: The value of the environment configuration parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfigurationparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                environment_configuration_parameter_property = datazone.CfnProjectProfile.EnvironmentConfigurationParameterProperty(
                    is_editable=False,
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bf7bbb8e1650467ecc0369100cdd1f22e8ec805fbddb090e6314b2b5a01ddb4a)
                check_type(argname="argument is_editable", value=is_editable, expected_type=type_hints["is_editable"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if is_editable is not None:
                self._values["is_editable"] = is_editable
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def is_editable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the environment parameter is editable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfigurationparameter.html#cfn-datazone-projectprofile-environmentconfigurationparameter-iseditable
            '''
            result = self._values.get("is_editable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the environment configuration parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfigurationparameter.html#cfn-datazone-projectprofile-environmentconfigurationparameter-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of the environment configuration parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfigurationparameter.html#cfn-datazone-projectprofile-environmentconfigurationparameter-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentConfigurationParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnProjectProfile.EnvironmentConfigurationParametersDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_overrides": "parameterOverrides",
            "resolved_parameters": "resolvedParameters",
            "ssm_path": "ssmPath",
        },
    )
    class EnvironmentConfigurationParametersDetailsProperty:
        def __init__(
            self,
            *,
            parameter_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnProjectProfile.EnvironmentConfigurationParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resolved_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnProjectProfile.EnvironmentConfigurationParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ssm_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The details of the environment configuration parameter.

            :param parameter_overrides: The parameter overrides.
            :param resolved_parameters: The resolved environment configuration parameters.
            :param ssm_path: Ssm path environment configuration parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfigurationparametersdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                environment_configuration_parameters_details_property = datazone.CfnProjectProfile.EnvironmentConfigurationParametersDetailsProperty(
                    parameter_overrides=[datazone.CfnProjectProfile.EnvironmentConfigurationParameterProperty(
                        is_editable=False,
                        name="name",
                        value="value"
                    )],
                    resolved_parameters=[datazone.CfnProjectProfile.EnvironmentConfigurationParameterProperty(
                        is_editable=False,
                        name="name",
                        value="value"
                    )],
                    ssm_path="ssmPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fab90e5736f5e6f3ffb1d2c481eba6fcd8f1f870000719d3c6a3852737b46e0b)
                check_type(argname="argument parameter_overrides", value=parameter_overrides, expected_type=type_hints["parameter_overrides"])
                check_type(argname="argument resolved_parameters", value=resolved_parameters, expected_type=type_hints["resolved_parameters"])
                check_type(argname="argument ssm_path", value=ssm_path, expected_type=type_hints["ssm_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if parameter_overrides is not None:
                self._values["parameter_overrides"] = parameter_overrides
            if resolved_parameters is not None:
                self._values["resolved_parameters"] = resolved_parameters
            if ssm_path is not None:
                self._values["ssm_path"] = ssm_path

        @builtins.property
        def parameter_overrides(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProjectProfile.EnvironmentConfigurationParameterProperty"]]]]:
            '''The parameter overrides.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfigurationparametersdetails.html#cfn-datazone-projectprofile-environmentconfigurationparametersdetails-parameteroverrides
            '''
            result = self._values.get("parameter_overrides")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProjectProfile.EnvironmentConfigurationParameterProperty"]]]], result)

        @builtins.property
        def resolved_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProjectProfile.EnvironmentConfigurationParameterProperty"]]]]:
            '''The resolved environment configuration parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfigurationparametersdetails.html#cfn-datazone-projectprofile-environmentconfigurationparametersdetails-resolvedparameters
            '''
            result = self._values.get("resolved_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProjectProfile.EnvironmentConfigurationParameterProperty"]]]], result)

        @builtins.property
        def ssm_path(self) -> typing.Optional[builtins.str]:
            '''Ssm path environment configuration parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfigurationparametersdetails.html#cfn-datazone-projectprofile-environmentconfigurationparametersdetails-ssmpath
            '''
            result = self._values.get("ssm_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentConfigurationParametersDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnProjectProfile.EnvironmentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_region": "awsRegion",
            "environment_blueprint_id": "environmentBlueprintId",
            "name": "name",
            "aws_account": "awsAccount",
            "configuration_parameters": "configurationParameters",
            "deployment_mode": "deploymentMode",
            "deployment_order": "deploymentOrder",
            "description": "description",
            "id": "id",
        },
    )
    class EnvironmentConfigurationProperty:
        def __init__(
            self,
            *,
            aws_region: typing.Union[_IResolvable_da3f097b, typing.Union["CfnProjectProfile.RegionProperty", typing.Dict[builtins.str, typing.Any]]],
            environment_blueprint_id: builtins.str,
            name: builtins.str,
            aws_account: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnProjectProfile.AwsAccountProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            configuration_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnProjectProfile.EnvironmentConfigurationParametersDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            deployment_mode: typing.Optional[builtins.str] = None,
            deployment_order: typing.Optional[jsii.Number] = None,
            description: typing.Optional[builtins.str] = None,
            id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration of an environment.

            :param aws_region: The AWS Region of the environment.
            :param environment_blueprint_id: The environment blueprint ID.
            :param name: The environment name.
            :param aws_account: The AWS account of the environment.
            :param configuration_parameters: The configuration parameters of the environment.
            :param deployment_mode: The deployment mode of the environment.
            :param deployment_order: The deployment order of the environment.
            :param description: The environment description.
            :param id: The environment ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                environment_configuration_property = datazone.CfnProjectProfile.EnvironmentConfigurationProperty(
                    aws_region=datazone.CfnProjectProfile.RegionProperty(
                        region_name="regionName"
                    ),
                    environment_blueprint_id="environmentBlueprintId",
                    name="name",
                
                    # the properties below are optional
                    aws_account=datazone.CfnProjectProfile.AwsAccountProperty(
                        aws_account_id="awsAccountId"
                    ),
                    configuration_parameters=datazone.CfnProjectProfile.EnvironmentConfigurationParametersDetailsProperty(
                        parameter_overrides=[datazone.CfnProjectProfile.EnvironmentConfigurationParameterProperty(
                            is_editable=False,
                            name="name",
                            value="value"
                        )],
                        resolved_parameters=[datazone.CfnProjectProfile.EnvironmentConfigurationParameterProperty(
                            is_editable=False,
                            name="name",
                            value="value"
                        )],
                        ssm_path="ssmPath"
                    ),
                    deployment_mode="deploymentMode",
                    deployment_order=123,
                    description="description",
                    id="id"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8addc3ada6a67b6cbb6b275c952d4659afeea35b806096cdb6322e14ea2ea99f)
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
                check_type(argname="argument environment_blueprint_id", value=environment_blueprint_id, expected_type=type_hints["environment_blueprint_id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument aws_account", value=aws_account, expected_type=type_hints["aws_account"])
                check_type(argname="argument configuration_parameters", value=configuration_parameters, expected_type=type_hints["configuration_parameters"])
                check_type(argname="argument deployment_mode", value=deployment_mode, expected_type=type_hints["deployment_mode"])
                check_type(argname="argument deployment_order", value=deployment_order, expected_type=type_hints["deployment_order"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "aws_region": aws_region,
                "environment_blueprint_id": environment_blueprint_id,
                "name": name,
            }
            if aws_account is not None:
                self._values["aws_account"] = aws_account
            if configuration_parameters is not None:
                self._values["configuration_parameters"] = configuration_parameters
            if deployment_mode is not None:
                self._values["deployment_mode"] = deployment_mode
            if deployment_order is not None:
                self._values["deployment_order"] = deployment_order
            if description is not None:
                self._values["description"] = description
            if id is not None:
                self._values["id"] = id

        @builtins.property
        def aws_region(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnProjectProfile.RegionProperty"]:
            '''The AWS Region of the environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfiguration.html#cfn-datazone-projectprofile-environmentconfiguration-awsregion
            '''
            result = self._values.get("aws_region")
            assert result is not None, "Required property 'aws_region' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnProjectProfile.RegionProperty"], result)

        @builtins.property
        def environment_blueprint_id(self) -> builtins.str:
            '''The environment blueprint ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfiguration.html#cfn-datazone-projectprofile-environmentconfiguration-environmentblueprintid
            '''
            result = self._values.get("environment_blueprint_id")
            assert result is not None, "Required property 'environment_blueprint_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The environment name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfiguration.html#cfn-datazone-projectprofile-environmentconfiguration-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def aws_account(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProjectProfile.AwsAccountProperty"]]:
            '''The AWS account of the environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfiguration.html#cfn-datazone-projectprofile-environmentconfiguration-awsaccount
            '''
            result = self._values.get("aws_account")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProjectProfile.AwsAccountProperty"]], result)

        @builtins.property
        def configuration_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProjectProfile.EnvironmentConfigurationParametersDetailsProperty"]]:
            '''The configuration parameters of the environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfiguration.html#cfn-datazone-projectprofile-environmentconfiguration-configurationparameters
            '''
            result = self._values.get("configuration_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProjectProfile.EnvironmentConfigurationParametersDetailsProperty"]], result)

        @builtins.property
        def deployment_mode(self) -> typing.Optional[builtins.str]:
            '''The deployment mode of the environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfiguration.html#cfn-datazone-projectprofile-environmentconfiguration-deploymentmode
            '''
            result = self._values.get("deployment_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def deployment_order(self) -> typing.Optional[jsii.Number]:
            '''The deployment order of the environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfiguration.html#cfn-datazone-projectprofile-environmentconfiguration-deploymentorder
            '''
            result = self._values.get("deployment_order")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The environment description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfiguration.html#cfn-datazone-projectprofile-environmentconfiguration-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The environment ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-environmentconfiguration.html#cfn-datazone-projectprofile-environmentconfiguration-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnProjectProfile.RegionProperty",
        jsii_struct_bases=[],
        name_mapping={"region_name": "regionName"},
    )
    class RegionProperty:
        def __init__(self, *, region_name: builtins.str) -> None:
            '''The AWS Region.

            :param region_name: The AWS Region name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-region.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                region_property = datazone.CfnProjectProfile.RegionProperty(
                    region_name="regionName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cc189c16fcab170d1d8d250893b0e4741d23998acae1597f3faa4ca36264479b)
                check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "region_name": region_name,
            }

        @builtins.property
        def region_name(self) -> builtins.str:
            '''The AWS Region name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectprofile-region.html#cfn-datazone-projectprofile-region-regionname
            '''
            result = self._values.get("region_name")
            assert result is not None, "Required property 'region_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnProjectProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "domain_identifier": "domainIdentifier",
        "domain_unit_identifier": "domainUnitIdentifier",
        "environment_configurations": "environmentConfigurations",
        "status": "status",
    },
)
class CfnProjectProfileProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        domain_identifier: typing.Optional[builtins.str] = None,
        domain_unit_identifier: typing.Optional[builtins.str] = None,
        environment_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProjectProfile.EnvironmentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnProjectProfile``.

        :param name: The name of a project profile.
        :param description: The description of the project profile.
        :param domain_identifier: A domain ID of the project profile.
        :param domain_unit_identifier: A domain unit ID of the project profile.
        :param environment_configurations: Environment configurations of a project profile.
        :param status: The status of a project profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_project_profile_props = datazone.CfnProjectProfileProps(
                name="name",
            
                # the properties below are optional
                description="description",
                domain_identifier="domainIdentifier",
                domain_unit_identifier="domainUnitIdentifier",
                environment_configurations=[datazone.CfnProjectProfile.EnvironmentConfigurationProperty(
                    aws_region=datazone.CfnProjectProfile.RegionProperty(
                        region_name="regionName"
                    ),
                    environment_blueprint_id="environmentBlueprintId",
                    name="name",
            
                    # the properties below are optional
                    aws_account=datazone.CfnProjectProfile.AwsAccountProperty(
                        aws_account_id="awsAccountId"
                    ),
                    configuration_parameters=datazone.CfnProjectProfile.EnvironmentConfigurationParametersDetailsProperty(
                        parameter_overrides=[datazone.CfnProjectProfile.EnvironmentConfigurationParameterProperty(
                            is_editable=False,
                            name="name",
                            value="value"
                        )],
                        resolved_parameters=[datazone.CfnProjectProfile.EnvironmentConfigurationParameterProperty(
                            is_editable=False,
                            name="name",
                            value="value"
                        )],
                        ssm_path="ssmPath"
                    ),
                    deployment_mode="deploymentMode",
                    deployment_order=123,
                    description="description",
                    id="id"
                )],
                status="status"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16088b85440c601f18ad4a194ccb23740aedaa1b4f93a76e720d939c57cb4d2e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument domain_unit_identifier", value=domain_unit_identifier, expected_type=type_hints["domain_unit_identifier"])
            check_type(argname="argument environment_configurations", value=environment_configurations, expected_type=type_hints["environment_configurations"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if domain_identifier is not None:
            self._values["domain_identifier"] = domain_identifier
        if domain_unit_identifier is not None:
            self._values["domain_unit_identifier"] = domain_unit_identifier
        if environment_configurations is not None:
            self._values["environment_configurations"] = environment_configurations
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of a project profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectprofile.html#cfn-datazone-projectprofile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the project profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectprofile.html#cfn-datazone-projectprofile-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_identifier(self) -> typing.Optional[builtins.str]:
        '''A domain ID of the project profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectprofile.html#cfn-datazone-projectprofile-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_unit_identifier(self) -> typing.Optional[builtins.str]:
        '''A domain unit ID of the project profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectprofile.html#cfn-datazone-projectprofile-domainunitidentifier
        '''
        result = self._values.get("domain_unit_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnProjectProfile.EnvironmentConfigurationProperty]]]]:
        '''Environment configurations of a project profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectprofile.html#cfn-datazone-projectprofile-environmentconfigurations
        '''
        result = self._values.get("environment_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnProjectProfile.EnvironmentConfigurationProperty]]]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of a project profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectprofile.html#cfn-datazone-projectprofile-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "name": "name",
        "description": "description",
        "domain_unit_id": "domainUnitId",
        "glossary_terms": "glossaryTerms",
        "project_profile_id": "projectProfileId",
        "project_profile_version": "projectProfileVersion",
        "user_parameters": "userParameters",
    },
)
class CfnProjectProps:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        domain_unit_id: typing.Optional[builtins.str] = None,
        glossary_terms: typing.Optional[typing.Sequence[builtins.str]] = None,
        project_profile_id: typing.Optional[builtins.str] = None,
        project_profile_version: typing.Optional[builtins.str] = None,
        user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.EnvironmentConfigurationUserParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProject``.

        :param domain_identifier: The identifier of a Amazon DataZone domain where the project exists.
        :param name: The name of a project.
        :param description: The description of a project.
        :param domain_unit_id: The ID of the domain unit. This parameter is not required and if it is not specified, then the project is created at the root domain unit level.
        :param glossary_terms: The glossary terms that can be used in this Amazon DataZone project.
        :param project_profile_id: The ID of the project profile.
        :param project_profile_version: The project profile version to which the project should be updated. You can only specify the following string for this parameter: ``latest`` .
        :param user_parameters: The user parameters of the project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_project_props = datazone.CfnProjectProps(
                domain_identifier="domainIdentifier",
                name="name",
            
                # the properties below are optional
                description="description",
                domain_unit_id="domainUnitId",
                glossary_terms=["glossaryTerms"],
                project_profile_id="projectProfileId",
                project_profile_version="projectProfileVersion",
                user_parameters=[datazone.CfnProject.EnvironmentConfigurationUserParameterProperty(
                    environment_configuration_name="environmentConfigurationName",
                    environment_id="environmentId",
                    environment_parameters=[datazone.CfnProject.EnvironmentParameterProperty(
                        name="name",
                        value="value"
                    )]
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d519699f8d5d172880216006cab9e8c1595fc99339cf485d2be1f6c37bbc5a4c)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument domain_unit_id", value=domain_unit_id, expected_type=type_hints["domain_unit_id"])
            check_type(argname="argument glossary_terms", value=glossary_terms, expected_type=type_hints["glossary_terms"])
            check_type(argname="argument project_profile_id", value=project_profile_id, expected_type=type_hints["project_profile_id"])
            check_type(argname="argument project_profile_version", value=project_profile_version, expected_type=type_hints["project_profile_version"])
            check_type(argname="argument user_parameters", value=user_parameters, expected_type=type_hints["user_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if domain_unit_id is not None:
            self._values["domain_unit_id"] = domain_unit_id
        if glossary_terms is not None:
            self._values["glossary_terms"] = glossary_terms
        if project_profile_id is not None:
            self._values["project_profile_id"] = project_profile_id
        if project_profile_version is not None:
            self._values["project_profile_version"] = project_profile_version
        if user_parameters is not None:
            self._values["user_parameters"] = user_parameters

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The identifier of a Amazon DataZone domain where the project exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html#cfn-datazone-project-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of a project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html#cfn-datazone-project-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of a project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html#cfn-datazone-project-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_unit_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the domain unit.

        This parameter is not required and if it is not specified, then the project is created at the root domain unit level.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html#cfn-datazone-project-domainunitid
        '''
        result = self._values.get("domain_unit_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def glossary_terms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The glossary terms that can be used in this Amazon DataZone project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html#cfn-datazone-project-glossaryterms
        '''
        result = self._values.get("glossary_terms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def project_profile_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the project profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html#cfn-datazone-project-projectprofileid
        '''
        result = self._values.get("project_profile_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_profile_version(self) -> typing.Optional[builtins.str]:
        '''The project profile version to which the project should be updated.

        You can only specify the following string for this parameter: ``latest`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html#cfn-datazone-project-projectprofileversion
        '''
        result = self._values.get("project_profile_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnProject.EnvironmentConfigurationUserParameterProperty]]]]:
        '''The user parameters of the project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html#cfn-datazone-project-userparameters
        '''
        result = self._values.get("user_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnProject.EnvironmentConfigurationUserParameterProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSubscriptionTarget(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnSubscriptionTarget",
):
    '''The ``AWS::DataZone::SubscriptionTarget`` resource specifies an Amazon DataZone subscription target.

    Subscription targets enable you to access the data to which you have subscribed in your projects. A subscription target specifies the location (for example, a database or a schema) and the required permissions (for example, an IAM role) that Amazon DataZone can use to establish a connection with the source data and to create the necessary grants so that members of the Amazon DataZone project can start querying the data to which they have subscribed.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html
    :cloudformationResource: AWS::DataZone::SubscriptionTarget
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_subscription_target = datazone.CfnSubscriptionTarget(self, "MyCfnSubscriptionTarget",
            applicable_asset_types=["applicableAssetTypes"],
            authorized_principals=["authorizedPrincipals"],
            domain_identifier="domainIdentifier",
            environment_identifier="environmentIdentifier",
            name="name",
            subscription_target_config=[datazone.CfnSubscriptionTarget.SubscriptionTargetFormProperty(
                content="content",
                form_name="formName"
            )],
            type="type",
        
            # the properties below are optional
            manage_access_role="manageAccessRole",
            provider="provider"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        applicable_asset_types: typing.Sequence[builtins.str],
        authorized_principals: typing.Sequence[builtins.str],
        domain_identifier: builtins.str,
        environment_identifier: builtins.str,
        name: builtins.str,
        subscription_target_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSubscriptionTarget.SubscriptionTargetFormProperty", typing.Dict[builtins.str, typing.Any]]]]],
        type: builtins.str,
        manage_access_role: typing.Optional[builtins.str] = None,
        provider: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param applicable_asset_types: The asset types included in the subscription target.
        :param authorized_principals: The authorized principals included in the subscription target.
        :param domain_identifier: The ID of the Amazon DataZone domain in which subscription target is created.
        :param environment_identifier: The ID of the environment in which subscription target is created.
        :param name: The name of the subscription target.
        :param subscription_target_config: The configuration of the subscription target.
        :param type: The type of the subscription target.
        :param manage_access_role: The manage access role that is used to create the subscription target.
        :param provider: The provider of the subscription target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c61b5cfe149791a4c62bad0056737a365bdf72f7f99e6e72c71be1058e91604d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSubscriptionTargetProps(
            applicable_asset_types=applicable_asset_types,
            authorized_principals=authorized_principals,
            domain_identifier=domain_identifier,
            environment_identifier=environment_identifier,
            name=name,
            subscription_target_config=subscription_target_config,
            type=type,
            manage_access_role=manage_access_role,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1ffb846a6baf7f8d43c947f31440c264738eb11477a914e6234e72e512226a7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__867dc79750bd91424b54ba2d5f7eca4a8d13f7f3c9f4ffc4effe5dae834ed869)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when the subscription target was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedBy")
    def attr_created_by(self) -> builtins.str:
        '''The Amazon DataZone user who created the subscription target.

        :cloudformationAttribute: CreatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the subscription target exists.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentId")
    def attr_environment_id(self) -> builtins.str:
        '''The identifier of the environment of the subscription target.

        :cloudformationAttribute: EnvironmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The identifier of the subscription target.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrProjectId")
    def attr_project_id(self) -> builtins.str:
        '''The identifier of the project specified in the subscription target.

        :cloudformationAttribute: ProjectId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp of when the subscription target was updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedBy")
    def attr_updated_by(self) -> builtins.str:
        '''The Amazon DataZone user who updated the subscription target.

        :cloudformationAttribute: UpdatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedBy"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="applicableAssetTypes")
    def applicable_asset_types(self) -> typing.List[builtins.str]:
        '''The asset types included in the subscription target.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "applicableAssetTypes"))

    @applicable_asset_types.setter
    def applicable_asset_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6db9fad0cfe2726fd2714cfa52499e265af46d2cacf4be9daa6378bd8c673b5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicableAssetTypes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="authorizedPrincipals")
    def authorized_principals(self) -> typing.List[builtins.str]:
        '''The authorized principals included in the subscription target.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "authorizedPrincipals"))

    @authorized_principals.setter
    def authorized_principals(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ec38d6c0d885e0ae64427a2407f691f11cd764f198652ece23783772c2611fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizedPrincipals", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The ID of the Amazon DataZone domain in which subscription target is created.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77bccb41f1eb7b5a32710e03ae6cfec74eb17bf3129bd372a11c92f7f67f5dc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentIdentifier")
    def environment_identifier(self) -> builtins.str:
        '''The ID of the environment in which subscription target is created.'''
        return typing.cast(builtins.str, jsii.get(self, "environmentIdentifier"))

    @environment_identifier.setter
    def environment_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20ed34c3b416019570831200db233eb4c407b91b53464c36e9fbdbdcd4a6da82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the subscription target.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc691c403b67912db7216c5f5fddda4101316ca719bd90e37c92640197c61004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subscriptionTargetConfig")
    def subscription_target_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSubscriptionTarget.SubscriptionTargetFormProperty"]]]:
        '''The configuration of the subscription target.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSubscriptionTarget.SubscriptionTargetFormProperty"]]], jsii.get(self, "subscriptionTargetConfig"))

    @subscription_target_config.setter
    def subscription_target_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSubscriptionTarget.SubscriptionTargetFormProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a19c0f2213973750a6cc503429c6ef8619a3d0885a2df0f54aad48a00a3c6f46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionTargetConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the subscription target.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8961cb77429dad851472db6b14a76c77606d0bffdc98a0cbb3cffd227c3ec500)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="manageAccessRole")
    def manage_access_role(self) -> typing.Optional[builtins.str]:
        '''The manage access role that is used to create the subscription target.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "manageAccessRole"))

    @manage_access_role.setter
    def manage_access_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83f19af57790aab3ddc6c4e1f64e1f68cf69073e46da8ac997fc9f0c83e93198)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manageAccessRole", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="provider")
    def provider(self) -> typing.Optional[builtins.str]:
        '''The provider of the subscription target.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "provider"))

    @provider.setter
    def provider(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4526f8f71696c8c7bf040cd042cda55182de538f2ebf276253751b5a497c037)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provider", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnSubscriptionTarget.SubscriptionTargetFormProperty",
        jsii_struct_bases=[],
        name_mapping={"content": "content", "form_name": "formName"},
    )
    class SubscriptionTargetFormProperty:
        def __init__(self, *, content: builtins.str, form_name: builtins.str) -> None:
            '''The details of the subscription target configuration.

            :param content: The content of the subscription target configuration.
            :param form_name: The form name included in the subscription target configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-subscriptiontarget-subscriptiontargetform.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                subscription_target_form_property = datazone.CfnSubscriptionTarget.SubscriptionTargetFormProperty(
                    content="content",
                    form_name="formName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__720cbd7aa436c84d94877993fe56ec1a54389edd9936074e71ebf65a3caffa9b)
                check_type(argname="argument content", value=content, expected_type=type_hints["content"])
                check_type(argname="argument form_name", value=form_name, expected_type=type_hints["form_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "content": content,
                "form_name": form_name,
            }

        @builtins.property
        def content(self) -> builtins.str:
            '''The content of the subscription target configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-subscriptiontarget-subscriptiontargetform.html#cfn-datazone-subscriptiontarget-subscriptiontargetform-content
            '''
            result = self._values.get("content")
            assert result is not None, "Required property 'content' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def form_name(self) -> builtins.str:
            '''The form name included in the subscription target configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-subscriptiontarget-subscriptiontargetform.html#cfn-datazone-subscriptiontarget-subscriptiontargetform-formname
            '''
            result = self._values.get("form_name")
            assert result is not None, "Required property 'form_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubscriptionTargetFormProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnSubscriptionTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "applicable_asset_types": "applicableAssetTypes",
        "authorized_principals": "authorizedPrincipals",
        "domain_identifier": "domainIdentifier",
        "environment_identifier": "environmentIdentifier",
        "name": "name",
        "subscription_target_config": "subscriptionTargetConfig",
        "type": "type",
        "manage_access_role": "manageAccessRole",
        "provider": "provider",
    },
)
class CfnSubscriptionTargetProps:
    def __init__(
        self,
        *,
        applicable_asset_types: typing.Sequence[builtins.str],
        authorized_principals: typing.Sequence[builtins.str],
        domain_identifier: builtins.str,
        environment_identifier: builtins.str,
        name: builtins.str,
        subscription_target_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriptionTarget.SubscriptionTargetFormProperty, typing.Dict[builtins.str, typing.Any]]]]],
        type: builtins.str,
        manage_access_role: typing.Optional[builtins.str] = None,
        provider: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSubscriptionTarget``.

        :param applicable_asset_types: The asset types included in the subscription target.
        :param authorized_principals: The authorized principals included in the subscription target.
        :param domain_identifier: The ID of the Amazon DataZone domain in which subscription target is created.
        :param environment_identifier: The ID of the environment in which subscription target is created.
        :param name: The name of the subscription target.
        :param subscription_target_config: The configuration of the subscription target.
        :param type: The type of the subscription target.
        :param manage_access_role: The manage access role that is used to create the subscription target.
        :param provider: The provider of the subscription target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_subscription_target_props = datazone.CfnSubscriptionTargetProps(
                applicable_asset_types=["applicableAssetTypes"],
                authorized_principals=["authorizedPrincipals"],
                domain_identifier="domainIdentifier",
                environment_identifier="environmentIdentifier",
                name="name",
                subscription_target_config=[datazone.CfnSubscriptionTarget.SubscriptionTargetFormProperty(
                    content="content",
                    form_name="formName"
                )],
                type="type",
            
                # the properties below are optional
                manage_access_role="manageAccessRole",
                provider="provider"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b970b38bc2b99a7ed3ef3830dfa5721ecc9ee442e5d627e01abfdcb22600151)
            check_type(argname="argument applicable_asset_types", value=applicable_asset_types, expected_type=type_hints["applicable_asset_types"])
            check_type(argname="argument authorized_principals", value=authorized_principals, expected_type=type_hints["authorized_principals"])
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument environment_identifier", value=environment_identifier, expected_type=type_hints["environment_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument subscription_target_config", value=subscription_target_config, expected_type=type_hints["subscription_target_config"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument manage_access_role", value=manage_access_role, expected_type=type_hints["manage_access_role"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "applicable_asset_types": applicable_asset_types,
            "authorized_principals": authorized_principals,
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
            "name": name,
            "subscription_target_config": subscription_target_config,
            "type": type,
        }
        if manage_access_role is not None:
            self._values["manage_access_role"] = manage_access_role
        if provider is not None:
            self._values["provider"] = provider

    @builtins.property
    def applicable_asset_types(self) -> typing.List[builtins.str]:
        '''The asset types included in the subscription target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-applicableassettypes
        '''
        result = self._values.get("applicable_asset_types")
        assert result is not None, "Required property 'applicable_asset_types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def authorized_principals(self) -> typing.List[builtins.str]:
        '''The authorized principals included in the subscription target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-authorizedprincipals
        '''
        result = self._values.get("authorized_principals")
        assert result is not None, "Required property 'authorized_principals' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The ID of the Amazon DataZone domain in which subscription target is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_identifier(self) -> builtins.str:
        '''The ID of the environment in which subscription target is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-environmentidentifier
        '''
        result = self._values.get("environment_identifier")
        assert result is not None, "Required property 'environment_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the subscription target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscription_target_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSubscriptionTarget.SubscriptionTargetFormProperty]]]:
        '''The configuration of the subscription target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-subscriptiontargetconfig
        '''
        result = self._values.get("subscription_target_config")
        assert result is not None, "Required property 'subscription_target_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSubscriptionTarget.SubscriptionTargetFormProperty]]], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the subscription target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def manage_access_role(self) -> typing.Optional[builtins.str]:
        '''The manage access role that is used to create the subscription target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-manageaccessrole
        '''
        result = self._values.get("manage_access_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider(self) -> typing.Optional[builtins.str]:
        '''The provider of the subscription target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-provider
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSubscriptionTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnUserProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnUserProfile",
):
    '''The user type of the user for which the user profile is created.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-userprofile.html
    :cloudformationResource: AWS::DataZone::UserProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_user_profile = datazone.CfnUserProfile(self, "MyCfnUserProfile",
            domain_identifier="domainIdentifier",
            user_identifier="userIdentifier",
        
            # the properties below are optional
            status="status",
            user_type="userType"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_identifier: builtins.str,
        user_identifier: builtins.str,
        status: typing.Optional[builtins.str] = None,
        user_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_identifier: The identifier of a Amazon DataZone domain in which a user profile exists.
        :param user_identifier: The identifier of the user for which the user profile is created.
        :param status: The status of the user profile.
        :param user_type: The user type of the user for which the user profile is created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43948fd61004932aa31394de53e9c49e34aa425f3682404de5d5f6a249734d82)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserProfileProps(
            domain_identifier=domain_identifier,
            user_identifier=user_identifier,
            status=status,
            user_type=user_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62409db933bd1f83a26e4a296f90a5aa33de9e2cd9f82db4084d8f1cb0f382e4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bac3d345ed2cf85373ed12e71655921f20ce2575e0f95a05a3dd29cfa7e804e0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDetails")
    def attr_details(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Details
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrDetails"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The identifier of a Amazon DataZone domain in which a user profile exists.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the user profile.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''The type of the user profile.

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The identifier of a Amazon DataZone domain in which a user profile exists.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57dc87f9b5d4209a76a54e631bab548eddbecf73d3a0cb39b30030a99c20dbb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="userIdentifier")
    def user_identifier(self) -> builtins.str:
        '''The identifier of the user for which the user profile is created.'''
        return typing.cast(builtins.str, jsii.get(self, "userIdentifier"))

    @user_identifier.setter
    def user_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bc695cbd1d290ebde7514044903060b533b99cd4f724f387512ffb614625693)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the user profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f391a63fdbc6b7a8aefbb3664fddfe91481bce941965f274ecad0166152935ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="userType")
    def user_type(self) -> typing.Optional[builtins.str]:
        '''The user type of the user for which the user profile is created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userType"))

    @user_type.setter
    def user_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b560448b79c8df59777bf516743c73a776fe419d2c08183dd62546f1fc65ae4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userType", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnUserProfile.IamUserProfileDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class IamUserProfileDetailsProperty:
        def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
            '''The details of an IAM user profile in Amazon DataZone.

            :param arn: The ARN of an IAM user profile in Amazon DataZone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-iamuserprofiledetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                iam_user_profile_details_property = datazone.CfnUserProfile.IamUserProfileDetailsProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3fd3b9b642370fd3593445a459418ba3df5f97586bee6446bed499fa533a4022)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of an IAM user profile in Amazon DataZone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-iamuserprofiledetails.html#cfn-datazone-userprofile-iamuserprofiledetails-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamUserProfileDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnUserProfile.SsoUserProfileDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "first_name": "firstName",
            "last_name": "lastName",
            "username": "username",
        },
    )
    class SsoUserProfileDetailsProperty:
        def __init__(
            self,
            *,
            first_name: typing.Optional[builtins.str] = None,
            last_name: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The single sign-on details of the user profile.

            :param first_name: The first name included in the single sign-on details of the user profile.
            :param last_name: The last name included in the single sign-on details of the user profile.
            :param username: The username included in the single sign-on details of the user profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-ssouserprofiledetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                sso_user_profile_details_property = datazone.CfnUserProfile.SsoUserProfileDetailsProperty(
                    first_name="firstName",
                    last_name="lastName",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__07963e9a65d43152452195ee221d80669fe4707d48ffd231ffc947c240448dbd)
                check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
                check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if first_name is not None:
                self._values["first_name"] = first_name
            if last_name is not None:
                self._values["last_name"] = last_name
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def first_name(self) -> typing.Optional[builtins.str]:
            '''The first name included in the single sign-on details of the user profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-ssouserprofiledetails.html#cfn-datazone-userprofile-ssouserprofiledetails-firstname
            '''
            result = self._values.get("first_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def last_name(self) -> typing.Optional[builtins.str]:
            '''The last name included in the single sign-on details of the user profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-ssouserprofiledetails.html#cfn-datazone-userprofile-ssouserprofiledetails-lastname
            '''
            result = self._values.get("last_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''The username included in the single sign-on details of the user profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-ssouserprofiledetails.html#cfn-datazone-userprofile-ssouserprofiledetails-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SsoUserProfileDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnUserProfile.UserProfileDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"iam": "iam", "sso": "sso"},
    )
    class UserProfileDetailsProperty:
        def __init__(
            self,
            *,
            iam: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnUserProfile.IamUserProfileDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sso: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnUserProfile.SsoUserProfileDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The details of the user profile in Amazon DataZone.

            :param iam: The IAM details included in the user profile details.
            :param sso: The single sign-on details included in the user profile details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-userprofiledetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                user_profile_details_property = datazone.CfnUserProfile.UserProfileDetailsProperty(
                    iam=datazone.CfnUserProfile.IamUserProfileDetailsProperty(
                        arn="arn"
                    ),
                    sso=datazone.CfnUserProfile.SsoUserProfileDetailsProperty(
                        first_name="firstName",
                        last_name="lastName",
                        username="username"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1a1351a79d8a8cf0246c7e7591c1c0736de90dfd896392c833f9cb3530c63997)
                check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
                check_type(argname="argument sso", value=sso, expected_type=type_hints["sso"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if iam is not None:
                self._values["iam"] = iam
            if sso is not None:
                self._values["sso"] = sso

        @builtins.property
        def iam(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUserProfile.IamUserProfileDetailsProperty"]]:
            '''The IAM details included in the user profile details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-userprofiledetails.html#cfn-datazone-userprofile-userprofiledetails-iam
            '''
            result = self._values.get("iam")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUserProfile.IamUserProfileDetailsProperty"]], result)

        @builtins.property
        def sso(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUserProfile.SsoUserProfileDetailsProperty"]]:
            '''The single sign-on details included in the user profile details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-userprofiledetails.html#cfn-datazone-userprofile-userprofiledetails-sso
            '''
            result = self._values.get("sso")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUserProfile.SsoUserProfileDetailsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserProfileDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnUserProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "user_identifier": "userIdentifier",
        "status": "status",
        "user_type": "userType",
    },
)
class CfnUserProfileProps:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        user_identifier: builtins.str,
        status: typing.Optional[builtins.str] = None,
        user_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnUserProfile``.

        :param domain_identifier: The identifier of a Amazon DataZone domain in which a user profile exists.
        :param user_identifier: The identifier of the user for which the user profile is created.
        :param status: The status of the user profile.
        :param user_type: The user type of the user for which the user profile is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-userprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_user_profile_props = datazone.CfnUserProfileProps(
                domain_identifier="domainIdentifier",
                user_identifier="userIdentifier",
            
                # the properties below are optional
                status="status",
                user_type="userType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__431134ef647ba94f8eb72ef3985b514bb86c42b53ca933a9fd51ea529bd0fec8)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument user_identifier", value=user_identifier, expected_type=type_hints["user_identifier"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument user_type", value=user_type, expected_type=type_hints["user_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "user_identifier": user_identifier,
        }
        if status is not None:
            self._values["status"] = status
        if user_type is not None:
            self._values["user_type"] = user_type

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The identifier of a Amazon DataZone domain in which a user profile exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-userprofile.html#cfn-datazone-userprofile-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_identifier(self) -> builtins.str:
        '''The identifier of the user for which the user profile is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-userprofile.html#cfn-datazone-userprofile-useridentifier
        '''
        result = self._values.get("user_identifier")
        assert result is not None, "Required property 'user_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the user profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-userprofile.html#cfn-datazone-userprofile-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_type(self) -> typing.Optional[builtins.str]:
        '''The user type of the user for which the user profile is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-userprofile.html#cfn-datazone-userprofile-usertype
        '''
        result = self._values.get("user_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConnection",
    "CfnConnectionProps",
    "CfnDataSource",
    "CfnDataSourceProps",
    "CfnDomain",
    "CfnDomainProps",
    "CfnDomainUnit",
    "CfnDomainUnitProps",
    "CfnEnvironment",
    "CfnEnvironmentActions",
    "CfnEnvironmentActionsProps",
    "CfnEnvironmentBlueprintConfiguration",
    "CfnEnvironmentBlueprintConfigurationProps",
    "CfnEnvironmentProfile",
    "CfnEnvironmentProfileProps",
    "CfnEnvironmentProps",
    "CfnGroupProfile",
    "CfnGroupProfileProps",
    "CfnOwner",
    "CfnOwnerProps",
    "CfnProject",
    "CfnProjectMembership",
    "CfnProjectMembershipProps",
    "CfnProjectProfile",
    "CfnProjectProfileProps",
    "CfnProjectProps",
    "CfnSubscriptionTarget",
    "CfnSubscriptionTargetProps",
    "CfnUserProfile",
    "CfnUserProfileProps",
]

publication.publish()

def _typecheckingstub__68db6ef5de752113ca6cf32190e1173ded9b82274379374d5e16834f4fed2680(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_identifier: builtins.str,
    environment_identifier: builtins.str,
    name: builtins.str,
    aws_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.AwsLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    props: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.ConnectionPropertiesInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__398c2006651598ffb80d8dc727165745adb2a6958c75f5926b613ba3177e9d64(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__136bd666b9e38ddb69494b10631ff5d0eaef6cf06229255303630179d477d90f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f8e028075d374db4fd60d67eeb1b9ec1a7ba6de37d2ff5159166ef7a5c1b36b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b4cbfbd3c4ab850b86dca1cc1c0182806c09d658dbbad4aeefac22ff57e747f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d602657575f2a77c389ea4e89f4d92dbe2bb3c30e0ccfc811aff15e122a98d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e0849d8ebdd0fce1643c3904bce5fd806bb233f7ff27eddb627fac859586e5c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnection.AwsLocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab8e0823bbef4ec627d5b737de745882d73474d54729e96b788a912f2dfe521c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17a641eb769944a69ded6b3f471012669d56d0ff95b65a8c7c137bc906851136(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnection.ConnectionPropertiesInputProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dc6a593151a7d129b46176dfadfaef1e3447a0d3883bc7e17f19c97bc36e3b3(
    *,
    workgroup_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bede0f21a390e4991cddbe5e8b7fc491f05c5af9d778e5f1ecb4a57c9c7144e9(
    *,
    authentication_type: typing.Optional[builtins.str] = None,
    basic_authentication_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.BasicAuthenticationCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_authentication_credentials: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    o_auth2_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.OAuth2PropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    secret_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__709c9a9c016d2e06938c1c1ea54063ae38a4addfc19c769dff4d0e585d8c7527(
    *,
    authorization_code: typing.Optional[builtins.str] = None,
    redirect_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__298e27e7bc1a0b15a9b79d0ebf0e4abe337d89521ddfa348fac1a78cdda506e7(
    *,
    access_role: typing.Optional[builtins.str] = None,
    aws_account_id: typing.Optional[builtins.str] = None,
    aws_region: typing.Optional[builtins.str] = None,
    iam_connection_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ee4cc1ea0ba5d5144e8b2c837d252087208460444755cfb7f5128e742a104c3(
    *,
    password: typing.Optional[builtins.str] = None,
    user_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afac89e500a9d5f348ce1c21e174ddef9825d543c744b00c3ff73a0c8dba8f38(
    *,
    athena_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.AthenaPropertiesInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    glue_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.GluePropertiesInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hyper_pod_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.HyperPodPropertiesInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iam_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.IamPropertiesInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.RedshiftPropertiesInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    spark_emr_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.SparkEmrPropertiesInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    spark_glue_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.SparkGluePropertiesInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__647e7cf0ba0ee1ab7c75fea7d6b34c8a50c95526cd1ec69c86c54c920adef3a9(
    *,
    athena_properties: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    authentication_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.AuthenticationConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    connection_properties: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    connection_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    match_criteria: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    physical_connection_requirements: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.PhysicalConnectionRequirementsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    python_properties: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    spark_properties: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    validate_credentials: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    validate_for_compute_environments: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d948c343e2b90a8893463e22eaab4033317f5a056da9d7e7559e3285f2c7ff17(
    *,
    access_token: typing.Optional[builtins.str] = None,
    jwt_token: typing.Optional[builtins.str] = None,
    refresh_token: typing.Optional[builtins.str] = None,
    user_managed_client_application_client_secret: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07f6c7fa8f6b6af10d26eadc862dfc837c455b56372fa29947bd67161af5e5c7(
    *,
    glue_connection_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.GlueConnectionInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2574ba013a10f07b6e0a61c5559f70c13b2de025bb4b8d00be0efcd15f721fd(
    *,
    cluster_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fcef45bd8fc26fdf37a0281f7789bd6e0fc1105a24dd2b5148ec9b0e0c27b75(
    *,
    glue_lineage_sync_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__807712ef4f77e804709861b4d4515e24f1b5cb14208414a29172fa52c5a8622e(
    *,
    schedule: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06033edd4e1d109e79d816fec5df671c9c991a52cf6e92d45aa0f6ca6cb72d98(
    *,
    aws_managed_client_application_reference: typing.Optional[builtins.str] = None,
    user_managed_client_application_client_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cba63b68fdb8bbf2e7a537a629e7f6c6d51267f6c2af7395b1464f0ecb29b7d(
    *,
    authorization_code_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.AuthorizationCodePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    o_auth2_client_application: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.OAuth2ClientApplicationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    o_auth2_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.GlueOAuth2CredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    o_auth2_grant_type: typing.Optional[builtins.str] = None,
    token_url: typing.Optional[builtins.str] = None,
    token_url_parameters_map: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33253a54618916e3372650927015127ea603d71a4c9363ab9570cdaaa038b28b(
    *,
    availability_zone: typing.Optional[builtins.str] = None,
    security_group_id_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    subnet_id_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__573044a4537dd6f740734285ebbb2dcd69d20a0dc8c1a613d8498d6a3bcb9504(
    *,
    secret_arn: typing.Optional[builtins.str] = None,
    username_password: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.UsernamePasswordProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86e732877333e36da3944ac0771866cd4ef9ef230040330b2a710ca0eba2f6f7(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.LineageSyncScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bad9bb99ea9342d656480e79701348e43bbb8385f639af2c2e92651653e3bb4(
    *,
    credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.RedshiftCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    database_name: typing.Optional[builtins.str] = None,
    host: typing.Optional[builtins.str] = None,
    lineage_sync: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.RedshiftLineageSyncConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    port: typing.Optional[jsii.Number] = None,
    storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.RedshiftStoragePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b195696e44f8816ec97423896e5a52b6ee46aa7c4c9e0e33aa0ac4a92900d2ea(
    *,
    cluster_name: typing.Optional[builtins.str] = None,
    workgroup_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94fbdb6dfc5f26da94f6f165997647170dbb3404b50c6d28eef32f77d6fcd395(
    *,
    compute_arn: typing.Optional[builtins.str] = None,
    instance_profile_arn: typing.Optional[builtins.str] = None,
    java_virtual_env: typing.Optional[builtins.str] = None,
    log_uri: typing.Optional[builtins.str] = None,
    python_virtual_env: typing.Optional[builtins.str] = None,
    runtime_role: typing.Optional[builtins.str] = None,
    trusted_certificates_s3_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc6a385f982dd6f3097586513e776c152b3210e81a751a74ccdf596b24edf2ba(
    *,
    connection: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44d0d0a8466990262ea9a97c7791e494a3b6f38cf1968ce4fcff9de3fc1a9c77(
    *,
    additional_args: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.SparkGlueArgsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    glue_connection_name: typing.Optional[builtins.str] = None,
    glue_version: typing.Optional[builtins.str] = None,
    idle_timeout: typing.Optional[jsii.Number] = None,
    java_virtual_env: typing.Optional[builtins.str] = None,
    number_of_workers: typing.Optional[jsii.Number] = None,
    python_virtual_env: typing.Optional[builtins.str] = None,
    worker_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09aad17749e39aa1e36aa16e65e288bbdbfd74b1ed996ed966f666f40ce8c31d(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8797ba459ed68920849c7b460987b708539d45c9d479ab52091ec466aebc8432(
    *,
    domain_identifier: builtins.str,
    environment_identifier: builtins.str,
    name: builtins.str,
    aws_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.AwsLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    props: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.ConnectionPropertiesInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b74a6ac4c3e98c769e70eb9dc6e8b5f1e8f347a3615d992ea7f1c0d421505732(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_identifier: builtins.str,
    name: builtins.str,
    project_identifier: builtins.str,
    type: builtins.str,
    asset_forms_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.FormInputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DataSourceConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    connection_identifier: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    enable_setting: typing.Optional[builtins.str] = None,
    environment_identifier: typing.Optional[builtins.str] = None,
    publish_on_import: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    recommendation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RecommendationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.ScheduleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33bcdad9dc3f66143343138916ff460345630898241997119efe034ff66c6a2d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__514e677208a85632dfb8a4fcf6a71bea051c78567845845ff000fb632aab7b5e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a7af31e6c5b528548b0d530d4c772805fb61420d812ed44382c7c390086f11a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2821916d0fb71bfe9878d75d49136fb173b8984bb70e31a4a9720eebf6db3ab3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__132e7e2cf26f81c0a6085283f4e8d4d9f57da8d3612dd55ee6749c192a2d2d48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d073c13da920100b2d471eb086a45db9d741e4fba0dc8a0677ffe38913dffe2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd33f5216eca4a4d866e941b183a5ef445088a5e6ecec69e2fbc695f6b40c3c8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataSource.FormInputProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89afb772730c8209e27316b8af14ef1a6fce9f26db9f31432460eff964f55b9d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DataSourceConfigurationInputProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caff1a5a915d2678ed1266a9c2f82efe4b3b9c3fcccd444c54fd11e49a43068e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7e5b5e600ceeed0171e7700fd1bb1de08837412c76a72396b54b2ddfcd29970(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c4b8af5e1647731587c5aaa0ac03d7e6980729c429135de819a778bb0e7a2eb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ed64595e5e156084952dfe11e1e064218cba6affcb8bf2736d3e0a177b08bea(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b8ce503c85a6ffdd243c0997e3ddab5dbbb39fc65cc2c74982964209c9e4eaa(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__213e25d07ce5c23cedc981ed540f97a1577533cd3dab4f6e0a08f166e38cfb49(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.RecommendationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__693f7d02be84739f3d95375e94a3b4c964749b34e7dbf67ac0aa2b011ca3f625(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.ScheduleConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9bda82e8d6905101b134276b283067e9b4fc8445ba4e98917ea7cd2937c5828(
    *,
    glue_run_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.GlueRunConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift_run_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RedshiftRunConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sage_maker_run_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.SageMakerRunConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb2b40bf6229fe763c7c585fa978f99e3900fbd6916fc58d9065ddc99d90df18(
    *,
    expression: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e39737bda51e6e9e0b04ce2c0598b00c495cf2dad8f53d4761c7a31ecf92227e(
    *,
    form_name: builtins.str,
    content: typing.Optional[builtins.str] = None,
    type_identifier: typing.Optional[builtins.str] = None,
    type_revision: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad6a5a243d0193849a3ba940cfbd956439268966f2ff08bff1fbcf5af20fe953(
    *,
    relational_filter_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RelationalFilterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    auto_import_data_quality_result: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    catalog_name: typing.Optional[builtins.str] = None,
    data_access_role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b892cb470f7ea420aeb56956a5375b815b6b2a91d0e3d5aaa0a3461f5924b22(
    *,
    enable_business_name_generation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf5e238c98cd0e25a8234c800e1db4699c482f8c18eb4b1a30bdf8afd3ca2718(
    *,
    cluster_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1df8fcf30634f3b35250f98172cf307551610fbd637ef517691ae5581ccb5f66(
    *,
    secret_manager_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dd4c8b6216739fc8295ada55b58407d555982639c53118e9be94f72b8eb8e7c(
    *,
    relational_filter_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RelationalFilterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    data_access_role: typing.Optional[builtins.str] = None,
    redshift_credential_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RedshiftCredentialConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RedshiftStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c58e081ae0c5b103243a5fb5e44d072e16021860d239dd719e8ecaa4696f2da8(
    *,
    workgroup_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6959cf31dac7c5d3c9ee4d255059c5f6007a01d1da657810b6e3e44f31806173(
    *,
    redshift_cluster_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RedshiftClusterStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift_serverless_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RedshiftServerlessStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b69950b3dd7224f1119f8c5e6a2c8675594377bc1e5845a101f3b5f210681258(
    *,
    database_name: builtins.str,
    filter_expressions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.FilterExpressionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    schema_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28babf5c4c5363adc4e0e12e10b52800bdefbc80558e5eb5e050bd3e2c484591(
    *,
    tracking_assets: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Sequence[builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fc1ad55dd2850c09e234b6cbea1fb383c32658a6b0f4b3e6c9ec1d67d8ae10c(
    *,
    schedule: typing.Optional[builtins.str] = None,
    timezone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc5ec98207dd171531ba923ab77ceb4e9c095a2ac7eb083b5faef7393c183f86(
    *,
    domain_identifier: builtins.str,
    name: builtins.str,
    project_identifier: builtins.str,
    type: builtins.str,
    asset_forms_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.FormInputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DataSourceConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    connection_identifier: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    enable_setting: typing.Optional[builtins.str] = None,
    environment_identifier: typing.Optional[builtins.str] = None,
    publish_on_import: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    recommendation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RecommendationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.ScheduleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__047efef40bc572d080b2e64b8f32c1db40e40ba16fc7d29d887073e9c6b44c3f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_execution_role: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    domain_version: typing.Optional[builtins.str] = None,
    kms_key_identifier: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[builtins.str] = None,
    single_sign_on: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SingleSignOnProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44ac286b6a265a7b8c549e9f75d607cdf3e71f300523940763c96adb368c15ac(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__595689c850e768a74bf0e3147031e1acd033e20ab08856209edf9954aa010432(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f0f91db144dcd37dc91c4f005e5e179143c7d40165baf625ef7e284af70358e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb44fad9b00c8b94e0193e65a7d6e38fbf79595a0c367032211eb3ddcec54145(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb0d62a189dbc4d1b327c1e7f651b95f580a2f6196abce203f4709bcca75c7c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01acac61c7163cf6379c6cbe162a62434376eca50700d6cfaaea6008ea3ec333(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49d22f79e701c8bd8ae540b270f397204f2285f1dc76ab7d1556d659a050f38b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fd383448cae4473b200d8583b604eef942f85827467ce9f6bf4b1fc6f61390c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee4595d765303396b66c3b59368637f839b950667fb4c707c509ac63e084f20b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.SingleSignOnProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d899e2a4a220703956ab7f56e7c810107ec736f8c6281bedb3bc027e6ddb2ba4(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7f4cd03b79bceb07fb9f1366c739ee9cc49b8cbf6b9077a564689e81698df16(
    *,
    idc_instance_arn: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    user_assignment: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d98e07f58a8aeb53fe8b36894639594f83be43ac8d182e1c384572cf0038d27(
    *,
    domain_execution_role: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    domain_version: typing.Optional[builtins.str] = None,
    kms_key_identifier: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[builtins.str] = None,
    single_sign_on: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SingleSignOnProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1700595f9c5a7d1c2312abf9e8d15687f79d83e5ead5d4136afe1d562d212c38(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_identifier: builtins.str,
    name: builtins.str,
    parent_domain_unit_identifier: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__253603c22b8126a36f68fce57f93a169ab3bae1eea3f4a0ed84da859e1a38444(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a243fcb8e7ead0c756ca762c1cdda3fa9d1e09b6cc2627c55905a3ba1c13d46a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf72156aa725b96faaed85404e23d70dc267cd0abb5f25a82730b49e79db3da3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e554b39a08bdebb47a996dd0ed4d2386500e1f97db8b2b102320bf4c229a429(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fc10ab18c77014087fe1354e8f1063236b8830e559cbc2287ef325f51d1ab0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a999765de6c52fcb132be3cd0b216fc666c0809dfc86c99a02dfc71a5fff2974(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__740935adbb77d29725778a65030d855aa614e033e09a756660d6c3eef6160bd9(
    *,
    domain_identifier: builtins.str,
    name: builtins.str,
    parent_domain_unit_identifier: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9dbab782927b08354bbafa4881abe3f775c9141395be836e6450777f8729b9b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_identifier: builtins.str,
    name: builtins.str,
    project_identifier: builtins.str,
    description: typing.Optional[builtins.str] = None,
    environment_account_identifier: typing.Optional[builtins.str] = None,
    environment_account_region: typing.Optional[builtins.str] = None,
    environment_profile_identifier: typing.Optional[builtins.str] = None,
    environment_role_arn: typing.Optional[builtins.str] = None,
    glossary_terms: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.EnvironmentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a28a39a0c7ba040029b6d28481def84a1131453e9259d7f220a8d8f9a9562fcf(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7a663cc771f3c58655975db4a99b46784c16b0b96c4bb006217531f931854d1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b36a4aa57667467b8bda95ca761a942a6f67e34e8549cd2dccc7a61d8399e9b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4376356ce7178baaec6de65e59f567c3496e08605a27833ed8e83bfe0ff4be4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baefbe7e97d72065b3b2c6be4e97a54bf9298376bb60dcac92eb7191397e306b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00e90ff4028654f7f45c97804aa061515407ac2ce2e55a21a1a4e4ff76fefd60(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43f5514f896b52007434785f6106a995073e27bf964e663b740911090d537bf3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c559df95e35a94ccf1ae460803faf8ff00fc715c3ad0b7cfafb1b92c2258564(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__123d0e6b3ed252019ec79f09a380206e446d8155ba73fc8e7518fbd3dbac8c2c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b4153aa4bfc638db19251feaaf147e1376f5797ff9dd67109f2a7bf538d8a17(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d52d21b9ab0852f8793f985e6f12ccea104ddc7e138f30b744d739af3c46b742(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d345163e4f1ef89a409f470c896454213d0735fe6e5011e7ec6df4ead799556d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.EnvironmentParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d32a764f93482ecbfe18350874389b17ae96f3d5f78686bae5b55a2dcdfc012b(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23d8a73d028f6e855c2cc806cf34d881ee774001b5faf55329f1186898cd5d1c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    domain_identifier: typing.Optional[builtins.str] = None,
    environment_identifier: typing.Optional[builtins.str] = None,
    identifier: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentActions.AwsConsoleLinkParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5619cfe3b3ca5963d029c87191973ca35ac3bb01102c8e807502ada262fedcc7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be72805e85c16a3d6d6a9862f3a07226b330cf4b3b110b5775de9db3c6d64dd2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af36c191170daaf1b24eec04f527e30281e32ee3f3f75aaacbd67e64aca1b10b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55c22815170a2513147f4e74885cc8ca51917b6ec8c0644bc9c6d05b0fa2f41d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa29021d0052df07430696eb45141a3ff12c83aa11f3fe5291138364d64bfe49(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__224d8bbf6ba3a5a13d6893687689bb34a69380029d8d4fe281607965ccb59065(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b0cf584a76af6d608e499b80f7ae532dcfdbe54a0d8d961ad67e4b52052f530(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d7a1e83f2300dd2bce221749201b3aef3859d465ce9d2e72bb7161776120da2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironmentActions.AwsConsoleLinkParametersProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a66aef49f4cbb5c05c7c82600d65a4b555f3e4321747102f3fc890d8498bac56(
    *,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c38a51ef4e52ffbf8312da8137617dd0e35055ad7636f23de55e829eae23750(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    domain_identifier: typing.Optional[builtins.str] = None,
    environment_identifier: typing.Optional[builtins.str] = None,
    identifier: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentActions.AwsConsoleLinkParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48d8677ae22ff2da132402ace39f998c6b914f7464ce38abe9373fdbc550c445(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_identifier: builtins.str,
    enabled_regions: typing.Sequence[builtins.str],
    environment_blueprint_identifier: builtins.str,
    environment_role_permission_boundary: typing.Optional[builtins.str] = None,
    manage_access_role_arn: typing.Optional[builtins.str] = None,
    provisioning_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentBlueprintConfiguration.ProvisioningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    provisioning_role_arn: typing.Optional[builtins.str] = None,
    regional_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeb5ba3f6738d175b0ca7714e77b6af191ccad2c9967480252920cb95dc6cb8f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86364c1d7caa870da909a60996d646dde31c0e41cb594d0e952262cd925d5bdf(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e6a26e61dc0bca0a16da5100bf8f8cfcb05985dcd52fd83afd7818c62445836(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9064df9af275b8a17afb82a8fc271f7b6e0ab19cdf01da41f144bac4832180e0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db2bf9c4c7f25403fe2aa03be854b8b8b1f530f8d53a317f87b2fb9470d906a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0142557047b6391f0c0d7425b73085935e7a1d5e07139d87dcb9c9ab709bd4ac(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13a80be3403ea5113203d40c0843c4e4965600487d58b5f1e83bf1b8a9fc3d11(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f945458658c5114bd92815174ffa8cabc189cbb27ef04cd8ca8a0ca6b933ad77(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentBlueprintConfiguration.ProvisioningConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09c1e18144766c7e8d72f080dbe9de88dc085cfbdaa47a10b50cf7e235be8d65(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93fe5a214b768cb7201e2f47a6073bdec0303c4cda4d1d0b739b124ba7858574(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b34e7436c5711c0e3c03f2d39f197fd5268605136341c021dfdb2f9be036a01(
    *,
    location_registration_exclude_s3_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
    location_registration_role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29b5e41d02462ac9818fbf0e54d1556527c5ab2ab685686237dee244c941e9bd(
    *,
    lake_formation_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentBlueprintConfiguration.LakeFormationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__563b6d6aa110d6b77fcca8e42c3020852fa0c12036e1ba7f6ee62b2ce30826ff(
    *,
    parameters: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca96f6fc24dc164f6fafb08d94645f48f6b4fc5c0a2ad8a3b95e170935e7353a(
    *,
    domain_identifier: builtins.str,
    enabled_regions: typing.Sequence[builtins.str],
    environment_blueprint_identifier: builtins.str,
    environment_role_permission_boundary: typing.Optional[builtins.str] = None,
    manage_access_role_arn: typing.Optional[builtins.str] = None,
    provisioning_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentBlueprintConfiguration.ProvisioningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    provisioning_role_arn: typing.Optional[builtins.str] = None,
    regional_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a22dac59a328e3776825e07c2891d034e7e205eeeb00866d9086cf2f1dceb4f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    aws_account_id: builtins.str,
    aws_account_region: builtins.str,
    domain_identifier: builtins.str,
    environment_blueprint_identifier: builtins.str,
    name: builtins.str,
    project_identifier: builtins.str,
    description: typing.Optional[builtins.str] = None,
    user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentProfile.EnvironmentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b72ea9dd66a1ceac9aed426988a2df917e784879f21b1f6f0c19ca29b30b31b0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d250e5f9b10cd5d865865b560ea448ee7860153a35651b00d758f6634aba260(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de45320506b6ea6065d4e8de40a649bf205ae44ef01638670599709d45fde670(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__929764ebd8bf0a538d63bf5bea864a4c6a1f1fa57874f35c72ee4cb0c977cdf1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9311c317e06fadb8c96c0e621239f5e4ce23903cdc1515f8f48973321817bc6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40d0761ec5bd844c4a1859c609961ac63da5ca2a42154f19f8cdf0482693545f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__894c00430dd4f51ab95f6ed5db99418bdfe03c4cd5e70df92930998dc03b23e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32f0a4cae84b8e4e478646d80c611ae0d63fbea35bd054197eaeb64b33b624c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__537f0658d3e004344b5e150e1c4182f64abe6101e2d21aaf1644347b19d27116(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f091fadf5731901077c11ba7bce182eb007b6bd8b291bb6a4676fd3fa8e0e689(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentProfile.EnvironmentParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d9a0947f6555aed5fe498e71fb0065f6dff69f004c35341f60523d1de281e5f(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24d37d0c5f53a77c5e5be4ffa574af7dd3da85d8b5eb31bff30362d6c63ac36b(
    *,
    aws_account_id: builtins.str,
    aws_account_region: builtins.str,
    domain_identifier: builtins.str,
    environment_blueprint_identifier: builtins.str,
    name: builtins.str,
    project_identifier: builtins.str,
    description: typing.Optional[builtins.str] = None,
    user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentProfile.EnvironmentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52cb17aae6cf0b0cbeef010a71f7f53573517f0a8e973b5881ae34c1691d672b(
    *,
    domain_identifier: builtins.str,
    name: builtins.str,
    project_identifier: builtins.str,
    description: typing.Optional[builtins.str] = None,
    environment_account_identifier: typing.Optional[builtins.str] = None,
    environment_account_region: typing.Optional[builtins.str] = None,
    environment_profile_identifier: typing.Optional[builtins.str] = None,
    environment_role_arn: typing.Optional[builtins.str] = None,
    glossary_terms: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.EnvironmentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bccafb3ac5ccb0c73cc0aaea6cf365a78e841d8d731ffbfa84165d7f8100f7a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_identifier: builtins.str,
    group_identifier: builtins.str,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3064788268855f6623aaf3b52a7be17022b3d0c8d206428bb22e10d7bd9791de(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66e617beac92ae83db2859cea30504a6e86d11714b8584d4212fe2f5634055e4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bfce5f937e19aa12105a026759b48056e8cb9facac990d4a84ae9ebf754349a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4cfe59401594c99ca6ed491e080ab3526afa6a5fbfa200d918455779f2c060f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__489105c9239ff5a560f37a1c161dc9de12874e97ca98bb0ac4df8139e29b6727(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f4f2d05f4850cb07cd88e6e5af875d2c16fa3ae4bcbc384b9a51f7f0d0ca2e4(
    *,
    domain_identifier: builtins.str,
    group_identifier: builtins.str,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94bfd7733fd63571746923975807ae8f32ba35341a37f7148bb545b4e9847274(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_identifier: builtins.str,
    entity_identifier: builtins.str,
    entity_type: builtins.str,
    owner: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOwner.OwnerPropertiesProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa3b09221ad53f7b391234ed414a2caf5be239897130cb63a881be90fd3d5159(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7abc3e34a10e4f417d29d275feb8d0afab58fee4bf106d762ec5e892461eaa7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9073faa55a5b23ffa32de5b7b260a878507e76f90477bf1a9c90357c2872891(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__553cfea40a703af75f1688c6e78763ca8d67d1e10486295a4f15880e459e83ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59a8766cde46db5fea0cab80e368951dc950c0c18bbe166065a74941ff7268d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9200651c9921dbe5e1d4780332c9e8f8b197d26e18954ed4949d2b2e1f42f642(
    value: typing.Union[_IResolvable_da3f097b, CfnOwner.OwnerPropertiesProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebdf17d77276482c77fb47efd9e4dbd02334583fe0ecbd40c08d7f701ee8d14b(
    *,
    group_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c101d7b0fa44737f68ea873c4543f1aaebe3e1acc72b89c5d6be7d3315a3f6a(
    *,
    group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOwner.OwnerGroupPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    user: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOwner.OwnerUserPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ddd200ac00629d27d95838e6fe38733e398593324aa72df62d033667a13781d(
    *,
    user_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d35804fdeb7af54df495ac452da3f154252f3e8b980bc354ae920748f4c8e46d(
    *,
    domain_identifier: builtins.str,
    entity_identifier: builtins.str,
    entity_type: builtins.str,
    owner: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOwner.OwnerPropertiesProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dd190e348e5421f499a11e44b2fb0c69295587e5e7717b13a56786a897efe7f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_identifier: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    domain_unit_id: typing.Optional[builtins.str] = None,
    glossary_terms: typing.Optional[typing.Sequence[builtins.str]] = None,
    project_profile_id: typing.Optional[builtins.str] = None,
    project_profile_version: typing.Optional[builtins.str] = None,
    user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.EnvironmentConfigurationUserParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dec99f127bfd691b7b1ab5260c233568e5b335a316a646dd759686435ab2eb32(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81361e533bde98a7e424eedf14591a679c836493433a44301b63cbf3357e5369(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c4440504b53716f23143b92e80a5ea3dcfaddd707d93cad9b77c33e5e19e7a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7972d56cc7ec2cdd1800b8f0d6a79f7b4ad88633cf64a2e04f072fab6c9454b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbb0277c9bfd29282afdae45a284966770345575b2854ec5cd9e6c04dffbac96(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38159bc2eeb309ee419b2f700c1738155e88fd699cb77897bb1441e19caa9250(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed99a8f1a094dd4883e961330ac91acc714a4a5fd200b2d53a52d4113d5a34f8(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd4329ffc5180ec3c489a9b9628b37fda4e7e56daeff4465877926e7905d64d8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fea851298bf6dff2224e18bba1dcf8117578fd86b764925c8087d78e2917049(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a8a1e223cb296d2e10e4a3c700e7f0c868d2c481c6f8c40ddf1c6a06e86a604(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnProject.EnvironmentConfigurationUserParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e38660ae766630ccadf35e49b4f78a771668296fc64a72a9c1e9b3d3b1a16a1(
    *,
    environment_configuration_name: typing.Optional[builtins.str] = None,
    environment_id: typing.Optional[builtins.str] = None,
    environment_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.EnvironmentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bfbfca939a617b6012dc8847e17b3567d673ec789228318c5d1c397165a7b9e(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__227cc3d5649ee98fd5579f9e1870652d6de5250e0390e91fec524565dc07c0b9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    designation: builtins.str,
    domain_identifier: builtins.str,
    member: typing.Union[_IResolvable_da3f097b, typing.Union[CfnProjectMembership.MemberProperty, typing.Dict[builtins.str, typing.Any]]],
    project_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e6a7791d79b9b8f15baba0f04bddbfa77afbfbdd8d2872a6e46acd2ccee79c4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e37a11438611477027ae5dde4a091dc361c7dc56ba7538221e222ef9083be907(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71ec417c1a2abac8b6037b5bfedeb8520a3be4a0844d46c1862cb259465e45f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66d809e4462dc85243bcc1ab3799cc4a5180f2f4119683718081fa5f79530ac7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50f6e6b64e6349a5c9d740955a9ccac88cf9da161bf02038bc9e12572958a93f(
    value: typing.Union[_IResolvable_da3f097b, CfnProjectMembership.MemberProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da845d5c47de18f48a6a2e21aa5b41e5193d4b3faad962602fc4d3b98d677eb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2184a0c3aa18e8899e2cb70b944b79d781e689bd543ac2140e9176025c2fa864(
    *,
    group_identifier: typing.Optional[builtins.str] = None,
    user_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b25f4db16efa2b368a4cf197bdf102ccdf0c613db5654c1186f9404f9259e4d7(
    *,
    designation: builtins.str,
    domain_identifier: builtins.str,
    member: typing.Union[_IResolvable_da3f097b, typing.Union[CfnProjectMembership.MemberProperty, typing.Dict[builtins.str, typing.Any]]],
    project_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be64eda6c4825457191dba5045e07eaa3e14f5b1d6605cefc1c291b8f70eb5b2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    domain_identifier: typing.Optional[builtins.str] = None,
    domain_unit_identifier: typing.Optional[builtins.str] = None,
    environment_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProjectProfile.EnvironmentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b4346bd08f5dc87b3a8b49fbf28cae8774624d1da19c5d260d4fbdf104d531f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85b771eebccea5f26f952595144e99a6c3ff8b1d0cce9803511978dff3785a2a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5acf0d662fb5f406ca391f15c3cadba1d68d0dc161876b2305e495701c03968(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3e1ff90e5fbfc5a555174f254ce075a9c3654511436a8acf04928992020df04(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__872e790316704042dc15857aaaff7b99878b643ac02f9de929f704cf6ca6762a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b87add426c25b8a2eafdfd51a8707432f3ee35363162b07265e414b1d427ff1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11d2d41d817a0c6b3e1fb33f36874d8544dda639fa89db0b3de59a24198ab098(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnProjectProfile.EnvironmentConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22f2f0484438c03962ae71a7a8c680afa1c54e8a672160956c3951d55a32ae02(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fcf2ee1bc8e5e84878993902463e74d2e0d59a5486d29b3270a330e403a11e1(
    *,
    aws_account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf7bbb8e1650467ecc0369100cdd1f22e8ec805fbddb090e6314b2b5a01ddb4a(
    *,
    is_editable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fab90e5736f5e6f3ffb1d2c481eba6fcd8f1f870000719d3c6a3852737b46e0b(
    *,
    parameter_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProjectProfile.EnvironmentConfigurationParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resolved_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProjectProfile.EnvironmentConfigurationParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ssm_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8addc3ada6a67b6cbb6b275c952d4659afeea35b806096cdb6322e14ea2ea99f(
    *,
    aws_region: typing.Union[_IResolvable_da3f097b, typing.Union[CfnProjectProfile.RegionProperty, typing.Dict[builtins.str, typing.Any]]],
    environment_blueprint_id: builtins.str,
    name: builtins.str,
    aws_account: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProjectProfile.AwsAccountProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    configuration_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProjectProfile.EnvironmentConfigurationParametersDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    deployment_mode: typing.Optional[builtins.str] = None,
    deployment_order: typing.Optional[jsii.Number] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc189c16fcab170d1d8d250893b0e4741d23998acae1597f3faa4ca36264479b(
    *,
    region_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16088b85440c601f18ad4a194ccb23740aedaa1b4f93a76e720d939c57cb4d2e(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    domain_identifier: typing.Optional[builtins.str] = None,
    domain_unit_identifier: typing.Optional[builtins.str] = None,
    environment_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProjectProfile.EnvironmentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d519699f8d5d172880216006cab9e8c1595fc99339cf485d2be1f6c37bbc5a4c(
    *,
    domain_identifier: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    domain_unit_id: typing.Optional[builtins.str] = None,
    glossary_terms: typing.Optional[typing.Sequence[builtins.str]] = None,
    project_profile_id: typing.Optional[builtins.str] = None,
    project_profile_version: typing.Optional[builtins.str] = None,
    user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.EnvironmentConfigurationUserParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c61b5cfe149791a4c62bad0056737a365bdf72f7f99e6e72c71be1058e91604d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    applicable_asset_types: typing.Sequence[builtins.str],
    authorized_principals: typing.Sequence[builtins.str],
    domain_identifier: builtins.str,
    environment_identifier: builtins.str,
    name: builtins.str,
    subscription_target_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriptionTarget.SubscriptionTargetFormProperty, typing.Dict[builtins.str, typing.Any]]]]],
    type: builtins.str,
    manage_access_role: typing.Optional[builtins.str] = None,
    provider: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1ffb846a6baf7f8d43c947f31440c264738eb11477a914e6234e72e512226a7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__867dc79750bd91424b54ba2d5f7eca4a8d13f7f3c9f4ffc4effe5dae834ed869(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6db9fad0cfe2726fd2714cfa52499e265af46d2cacf4be9daa6378bd8c673b5a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ec38d6c0d885e0ae64427a2407f691f11cd764f198652ece23783772c2611fb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77bccb41f1eb7b5a32710e03ae6cfec74eb17bf3129bd372a11c92f7f67f5dc0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20ed34c3b416019570831200db233eb4c407b91b53464c36e9fbdbdcd4a6da82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc691c403b67912db7216c5f5fddda4101316ca719bd90e37c92640197c61004(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a19c0f2213973750a6cc503429c6ef8619a3d0885a2df0f54aad48a00a3c6f46(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSubscriptionTarget.SubscriptionTargetFormProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8961cb77429dad851472db6b14a76c77606d0bffdc98a0cbb3cffd227c3ec500(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83f19af57790aab3ddc6c4e1f64e1f68cf69073e46da8ac997fc9f0c83e93198(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4526f8f71696c8c7bf040cd042cda55182de538f2ebf276253751b5a497c037(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__720cbd7aa436c84d94877993fe56ec1a54389edd9936074e71ebf65a3caffa9b(
    *,
    content: builtins.str,
    form_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b970b38bc2b99a7ed3ef3830dfa5721ecc9ee442e5d627e01abfdcb22600151(
    *,
    applicable_asset_types: typing.Sequence[builtins.str],
    authorized_principals: typing.Sequence[builtins.str],
    domain_identifier: builtins.str,
    environment_identifier: builtins.str,
    name: builtins.str,
    subscription_target_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriptionTarget.SubscriptionTargetFormProperty, typing.Dict[builtins.str, typing.Any]]]]],
    type: builtins.str,
    manage_access_role: typing.Optional[builtins.str] = None,
    provider: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43948fd61004932aa31394de53e9c49e34aa425f3682404de5d5f6a249734d82(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_identifier: builtins.str,
    user_identifier: builtins.str,
    status: typing.Optional[builtins.str] = None,
    user_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62409db933bd1f83a26e4a296f90a5aa33de9e2cd9f82db4084d8f1cb0f382e4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bac3d345ed2cf85373ed12e71655921f20ce2575e0f95a05a3dd29cfa7e804e0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57dc87f9b5d4209a76a54e631bab548eddbecf73d3a0cb39b30030a99c20dbb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bc695cbd1d290ebde7514044903060b533b99cd4f724f387512ffb614625693(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f391a63fdbc6b7a8aefbb3664fddfe91481bce941965f274ecad0166152935ce(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b560448b79c8df59777bf516743c73a776fe419d2c08183dd62546f1fc65ae4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fd3b9b642370fd3593445a459418ba3df5f97586bee6446bed499fa533a4022(
    *,
    arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07963e9a65d43152452195ee221d80669fe4707d48ffd231ffc947c240448dbd(
    *,
    first_name: typing.Optional[builtins.str] = None,
    last_name: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a1351a79d8a8cf0246c7e7591c1c0736de90dfd896392c833f9cb3530c63997(
    *,
    iam: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUserProfile.IamUserProfileDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sso: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUserProfile.SsoUserProfileDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__431134ef647ba94f8eb72ef3985b514bb86c42b53ca933a9fd51ea529bd0fec8(
    *,
    domain_identifier: builtins.str,
    user_identifier: builtins.str,
    status: typing.Optional[builtins.str] = None,
    user_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
