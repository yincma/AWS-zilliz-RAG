r'''
# Amazon Cognito Identity Pool Construct Library

[Amazon Cognito Identity Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html) enable you to grant your users access to other AWS services.

Identity Pools are one of the two main components of [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html), which provides authentication, authorization, and
user management for your web and mobile apps. Your users can sign in through a a trusted identity provider, like a user
pool or a SAML 2.0 service, as well as with third party providers such as Facebook, Amazon, Google or Apple.

The other main component in Amazon Cognito is [user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html). User Pools are user directories that provide sign-up and
sign-in options for your app users.

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
from aws_cdk.aws_cognito_identitypool import IdentityPool, UserPoolAuthenticationProvider
```

## Table of Contents

* [Identity Pools](#identity-pools)

  * [Authenticated and Unauthenticated Identities](#authenticated-and-unauthenticated-identities)
  * [Authentication Providers](#authentication-providers)

    * [User Pool Authentication Provider](#user-pool-authentication-provider)
    * [Server Side Token Check](#server-side-token-check)
    * [Associating an External Provider Directly](#associating-an-external-provider-directly)
    * [OpenIdConnect and Saml](#openid-connect-and-saml)
    * [Custom Providers](#custom-providers)
  * [Role Mapping](#role-mapping)

    * [Provider Urls](#provider-urls)
  * [Authentication Flow](#authentication-flow)
  * [Cognito Sync](#cognito-sync)
  * [Importing Identity Pools](#importing-identity-pools)

## Identity Pools

Identity pools provide temporary AWS credentials for users who are guests (unauthenticated) and for users who have
authenticated by presenting a token from another identity provider. An identity pool is a store of user identity data
specific to an account.

Identity pools can be used in conjunction with Cognito User Pools or by accessing external federated identity providers
directly. Learn more at [Amazon Cognito Identity Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html).

### Authenticated and Unauthenticated Identities

Identity pools define two types of identities: authenticated(`user`) and unauthenticated (`guest`). Every identity in
an identity pool is either authenticated or unauthenticated. Each identity pool has a default role for authenticated
identities, and a default role for unauthenticated identities. Absent other overriding rules (see below), these are the
roles that will be assumed by the corresponding users in the authentication process.

A basic Identity Pool with minimal configuration has no required props, with default authenticated (user) and
unauthenticated (guest) roles applied to the identity pool:

```python
IdentityPool(self, "myIdentityPool")
```

By default, both the authenticated and unauthenticated roles will have no permissions attached. When granting permissions,
you should ensure that you are granting the least privileged permissions required for your use case. Grant permissions
to roles using the public `authenticatedRole` and `unauthenticatedRole` properties:

```python
import aws_cdk.aws_dynamodb as dynamodb
# table: dynamodb.Table


identity_pool = IdentityPool(self, "myIdentityPool")

# Grant permissions to authenticated users
table.grant_read_write_data(identity_pool.authenticated_role)
# Grant permissions to unauthenticated guest users
table.grant_read_data(identity_pool.unauthenticated_role)

# Or add policy statements straight to the role
identity_pool.authenticated_role.add_to_principal_policy(iam.PolicyStatement(
    effect=iam.Effect.ALLOW,
    actions=["dynamodb:UpdateItem"],
    resources=[table.table_arn]
))
```

The default roles can also be supplied in `IdentityPoolProps`:

```python
stack = Stack()
authenticated_role = iam.Role(self, "authRole",
    assumed_by=iam.ServicePrincipal("service.amazonaws.com")
)
unauthenticated_role = iam.Role(self, "unauthRole",
    assumed_by=iam.ServicePrincipal("service.amazonaws.com")
)
identity_pool = IdentityPool(self, "TestIdentityPoolActions",
    authenticated_role=authenticated_role,
    unauthenticated_role=unauthenticated_role
)
```

### Authentication Providers

Authenticated identities belong to users who are authenticated by a public login provider (Amazon Cognito user pools,
Login with Amazon, Sign in with Apple, Facebook, Google, SAML, or any OpenID Connect Providers) or a developer provider
(your own backend authentication process).

[Authentication providers](https://docs.aws.amazon.com/cognito/latest/developerguide/external-identity-providers.html) can be associated with an Identity Pool by first associating them with a Cognito User Pool or by
associating the provider directly with the identity pool.

#### User Pool Authentication Provider

In order to attach a user pool to an identity pool as an authentication provider, the identity pool needs properties
from both the user pool and the user pool client. For this reason identity pools use a `UserPoolAuthenticationProvider`
to gather the necessary properties from the user pool constructs.

```python
user_pool = cognito.UserPool(self, "Pool")

IdentityPool(self, "myidentitypool",
    identity_pool_name="myidentitypool",
    authentication_providers=IdentityPoolAuthenticationProviders(
        user_pools=[UserPoolAuthenticationProvider(user_pool=user_pool)]
    )
)
```

User pools can also be associated with an identity pool after instantiation. The Identity Pool's `addUserPoolAuthentication` method
returns the User Pool Client that has been created:

```python
# identity_pool: IdentityPool

user_pool = cognito.UserPool(self, "Pool")
user_pool_client = identity_pool.add_user_pool_authentication(UserPoolAuthenticationProvider(
    user_pool=user_pool
))
```

#### Server Side Token Check

With the `IdentityPool` CDK Construct, by default the pool is configured to check with the integrated user pools to
make sure that the user has not been globally signed out or deleted before the identity pool provides an OIDC token or
AWS credentials for the user.

If the user is signed out or deleted, the identity pool will return a 400 Not Authorized error. This setting can be
disabled, however, in several ways.

Setting `disableServerSideTokenCheck` to true will change the default behavior to no server side token check. Learn
more [here](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_CognitoIdentityProvider.html#CognitoIdentity-Type-CognitoIdentityProvider-ServerSideTokenCheck):

```python
# identity_pool: IdentityPool

user_pool = cognito.UserPool(self, "Pool")
identity_pool.add_user_pool_authentication(UserPoolAuthenticationProvider(
    user_pool=user_pool,
    disable_server_side_token_check=True
))
```

#### Associating an External Provider Directly

One or more [external identity providers](https://docs.aws.amazon.com/cognito/latest/developerguide/external-identity-providers.html) can be associated with an identity pool directly using
`authenticationProviders`:

```python
IdentityPool(self, "myidentitypool",
    identity_pool_name="myidentitypool",
    authentication_providers=IdentityPoolAuthenticationProviders(
        amazon=IdentityPoolAmazonLoginProvider(
            app_id="amzn1.application.12312k3j234j13rjiwuenf"
        ),
        facebook=IdentityPoolFacebookLoginProvider(
            app_id="1234567890123"
        ),
        google=IdentityPoolGoogleLoginProvider(
            client_id="12345678012.apps.googleusercontent.com"
        ),
        apple=IdentityPoolAppleLoginProvider(
            services_id="com.myappleapp.auth"
        ),
        twitter=IdentityPoolTwitterLoginProvider(
            consumer_key="my-twitter-id",
            consumer_secret="my-twitter-secret"
        )
    )
)
```

To associate more than one provider of the same type with the identity pool, use User
Pools, OpenIdConnect, or SAML. Only one provider per external service can be attached directly to the identity pool.

#### OpenId Connect and Saml

[OpenID Connect](https://docs.aws.amazon.com/cognito/latest/developerguide/open-id.html) is an open standard for
authentication that is supported by a number of login providers. Amazon Cognito supports linking of identities with
OpenID Connect providers that are configured through [AWS Identity and Access Management](http://aws.amazon.com/iam/).

An identity provider that supports [Security Assertion Markup Language 2.0 (SAML 2.0)](https://docs.aws.amazon.com/cognito/latest/developerguide/saml-identity-provider.html) can be used to provide a simple
onboarding flow for users. The SAML-supporting identity provider specifies the IAM roles that can be assumed by users
so that different users can be granted different sets of permissions. Associating an OpenId Connect or Saml provider
with an identity pool:

```python
# open_id_connect_provider: iam.OpenIdConnectProvider
# saml_provider: iam.SamlProvider


IdentityPool(self, "myidentitypool",
    identity_pool_name="myidentitypool",
    authentication_providers=IdentityPoolAuthenticationProviders(
        open_id_connect_providers=[open_id_connect_provider],
        saml_providers=[saml_provider]
    )
)
```

#### Custom Providers

The identity pool's behavior can be customized further using custom [developer authenticated identities](https://docs.aws.amazon.com/cognito/latest/developerguide/developer-authenticated-identities.html).
With developer authenticated identities, users can be registered and authenticated via an existing authentication
process while still using Amazon Cognito to synchronize user data and access AWS resources.

Like the supported external providers, though, only one custom provider can be directly associated with the identity
pool.

```python
# open_id_connect_provider: iam.OpenIdConnectProvider

IdentityPool(self, "myidentitypool",
    identity_pool_name="myidentitypool",
    authentication_providers=IdentityPoolAuthenticationProviders(
        google=IdentityPoolGoogleLoginProvider(
            client_id="12345678012.apps.googleusercontent.com"
        ),
        open_id_connect_providers=[open_id_connect_provider],
        custom_provider="my-custom-provider.example.com"
    )
)
```

### Role Mapping

In addition to setting default roles for authenticated and unauthenticated users, identity pools can also be used to
define rules to choose the role for each user based on claims in the user's ID token by using Role Mapping. When using
role mapping, it's important to be aware of some of the permissions the role will need, and that the least privileged
roles necessary are given for your specific use case. An in depth
review of roles and role mapping can be found [here](https://docs.aws.amazon.com/cognito/latest/developerguide/role-based-access-control.html).

Using a [token-based approach](https://docs.aws.amazon.com/cognito/latest/developerguide/role-based-access-control.html#using-tokens-to-assign-roles-to-users) to role mapping will allow mapped roles to be passed through the `cognito:roles` or
`cognito:preferred_role` claims from the identity provider:

```python
from aws_cdk.aws_cognito_identitypool import IdentityPoolProviderUrl


IdentityPool(self, "myidentitypool",
    identity_pool_name="myidentitypool",
    role_mappings=[IdentityPoolRoleMapping(
        provider_url=IdentityPoolProviderUrl.AMAZON,
        use_token=True
    )]
)
```

Using a rule-based approach to role mapping allows roles to be assigned based on custom claims passed from the identity provider:

```python
from aws_cdk.aws_cognito_identitypool import IdentityPoolProviderUrl, RoleMappingMatchType

# admin_role: iam.Role
# non_admin_role: iam.Role

IdentityPool(self, "myidentitypool",
    identity_pool_name="myidentitypool",
    # Assign specific roles to users based on whether or not the custom admin claim is passed from the identity provider
    role_mappings=[IdentityPoolRoleMapping(
        provider_url=IdentityPoolProviderUrl.AMAZON,
        rules=[RoleMappingRule(
            claim="custom:admin",
            claim_value="admin",
            mapped_role=admin_role
        ), RoleMappingRule(
            claim="custom:admin",
            claim_value="admin",
            match_type=RoleMappingMatchType.NOTEQUAL,
            mapped_role=non_admin_role
        )
        ]
    )]
)
```

#### Provider Urls

Role mappings must be associated with the url of an Identity Provider which can be supplied
`IdentityPoolProviderUrl`. Supported Providers have static Urls that can be used:

```python
from aws_cdk.aws_cognito_identitypool import IdentityPoolProviderUrl


IdentityPool(self, "myidentitypool",
    identity_pool_name="myidentitypool",
    role_mappings=[IdentityPoolRoleMapping(
        provider_url=IdentityPoolProviderUrl.FACEBOOK,
        use_token=True
    )]
)
```

For identity providers that don't have static Urls, a custom Url can be supplied:

```python
from aws_cdk.aws_cognito_identitypool import IdentityPoolProviderUrl


IdentityPool(self, "myidentitypool",
    identity_pool_name="myidentitypool",
    role_mappings=[IdentityPoolRoleMapping(
        provider_url=IdentityPoolProviderUrl.custom("my-custom-provider.com"),
        use_token=True
    )
    ]
)
```

If a provider URL is a CDK Token, as it will be if you are trying to use a previously defined Cognito User Pool, you will need to also provide a mappingKey.
This is because by default, the key in the Cloudformation role mapping hash is the providerUrl, and Cloudformation map keys must be concrete strings, they
cannot be references. For example:

```python
from aws_cdk.aws_cognito import UserPool, UserPoolClient
from aws_cdk.aws_cognito_identitypool import IdentityPoolProviderUrl

# user_pool: UserPool
# user_pool_client: UserPoolClient

IdentityPool(self, "myidentitypool",
    identity_pool_name="myidentitypool",
    role_mappings=[IdentityPoolRoleMapping(
        mapping_key="cognito",
        provider_url=IdentityPoolProviderUrl.user_pool(user_pool, user_pool_client),
        use_token=True
    )]
)
```

See [here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rolemapping.html#cfn-cognito-identitypoolroleattachment-rolemapping-identityprovider) for more information.

### Authentication Flow

Identity Pool [Authentication Flow](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html) defaults to the enhanced, simplified flow. The Classic (basic) Authentication Flow
can also be implemented using `allowClassicFlow`:

```python
IdentityPool(self, "myidentitypool",
    identity_pool_name="myidentitypool",
    allow_classic_flow=True
)
```

### Cognito Sync

It's now recommended to integrate [AWS AppSync](https://aws.amazon.com/appsync/) for synchronizing app data across devices, so
Cognito Sync features like `PushSync`, `CognitoEvents`, and `CognitoStreams` are not a part of `IdentityPool`. More
information can be found [here](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sync.html).

### Importing Identity Pools

You can import existing identity pools into your stack using Identity Pool static methods with the Identity Pool Id or
Arn:

```python
IdentityPool.from_identity_pool_id(self, "my-imported-identity-pool", "us-east-1:dj2823ryiwuhef937")
IdentityPool.from_identity_pool_arn(self, "my-imported-identity-pool", "arn:aws:cognito-identity:us-east-1:123456789012:identitypool/us-east-1:dj2823ryiwuhef937")
```
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
from .. import IResource as _IResource_c80c4260, Resource as _Resource_45bc6135
from ..aws_cognito import (
    CfnIdentityPoolRoleAttachment as _CfnIdentityPoolRoleAttachment_6213757a,
    IUserPool as _IUserPool_1f1029e2,
    IUserPoolClient as _IUserPoolClient_75623ba4,
)
from ..aws_iam import (
    IOpenIdConnectProvider as _IOpenIdConnectProvider_203f0793,
    IRole as _IRole_235f5d8e,
    ISamlProvider as _ISamlProvider_63f03582,
)


@jsii.interface(jsii_type="aws-cdk-lib.aws_cognito_identitypool.IIdentityPool")
class IIdentityPool(_IResource_c80c4260, typing_extensions.Protocol):
    '''Represents a Cognito Identity Pool.'''

    @builtins.property
    @jsii.member(jsii_name="identityPoolArn")
    def identity_pool_arn(self) -> builtins.str:
        '''The ARN of the Identity Pool.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="identityPoolId")
    def identity_pool_id(self) -> builtins.str:
        '''The ID of the Identity Pool in the format REGION:GUID.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="identityPoolName")
    def identity_pool_name(self) -> builtins.str:
        '''Name of the Identity Pool.

        :attribute: true
        '''
        ...


class _IIdentityPoolProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Represents a Cognito Identity Pool.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_cognito_identitypool.IIdentityPool"

    @builtins.property
    @jsii.member(jsii_name="identityPoolArn")
    def identity_pool_arn(self) -> builtins.str:
        '''The ARN of the Identity Pool.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "identityPoolArn"))

    @builtins.property
    @jsii.member(jsii_name="identityPoolId")
    def identity_pool_id(self) -> builtins.str:
        '''The ID of the Identity Pool in the format REGION:GUID.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "identityPoolId"))

    @builtins.property
    @jsii.member(jsii_name="identityPoolName")
    def identity_pool_name(self) -> builtins.str:
        '''Name of the Identity Pool.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "identityPoolName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIdentityPool).__jsii_proxy_class__ = lambda : _IIdentityPoolProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.aws_cognito_identitypool.IUserPoolAuthenticationProvider"
)
class IUserPoolAuthenticationProvider(typing_extensions.Protocol):
    '''Represents the concept of a User Pool Authentication Provider.

    You use user pool authentication providers to configure User Pools
    and User Pool Clients for use with Identity Pools
    '''

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        identity_pool: IIdentityPool,
    ) -> "UserPoolAuthenticationProviderBindConfig":
        '''The method called when a given User Pool Authentication Provider is added (for the first time) to an Identity Pool.

        :param scope: -
        :param identity_pool: -
        '''
        ...


class _IUserPoolAuthenticationProviderProxy:
    '''Represents the concept of a User Pool Authentication Provider.

    You use user pool authentication providers to configure User Pools
    and User Pool Clients for use with Identity Pools
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_cognito_identitypool.IUserPoolAuthenticationProvider"

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        identity_pool: IIdentityPool,
    ) -> "UserPoolAuthenticationProviderBindConfig":
        '''The method called when a given User Pool Authentication Provider is added (for the first time) to an Identity Pool.

        :param scope: -
        :param identity_pool: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c814fdc426f731ac5e76cbccdb476b3226db8e3f5c19b9f57f6ed181043dd60)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument identity_pool", value=identity_pool, expected_type=type_hints["identity_pool"])
        options = UserPoolAuthenticationProviderBindOptions()

        return typing.cast("UserPoolAuthenticationProviderBindConfig", jsii.invoke(self, "bind", [scope, identity_pool, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserPoolAuthenticationProvider).__jsii_proxy_class__ = lambda : _IUserPoolAuthenticationProviderProxy


@jsii.implements(IIdentityPool)
class IdentityPool(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cognito_identitypool.IdentityPool",
):
    '''Define a Cognito Identity Pool.

    :resource: AWS::Cognito::IdentityPool
    :exampleMetadata: infused

    Example::

        # open_id_connect_provider: iam.OpenIdConnectProvider
        
        IdentityPool(self, "myidentitypool",
            identity_pool_name="myidentitypool",
            authentication_providers=IdentityPoolAuthenticationProviders(
                google=IdentityPoolGoogleLoginProvider(
                    client_id="12345678012.apps.googleusercontent.com"
                ),
                open_id_connect_providers=[open_id_connect_provider],
                custom_provider="my-custom-provider.example.com"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        allow_classic_flow: typing.Optional[builtins.bool] = None,
        allow_unauthenticated_identities: typing.Optional[builtins.bool] = None,
        authenticated_role: typing.Optional[_IRole_235f5d8e] = None,
        authentication_providers: typing.Optional[typing.Union["IdentityPoolAuthenticationProviders", typing.Dict[builtins.str, typing.Any]]] = None,
        identity_pool_name: typing.Optional[builtins.str] = None,
        role_mappings: typing.Optional[typing.Sequence[typing.Union["IdentityPoolRoleMapping", typing.Dict[builtins.str, typing.Any]]]] = None,
        unauthenticated_role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param allow_classic_flow: Enables the Basic (Classic) authentication flow. Default: - Classic Flow not allowed
        :param allow_unauthenticated_identities: Whether the Identity Pool supports unauthenticated logins. Default: - false
        :param authenticated_role: The default Role to be assumed by authenticated users. Default: - A default authenticated Role will be added
        :param authentication_providers: Authentication Providers for using in Identity Pool. Default: - No Authentication Providers passed directly to Identity Pool
        :param identity_pool_name: The name of the Identity Pool. Default: - Automatically generated name by CloudFormation at deploy time
        :param role_mappings: Rules for mapping roles to users. Default: - no role mappings
        :param unauthenticated_role: The default Role to be assumed by unauthenticated users. Default: - A default unauthenticated Role will be added
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7508ece930af8922e09956e6b9166bbdbf4f94d0b43649c6d1c63f6bd90fc80)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = IdentityPoolProps(
            allow_classic_flow=allow_classic_flow,
            allow_unauthenticated_identities=allow_unauthenticated_identities,
            authenticated_role=authenticated_role,
            authentication_providers=authentication_providers,
            identity_pool_name=identity_pool_name,
            role_mappings=role_mappings,
            unauthenticated_role=unauthenticated_role,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromIdentityPoolArn")
    @builtins.classmethod
    def from_identity_pool_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        identity_pool_arn: builtins.str,
    ) -> IIdentityPool:
        '''Import an existing Identity Pool from its ARN.

        :param scope: -
        :param id: -
        :param identity_pool_arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3173746cd04dd07f081f1f960cd91b67ec8367052f383c0ed193eaf98bcf47c6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity_pool_arn", value=identity_pool_arn, expected_type=type_hints["identity_pool_arn"])
        return typing.cast(IIdentityPool, jsii.sinvoke(cls, "fromIdentityPoolArn", [scope, id, identity_pool_arn]))

    @jsii.member(jsii_name="fromIdentityPoolId")
    @builtins.classmethod
    def from_identity_pool_id(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        identity_pool_id: builtins.str,
    ) -> IIdentityPool:
        '''Import an existing Identity Pool from its ID.

        :param scope: -
        :param id: -
        :param identity_pool_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7094f2ba90c5fab8d158b4276f0bc0876fb3f0e3dd42cafa6fb6cb1e02a6893)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity_pool_id", value=identity_pool_id, expected_type=type_hints["identity_pool_id"])
        return typing.cast(IIdentityPool, jsii.sinvoke(cls, "fromIdentityPoolId", [scope, id, identity_pool_id]))

    @jsii.member(jsii_name="addUserPoolAuthentication")
    def add_user_pool_authentication(
        self,
        user_pool: IUserPoolAuthenticationProvider,
    ) -> None:
        '''Add a User Pool to the Identity Pool and configure the User Pool client to handle identities.

        :param user_pool: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd6d23271053899a9cf9a7ec303ccebbcc3f4c4aa45de84fb3586658a176cb3a)
            check_type(argname="argument user_pool", value=user_pool, expected_type=type_hints["user_pool"])
        return typing.cast(None, jsii.invoke(self, "addUserPoolAuthentication", [user_pool]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))

    @builtins.property
    @jsii.member(jsii_name="authenticatedRole")
    def authenticated_role(self) -> _IRole_235f5d8e:
        '''Default Role for authenticated users.'''
        return typing.cast(_IRole_235f5d8e, jsii.get(self, "authenticatedRole"))

    @builtins.property
    @jsii.member(jsii_name="identityPoolArn")
    def identity_pool_arn(self) -> builtins.str:
        '''The ARN of the Identity Pool.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "identityPoolArn"))

    @builtins.property
    @jsii.member(jsii_name="identityPoolId")
    def identity_pool_id(self) -> builtins.str:
        '''The ID of the Identity Pool in the format REGION:GUID.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "identityPoolId"))

    @builtins.property
    @jsii.member(jsii_name="identityPoolName")
    def identity_pool_name(self) -> builtins.str:
        '''The name of the Identity Pool.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "identityPoolName"))

    @builtins.property
    @jsii.member(jsii_name="roleAttachment")
    def role_attachment(self) -> _CfnIdentityPoolRoleAttachment_6213757a:
        '''Role Provider for the default Role for authenticated users.'''
        return typing.cast(_CfnIdentityPoolRoleAttachment_6213757a, jsii.get(self, "roleAttachment"))

    @builtins.property
    @jsii.member(jsii_name="unauthenticatedRole")
    def unauthenticated_role(self) -> _IRole_235f5d8e:
        '''Default Role for unauthenticated users.'''
        return typing.cast(_IRole_235f5d8e, jsii.get(self, "unauthenticatedRole"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cognito_identitypool.IdentityPoolAmazonLoginProvider",
    jsii_struct_bases=[],
    name_mapping={"app_id": "appId"},
)
class IdentityPoolAmazonLoginProvider:
    def __init__(self, *, app_id: builtins.str) -> None:
        '''Login Provider for identity federation using Amazon credentials.

        :param app_id: App ID for Amazon identity federation.

        :exampleMetadata: infused

        Example::

            IdentityPool(self, "myidentitypool",
                identity_pool_name="myidentitypool",
                authentication_providers=IdentityPoolAuthenticationProviders(
                    amazon=IdentityPoolAmazonLoginProvider(
                        app_id="amzn1.application.12312k3j234j13rjiwuenf"
                    ),
                    facebook=IdentityPoolFacebookLoginProvider(
                        app_id="1234567890123"
                    ),
                    google=IdentityPoolGoogleLoginProvider(
                        client_id="12345678012.apps.googleusercontent.com"
                    ),
                    apple=IdentityPoolAppleLoginProvider(
                        services_id="com.myappleapp.auth"
                    ),
                    twitter=IdentityPoolTwitterLoginProvider(
                        consumer_key="my-twitter-id",
                        consumer_secret="my-twitter-secret"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__469abe646a9b1de4f31f3b04632a02d728f0da52b1c7b2fb1c31b02e48ab80b9)
            check_type(argname="argument app_id", value=app_id, expected_type=type_hints["app_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_id": app_id,
        }

    @builtins.property
    def app_id(self) -> builtins.str:
        '''App ID for Amazon identity federation.'''
        result = self._values.get("app_id")
        assert result is not None, "Required property 'app_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityPoolAmazonLoginProvider(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cognito_identitypool.IdentityPoolAppleLoginProvider",
    jsii_struct_bases=[],
    name_mapping={"services_id": "servicesId"},
)
class IdentityPoolAppleLoginProvider:
    def __init__(self, *, services_id: builtins.str) -> None:
        '''Login Provider for identity federation using Apple credentials.

        :param services_id: Services ID for Apple identity federation.

        :exampleMetadata: infused

        Example::

            IdentityPool(self, "myidentitypool",
                identity_pool_name="myidentitypool",
                authentication_providers=IdentityPoolAuthenticationProviders(
                    amazon=IdentityPoolAmazonLoginProvider(
                        app_id="amzn1.application.12312k3j234j13rjiwuenf"
                    ),
                    facebook=IdentityPoolFacebookLoginProvider(
                        app_id="1234567890123"
                    ),
                    google=IdentityPoolGoogleLoginProvider(
                        client_id="12345678012.apps.googleusercontent.com"
                    ),
                    apple=IdentityPoolAppleLoginProvider(
                        services_id="com.myappleapp.auth"
                    ),
                    twitter=IdentityPoolTwitterLoginProvider(
                        consumer_key="my-twitter-id",
                        consumer_secret="my-twitter-secret"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9b4447874c9fdd7fed07df178fcf069b944be0d670ec52b85e362202ed6ca80)
            check_type(argname="argument services_id", value=services_id, expected_type=type_hints["services_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "services_id": services_id,
        }

    @builtins.property
    def services_id(self) -> builtins.str:
        '''Services ID for Apple identity federation.'''
        result = self._values.get("services_id")
        assert result is not None, "Required property 'services_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityPoolAppleLoginProvider(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cognito_identitypool.IdentityPoolAuthenticationProviders",
    jsii_struct_bases=[],
    name_mapping={
        "amazon": "amazon",
        "apple": "apple",
        "custom_provider": "customProvider",
        "facebook": "facebook",
        "google": "google",
        "open_id_connect_providers": "openIdConnectProviders",
        "saml_providers": "samlProviders",
        "twitter": "twitter",
        "user_pools": "userPools",
    },
)
class IdentityPoolAuthenticationProviders:
    def __init__(
        self,
        *,
        amazon: typing.Optional[typing.Union[IdentityPoolAmazonLoginProvider, typing.Dict[builtins.str, typing.Any]]] = None,
        apple: typing.Optional[typing.Union[IdentityPoolAppleLoginProvider, typing.Dict[builtins.str, typing.Any]]] = None,
        custom_provider: typing.Optional[builtins.str] = None,
        facebook: typing.Optional[typing.Union["IdentityPoolFacebookLoginProvider", typing.Dict[builtins.str, typing.Any]]] = None,
        google: typing.Optional[typing.Union["IdentityPoolGoogleLoginProvider", typing.Dict[builtins.str, typing.Any]]] = None,
        open_id_connect_providers: typing.Optional[typing.Sequence[_IOpenIdConnectProvider_203f0793]] = None,
        saml_providers: typing.Optional[typing.Sequence[_ISamlProvider_63f03582]] = None,
        twitter: typing.Optional[typing.Union["IdentityPoolTwitterLoginProvider", typing.Dict[builtins.str, typing.Any]]] = None,
        user_pools: typing.Optional[typing.Sequence[IUserPoolAuthenticationProvider]] = None,
    ) -> None:
        '''External Authentication Providers for usage in Identity Pool.

        :param amazon: The Amazon Authentication Provider associated with this Identity Pool. Default: - No Amazon Authentication Provider used without OpenIdConnect or a User Pool
        :param apple: The Apple Authentication Provider associated with this Identity Pool. Default: - No Apple Authentication Provider used without OpenIdConnect or a User Pool
        :param custom_provider: The developer provider name to associate with this Identity Pool. Default: - no custom provider
        :param facebook: The Facebook Authentication Provider associated with this Identity Pool. Default: - No Facebook Authentication Provider used without OpenIdConnect or a User Pool
        :param google: The Google Authentication Provider associated with this Identity Pool. Default: - No Google Authentication Provider used without OpenIdConnect or a User Pool
        :param open_id_connect_providers: The OpenIdConnect Provider associated with this Identity Pool. Default: - no OpenIdConnectProvider
        :param saml_providers: The Security Assertion Markup Language provider associated with this Identity Pool. Default: - no SamlProvider
        :param twitter: The Twitter Authentication Provider associated with this Identity Pool. Default: - No Twitter Authentication Provider used without OpenIdConnect or a User Pool
        :param user_pools: The User Pool Authentication Providers associated with this Identity Pool. Default: - no User Pools associated

        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/external-identity-providers.html
        :exampleMetadata: infused

        Example::

            # open_id_connect_provider: iam.OpenIdConnectProvider
            
            IdentityPool(self, "myidentitypool",
                identity_pool_name="myidentitypool",
                authentication_providers=IdentityPoolAuthenticationProviders(
                    google=IdentityPoolGoogleLoginProvider(
                        client_id="12345678012.apps.googleusercontent.com"
                    ),
                    open_id_connect_providers=[open_id_connect_provider],
                    custom_provider="my-custom-provider.example.com"
                )
            )
        '''
        if isinstance(amazon, dict):
            amazon = IdentityPoolAmazonLoginProvider(**amazon)
        if isinstance(apple, dict):
            apple = IdentityPoolAppleLoginProvider(**apple)
        if isinstance(facebook, dict):
            facebook = IdentityPoolFacebookLoginProvider(**facebook)
        if isinstance(google, dict):
            google = IdentityPoolGoogleLoginProvider(**google)
        if isinstance(twitter, dict):
            twitter = IdentityPoolTwitterLoginProvider(**twitter)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5736f06974c68519c1ae6c3b7a96f6631b848c6e335b1b26878af4283639ee6)
            check_type(argname="argument amazon", value=amazon, expected_type=type_hints["amazon"])
            check_type(argname="argument apple", value=apple, expected_type=type_hints["apple"])
            check_type(argname="argument custom_provider", value=custom_provider, expected_type=type_hints["custom_provider"])
            check_type(argname="argument facebook", value=facebook, expected_type=type_hints["facebook"])
            check_type(argname="argument google", value=google, expected_type=type_hints["google"])
            check_type(argname="argument open_id_connect_providers", value=open_id_connect_providers, expected_type=type_hints["open_id_connect_providers"])
            check_type(argname="argument saml_providers", value=saml_providers, expected_type=type_hints["saml_providers"])
            check_type(argname="argument twitter", value=twitter, expected_type=type_hints["twitter"])
            check_type(argname="argument user_pools", value=user_pools, expected_type=type_hints["user_pools"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if amazon is not None:
            self._values["amazon"] = amazon
        if apple is not None:
            self._values["apple"] = apple
        if custom_provider is not None:
            self._values["custom_provider"] = custom_provider
        if facebook is not None:
            self._values["facebook"] = facebook
        if google is not None:
            self._values["google"] = google
        if open_id_connect_providers is not None:
            self._values["open_id_connect_providers"] = open_id_connect_providers
        if saml_providers is not None:
            self._values["saml_providers"] = saml_providers
        if twitter is not None:
            self._values["twitter"] = twitter
        if user_pools is not None:
            self._values["user_pools"] = user_pools

    @builtins.property
    def amazon(self) -> typing.Optional[IdentityPoolAmazonLoginProvider]:
        '''The Amazon Authentication Provider associated with this Identity Pool.

        :default: - No Amazon Authentication Provider used without OpenIdConnect or a User Pool
        '''
        result = self._values.get("amazon")
        return typing.cast(typing.Optional[IdentityPoolAmazonLoginProvider], result)

    @builtins.property
    def apple(self) -> typing.Optional[IdentityPoolAppleLoginProvider]:
        '''The Apple Authentication Provider associated with this Identity Pool.

        :default: - No Apple Authentication Provider used without OpenIdConnect or a User Pool
        '''
        result = self._values.get("apple")
        return typing.cast(typing.Optional[IdentityPoolAppleLoginProvider], result)

    @builtins.property
    def custom_provider(self) -> typing.Optional[builtins.str]:
        '''The developer provider name to associate with this Identity Pool.

        :default: - no custom provider
        '''
        result = self._values.get("custom_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def facebook(self) -> typing.Optional["IdentityPoolFacebookLoginProvider"]:
        '''The Facebook Authentication Provider associated with this Identity Pool.

        :default: - No Facebook Authentication Provider used without OpenIdConnect or a User Pool
        '''
        result = self._values.get("facebook")
        return typing.cast(typing.Optional["IdentityPoolFacebookLoginProvider"], result)

    @builtins.property
    def google(self) -> typing.Optional["IdentityPoolGoogleLoginProvider"]:
        '''The Google Authentication Provider associated with this Identity Pool.

        :default: - No Google Authentication Provider used without OpenIdConnect or a User Pool
        '''
        result = self._values.get("google")
        return typing.cast(typing.Optional["IdentityPoolGoogleLoginProvider"], result)

    @builtins.property
    def open_id_connect_providers(
        self,
    ) -> typing.Optional[typing.List[_IOpenIdConnectProvider_203f0793]]:
        '''The OpenIdConnect Provider associated with this Identity Pool.

        :default: - no OpenIdConnectProvider
        '''
        result = self._values.get("open_id_connect_providers")
        return typing.cast(typing.Optional[typing.List[_IOpenIdConnectProvider_203f0793]], result)

    @builtins.property
    def saml_providers(self) -> typing.Optional[typing.List[_ISamlProvider_63f03582]]:
        '''The Security Assertion Markup Language provider associated with this Identity Pool.

        :default: - no SamlProvider
        '''
        result = self._values.get("saml_providers")
        return typing.cast(typing.Optional[typing.List[_ISamlProvider_63f03582]], result)

    @builtins.property
    def twitter(self) -> typing.Optional["IdentityPoolTwitterLoginProvider"]:
        '''The Twitter Authentication Provider associated with this Identity Pool.

        :default: - No Twitter Authentication Provider used without OpenIdConnect or a User Pool
        '''
        result = self._values.get("twitter")
        return typing.cast(typing.Optional["IdentityPoolTwitterLoginProvider"], result)

    @builtins.property
    def user_pools(
        self,
    ) -> typing.Optional[typing.List[IUserPoolAuthenticationProvider]]:
        '''The User Pool Authentication Providers associated with this Identity Pool.

        :default: - no User Pools associated
        '''
        result = self._values.get("user_pools")
        return typing.cast(typing.Optional[typing.List[IUserPoolAuthenticationProvider]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityPoolAuthenticationProviders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cognito_identitypool.IdentityPoolFacebookLoginProvider",
    jsii_struct_bases=[],
    name_mapping={"app_id": "appId"},
)
class IdentityPoolFacebookLoginProvider:
    def __init__(self, *, app_id: builtins.str) -> None:
        '''Login Provider for identity federation using Facebook credentials.

        :param app_id: App ID for Facebook identity federation.

        :exampleMetadata: infused

        Example::

            IdentityPool(self, "myidentitypool",
                identity_pool_name="myidentitypool",
                authentication_providers=IdentityPoolAuthenticationProviders(
                    amazon=IdentityPoolAmazonLoginProvider(
                        app_id="amzn1.application.12312k3j234j13rjiwuenf"
                    ),
                    facebook=IdentityPoolFacebookLoginProvider(
                        app_id="1234567890123"
                    ),
                    google=IdentityPoolGoogleLoginProvider(
                        client_id="12345678012.apps.googleusercontent.com"
                    ),
                    apple=IdentityPoolAppleLoginProvider(
                        services_id="com.myappleapp.auth"
                    ),
                    twitter=IdentityPoolTwitterLoginProvider(
                        consumer_key="my-twitter-id",
                        consumer_secret="my-twitter-secret"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79f268d6507a7ea842aa4eecfa40a33ff4b75964393a3608ad305361f40fbfa4)
            check_type(argname="argument app_id", value=app_id, expected_type=type_hints["app_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_id": app_id,
        }

    @builtins.property
    def app_id(self) -> builtins.str:
        '''App ID for Facebook identity federation.'''
        result = self._values.get("app_id")
        assert result is not None, "Required property 'app_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityPoolFacebookLoginProvider(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cognito_identitypool.IdentityPoolGoogleLoginProvider",
    jsii_struct_bases=[],
    name_mapping={"client_id": "clientId"},
)
class IdentityPoolGoogleLoginProvider:
    def __init__(self, *, client_id: builtins.str) -> None:
        '''Login Provider for identity federation using Google credentials.

        :param client_id: Client ID for Google identity federation.

        :exampleMetadata: infused

        Example::

            IdentityPool(self, "myidentitypool",
                identity_pool_name="myidentitypool",
                authentication_providers=IdentityPoolAuthenticationProviders(
                    amazon=IdentityPoolAmazonLoginProvider(
                        app_id="amzn1.application.12312k3j234j13rjiwuenf"
                    ),
                    facebook=IdentityPoolFacebookLoginProvider(
                        app_id="1234567890123"
                    ),
                    google=IdentityPoolGoogleLoginProvider(
                        client_id="12345678012.apps.googleusercontent.com"
                    ),
                    apple=IdentityPoolAppleLoginProvider(
                        services_id="com.myappleapp.auth"
                    ),
                    twitter=IdentityPoolTwitterLoginProvider(
                        consumer_key="my-twitter-id",
                        consumer_secret="my-twitter-secret"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cf50453dd8eb6086b031602235511412f140c8a0fd75af98cf94efd203caf0c)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
        }

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Client ID for Google identity federation.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityPoolGoogleLoginProvider(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cognito_identitypool.IdentityPoolProps",
    jsii_struct_bases=[],
    name_mapping={
        "allow_classic_flow": "allowClassicFlow",
        "allow_unauthenticated_identities": "allowUnauthenticatedIdentities",
        "authenticated_role": "authenticatedRole",
        "authentication_providers": "authenticationProviders",
        "identity_pool_name": "identityPoolName",
        "role_mappings": "roleMappings",
        "unauthenticated_role": "unauthenticatedRole",
    },
)
class IdentityPoolProps:
    def __init__(
        self,
        *,
        allow_classic_flow: typing.Optional[builtins.bool] = None,
        allow_unauthenticated_identities: typing.Optional[builtins.bool] = None,
        authenticated_role: typing.Optional[_IRole_235f5d8e] = None,
        authentication_providers: typing.Optional[typing.Union[IdentityPoolAuthenticationProviders, typing.Dict[builtins.str, typing.Any]]] = None,
        identity_pool_name: typing.Optional[builtins.str] = None,
        role_mappings: typing.Optional[typing.Sequence[typing.Union["IdentityPoolRoleMapping", typing.Dict[builtins.str, typing.Any]]]] = None,
        unauthenticated_role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Props for the Identity Pool construct.

        :param allow_classic_flow: Enables the Basic (Classic) authentication flow. Default: - Classic Flow not allowed
        :param allow_unauthenticated_identities: Whether the Identity Pool supports unauthenticated logins. Default: - false
        :param authenticated_role: The default Role to be assumed by authenticated users. Default: - A default authenticated Role will be added
        :param authentication_providers: Authentication Providers for using in Identity Pool. Default: - No Authentication Providers passed directly to Identity Pool
        :param identity_pool_name: The name of the Identity Pool. Default: - Automatically generated name by CloudFormation at deploy time
        :param role_mappings: Rules for mapping roles to users. Default: - no role mappings
        :param unauthenticated_role: The default Role to be assumed by unauthenticated users. Default: - A default unauthenticated Role will be added

        :exampleMetadata: infused

        Example::

            # open_id_connect_provider: iam.OpenIdConnectProvider
            
            IdentityPool(self, "myidentitypool",
                identity_pool_name="myidentitypool",
                authentication_providers=IdentityPoolAuthenticationProviders(
                    google=IdentityPoolGoogleLoginProvider(
                        client_id="12345678012.apps.googleusercontent.com"
                    ),
                    open_id_connect_providers=[open_id_connect_provider],
                    custom_provider="my-custom-provider.example.com"
                )
            )
        '''
        if isinstance(authentication_providers, dict):
            authentication_providers = IdentityPoolAuthenticationProviders(**authentication_providers)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af198fbf56ac885d5c6c92255ff0143c4ee67b99a01cce4cfb3113296d3d7265)
            check_type(argname="argument allow_classic_flow", value=allow_classic_flow, expected_type=type_hints["allow_classic_flow"])
            check_type(argname="argument allow_unauthenticated_identities", value=allow_unauthenticated_identities, expected_type=type_hints["allow_unauthenticated_identities"])
            check_type(argname="argument authenticated_role", value=authenticated_role, expected_type=type_hints["authenticated_role"])
            check_type(argname="argument authentication_providers", value=authentication_providers, expected_type=type_hints["authentication_providers"])
            check_type(argname="argument identity_pool_name", value=identity_pool_name, expected_type=type_hints["identity_pool_name"])
            check_type(argname="argument role_mappings", value=role_mappings, expected_type=type_hints["role_mappings"])
            check_type(argname="argument unauthenticated_role", value=unauthenticated_role, expected_type=type_hints["unauthenticated_role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allow_classic_flow is not None:
            self._values["allow_classic_flow"] = allow_classic_flow
        if allow_unauthenticated_identities is not None:
            self._values["allow_unauthenticated_identities"] = allow_unauthenticated_identities
        if authenticated_role is not None:
            self._values["authenticated_role"] = authenticated_role
        if authentication_providers is not None:
            self._values["authentication_providers"] = authentication_providers
        if identity_pool_name is not None:
            self._values["identity_pool_name"] = identity_pool_name
        if role_mappings is not None:
            self._values["role_mappings"] = role_mappings
        if unauthenticated_role is not None:
            self._values["unauthenticated_role"] = unauthenticated_role

    @builtins.property
    def allow_classic_flow(self) -> typing.Optional[builtins.bool]:
        '''Enables the Basic (Classic) authentication flow.

        :default: - Classic Flow not allowed
        '''
        result = self._values.get("allow_classic_flow")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_unauthenticated_identities(self) -> typing.Optional[builtins.bool]:
        '''Whether the Identity Pool supports unauthenticated logins.

        :default: - false
        '''
        result = self._values.get("allow_unauthenticated_identities")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def authenticated_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The default Role to be assumed by authenticated users.

        :default: - A default authenticated Role will be added
        '''
        result = self._values.get("authenticated_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def authentication_providers(
        self,
    ) -> typing.Optional[IdentityPoolAuthenticationProviders]:
        '''Authentication Providers for using in Identity Pool.

        :default: - No Authentication Providers passed directly to Identity Pool
        '''
        result = self._values.get("authentication_providers")
        return typing.cast(typing.Optional[IdentityPoolAuthenticationProviders], result)

    @builtins.property
    def identity_pool_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Identity Pool.

        :default: - Automatically generated name by CloudFormation at deploy time
        '''
        result = self._values.get("identity_pool_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_mappings(self) -> typing.Optional[typing.List["IdentityPoolRoleMapping"]]:
        '''Rules for mapping roles to users.

        :default: - no role mappings
        '''
        result = self._values.get("role_mappings")
        return typing.cast(typing.Optional[typing.List["IdentityPoolRoleMapping"]], result)

    @builtins.property
    def unauthenticated_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The default Role to be assumed by unauthenticated users.

        :default: - A default unauthenticated Role will be added
        '''
        result = self._values.get("unauthenticated_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityPoolProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_cognito_identitypool.IdentityPoolProviderType")
class IdentityPoolProviderType(enum.Enum):
    '''Types of Identity Pool Login Providers.'''

    FACEBOOK = "FACEBOOK"
    '''Facebook provider type.'''
    GOOGLE = "GOOGLE"
    '''Google provider type.'''
    AMAZON = "AMAZON"
    '''Amazon provider type.'''
    APPLE = "APPLE"
    '''Apple provider type.'''
    TWITTER = "TWITTER"
    '''Twitter provider type.'''
    OPEN_ID = "OPEN_ID"
    '''Open Id provider type.'''
    SAML = "SAML"
    '''Saml provider type.'''
    USER_POOL = "USER_POOL"
    '''User Pool provider type.'''
    CUSTOM = "CUSTOM"
    '''Custom provider type.'''


class IdentityPoolProviderUrl(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cognito_identitypool.IdentityPoolProviderUrl",
):
    '''Keys for Login Providers - each correspond to the client IDs of their respective federation Identity Providers.

    :exampleMetadata: infused

    Example::

        from aws_cdk.aws_cognito_identitypool import IdentityPoolProviderUrl
        
        
        IdentityPool(self, "myidentitypool",
            identity_pool_name="myidentitypool",
            role_mappings=[IdentityPoolRoleMapping(
                provider_url=IdentityPoolProviderUrl.custom("my-custom-provider.com"),
                use_token=True
            )
            ]
        )
    '''

    def __init__(self, type: IdentityPoolProviderType, value: builtins.str) -> None:
        '''
        :param type: The type of Identity Pool Provider.
        :param value: The value of the Identity Pool Provider.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e21346602560f1cca6af9cafa3890159f40fe201ff2586fe35bff0fa41238584)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.create(self.__class__, self, [type, value])

    @jsii.member(jsii_name="custom")
    @builtins.classmethod
    def custom(cls, url: builtins.str) -> "IdentityPoolProviderUrl":
        '''Custom Provider url.

        :param url: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d20114b4fee683d84de101e404d5d8ef6cfea15634e2d35c6cc734c6009b8bad)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        return typing.cast("IdentityPoolProviderUrl", jsii.sinvoke(cls, "custom", [url]))

    @jsii.member(jsii_name="openId")
    @builtins.classmethod
    def open_id(cls, url: builtins.str) -> "IdentityPoolProviderUrl":
        '''OpenId Provider url.

        :param url: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c92bcc9f8137a1d3e5beb43462992a38aaa0afc35af1ed27bb9a025f816fbda)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        return typing.cast("IdentityPoolProviderUrl", jsii.sinvoke(cls, "openId", [url]))

    @jsii.member(jsii_name="saml")
    @builtins.classmethod
    def saml(cls, url: builtins.str) -> "IdentityPoolProviderUrl":
        '''Saml Provider url.

        :param url: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c7e07ca5a6f8dcc0f5236108ff2bb3698b65026b062307b86b3d67f3c6bda1f)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        return typing.cast("IdentityPoolProviderUrl", jsii.sinvoke(cls, "saml", [url]))

    @jsii.member(jsii_name="userPool")
    @builtins.classmethod
    def user_pool(
        cls,
        user_pool: _IUserPool_1f1029e2,
        user_pool_client: _IUserPoolClient_75623ba4,
    ) -> "IdentityPoolProviderUrl":
        '''User Pool Provider Url.

        :param user_pool: -
        :param user_pool_client: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__121c7b058215a85a8a95870556fad2d21fc96c58ad014823e300286ace7fde64)
            check_type(argname="argument user_pool", value=user_pool, expected_type=type_hints["user_pool"])
            check_type(argname="argument user_pool_client", value=user_pool_client, expected_type=type_hints["user_pool_client"])
        return typing.cast("IdentityPoolProviderUrl", jsii.sinvoke(cls, "userPool", [user_pool, user_pool_client]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON")
    def AMAZON(cls) -> "IdentityPoolProviderUrl":
        '''Amazon Provider url.'''
        return typing.cast("IdentityPoolProviderUrl", jsii.sget(cls, "AMAZON"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APPLE")
    def APPLE(cls) -> "IdentityPoolProviderUrl":
        '''Apple Provider url.'''
        return typing.cast("IdentityPoolProviderUrl", jsii.sget(cls, "APPLE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FACEBOOK")
    def FACEBOOK(cls) -> "IdentityPoolProviderUrl":
        '''Facebook Provider url.'''
        return typing.cast("IdentityPoolProviderUrl", jsii.sget(cls, "FACEBOOK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GOOGLE")
    def GOOGLE(cls) -> "IdentityPoolProviderUrl":
        '''Google Provider url.'''
        return typing.cast("IdentityPoolProviderUrl", jsii.sget(cls, "GOOGLE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="TWITTER")
    def TWITTER(cls) -> "IdentityPoolProviderUrl":
        '''Twitter Provider url.'''
        return typing.cast("IdentityPoolProviderUrl", jsii.sget(cls, "TWITTER"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> IdentityPoolProviderType:
        '''The type of Identity Pool Provider.'''
        return typing.cast(IdentityPoolProviderType, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        '''The value of the Identity Pool Provider.'''
        return typing.cast(builtins.str, jsii.get(self, "value"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cognito_identitypool.IdentityPoolRoleMapping",
    jsii_struct_bases=[],
    name_mapping={
        "provider_url": "providerUrl",
        "mapping_key": "mappingKey",
        "resolve_ambiguous_roles": "resolveAmbiguousRoles",
        "rules": "rules",
        "use_token": "useToken",
    },
)
class IdentityPoolRoleMapping:
    def __init__(
        self,
        *,
        provider_url: IdentityPoolProviderUrl,
        mapping_key: typing.Optional[builtins.str] = None,
        resolve_ambiguous_roles: typing.Optional[builtins.bool] = None,
        rules: typing.Optional[typing.Sequence[typing.Union["RoleMappingRule", typing.Dict[builtins.str, typing.Any]]]] = None,
        use_token: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Map roles to users in the Identity Pool based on claims from the Identity Provider.

        :param provider_url: The url of the Provider for which the role is mapped.
        :param mapping_key: The key used for the role mapping in the role mapping hash. Required if the providerUrl is a token. Default: - The provided providerUrl
        :param resolve_ambiguous_roles: Allow for role assumption when results of role mapping are ambiguous. Default: false - Ambiguous role resolutions will lead to requester being denied
        :param rules: The claim and value that must be matched in order to assume the role. Required if useToken is false Default: - No role mapping rule
        :param use_token: If true then mapped roles must be passed through the cognito:roles or cognito:preferred_role claims from Identity Provider. Default: false

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cognito_identitypool as cognito_identitypool
            from aws_cdk import aws_iam as iam
            
            # identity_pool_provider_url: cognito_identitypool.IdentityPoolProviderUrl
            # role: iam.Role
            
            identity_pool_role_mapping = cognito_identitypool.IdentityPoolRoleMapping(
                provider_url=identity_pool_provider_url,
            
                # the properties below are optional
                mapping_key="mappingKey",
                resolve_ambiguous_roles=False,
                rules=[cognito_identitypool.RoleMappingRule(
                    claim="claim",
                    claim_value="claimValue",
                    mapped_role=role,
            
                    # the properties below are optional
                    match_type=cognito_identitypool.RoleMappingMatchType.EQUALS
                )],
                use_token=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05374fa9238ffbe78c089d88ef40291976f7b4f0da96abe1bc7076a3dc7f654a)
            check_type(argname="argument provider_url", value=provider_url, expected_type=type_hints["provider_url"])
            check_type(argname="argument mapping_key", value=mapping_key, expected_type=type_hints["mapping_key"])
            check_type(argname="argument resolve_ambiguous_roles", value=resolve_ambiguous_roles, expected_type=type_hints["resolve_ambiguous_roles"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument use_token", value=use_token, expected_type=type_hints["use_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "provider_url": provider_url,
        }
        if mapping_key is not None:
            self._values["mapping_key"] = mapping_key
        if resolve_ambiguous_roles is not None:
            self._values["resolve_ambiguous_roles"] = resolve_ambiguous_roles
        if rules is not None:
            self._values["rules"] = rules
        if use_token is not None:
            self._values["use_token"] = use_token

    @builtins.property
    def provider_url(self) -> IdentityPoolProviderUrl:
        '''The url of the Provider for which the role is mapped.'''
        result = self._values.get("provider_url")
        assert result is not None, "Required property 'provider_url' is missing"
        return typing.cast(IdentityPoolProviderUrl, result)

    @builtins.property
    def mapping_key(self) -> typing.Optional[builtins.str]:
        '''The key used for the role mapping in the role mapping hash.

        Required if the providerUrl is a token.

        :default: - The provided providerUrl
        '''
        result = self._values.get("mapping_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resolve_ambiguous_roles(self) -> typing.Optional[builtins.bool]:
        '''Allow for role assumption when results of role mapping are ambiguous.

        :default: false - Ambiguous role resolutions will lead to requester being denied
        '''
        result = self._values.get("resolve_ambiguous_roles")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.List["RoleMappingRule"]]:
        '''The claim and value that must be matched in order to assume the role.

        Required if useToken is false

        :default: - No role mapping rule
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.List["RoleMappingRule"]], result)

    @builtins.property
    def use_token(self) -> typing.Optional[builtins.bool]:
        '''If true then mapped roles must be passed through the cognito:roles or cognito:preferred_role claims from Identity Provider.

        :default: false

        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/role-based-access-control.html#using-tokens-to-assign-roles-to-users
        '''
        result = self._values.get("use_token")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityPoolRoleMapping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cognito_identitypool.IdentityPoolTwitterLoginProvider",
    jsii_struct_bases=[],
    name_mapping={"consumer_key": "consumerKey", "consumer_secret": "consumerSecret"},
)
class IdentityPoolTwitterLoginProvider:
    def __init__(
        self,
        *,
        consumer_key: builtins.str,
        consumer_secret: builtins.str,
    ) -> None:
        '''Login Provider for identity federation using Twitter credentials.

        :param consumer_key: Consumer key for Twitter identity federation.
        :param consumer_secret: Consumer secret for identity federation.

        :exampleMetadata: infused

        Example::

            IdentityPool(self, "myidentitypool",
                identity_pool_name="myidentitypool",
                authentication_providers=IdentityPoolAuthenticationProviders(
                    amazon=IdentityPoolAmazonLoginProvider(
                        app_id="amzn1.application.12312k3j234j13rjiwuenf"
                    ),
                    facebook=IdentityPoolFacebookLoginProvider(
                        app_id="1234567890123"
                    ),
                    google=IdentityPoolGoogleLoginProvider(
                        client_id="12345678012.apps.googleusercontent.com"
                    ),
                    apple=IdentityPoolAppleLoginProvider(
                        services_id="com.myappleapp.auth"
                    ),
                    twitter=IdentityPoolTwitterLoginProvider(
                        consumer_key="my-twitter-id",
                        consumer_secret="my-twitter-secret"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__786d99918d74ebff131cc6829f43e101b4ff2f81ae8498f6e87eeb4d19eeaab6)
            check_type(argname="argument consumer_key", value=consumer_key, expected_type=type_hints["consumer_key"])
            check_type(argname="argument consumer_secret", value=consumer_secret, expected_type=type_hints["consumer_secret"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "consumer_key": consumer_key,
            "consumer_secret": consumer_secret,
        }

    @builtins.property
    def consumer_key(self) -> builtins.str:
        '''Consumer key for Twitter identity federation.'''
        result = self._values.get("consumer_key")
        assert result is not None, "Required property 'consumer_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def consumer_secret(self) -> builtins.str:
        '''Consumer secret for identity federation.'''
        result = self._values.get("consumer_secret")
        assert result is not None, "Required property 'consumer_secret' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityPoolTwitterLoginProvider(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_cognito_identitypool.RoleMappingMatchType")
class RoleMappingMatchType(enum.Enum):
    '''Types of matches allowed for role mapping.

    :exampleMetadata: infused

    Example::

        from aws_cdk.aws_cognito_identitypool import IdentityPoolProviderUrl, RoleMappingMatchType
        
        # admin_role: iam.Role
        # non_admin_role: iam.Role
        
        IdentityPool(self, "myidentitypool",
            identity_pool_name="myidentitypool",
            # Assign specific roles to users based on whether or not the custom admin claim is passed from the identity provider
            role_mappings=[IdentityPoolRoleMapping(
                provider_url=IdentityPoolProviderUrl.AMAZON,
                rules=[RoleMappingRule(
                    claim="custom:admin",
                    claim_value="admin",
                    mapped_role=admin_role
                ), RoleMappingRule(
                    claim="custom:admin",
                    claim_value="admin",
                    match_type=RoleMappingMatchType.NOTEQUAL,
                    mapped_role=non_admin_role
                )
                ]
            )]
        )
    '''

    EQUALS = "EQUALS"
    '''The claim from the token must equal the given value in order for a match.'''
    CONTAINS = "CONTAINS"
    '''The claim from the token must contain the given value in order for a match.'''
    STARTS_WITH = "STARTS_WITH"
    '''The claim from the token must start with the given value in order for a match.'''
    NOTEQUAL = "NOTEQUAL"
    '''The claim from the token must not equal the given value in order for a match.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cognito_identitypool.RoleMappingRule",
    jsii_struct_bases=[],
    name_mapping={
        "claim": "claim",
        "claim_value": "claimValue",
        "mapped_role": "mappedRole",
        "match_type": "matchType",
    },
)
class RoleMappingRule:
    def __init__(
        self,
        *,
        claim: builtins.str,
        claim_value: builtins.str,
        mapped_role: _IRole_235f5d8e,
        match_type: typing.Optional[RoleMappingMatchType] = None,
    ) -> None:
        '''Represents an Identity Pool Role Attachment role mapping rule.

        :param claim: The key sent in the token by the federated Identity Provider.
        :param claim_value: The value of the claim that must be matched.
        :param mapped_role: The role to be assumed when the claim value is matched.
        :param match_type: How to match with the claim value. Default: RoleMappingMatchType.EQUALS

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cognito_identitypool as cognito_identitypool
            from aws_cdk import aws_iam as iam
            
            # role: iam.Role
            
            role_mapping_rule = cognito_identitypool.RoleMappingRule(
                claim="claim",
                claim_value="claimValue",
                mapped_role=role,
            
                # the properties below are optional
                match_type=cognito_identitypool.RoleMappingMatchType.EQUALS
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a3e6602f3dd1fc95d5e6a85eb1c6cd033f9584c3a5e317879694442cae64080)
            check_type(argname="argument claim", value=claim, expected_type=type_hints["claim"])
            check_type(argname="argument claim_value", value=claim_value, expected_type=type_hints["claim_value"])
            check_type(argname="argument mapped_role", value=mapped_role, expected_type=type_hints["mapped_role"])
            check_type(argname="argument match_type", value=match_type, expected_type=type_hints["match_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "claim": claim,
            "claim_value": claim_value,
            "mapped_role": mapped_role,
        }
        if match_type is not None:
            self._values["match_type"] = match_type

    @builtins.property
    def claim(self) -> builtins.str:
        '''The key sent in the token by the federated Identity Provider.'''
        result = self._values.get("claim")
        assert result is not None, "Required property 'claim' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def claim_value(self) -> builtins.str:
        '''The value of the claim that must be matched.'''
        result = self._values.get("claim_value")
        assert result is not None, "Required property 'claim_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mapped_role(self) -> _IRole_235f5d8e:
        '''The role to be assumed when the claim value is matched.'''
        result = self._values.get("mapped_role")
        assert result is not None, "Required property 'mapped_role' is missing"
        return typing.cast(_IRole_235f5d8e, result)

    @builtins.property
    def match_type(self) -> typing.Optional[RoleMappingMatchType]:
        '''How to match with the claim value.

        :default: RoleMappingMatchType.EQUALS
        '''
        result = self._values.get("match_type")
        return typing.cast(typing.Optional[RoleMappingMatchType], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoleMappingRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IUserPoolAuthenticationProvider)
class UserPoolAuthenticationProvider(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cognito_identitypool.UserPoolAuthenticationProvider",
):
    '''Defines a User Pool Authentication Provider.

    :exampleMetadata: infused

    Example::

        # identity_pool: IdentityPool
        
        user_pool = cognito.UserPool(self, "Pool")
        identity_pool.add_user_pool_authentication(UserPoolAuthenticationProvider(
            user_pool=user_pool,
            disable_server_side_token_check=True
        ))
    '''

    def __init__(
        self,
        *,
        user_pool: _IUserPool_1f1029e2,
        disable_server_side_token_check: typing.Optional[builtins.bool] = None,
        user_pool_client: typing.Optional[_IUserPoolClient_75623ba4] = None,
    ) -> None:
        '''
        :param user_pool: The User Pool of the Associated Identity Providers.
        :param disable_server_side_token_check: Setting this to true turns off identity pool checks for this user pool to make sure the user has not been globally signed out or deleted before the identity pool provides an OIDC token or AWS credentials for the user. Default: false
        :param user_pool_client: The User Pool Client for the provided User Pool. Default: - A default user pool client will be added to User Pool
        '''
        props = UserPoolAuthenticationProviderProps(
            user_pool=user_pool,
            disable_server_side_token_check=disable_server_side_token_check,
            user_pool_client=user_pool_client,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        identity_pool: IIdentityPool,
    ) -> "UserPoolAuthenticationProviderBindConfig":
        '''The method called when a given User Pool Authentication Provider is added (for the first time) to an Identity Pool.

        :param scope: -
        :param identity_pool: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba6eb139548890358ee0627f6ab76a68ed34453606a7c47e22b81e13d0d8b649)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument identity_pool", value=identity_pool, expected_type=type_hints["identity_pool"])
        _options = UserPoolAuthenticationProviderBindOptions()

        return typing.cast("UserPoolAuthenticationProviderBindConfig", jsii.invoke(self, "bind", [scope, identity_pool, _options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cognito_identitypool.UserPoolAuthenticationProviderBindConfig",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "provider_name": "providerName",
        "server_side_token_check": "serverSideTokenCheck",
    },
)
class UserPoolAuthenticationProviderBindConfig:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        provider_name: builtins.str,
        server_side_token_check: builtins.bool,
    ) -> None:
        '''Represents a UserPoolAuthenticationProvider Bind Configuration.

        :param client_id: Client Id of the Associated User Pool Client.
        :param provider_name: The identity providers associated with the UserPool.
        :param server_side_token_check: Whether to enable the identity pool's server side token check.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cognito_identitypool as cognito_identitypool
            
            user_pool_authentication_provider_bind_config = cognito_identitypool.UserPoolAuthenticationProviderBindConfig(
                client_id="clientId",
                provider_name="providerName",
                server_side_token_check=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e30a131979e49e3de120bda434e1aadc44c66a60ebb331ed0a7cb68845b2e58)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument server_side_token_check", value=server_side_token_check, expected_type=type_hints["server_side_token_check"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "provider_name": provider_name,
            "server_side_token_check": server_side_token_check,
        }

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Client Id of the Associated User Pool Client.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def provider_name(self) -> builtins.str:
        '''The identity providers associated with the UserPool.'''
        result = self._values.get("provider_name")
        assert result is not None, "Required property 'provider_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_side_token_check(self) -> builtins.bool:
        '''Whether to enable the identity pool's server side token check.'''
        result = self._values.get("server_side_token_check")
        assert result is not None, "Required property 'server_side_token_check' is missing"
        return typing.cast(builtins.bool, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolAuthenticationProviderBindConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cognito_identitypool.UserPoolAuthenticationProviderBindOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class UserPoolAuthenticationProviderBindOptions:
    def __init__(self) -> None:
        '''Represents UserPoolAuthenticationProvider Bind Options.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cognito_identitypool as cognito_identitypool
            
            user_pool_authentication_provider_bind_options = cognito_identitypool.UserPoolAuthenticationProviderBindOptions()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolAuthenticationProviderBindOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cognito_identitypool.UserPoolAuthenticationProviderProps",
    jsii_struct_bases=[],
    name_mapping={
        "user_pool": "userPool",
        "disable_server_side_token_check": "disableServerSideTokenCheck",
        "user_pool_client": "userPoolClient",
    },
)
class UserPoolAuthenticationProviderProps:
    def __init__(
        self,
        *,
        user_pool: _IUserPool_1f1029e2,
        disable_server_side_token_check: typing.Optional[builtins.bool] = None,
        user_pool_client: typing.Optional[_IUserPoolClient_75623ba4] = None,
    ) -> None:
        '''Props for the User Pool Authentication Provider.

        :param user_pool: The User Pool of the Associated Identity Providers.
        :param disable_server_side_token_check: Setting this to true turns off identity pool checks for this user pool to make sure the user has not been globally signed out or deleted before the identity pool provides an OIDC token or AWS credentials for the user. Default: false
        :param user_pool_client: The User Pool Client for the provided User Pool. Default: - A default user pool client will be added to User Pool

        :exampleMetadata: infused

        Example::

            # identity_pool: IdentityPool
            
            user_pool = cognito.UserPool(self, "Pool")
            identity_pool.add_user_pool_authentication(UserPoolAuthenticationProvider(
                user_pool=user_pool,
                disable_server_side_token_check=True
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96b0f5e74875a97abd1e74170f934c5a7746bf416d00b5b9a3a2b79560e66c96)
            check_type(argname="argument user_pool", value=user_pool, expected_type=type_hints["user_pool"])
            check_type(argname="argument disable_server_side_token_check", value=disable_server_side_token_check, expected_type=type_hints["disable_server_side_token_check"])
            check_type(argname="argument user_pool_client", value=user_pool_client, expected_type=type_hints["user_pool_client"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_pool": user_pool,
        }
        if disable_server_side_token_check is not None:
            self._values["disable_server_side_token_check"] = disable_server_side_token_check
        if user_pool_client is not None:
            self._values["user_pool_client"] = user_pool_client

    @builtins.property
    def user_pool(self) -> _IUserPool_1f1029e2:
        '''The User Pool of the Associated Identity Providers.'''
        result = self._values.get("user_pool")
        assert result is not None, "Required property 'user_pool' is missing"
        return typing.cast(_IUserPool_1f1029e2, result)

    @builtins.property
    def disable_server_side_token_check(self) -> typing.Optional[builtins.bool]:
        '''Setting this to true turns off identity pool checks for this user pool to make sure the user has not been globally signed out or deleted before the identity pool provides an OIDC token or AWS credentials for the user.

        :default: false

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitoidentityprovider.html
        '''
        result = self._values.get("disable_server_side_token_check")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def user_pool_client(self) -> typing.Optional[_IUserPoolClient_75623ba4]:
        '''The User Pool Client for the provided User Pool.

        :default: - A default user pool client will be added to User Pool
        '''
        result = self._values.get("user_pool_client")
        return typing.cast(typing.Optional[_IUserPoolClient_75623ba4], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolAuthenticationProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IIdentityPool",
    "IUserPoolAuthenticationProvider",
    "IdentityPool",
    "IdentityPoolAmazonLoginProvider",
    "IdentityPoolAppleLoginProvider",
    "IdentityPoolAuthenticationProviders",
    "IdentityPoolFacebookLoginProvider",
    "IdentityPoolGoogleLoginProvider",
    "IdentityPoolProps",
    "IdentityPoolProviderType",
    "IdentityPoolProviderUrl",
    "IdentityPoolRoleMapping",
    "IdentityPoolTwitterLoginProvider",
    "RoleMappingMatchType",
    "RoleMappingRule",
    "UserPoolAuthenticationProvider",
    "UserPoolAuthenticationProviderBindConfig",
    "UserPoolAuthenticationProviderBindOptions",
    "UserPoolAuthenticationProviderProps",
]

publication.publish()

def _typecheckingstub__5c814fdc426f731ac5e76cbccdb476b3226db8e3f5c19b9f57f6ed181043dd60(
    scope: _constructs_77d1e7e8.Construct,
    identity_pool: IIdentityPool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7508ece930af8922e09956e6b9166bbdbf4f94d0b43649c6d1c63f6bd90fc80(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    allow_classic_flow: typing.Optional[builtins.bool] = None,
    allow_unauthenticated_identities: typing.Optional[builtins.bool] = None,
    authenticated_role: typing.Optional[_IRole_235f5d8e] = None,
    authentication_providers: typing.Optional[typing.Union[IdentityPoolAuthenticationProviders, typing.Dict[builtins.str, typing.Any]]] = None,
    identity_pool_name: typing.Optional[builtins.str] = None,
    role_mappings: typing.Optional[typing.Sequence[typing.Union[IdentityPoolRoleMapping, typing.Dict[builtins.str, typing.Any]]]] = None,
    unauthenticated_role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3173746cd04dd07f081f1f960cd91b67ec8367052f383c0ed193eaf98bcf47c6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    identity_pool_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7094f2ba90c5fab8d158b4276f0bc0876fb3f0e3dd42cafa6fb6cb1e02a6893(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    identity_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd6d23271053899a9cf9a7ec303ccebbcc3f4c4aa45de84fb3586658a176cb3a(
    user_pool: IUserPoolAuthenticationProvider,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__469abe646a9b1de4f31f3b04632a02d728f0da52b1c7b2fb1c31b02e48ab80b9(
    *,
    app_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9b4447874c9fdd7fed07df178fcf069b944be0d670ec52b85e362202ed6ca80(
    *,
    services_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5736f06974c68519c1ae6c3b7a96f6631b848c6e335b1b26878af4283639ee6(
    *,
    amazon: typing.Optional[typing.Union[IdentityPoolAmazonLoginProvider, typing.Dict[builtins.str, typing.Any]]] = None,
    apple: typing.Optional[typing.Union[IdentityPoolAppleLoginProvider, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_provider: typing.Optional[builtins.str] = None,
    facebook: typing.Optional[typing.Union[IdentityPoolFacebookLoginProvider, typing.Dict[builtins.str, typing.Any]]] = None,
    google: typing.Optional[typing.Union[IdentityPoolGoogleLoginProvider, typing.Dict[builtins.str, typing.Any]]] = None,
    open_id_connect_providers: typing.Optional[typing.Sequence[_IOpenIdConnectProvider_203f0793]] = None,
    saml_providers: typing.Optional[typing.Sequence[_ISamlProvider_63f03582]] = None,
    twitter: typing.Optional[typing.Union[IdentityPoolTwitterLoginProvider, typing.Dict[builtins.str, typing.Any]]] = None,
    user_pools: typing.Optional[typing.Sequence[IUserPoolAuthenticationProvider]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79f268d6507a7ea842aa4eecfa40a33ff4b75964393a3608ad305361f40fbfa4(
    *,
    app_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cf50453dd8eb6086b031602235511412f140c8a0fd75af98cf94efd203caf0c(
    *,
    client_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af198fbf56ac885d5c6c92255ff0143c4ee67b99a01cce4cfb3113296d3d7265(
    *,
    allow_classic_flow: typing.Optional[builtins.bool] = None,
    allow_unauthenticated_identities: typing.Optional[builtins.bool] = None,
    authenticated_role: typing.Optional[_IRole_235f5d8e] = None,
    authentication_providers: typing.Optional[typing.Union[IdentityPoolAuthenticationProviders, typing.Dict[builtins.str, typing.Any]]] = None,
    identity_pool_name: typing.Optional[builtins.str] = None,
    role_mappings: typing.Optional[typing.Sequence[typing.Union[IdentityPoolRoleMapping, typing.Dict[builtins.str, typing.Any]]]] = None,
    unauthenticated_role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e21346602560f1cca6af9cafa3890159f40fe201ff2586fe35bff0fa41238584(
    type: IdentityPoolProviderType,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d20114b4fee683d84de101e404d5d8ef6cfea15634e2d35c6cc734c6009b8bad(
    url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c92bcc9f8137a1d3e5beb43462992a38aaa0afc35af1ed27bb9a025f816fbda(
    url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c7e07ca5a6f8dcc0f5236108ff2bb3698b65026b062307b86b3d67f3c6bda1f(
    url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__121c7b058215a85a8a95870556fad2d21fc96c58ad014823e300286ace7fde64(
    user_pool: _IUserPool_1f1029e2,
    user_pool_client: _IUserPoolClient_75623ba4,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05374fa9238ffbe78c089d88ef40291976f7b4f0da96abe1bc7076a3dc7f654a(
    *,
    provider_url: IdentityPoolProviderUrl,
    mapping_key: typing.Optional[builtins.str] = None,
    resolve_ambiguous_roles: typing.Optional[builtins.bool] = None,
    rules: typing.Optional[typing.Sequence[typing.Union[RoleMappingRule, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_token: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__786d99918d74ebff131cc6829f43e101b4ff2f81ae8498f6e87eeb4d19eeaab6(
    *,
    consumer_key: builtins.str,
    consumer_secret: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a3e6602f3dd1fc95d5e6a85eb1c6cd033f9584c3a5e317879694442cae64080(
    *,
    claim: builtins.str,
    claim_value: builtins.str,
    mapped_role: _IRole_235f5d8e,
    match_type: typing.Optional[RoleMappingMatchType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba6eb139548890358ee0627f6ab76a68ed34453606a7c47e22b81e13d0d8b649(
    scope: _constructs_77d1e7e8.Construct,
    identity_pool: IIdentityPool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e30a131979e49e3de120bda434e1aadc44c66a60ebb331ed0a7cb68845b2e58(
    *,
    client_id: builtins.str,
    provider_name: builtins.str,
    server_side_token_check: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96b0f5e74875a97abd1e74170f934c5a7746bf416d00b5b9a3a2b79560e66c96(
    *,
    user_pool: _IUserPool_1f1029e2,
    disable_server_side_token_check: typing.Optional[builtins.bool] = None,
    user_pool_client: typing.Optional[_IUserPoolClient_75623ba4] = None,
) -> None:
    """Type checking stubs"""
    pass
