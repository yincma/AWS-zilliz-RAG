r'''
# AWS::OpenSearchServerless Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_opensearchserverless as opensearchserverless
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for OpenSearchServerless construct libraries](https://constructs.dev/search?q=opensearchserverless)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::OpenSearchServerless resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_OpenSearchServerless.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::OpenSearchServerless](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_OpenSearchServerless.html).

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
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnAccessPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnAccessPolicy",
):
    '''Creates a data access policy for OpenSearch Serverless.

    Access policies limit access to collections and the resources within them, and allow a user to access that data irrespective of the access mechanism or network source. For more information, see `Data access control for Amazon OpenSearch Serverless <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-accesspolicy.html
    :cloudformationResource: AWS::OpenSearchServerless::AccessPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opensearchserverless as opensearchserverless
        
        cfn_access_policy = opensearchserverless.CfnAccessPolicy(self, "MyCfnAccessPolicy",
            name="name",
            policy="policy",
            type="type",
        
            # the properties below are optional
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        policy: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the policy.
        :param policy: The JSON policy document without any whitespaces.
        :param type: The type of access policy. Currently the only option is ``data`` .
        :param description: The description of the policy.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f3695018b497271b2884c3d90b44513c0e4644d1625baefd3c5f2880a1223da)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccessPolicyProps(
            name=name, policy=policy, type=type, description=description
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21888f21364bcb4177baf2ccd610dc59283ab52bb27386322330ad2d3381e0de)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e00c49a5052cb7959a45d9347290149a3138d4d622e0aca3118485fae647010e)
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the policy.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54b3786c37ee33848fa7b21ba500dd1920002dea0fe9ec5bd1440f81686f4638)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        '''The JSON policy document without any whitespaces.'''
        return typing.cast(builtins.str, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7da9c131bb5f7ae3527dc4b4934b48aac60a8f0b88b51d40a50c13df36532b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of access policy.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d72ffab9810a9603f58d764e6a8f7a88c9198aea6ffc88f14cc048f6834586e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__768c8582758ca3add7a55a7e6ef420b56cc700d0f10d913632558c56f7cb16b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnAccessPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "policy": "policy",
        "type": "type",
        "description": "description",
    },
)
class CfnAccessPolicyProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        policy: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAccessPolicy``.

        :param name: The name of the policy.
        :param policy: The JSON policy document without any whitespaces.
        :param type: The type of access policy. Currently the only option is ``data`` .
        :param description: The description of the policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-accesspolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opensearchserverless as opensearchserverless
            
            cfn_access_policy_props = opensearchserverless.CfnAccessPolicyProps(
                name="name",
                policy="policy",
                type="type",
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fd3a5bd693a196541a3a98339eef4fd1a25680f2e37fa2c50932ab018651a65)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "policy": policy,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-accesspolicy.html#cfn-opensearchserverless-accesspolicy-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy(self) -> builtins.str:
        '''The JSON policy document without any whitespaces.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-accesspolicy.html#cfn-opensearchserverless-accesspolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of access policy.

        Currently the only option is ``data`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-accesspolicy.html#cfn-opensearchserverless-accesspolicy-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-accesspolicy.html#cfn-opensearchserverless-accesspolicy-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccessPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCollection(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnCollection",
):
    '''Specifies an OpenSearch Serverless collection.

    For more information, see `Creating and managing Amazon OpenSearch Serverless collections <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html>`_ in the *Amazon OpenSearch Service Developer Guide* .
    .. epigraph::

       You must create a matching `encryption policy <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html>`_ in order for a collection to be created successfully. You can specify the policy resource within the same CloudFormation template as the collection resource if you use the `DependsOn <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ attribute. See `Examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-collection.html#aws-resource-opensearchserverless-collection--examples>`_ for a sample template. Otherwise the encryption policy must already exist before you create the collection.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-collection.html
    :cloudformationResource: AWS::OpenSearchServerless::Collection
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opensearchserverless as opensearchserverless
        
        cfn_collection = opensearchserverless.CfnCollection(self, "MyCfnCollection",
            name="name",
        
            # the properties below are optional
            description="description",
            standby_replicas="standbyReplicas",
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
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        standby_replicas: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the collection. Collection names must meet the following criteria: - Starts with a lowercase letter - Unique to your account and AWS Region - Contains between 3 and 28 characters - Contains only lowercase letters a-z, the numbers 0-9, and the hyphen (-)
        :param description: A description of the collection.
        :param standby_replicas: Indicates whether to use standby replicas for the collection. You can't update this property after the collection is already created. If you attempt to modify this property, the collection continues to use the original value.
        :param tags: An arbitrary set of tags (key–value pairs) to associate with the collection. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param type: The type of collection. Possible values are ``SEARCH`` , ``TIMESERIES`` , and ``VECTORSEARCH`` . For more information, see `Choosing a collection type <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html#serverless-usecase>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14f72b773d506ce15b59731aeb24f2f4a877a32d31af6ebf57a32ce707e0cb16)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCollectionProps(
            name=name,
            description=description,
            standby_replicas=standby_replicas,
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c88f558406d9de750b6a01e95a1eade398fef738592cdd78170d3f472b7ff7e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d48674433624514f2cfa361d4ec0903ae028ce45853117cd29b576baa3f723aa)
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
        '''The Amazon Resource Name (ARN) of the collection.

        For example, ``arn:aws:aoss:us-east-1:123456789012:collection/07tjusf2h91cunochc`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCollectionEndpoint")
    def attr_collection_endpoint(self) -> builtins.str:
        '''Collection-specific endpoint used to submit index, search, and data upload requests to an OpenSearch Serverless collection.

        For example, ``https://07tjusf2h91cunochc.us-east-1.aoss.amazonaws.com`` .

        :cloudformationAttribute: CollectionEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollectionEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrDashboardEndpoint")
    def attr_dashboard_endpoint(self) -> builtins.str:
        '''The collection-specific endpoint used to access OpenSearch Dashboards.

        For example, ``https://07tjusf2h91cunochc.us-east-1.aoss.amazonaws.com/_dashboards`` .

        :cloudformationAttribute: DashboardEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDashboardEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''A unique identifier for the collection.

        For example, ``07tjusf2h91cunochc`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
        '''The name of the collection.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cdb6f4e81b00df109517f1c4b90835cef7bd07218c9f75976d033888175c41c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the collection.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85980a9398a34a6ff3d72193d32c1438940d0a83c1d83a04ccfa6ebaaccb9612)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="standbyReplicas")
    def standby_replicas(self) -> typing.Optional[builtins.str]:
        '''Indicates whether to use standby replicas for the collection.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "standbyReplicas"))

    @standby_replicas.setter
    def standby_replicas(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54a6dd56a4e746b5f7a24ddd10fa03aa9a0a5c238a5085c7b0ee67caee9db79b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "standbyReplicas", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An arbitrary set of tags (key–value pairs) to associate with the collection.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cfcacecc11d4e30df3a59ae6680ab93be461bc979a2e413a2a77eab2575087a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of collection.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f407bc0eeb99c42f4a9d1d97573b8b10069685ea3e596d162939418b9ddce0ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnCollectionProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "standby_replicas": "standbyReplicas",
        "tags": "tags",
        "type": "type",
    },
)
class CfnCollectionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        standby_replicas: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnCollection``.

        :param name: The name of the collection. Collection names must meet the following criteria: - Starts with a lowercase letter - Unique to your account and AWS Region - Contains between 3 and 28 characters - Contains only lowercase letters a-z, the numbers 0-9, and the hyphen (-)
        :param description: A description of the collection.
        :param standby_replicas: Indicates whether to use standby replicas for the collection. You can't update this property after the collection is already created. If you attempt to modify this property, the collection continues to use the original value.
        :param tags: An arbitrary set of tags (key–value pairs) to associate with the collection. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param type: The type of collection. Possible values are ``SEARCH`` , ``TIMESERIES`` , and ``VECTORSEARCH`` . For more information, see `Choosing a collection type <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html#serverless-usecase>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-collection.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opensearchserverless as opensearchserverless
            
            cfn_collection_props = opensearchserverless.CfnCollectionProps(
                name="name",
            
                # the properties below are optional
                description="description",
                standby_replicas="standbyReplicas",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                type="type"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc3a9fff4dd66b4fe4e69ca639823a978df78a02743764020419d9b37d4f540e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument standby_replicas", value=standby_replicas, expected_type=type_hints["standby_replicas"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if standby_replicas is not None:
            self._values["standby_replicas"] = standby_replicas
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the collection.

        Collection names must meet the following criteria:

        - Starts with a lowercase letter
        - Unique to your account and AWS Region
        - Contains between 3 and 28 characters
        - Contains only lowercase letters a-z, the numbers 0-9, and the hyphen (-)

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-collection.html#cfn-opensearchserverless-collection-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the collection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-collection.html#cfn-opensearchserverless-collection-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def standby_replicas(self) -> typing.Optional[builtins.str]:
        '''Indicates whether to use standby replicas for the collection.

        You can't update this property after the collection is already created. If you attempt to modify this property, the collection continues to use the original value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-collection.html#cfn-opensearchserverless-collection-standbyreplicas
        '''
        result = self._values.get("standby_replicas")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An arbitrary set of tags (key–value pairs) to associate with the collection.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-collection.html#cfn-opensearchserverless-collection-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of collection.

        Possible values are ``SEARCH`` , ``TIMESERIES`` , and ``VECTORSEARCH`` . For more information, see `Choosing a collection type <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html#serverless-usecase>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-collection.html#cfn-opensearchserverless-collection-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnIndex(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnIndex",
):
    '''An OpenSearch Serverless index resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-index.html
    :cloudformationResource: AWS::OpenSearchServerless::Index
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opensearchserverless as opensearchserverless
        
        # property_mapping_property_: opensearchserverless.CfnIndex.PropertyMappingProperty
        
        cfn_index = opensearchserverless.CfnIndex(self, "MyCfnIndex",
            collection_endpoint="collectionEndpoint",
            index_name="indexName",
        
            # the properties below are optional
            mappings=opensearchserverless.CfnIndex.MappingsProperty(
                properties={
                    "properties_key": opensearchserverless.CfnIndex.PropertyMappingProperty(
                        type="type",
        
                        # the properties below are optional
                        dimension=123,
                        index=False,
                        method=opensearchserverless.CfnIndex.MethodProperty(
                            engine="engine",
                            name="name",
        
                            # the properties below are optional
                            parameters=opensearchserverless.CfnIndex.ParametersProperty(
                                ef_construction=123,
                                m=123
                            ),
                            space_type="spaceType"
                        ),
                        properties={
                            "properties_key": property_mapping_property_
                        },
                        value="value"
                    )
                }
            ),
            settings=opensearchserverless.CfnIndex.IndexSettingsProperty(
                index=opensearchserverless.CfnIndex.IndexProperty(
                    knn=False,
                    knn_algo_param_ef_search=123,
                    refresh_interval="refreshInterval"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        collection_endpoint: builtins.str,
        index_name: builtins.str,
        mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIndex.MappingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIndex.IndexSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param collection_endpoint: The endpoint for the collection.
        :param index_name: The name of the OpenSearch Serverless index.
        :param mappings: Index mappings for the OpenSearch Serverless index.
        :param settings: Index settings for the OpenSearch Serverless index.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a029f2a84e6e81eb77a837c5b057c54ae69d5f1ddda222ff52881f5d0f352fea)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIndexProps(
            collection_endpoint=collection_endpoint,
            index_name=index_name,
            mappings=mappings,
            settings=settings,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72216bdab3dcf25c4879e6aed5404e682fbe3d1fd832814ab5bb77a77f3258c5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f26c002ce18fad76e8c679969cbf05ddf77445cb22669f37a41940c49638cba7)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrUuid")
    def attr_uuid(self) -> builtins.str:
        '''The unique identifier for the index.

        :cloudformationAttribute: Uuid
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUuid"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="collectionEndpoint")
    def collection_endpoint(self) -> builtins.str:
        '''The endpoint for the collection.'''
        return typing.cast(builtins.str, jsii.get(self, "collectionEndpoint"))

    @collection_endpoint.setter
    def collection_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84fc2fc583ee69579f5b7f33f8afc9e23bef75f86f99a2b3e46cf07707ab26bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collectionEndpoint", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="indexName")
    def index_name(self) -> builtins.str:
        '''The name of the OpenSearch Serverless index.'''
        return typing.cast(builtins.str, jsii.get(self, "indexName"))

    @index_name.setter
    def index_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a1f9a03417bd926596068b7f503b95c60abebc00e23689dd4dff83cf372576d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mappings")
    def mappings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.MappingsProperty"]]:
        '''Index mappings for the OpenSearch Serverless index.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.MappingsProperty"]], jsii.get(self, "mappings"))

    @mappings.setter
    def mappings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.MappingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01f2947a1782e9f60537bf751bb6fc12efd44df6bc7c2efab931f974a2048326)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mappings", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.IndexSettingsProperty"]]:
        '''Index settings for the OpenSearch Serverless index.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.IndexSettingsProperty"]], jsii.get(self, "settings"))

    @settings.setter
    def settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.IndexSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fa35242932bdcac5598aa8d9552388d7e12b08b01413c30a72c824979d9345c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnIndex.IndexProperty",
        jsii_struct_bases=[],
        name_mapping={
            "knn": "knn",
            "knn_algo_param_ef_search": "knnAlgoParamEfSearch",
            "refresh_interval": "refreshInterval",
        },
    )
    class IndexProperty:
        def __init__(
            self,
            *,
            knn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            knn_algo_param_ef_search: typing.Optional[jsii.Number] = None,
            refresh_interval: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An OpenSearch Serverless index resource.

            :param knn: Enable or disable k-nearest neighbor search capability.
            :param knn_algo_param_ef_search: The size of the dynamic list for the nearest neighbors.
            :param refresh_interval: How often to perform a refresh operation. For example, 1s or 5s.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-index.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchserverless as opensearchserverless
                
                index_property = opensearchserverless.CfnIndex.IndexProperty(
                    knn=False,
                    knn_algo_param_ef_search=123,
                    refresh_interval="refreshInterval"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1a85f85e738bf9023ab824f21e3c4b9a2f4e256a148a314ec2c2b5a47bb64698)
                check_type(argname="argument knn", value=knn, expected_type=type_hints["knn"])
                check_type(argname="argument knn_algo_param_ef_search", value=knn_algo_param_ef_search, expected_type=type_hints["knn_algo_param_ef_search"])
                check_type(argname="argument refresh_interval", value=refresh_interval, expected_type=type_hints["refresh_interval"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if knn is not None:
                self._values["knn"] = knn
            if knn_algo_param_ef_search is not None:
                self._values["knn_algo_param_ef_search"] = knn_algo_param_ef_search
            if refresh_interval is not None:
                self._values["refresh_interval"] = refresh_interval

        @builtins.property
        def knn(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enable or disable k-nearest neighbor search capability.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-index.html#cfn-opensearchserverless-index-index-knn
            '''
            result = self._values.get("knn")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def knn_algo_param_ef_search(self) -> typing.Optional[jsii.Number]:
            '''The size of the dynamic list for the nearest neighbors.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-index.html#cfn-opensearchserverless-index-index-knnalgoparamefsearch
            '''
            result = self._values.get("knn_algo_param_ef_search")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def refresh_interval(self) -> typing.Optional[builtins.str]:
            '''How often to perform a refresh operation.

            For example, 1s or 5s.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-index.html#cfn-opensearchserverless-index-index-refreshinterval
            '''
            result = self._values.get("refresh_interval")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IndexProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnIndex.IndexSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"index": "index"},
    )
    class IndexSettingsProperty:
        def __init__(
            self,
            *,
            index: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIndex.IndexProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Index settings for the OpenSearch Serverless index.

            :param index: Index settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-indexsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchserverless as opensearchserverless
                
                index_settings_property = opensearchserverless.CfnIndex.IndexSettingsProperty(
                    index=opensearchserverless.CfnIndex.IndexProperty(
                        knn=False,
                        knn_algo_param_ef_search=123,
                        refresh_interval="refreshInterval"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2062be5b5132fc74ed29db0c10805e0731b612aad10b8ddbab3dda1eac563bc0)
                check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if index is not None:
                self._values["index"] = index

        @builtins.property
        def index(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.IndexProperty"]]:
            '''Index settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-indexsettings.html#cfn-opensearchserverless-index-indexsettings-index
            '''
            result = self._values.get("index")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.IndexProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IndexSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnIndex.MappingsProperty",
        jsii_struct_bases=[],
        name_mapping={"properties": "properties"},
    )
    class MappingsProperty:
        def __init__(
            self,
            *,
            properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnIndex.PropertyMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Index mappings for the OpenSearch Serverless index.

            :param properties: Nested fields within an object or nested field type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-mappings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchserverless as opensearchserverless
                
                # property_mapping_property_: opensearchserverless.CfnIndex.PropertyMappingProperty
                
                mappings_property = opensearchserverless.CfnIndex.MappingsProperty(
                    properties={
                        "properties_key": opensearchserverless.CfnIndex.PropertyMappingProperty(
                            type="type",
                
                            # the properties below are optional
                            dimension=123,
                            index=False,
                            method=opensearchserverless.CfnIndex.MethodProperty(
                                engine="engine",
                                name="name",
                
                                # the properties below are optional
                                parameters=opensearchserverless.CfnIndex.ParametersProperty(
                                    ef_construction=123,
                                    m=123
                                ),
                                space_type="spaceType"
                            ),
                            properties={
                                "properties_key": property_mapping_property_
                            },
                            value="value"
                        )
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5bb392b8c065f198a0fe7fd6e0fa2156f493990b76e0fee04edb929794b7223)
                check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if properties is not None:
                self._values["properties"] = properties

        @builtins.property
        def properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnIndex.PropertyMappingProperty"]]]]:
            '''Nested fields within an object or nested field type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-mappings.html#cfn-opensearchserverless-index-mappings-properties
            '''
            result = self._values.get("properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnIndex.PropertyMappingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MappingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnIndex.MethodProperty",
        jsii_struct_bases=[],
        name_mapping={
            "engine": "engine",
            "name": "name",
            "parameters": "parameters",
            "space_type": "spaceType",
        },
    )
    class MethodProperty:
        def __init__(
            self,
            *,
            engine: builtins.str,
            name: builtins.str,
            parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIndex.ParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            space_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration for k-NN search method.

            :param engine: The k-NN search engine to use.
            :param name: The algorithm name for k-NN search.
            :param parameters: Additional parameters for the k-NN algorithm.
            :param space_type: The distance function used for k-NN search.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-method.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchserverless as opensearchserverless
                
                method_property = opensearchserverless.CfnIndex.MethodProperty(
                    engine="engine",
                    name="name",
                
                    # the properties below are optional
                    parameters=opensearchserverless.CfnIndex.ParametersProperty(
                        ef_construction=123,
                        m=123
                    ),
                    space_type="spaceType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1f32a7c2cc9cc53a405856608b840b3cd657cad90afeb4b25d6577b3e1573b35)
                check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument space_type", value=space_type, expected_type=type_hints["space_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "engine": engine,
                "name": name,
            }
            if parameters is not None:
                self._values["parameters"] = parameters
            if space_type is not None:
                self._values["space_type"] = space_type

        @builtins.property
        def engine(self) -> builtins.str:
            '''The k-NN search engine to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-method.html#cfn-opensearchserverless-index-method-engine
            '''
            result = self._values.get("engine")
            assert result is not None, "Required property 'engine' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The algorithm name for k-NN search.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-method.html#cfn-opensearchserverless-index-method-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.ParametersProperty"]]:
            '''Additional parameters for the k-NN algorithm.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-method.html#cfn-opensearchserverless-index-method-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.ParametersProperty"]], result)

        @builtins.property
        def space_type(self) -> typing.Optional[builtins.str]:
            '''The distance function used for k-NN search.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-method.html#cfn-opensearchserverless-index-method-spacetype
            '''
            result = self._values.get("space_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MethodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnIndex.ParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"ef_construction": "efConstruction", "m": "m"},
    )
    class ParametersProperty:
        def __init__(
            self,
            *,
            ef_construction: typing.Optional[jsii.Number] = None,
            m: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Additional parameters for the k-NN algorithm.

            :param ef_construction: The size of the dynamic list used during k-NN graph creation.
            :param m: Number of neighbors to consider during k-NN search.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-parameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchserverless as opensearchserverless
                
                parameters_property = opensearchserverless.CfnIndex.ParametersProperty(
                    ef_construction=123,
                    m=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__af09bec36bc7cc06df73ca75b408b7f4402421f3feaaa06806d3ec93cfc2435d)
                check_type(argname="argument ef_construction", value=ef_construction, expected_type=type_hints["ef_construction"])
                check_type(argname="argument m", value=m, expected_type=type_hints["m"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ef_construction is not None:
                self._values["ef_construction"] = ef_construction
            if m is not None:
                self._values["m"] = m

        @builtins.property
        def ef_construction(self) -> typing.Optional[jsii.Number]:
            '''The size of the dynamic list used during k-NN graph creation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-parameters.html#cfn-opensearchserverless-index-parameters-efconstruction
            '''
            result = self._values.get("ef_construction")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def m(self) -> typing.Optional[jsii.Number]:
            '''Number of neighbors to consider during k-NN search.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-parameters.html#cfn-opensearchserverless-index-parameters-m
            '''
            result = self._values.get("m")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnIndex.PropertyMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "dimension": "dimension",
            "index": "index",
            "method": "method",
            "properties": "properties",
            "value": "value",
        },
    )
    class PropertyMappingProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            dimension: typing.Optional[jsii.Number] = None,
            index: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            method: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIndex.MethodProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnIndex.PropertyMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Property mappings for the OpenSearch Serverless index.

            :param type: The field data type. Must be a valid OpenSearch field type.
            :param dimension: Dimension size for vector fields, defines the number of dimensions in the vector.
            :param index: Whether a field should be indexed.
            :param method: Configuration for k-NN search method.
            :param properties: Defines the fields within the mapping, including their types and configurations.
            :param value: Default value for the field when not specified in a document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-propertymapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchserverless as opensearchserverless
                
                # property_mapping_property_: opensearchserverless.CfnIndex.PropertyMappingProperty
                
                property_mapping_property = opensearchserverless.CfnIndex.PropertyMappingProperty(
                    type="type",
                
                    # the properties below are optional
                    dimension=123,
                    index=False,
                    method=opensearchserverless.CfnIndex.MethodProperty(
                        engine="engine",
                        name="name",
                
                        # the properties below are optional
                        parameters=opensearchserverless.CfnIndex.ParametersProperty(
                            ef_construction=123,
                            m=123
                        ),
                        space_type="spaceType"
                    ),
                    properties={
                        "properties_key": property_mapping_property_
                    },
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3f7c10818297058609492c7bc5b994ff55948eef9013ef34074e5e42d61fd371)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
                check_type(argname="argument index", value=index, expected_type=type_hints["index"])
                check_type(argname="argument method", value=method, expected_type=type_hints["method"])
                check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if dimension is not None:
                self._values["dimension"] = dimension
            if index is not None:
                self._values["index"] = index
            if method is not None:
                self._values["method"] = method
            if properties is not None:
                self._values["properties"] = properties
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def type(self) -> builtins.str:
            '''The field data type.

            Must be a valid OpenSearch field type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-propertymapping.html#cfn-opensearchserverless-index-propertymapping-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimension(self) -> typing.Optional[jsii.Number]:
            '''Dimension size for vector fields, defines the number of dimensions in the vector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-propertymapping.html#cfn-opensearchserverless-index-propertymapping-dimension
            '''
            result = self._values.get("dimension")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def index(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether a field should be indexed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-propertymapping.html#cfn-opensearchserverless-index-propertymapping-index
            '''
            result = self._values.get("index")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def method(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.MethodProperty"]]:
            '''Configuration for k-NN search method.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-propertymapping.html#cfn-opensearchserverless-index-propertymapping-method
            '''
            result = self._values.get("method")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.MethodProperty"]], result)

        @builtins.property
        def properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnIndex.PropertyMappingProperty"]]]]:
            '''Defines the fields within the mapping, including their types and configurations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-propertymapping.html#cfn-opensearchserverless-index-propertymapping-properties
            '''
            result = self._values.get("properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnIndex.PropertyMappingProperty"]]]], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''Default value for the field when not specified in a document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-index-propertymapping.html#cfn-opensearchserverless-index-propertymapping-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PropertyMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnIndexProps",
    jsii_struct_bases=[],
    name_mapping={
        "collection_endpoint": "collectionEndpoint",
        "index_name": "indexName",
        "mappings": "mappings",
        "settings": "settings",
    },
)
class CfnIndexProps:
    def __init__(
        self,
        *,
        collection_endpoint: builtins.str,
        index_name: builtins.str,
        mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.MappingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.IndexSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnIndex``.

        :param collection_endpoint: The endpoint for the collection.
        :param index_name: The name of the OpenSearch Serverless index.
        :param mappings: Index mappings for the OpenSearch Serverless index.
        :param settings: Index settings for the OpenSearch Serverless index.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-index.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opensearchserverless as opensearchserverless
            
            # property_mapping_property_: opensearchserverless.CfnIndex.PropertyMappingProperty
            
            cfn_index_props = opensearchserverless.CfnIndexProps(
                collection_endpoint="collectionEndpoint",
                index_name="indexName",
            
                # the properties below are optional
                mappings=opensearchserverless.CfnIndex.MappingsProperty(
                    properties={
                        "properties_key": opensearchserverless.CfnIndex.PropertyMappingProperty(
                            type="type",
            
                            # the properties below are optional
                            dimension=123,
                            index=False,
                            method=opensearchserverless.CfnIndex.MethodProperty(
                                engine="engine",
                                name="name",
            
                                # the properties below are optional
                                parameters=opensearchserverless.CfnIndex.ParametersProperty(
                                    ef_construction=123,
                                    m=123
                                ),
                                space_type="spaceType"
                            ),
                            properties={
                                "properties_key": property_mapping_property_
                            },
                            value="value"
                        )
                    }
                ),
                settings=opensearchserverless.CfnIndex.IndexSettingsProperty(
                    index=opensearchserverless.CfnIndex.IndexProperty(
                        knn=False,
                        knn_algo_param_ef_search=123,
                        refresh_interval="refreshInterval"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__663cdeaeaa67ae562243597848e75d79ee7310523ecd791e0c37af19d4197d1a)
            check_type(argname="argument collection_endpoint", value=collection_endpoint, expected_type=type_hints["collection_endpoint"])
            check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
            check_type(argname="argument mappings", value=mappings, expected_type=type_hints["mappings"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "collection_endpoint": collection_endpoint,
            "index_name": index_name,
        }
        if mappings is not None:
            self._values["mappings"] = mappings
        if settings is not None:
            self._values["settings"] = settings

    @builtins.property
    def collection_endpoint(self) -> builtins.str:
        '''The endpoint for the collection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-index.html#cfn-opensearchserverless-index-collectionendpoint
        '''
        result = self._values.get("collection_endpoint")
        assert result is not None, "Required property 'collection_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_name(self) -> builtins.str:
        '''The name of the OpenSearch Serverless index.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-index.html#cfn-opensearchserverless-index-indexname
        '''
        result = self._values.get("index_name")
        assert result is not None, "Required property 'index_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mappings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIndex.MappingsProperty]]:
        '''Index mappings for the OpenSearch Serverless index.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-index.html#cfn-opensearchserverless-index-mappings
        '''
        result = self._values.get("mappings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIndex.MappingsProperty]], result)

    @builtins.property
    def settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIndex.IndexSettingsProperty]]:
        '''Index settings for the OpenSearch Serverless index.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-index.html#cfn-opensearchserverless-index-settings
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIndex.IndexSettingsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIndexProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLifecyclePolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnLifecyclePolicy",
):
    '''Creates a lifecyle policy to be applied to OpenSearch Serverless indexes.

    Lifecycle policies define the number of days or hours to retain the data on an OpenSearch Serverless index. For more information, see `Creating data lifecycle policies <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-create>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-lifecyclepolicy.html
    :cloudformationResource: AWS::OpenSearchServerless::LifecyclePolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opensearchserverless as opensearchserverless
        
        cfn_lifecycle_policy = opensearchserverless.CfnLifecyclePolicy(self, "MyCfnLifecyclePolicy",
            name="name",
            policy="policy",
            type="type",
        
            # the properties below are optional
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        policy: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the lifecycle policy.
        :param policy: The JSON policy document without any whitespaces.
        :param type: The type of lifecycle policy.
        :param description: The description of the lifecycle policy.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2b4914847f05bdf08e17005048ebb9904d2b6ed6657b54ce1cd05b975532b69)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLifecyclePolicyProps(
            name=name, policy=policy, type=type, description=description
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c78f8ec3b43e4960c131cba61e28ebe6cb28537e3d1b3ec0b3a6c0e6f186057)
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
            type_hints = typing.get_type_hints(_typecheckingstub__16ee685b93f73b8ba4242181166437089d5bff858d119adc3028a367278466e2)
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the lifecycle policy.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb4a4eb0b76c6d91faee7176a0f9015ab259d8776d1b156a0377259606821363)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        '''The JSON policy document without any whitespaces.'''
        return typing.cast(builtins.str, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dc5a59ad7f953682920ee2a549626a162f5c17d08a0b55a01701a1c5d2e68f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of lifecycle policy.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf5256649189217c6e468732c9804810a03866c558be69a399dbe3b582445734)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the lifecycle policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c81c3df41fd5687002fc21d059d65a24285a46691ea0b5927cb8bed64ce7b34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnLifecyclePolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "policy": "policy",
        "type": "type",
        "description": "description",
    },
)
class CfnLifecyclePolicyProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        policy: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnLifecyclePolicy``.

        :param name: The name of the lifecycle policy.
        :param policy: The JSON policy document without any whitespaces.
        :param type: The type of lifecycle policy.
        :param description: The description of the lifecycle policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-lifecyclepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opensearchserverless as opensearchserverless
            
            cfn_lifecycle_policy_props = opensearchserverless.CfnLifecyclePolicyProps(
                name="name",
                policy="policy",
                type="type",
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e73912f69bcf372f36058fe91d3360e53142205e8eb7f06190c7963adf67c8df)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "policy": policy,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the lifecycle policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-lifecyclepolicy.html#cfn-opensearchserverless-lifecyclepolicy-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy(self) -> builtins.str:
        '''The JSON policy document without any whitespaces.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-lifecyclepolicy.html#cfn-opensearchserverless-lifecyclepolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of lifecycle policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-lifecyclepolicy.html#cfn-opensearchserverless-lifecyclepolicy-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the lifecycle policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-lifecyclepolicy.html#cfn-opensearchserverless-lifecyclepolicy-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLifecyclePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSecurityConfig(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnSecurityConfig",
):
    '''Specifies a security configuration for OpenSearch Serverless.

    For more information, see `SAML authentication for Amazon OpenSearch Serverless <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securityconfig.html
    :cloudformationResource: AWS::OpenSearchServerless::SecurityConfig
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opensearchserverless as opensearchserverless
        
        cfn_security_config = opensearchserverless.CfnSecurityConfig(self, "MyCfnSecurityConfig",
            description="description",
            iam_identity_center_options=opensearchserverless.CfnSecurityConfig.IamIdentityCenterConfigOptionsProperty(
                instance_arn="instanceArn",
        
                # the properties below are optional
                application_arn="applicationArn",
                application_description="applicationDescription",
                application_name="applicationName",
                group_attribute="groupAttribute",
                user_attribute="userAttribute"
            ),
            name="name",
            saml_options=opensearchserverless.CfnSecurityConfig.SamlConfigOptionsProperty(
                metadata="metadata",
        
                # the properties below are optional
                group_attribute="groupAttribute",
                open_search_serverless_entity_id="openSearchServerlessEntityId",
                session_timeout=123,
                user_attribute="userAttribute"
            ),
            type="type"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        iam_identity_center_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSecurityConfig.IamIdentityCenterConfigOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        saml_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSecurityConfig.SamlConfigOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: The description of the security configuration.
        :param iam_identity_center_options: Describes IAM Identity Center options in the form of a key-value map.
        :param name: The name of the security configuration.
        :param saml_options: SAML options for the security configuration in the form of a key-value map.
        :param type: The type of security configuration. Currently the only option is ``saml`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed9d460597a09f666d8e08c01fd366ec5026a44848df01fe64ec8aa93e33a324)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSecurityConfigProps(
            description=description,
            iam_identity_center_options=iam_identity_center_options,
            name=name,
            saml_options=saml_options,
            type=type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38f5fc0cab059c4e5a2ba6a67ec4a99b2d4f71900706b4a9ffc575e8c1a23f5e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__083c1ea4e59851a4f8ad8f95d1f7dcb7f837bc36fd716be37a9b89e13dfc122c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIamIdentityCenterOptionsApplicationArn")
    def attr_iam_identity_center_options_application_arn(self) -> builtins.str:
        '''The ARN of the IAM Identity Center application used to integrate with OpenSearch Serverless.

        :cloudformationAttribute: IamIdentityCenterOptions.ApplicationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIamIdentityCenterOptionsApplicationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrIamIdentityCenterOptionsApplicationDescription")
    def attr_iam_identity_center_options_application_description(self) -> builtins.str:
        '''The description of the IAM Identity Center application used to integrate with OpenSearch Serverless.

        :cloudformationAttribute: IamIdentityCenterOptions.ApplicationDescription
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIamIdentityCenterOptionsApplicationDescription"))

    @builtins.property
    @jsii.member(jsii_name="attrIamIdentityCenterOptionsApplicationName")
    def attr_iam_identity_center_options_application_name(self) -> builtins.str:
        '''The name of the IAM Identity Center application used to integrate with OpenSearch Serverless.

        :cloudformationAttribute: IamIdentityCenterOptions.ApplicationName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIamIdentityCenterOptionsApplicationName"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier of the security configuration.

        For example, ``saml/123456789012/myprovider`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the security configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7b44e920b0f0e4d138dcb200c4536168d3965f24eed3226a4574e9279077710)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="iamIdentityCenterOptions")
    def iam_identity_center_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSecurityConfig.IamIdentityCenterConfigOptionsProperty"]]:
        '''Describes IAM Identity Center options in the form of a key-value map.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSecurityConfig.IamIdentityCenterConfigOptionsProperty"]], jsii.get(self, "iamIdentityCenterOptions"))

    @iam_identity_center_options.setter
    def iam_identity_center_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSecurityConfig.IamIdentityCenterConfigOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1158fc0f587cad32843a157af521fc2d669a0bc1f7c84c5e1dcd753237a9ca9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamIdentityCenterOptions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the security configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__940c51c2c1e431ab9c4c070593d5d7662323951afe83dc31ea2eafebbe59ac3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="samlOptions")
    def saml_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSecurityConfig.SamlConfigOptionsProperty"]]:
        '''SAML options for the security configuration in the form of a key-value map.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSecurityConfig.SamlConfigOptionsProperty"]], jsii.get(self, "samlOptions"))

    @saml_options.setter
    def saml_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSecurityConfig.SamlConfigOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__470a9a05248daf375f793933f5c035aad9eb0363381a3a0f6edb816e11340a12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samlOptions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of security configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80701c5b69899d2a5416bba637f7adf26445dcef6c813c58399037cc3941a3cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnSecurityConfig.IamIdentityCenterConfigOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_arn": "instanceArn",
            "application_arn": "applicationArn",
            "application_description": "applicationDescription",
            "application_name": "applicationName",
            "group_attribute": "groupAttribute",
            "user_attribute": "userAttribute",
        },
    )
    class IamIdentityCenterConfigOptionsProperty:
        def __init__(
            self,
            *,
            instance_arn: builtins.str,
            application_arn: typing.Optional[builtins.str] = None,
            application_description: typing.Optional[builtins.str] = None,
            application_name: typing.Optional[builtins.str] = None,
            group_attribute: typing.Optional[builtins.str] = None,
            user_attribute: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes IAM Identity Center options for an OpenSearch Serverless security configuration in the form of a key-value map.

            :param instance_arn: The ARN of the IAM Identity Center instance used to integrate with OpenSearch Serverless.
            :param application_arn: The ARN of the IAM Identity Center application used to integrate with OpenSearch Serverless.
            :param application_description: The description of the IAM Identity Center application used to integrate with OpenSearch Serverless.
            :param application_name: The name of the IAM Identity Center application used to integrate with OpenSearch Serverless.
            :param group_attribute: The group attribute for this IAM Identity Center integration. Defaults to ``GroupId`` .
            :param user_attribute: The user attribute for this IAM Identity Center integration. Defaults to ``UserId``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-iamidentitycenterconfigoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchserverless as opensearchserverless
                
                iam_identity_center_config_options_property = opensearchserverless.CfnSecurityConfig.IamIdentityCenterConfigOptionsProperty(
                    instance_arn="instanceArn",
                
                    # the properties below are optional
                    application_arn="applicationArn",
                    application_description="applicationDescription",
                    application_name="applicationName",
                    group_attribute="groupAttribute",
                    user_attribute="userAttribute"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7013bb6fc78d2c057c35211835fafe79d7d06fc41bdb98c07e46a37fd20caff9)
                check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
                check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
                check_type(argname="argument application_description", value=application_description, expected_type=type_hints["application_description"])
                check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
                check_type(argname="argument group_attribute", value=group_attribute, expected_type=type_hints["group_attribute"])
                check_type(argname="argument user_attribute", value=user_attribute, expected_type=type_hints["user_attribute"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_arn": instance_arn,
            }
            if application_arn is not None:
                self._values["application_arn"] = application_arn
            if application_description is not None:
                self._values["application_description"] = application_description
            if application_name is not None:
                self._values["application_name"] = application_name
            if group_attribute is not None:
                self._values["group_attribute"] = group_attribute
            if user_attribute is not None:
                self._values["user_attribute"] = user_attribute

        @builtins.property
        def instance_arn(self) -> builtins.str:
            '''The ARN of the IAM Identity Center instance used to integrate with OpenSearch Serverless.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-iamidentitycenterconfigoptions.html#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-instancearn
            '''
            result = self._values.get("instance_arn")
            assert result is not None, "Required property 'instance_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def application_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the IAM Identity Center application used to integrate with OpenSearch Serverless.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-iamidentitycenterconfigoptions.html#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-applicationarn
            '''
            result = self._values.get("application_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def application_description(self) -> typing.Optional[builtins.str]:
            '''The description of the IAM Identity Center application used to integrate with OpenSearch Serverless.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-iamidentitycenterconfigoptions.html#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-applicationdescription
            '''
            result = self._values.get("application_description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def application_name(self) -> typing.Optional[builtins.str]:
            '''The name of the IAM Identity Center application used to integrate with OpenSearch Serverless.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-iamidentitycenterconfigoptions.html#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-applicationname
            '''
            result = self._values.get("application_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def group_attribute(self) -> typing.Optional[builtins.str]:
            '''The group attribute for this IAM Identity Center integration.

            Defaults to ``GroupId`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-iamidentitycenterconfigoptions.html#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-groupattribute
            '''
            result = self._values.get("group_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_attribute(self) -> typing.Optional[builtins.str]:
            '''The user attribute for this IAM Identity Center integration.

            Defaults to ``UserId``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-iamidentitycenterconfigoptions.html#cfn-opensearchserverless-securityconfig-iamidentitycenterconfigoptions-userattribute
            '''
            result = self._values.get("user_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamIdentityCenterConfigOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnSecurityConfig.SamlConfigOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metadata": "metadata",
            "group_attribute": "groupAttribute",
            "open_search_serverless_entity_id": "openSearchServerlessEntityId",
            "session_timeout": "sessionTimeout",
            "user_attribute": "userAttribute",
        },
    )
    class SamlConfigOptionsProperty:
        def __init__(
            self,
            *,
            metadata: builtins.str,
            group_attribute: typing.Optional[builtins.str] = None,
            open_search_serverless_entity_id: typing.Optional[builtins.str] = None,
            session_timeout: typing.Optional[jsii.Number] = None,
            user_attribute: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes SAML options for an OpenSearch Serverless security configuration in the form of a key-value map.

            :param metadata: The XML IdP metadata file generated from your identity provider.
            :param group_attribute: The group attribute for this SAML integration.
            :param open_search_serverless_entity_id: Custom entity ID attribute to override the default entity ID for this SAML integration.
            :param session_timeout: The session timeout, in minutes. Default is 60 minutes (12 hours).
            :param user_attribute: A user attribute for this SAML integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-samlconfigoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearchserverless as opensearchserverless
                
                saml_config_options_property = opensearchserverless.CfnSecurityConfig.SamlConfigOptionsProperty(
                    metadata="metadata",
                
                    # the properties below are optional
                    group_attribute="groupAttribute",
                    open_search_serverless_entity_id="openSearchServerlessEntityId",
                    session_timeout=123,
                    user_attribute="userAttribute"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0390198d9b44e1b80737604ac5328dbfc7481d5b1ba8f915caa2e8c2a8028a9c)
                check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
                check_type(argname="argument group_attribute", value=group_attribute, expected_type=type_hints["group_attribute"])
                check_type(argname="argument open_search_serverless_entity_id", value=open_search_serverless_entity_id, expected_type=type_hints["open_search_serverless_entity_id"])
                check_type(argname="argument session_timeout", value=session_timeout, expected_type=type_hints["session_timeout"])
                check_type(argname="argument user_attribute", value=user_attribute, expected_type=type_hints["user_attribute"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "metadata": metadata,
            }
            if group_attribute is not None:
                self._values["group_attribute"] = group_attribute
            if open_search_serverless_entity_id is not None:
                self._values["open_search_serverless_entity_id"] = open_search_serverless_entity_id
            if session_timeout is not None:
                self._values["session_timeout"] = session_timeout
            if user_attribute is not None:
                self._values["user_attribute"] = user_attribute

        @builtins.property
        def metadata(self) -> builtins.str:
            '''The XML IdP metadata file generated from your identity provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-samlconfigoptions.html#cfn-opensearchserverless-securityconfig-samlconfigoptions-metadata
            '''
            result = self._values.get("metadata")
            assert result is not None, "Required property 'metadata' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def group_attribute(self) -> typing.Optional[builtins.str]:
            '''The group attribute for this SAML integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-samlconfigoptions.html#cfn-opensearchserverless-securityconfig-samlconfigoptions-groupattribute
            '''
            result = self._values.get("group_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def open_search_serverless_entity_id(self) -> typing.Optional[builtins.str]:
            '''Custom entity ID attribute to override the default entity ID for this SAML integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-samlconfigoptions.html#cfn-opensearchserverless-securityconfig-samlconfigoptions-opensearchserverlessentityid
            '''
            result = self._values.get("open_search_serverless_entity_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def session_timeout(self) -> typing.Optional[jsii.Number]:
            '''The session timeout, in minutes.

            Default is 60 minutes (12 hours).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-samlconfigoptions.html#cfn-opensearchserverless-securityconfig-samlconfigoptions-sessiontimeout
            '''
            result = self._values.get("session_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def user_attribute(self) -> typing.Optional[builtins.str]:
            '''A user attribute for this SAML integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-samlconfigoptions.html#cfn-opensearchserverless-securityconfig-samlconfigoptions-userattribute
            '''
            result = self._values.get("user_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SamlConfigOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnSecurityConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "iam_identity_center_options": "iamIdentityCenterOptions",
        "name": "name",
        "saml_options": "samlOptions",
        "type": "type",
    },
)
class CfnSecurityConfigProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        iam_identity_center_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfig.IamIdentityCenterConfigOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        saml_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfig.SamlConfigOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSecurityConfig``.

        :param description: The description of the security configuration.
        :param iam_identity_center_options: Describes IAM Identity Center options in the form of a key-value map.
        :param name: The name of the security configuration.
        :param saml_options: SAML options for the security configuration in the form of a key-value map.
        :param type: The type of security configuration. Currently the only option is ``saml`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securityconfig.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opensearchserverless as opensearchserverless
            
            cfn_security_config_props = opensearchserverless.CfnSecurityConfigProps(
                description="description",
                iam_identity_center_options=opensearchserverless.CfnSecurityConfig.IamIdentityCenterConfigOptionsProperty(
                    instance_arn="instanceArn",
            
                    # the properties below are optional
                    application_arn="applicationArn",
                    application_description="applicationDescription",
                    application_name="applicationName",
                    group_attribute="groupAttribute",
                    user_attribute="userAttribute"
                ),
                name="name",
                saml_options=opensearchserverless.CfnSecurityConfig.SamlConfigOptionsProperty(
                    metadata="metadata",
            
                    # the properties below are optional
                    group_attribute="groupAttribute",
                    open_search_serverless_entity_id="openSearchServerlessEntityId",
                    session_timeout=123,
                    user_attribute="userAttribute"
                ),
                type="type"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83172f8fcf5e40df2e2a8ddc136c744969aad86c37d45de37b6d75f0dc154be4)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument iam_identity_center_options", value=iam_identity_center_options, expected_type=type_hints["iam_identity_center_options"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument saml_options", value=saml_options, expected_type=type_hints["saml_options"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if iam_identity_center_options is not None:
            self._values["iam_identity_center_options"] = iam_identity_center_options
        if name is not None:
            self._values["name"] = name
        if saml_options is not None:
            self._values["saml_options"] = saml_options
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the security configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securityconfig.html#cfn-opensearchserverless-securityconfig-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_identity_center_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSecurityConfig.IamIdentityCenterConfigOptionsProperty]]:
        '''Describes IAM Identity Center options in the form of a key-value map.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securityconfig.html#cfn-opensearchserverless-securityconfig-iamidentitycenteroptions
        '''
        result = self._values.get("iam_identity_center_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSecurityConfig.IamIdentityCenterConfigOptionsProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the security configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securityconfig.html#cfn-opensearchserverless-securityconfig-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def saml_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSecurityConfig.SamlConfigOptionsProperty]]:
        '''SAML options for the security configuration in the form of a key-value map.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securityconfig.html#cfn-opensearchserverless-securityconfig-samloptions
        '''
        result = self._values.get("saml_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSecurityConfig.SamlConfigOptionsProperty]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of security configuration.

        Currently the only option is ``saml`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securityconfig.html#cfn-opensearchserverless-securityconfig-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSecurityConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSecurityPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnSecurityPolicy",
):
    '''Creates an encryption or network policy to be used by one or more OpenSearch Serverless collections.

    Network policies specify access to a collection and its OpenSearch Dashboards endpoint from public networks or specific VPC endpoints. For more information, see `Network access for Amazon OpenSearch Serverless <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html>`_ .

    Encryption policies specify a KMS encryption key to assign to particular collections. For more information, see `Encryption at rest for Amazon OpenSearch Serverless <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securitypolicy.html
    :cloudformationResource: AWS::OpenSearchServerless::SecurityPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opensearchserverless as opensearchserverless
        
        cfn_security_policy = opensearchserverless.CfnSecurityPolicy(self, "MyCfnSecurityPolicy",
            name="name",
            policy="policy",
            type="type",
        
            # the properties below are optional
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        policy: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the policy.
        :param policy: The JSON policy document without any whitespaces.
        :param type: The type of security policy. Can be either ``encryption`` or ``network`` .
        :param description: The description of the security policy.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d59762ee8817ade49618bf2f3f983fdef4c91ba0b7b556420f82eddfb0b1816)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSecurityPolicyProps(
            name=name, policy=policy, type=type, description=description
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__082186cf455a2980e2761e5de897ccbc69e4eb353276a694ba5eaed492d1c355)
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
            type_hints = typing.get_type_hints(_typecheckingstub__94213ecca06ef4d1b31be275656e0580546ffc23edd245cd11f0d9478cc73a0f)
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the policy.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b316bc27ccc1ef30b97da9a17a74f0ff2bff96451af36684e44c9f423c3e2570)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        '''The JSON policy document without any whitespaces.'''
        return typing.cast(builtins.str, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5493100628b14c83d55bc872a41a8cf9eaea303260b8dc55ee15cecf3f8f70c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of security policy.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1da1adb4e533469b0a999434c11dbe4890dc3a1f9016c7411f9393c642243f52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the security policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32e52e449f522d03728147da62ce5f50c6d6fbd70bb94d13ddb359a01e62346b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnSecurityPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "policy": "policy",
        "type": "type",
        "description": "description",
    },
)
class CfnSecurityPolicyProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        policy: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSecurityPolicy``.

        :param name: The name of the policy.
        :param policy: The JSON policy document without any whitespaces.
        :param type: The type of security policy. Can be either ``encryption`` or ``network`` .
        :param description: The description of the security policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securitypolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opensearchserverless as opensearchserverless
            
            cfn_security_policy_props = opensearchserverless.CfnSecurityPolicyProps(
                name="name",
                policy="policy",
                type="type",
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4075edd6277d95d95112af6e1299774fad3d68ddeaf766c63e97d6deae2b5216)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "policy": policy,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securitypolicy.html#cfn-opensearchserverless-securitypolicy-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy(self) -> builtins.str:
        '''The JSON policy document without any whitespaces.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securitypolicy.html#cfn-opensearchserverless-securitypolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of security policy.

        Can be either ``encryption`` or ``network`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securitypolicy.html#cfn-opensearchserverless-securitypolicy-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the security policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securitypolicy.html#cfn-opensearchserverless-securitypolicy-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSecurityPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnVpcEndpoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnVpcEndpoint",
):
    '''Creates an OpenSearch Serverless-managed interface VPC endpoint.

    For more information, see `Access Amazon OpenSearch Serverless using an interface endpoint <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-vpcendpoint.html
    :cloudformationResource: AWS::OpenSearchServerless::VpcEndpoint
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opensearchserverless as opensearchserverless
        
        cfn_vpc_endpoint = opensearchserverless.CfnVpcEndpoint(self, "MyCfnVpcEndpoint",
            name="name",
            subnet_ids=["subnetIds"],
            vpc_id="vpcId",
        
            # the properties below are optional
            security_group_ids=["securityGroupIds"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the endpoint.
        :param subnet_ids: The ID of the subnets from which you access OpenSearch Serverless.
        :param vpc_id: The ID of the VPC from which you access OpenSearch Serverless.
        :param security_group_ids: The unique identifiers of the security groups that define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbe678d204c3b8154a4eab3294ad9caae2eddc54ea43a540534d5f5624ad1d38)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVpcEndpointProps(
            name=name,
            subnet_ids=subnet_ids,
            vpc_id=vpc_id,
            security_group_ids=security_group_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec366f8ee866b62daafbb0ed59aad63cbce0b37c6d7cda29a3f04ad886403435)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd1080f5a19985973434c3c31bd16ed1d4e440700fa1532707bb82e42894884c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier of the endpoint.

        For example, ``vpce-050f79086ee71ac05`` .

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
        '''The name of the endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed8fdc67240218bbfca2dacf601018706cd414f07f91be7da8354ca5d461fc33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''The ID of the subnets from which you access OpenSearch Serverless.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b92741da8601cb0520b9fc2a44353cb2f5a8ffcff1e41c81daf305e4e57ae3bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''The ID of the VPC from which you access OpenSearch Serverless.'''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51ceb4d899497efe9654e160fb2cbb074280677360f698cdb3bbd71b621a292c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The unique identifiers of the security groups that define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__129e2ed568043eda0de359b0547f1ce5769e90a17a23c8ec9e16b8fb0b424f23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearchserverless.CfnVpcEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "subnet_ids": "subnetIds",
        "vpc_id": "vpcId",
        "security_group_ids": "securityGroupIds",
    },
)
class CfnVpcEndpointProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVpcEndpoint``.

        :param name: The name of the endpoint.
        :param subnet_ids: The ID of the subnets from which you access OpenSearch Serverless.
        :param vpc_id: The ID of the VPC from which you access OpenSearch Serverless.
        :param security_group_ids: The unique identifiers of the security groups that define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-vpcendpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opensearchserverless as opensearchserverless
            
            cfn_vpc_endpoint_props = opensearchserverless.CfnVpcEndpointProps(
                name="name",
                subnet_ids=["subnetIds"],
                vpc_id="vpcId",
            
                # the properties below are optional
                security_group_ids=["securityGroupIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e4b9618641af3075893df923c3e35190dd8ae1fdea8503917862efecb66990a)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "subnet_ids": subnet_ids,
            "vpc_id": vpc_id,
        }
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-vpcendpoint.html#cfn-opensearchserverless-vpcendpoint-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''The ID of the subnets from which you access OpenSearch Serverless.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-vpcendpoint.html#cfn-opensearchserverless-vpcendpoint-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The ID of the VPC from which you access OpenSearch Serverless.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-vpcendpoint.html#cfn-opensearchserverless-vpcendpoint-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The unique identifiers of the security groups that define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-vpcendpoint.html#cfn-opensearchserverless-vpcendpoint-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAccessPolicy",
    "CfnAccessPolicyProps",
    "CfnCollection",
    "CfnCollectionProps",
    "CfnIndex",
    "CfnIndexProps",
    "CfnLifecyclePolicy",
    "CfnLifecyclePolicyProps",
    "CfnSecurityConfig",
    "CfnSecurityConfigProps",
    "CfnSecurityPolicy",
    "CfnSecurityPolicyProps",
    "CfnVpcEndpoint",
    "CfnVpcEndpointProps",
]

publication.publish()

def _typecheckingstub__0f3695018b497271b2884c3d90b44513c0e4644d1625baefd3c5f2880a1223da(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    policy: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21888f21364bcb4177baf2ccd610dc59283ab52bb27386322330ad2d3381e0de(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e00c49a5052cb7959a45d9347290149a3138d4d622e0aca3118485fae647010e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54b3786c37ee33848fa7b21ba500dd1920002dea0fe9ec5bd1440f81686f4638(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7da9c131bb5f7ae3527dc4b4934b48aac60a8f0b88b51d40a50c13df36532b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d72ffab9810a9603f58d764e6a8f7a88c9198aea6ffc88f14cc048f6834586e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__768c8582758ca3add7a55a7e6ef420b56cc700d0f10d913632558c56f7cb16b4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fd3a5bd693a196541a3a98339eef4fd1a25680f2e37fa2c50932ab018651a65(
    *,
    name: builtins.str,
    policy: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14f72b773d506ce15b59731aeb24f2f4a877a32d31af6ebf57a32ce707e0cb16(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    standby_replicas: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c88f558406d9de750b6a01e95a1eade398fef738592cdd78170d3f472b7ff7e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d48674433624514f2cfa361d4ec0903ae028ce45853117cd29b576baa3f723aa(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cdb6f4e81b00df109517f1c4b90835cef7bd07218c9f75976d033888175c41c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85980a9398a34a6ff3d72193d32c1438940d0a83c1d83a04ccfa6ebaaccb9612(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54a6dd56a4e746b5f7a24ddd10fa03aa9a0a5c238a5085c7b0ee67caee9db79b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cfcacecc11d4e30df3a59ae6680ab93be461bc979a2e413a2a77eab2575087a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f407bc0eeb99c42f4a9d1d97573b8b10069685ea3e596d162939418b9ddce0ab(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc3a9fff4dd66b4fe4e69ca639823a978df78a02743764020419d9b37d4f540e(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    standby_replicas: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a029f2a84e6e81eb77a837c5b057c54ae69d5f1ddda222ff52881f5d0f352fea(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    collection_endpoint: builtins.str,
    index_name: builtins.str,
    mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.MappingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.IndexSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72216bdab3dcf25c4879e6aed5404e682fbe3d1fd832814ab5bb77a77f3258c5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f26c002ce18fad76e8c679969cbf05ddf77445cb22669f37a41940c49638cba7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84fc2fc583ee69579f5b7f33f8afc9e23bef75f86f99a2b3e46cf07707ab26bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a1f9a03417bd926596068b7f503b95c60abebc00e23689dd4dff83cf372576d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01f2947a1782e9f60537bf751bb6fc12efd44df6bc7c2efab931f974a2048326(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIndex.MappingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fa35242932bdcac5598aa8d9552388d7e12b08b01413c30a72c824979d9345c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIndex.IndexSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a85f85e738bf9023ab824f21e3c4b9a2f4e256a148a314ec2c2b5a47bb64698(
    *,
    knn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    knn_algo_param_ef_search: typing.Optional[jsii.Number] = None,
    refresh_interval: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2062be5b5132fc74ed29db0c10805e0731b612aad10b8ddbab3dda1eac563bc0(
    *,
    index: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.IndexProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5bb392b8c065f198a0fe7fd6e0fa2156f493990b76e0fee04edb929794b7223(
    *,
    properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.PropertyMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f32a7c2cc9cc53a405856608b840b3cd657cad90afeb4b25d6577b3e1573b35(
    *,
    engine: builtins.str,
    name: builtins.str,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.ParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    space_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af09bec36bc7cc06df73ca75b408b7f4402421f3feaaa06806d3ec93cfc2435d(
    *,
    ef_construction: typing.Optional[jsii.Number] = None,
    m: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f7c10818297058609492c7bc5b994ff55948eef9013ef34074e5e42d61fd371(
    *,
    type: builtins.str,
    dimension: typing.Optional[jsii.Number] = None,
    index: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    method: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.MethodProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.PropertyMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__663cdeaeaa67ae562243597848e75d79ee7310523ecd791e0c37af19d4197d1a(
    *,
    collection_endpoint: builtins.str,
    index_name: builtins.str,
    mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.MappingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.IndexSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2b4914847f05bdf08e17005048ebb9904d2b6ed6657b54ce1cd05b975532b69(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    policy: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c78f8ec3b43e4960c131cba61e28ebe6cb28537e3d1b3ec0b3a6c0e6f186057(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16ee685b93f73b8ba4242181166437089d5bff858d119adc3028a367278466e2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb4a4eb0b76c6d91faee7176a0f9015ab259d8776d1b156a0377259606821363(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dc5a59ad7f953682920ee2a549626a162f5c17d08a0b55a01701a1c5d2e68f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf5256649189217c6e468732c9804810a03866c558be69a399dbe3b582445734(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c81c3df41fd5687002fc21d059d65a24285a46691ea0b5927cb8bed64ce7b34(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e73912f69bcf372f36058fe91d3360e53142205e8eb7f06190c7963adf67c8df(
    *,
    name: builtins.str,
    policy: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed9d460597a09f666d8e08c01fd366ec5026a44848df01fe64ec8aa93e33a324(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    iam_identity_center_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfig.IamIdentityCenterConfigOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    saml_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfig.SamlConfigOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38f5fc0cab059c4e5a2ba6a67ec4a99b2d4f71900706b4a9ffc575e8c1a23f5e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__083c1ea4e59851a4f8ad8f95d1f7dcb7f837bc36fd716be37a9b89e13dfc122c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7b44e920b0f0e4d138dcb200c4536168d3965f24eed3226a4574e9279077710(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1158fc0f587cad32843a157af521fc2d669a0bc1f7c84c5e1dcd753237a9ca9a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSecurityConfig.IamIdentityCenterConfigOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__940c51c2c1e431ab9c4c070593d5d7662323951afe83dc31ea2eafebbe59ac3f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__470a9a05248daf375f793933f5c035aad9eb0363381a3a0f6edb816e11340a12(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSecurityConfig.SamlConfigOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80701c5b69899d2a5416bba637f7adf26445dcef6c813c58399037cc3941a3cf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7013bb6fc78d2c057c35211835fafe79d7d06fc41bdb98c07e46a37fd20caff9(
    *,
    instance_arn: builtins.str,
    application_arn: typing.Optional[builtins.str] = None,
    application_description: typing.Optional[builtins.str] = None,
    application_name: typing.Optional[builtins.str] = None,
    group_attribute: typing.Optional[builtins.str] = None,
    user_attribute: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0390198d9b44e1b80737604ac5328dbfc7481d5b1ba8f915caa2e8c2a8028a9c(
    *,
    metadata: builtins.str,
    group_attribute: typing.Optional[builtins.str] = None,
    open_search_serverless_entity_id: typing.Optional[builtins.str] = None,
    session_timeout: typing.Optional[jsii.Number] = None,
    user_attribute: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83172f8fcf5e40df2e2a8ddc136c744969aad86c37d45de37b6d75f0dc154be4(
    *,
    description: typing.Optional[builtins.str] = None,
    iam_identity_center_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfig.IamIdentityCenterConfigOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    saml_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfig.SamlConfigOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d59762ee8817ade49618bf2f3f983fdef4c91ba0b7b556420f82eddfb0b1816(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    policy: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__082186cf455a2980e2761e5de897ccbc69e4eb353276a694ba5eaed492d1c355(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94213ecca06ef4d1b31be275656e0580546ffc23edd245cd11f0d9478cc73a0f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b316bc27ccc1ef30b97da9a17a74f0ff2bff96451af36684e44c9f423c3e2570(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5493100628b14c83d55bc872a41a8cf9eaea303260b8dc55ee15cecf3f8f70c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1da1adb4e533469b0a999434c11dbe4890dc3a1f9016c7411f9393c642243f52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32e52e449f522d03728147da62ce5f50c6d6fbd70bb94d13ddb359a01e62346b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4075edd6277d95d95112af6e1299774fad3d68ddeaf766c63e97d6deae2b5216(
    *,
    name: builtins.str,
    policy: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbe678d204c3b8154a4eab3294ad9caae2eddc54ea43a540534d5f5624ad1d38(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec366f8ee866b62daafbb0ed59aad63cbce0b37c6d7cda29a3f04ad886403435(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd1080f5a19985973434c3c31bd16ed1d4e440700fa1532707bb82e42894884c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed8fdc67240218bbfca2dacf601018706cd414f07f91be7da8354ca5d461fc33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b92741da8601cb0520b9fc2a44353cb2f5a8ffcff1e41c81daf305e4e57ae3bb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51ceb4d899497efe9654e160fb2cbb074280677360f698cdb3bbd71b621a292c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__129e2ed568043eda0de359b0547f1ce5769e90a17a23c8ec9e16b8fb0b424f23(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e4b9618641af3075893df923c3e35190dd8ae1fdea8503917862efecb66990a(
    *,
    name: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
