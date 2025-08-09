r'''
# CDK Construct Library for Amazon Simple Notification Service Subscriptions

This library provides constructs for adding subscriptions to an Amazon SNS topic.
Subscriptions can be added by calling the `.addSubscription(...)` method on the topic.

## Subscriptions

Subscriptions can be added to the following endpoints:

* HTTPS
* Amazon SQS
* AWS Lambda
* Email
* SMS
* Amazon Data Firehose

Subscriptions to Amazon SQS, AWS Lambda and Amazon Data Firehose can be added on topics across regions.

Create an Amazon SNS Topic to add subscriptions.

```python
my_topic = sns.Topic(self, "MyTopic")
```

### HTTPS

Add an HTTP or HTTPS Subscription to your topic:

```python
my_topic = sns.Topic(self, "MyTopic")

my_topic.add_subscription(subscriptions.UrlSubscription("https://foobar.com/"))
```

The URL being subscribed can also be [tokens](https://docs.aws.amazon.com/cdk/latest/guide/tokens.html), that resolve
to a URL during deployment. A typical use case is when the URL is passed in as a [CloudFormation
parameter](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html). The
following code defines a CloudFormation parameter and uses it in a URL subscription.

```python
my_topic = sns.Topic(self, "MyTopic")
url = CfnParameter(self, "url-param")

my_topic.add_subscription(subscriptions.UrlSubscription(url.value_as_string))
```

The [delivery policy](https://docs.aws.amazon.com/sns/latest/dg/sns-message-delivery-retries.html) can also be set like so:

```python
my_topic = sns.Topic(self, "MyTopic")

my_topic.add_subscription(
    subscriptions.UrlSubscription("https://foobar.com/",
        delivery_policy=sns.DeliveryPolicy(
            healthy_retry_policy=sns.HealthyRetryPolicy(
                min_delay_target=Duration.seconds(5),
                max_delay_target=Duration.seconds(10),
                num_retries=6,
                backoff_function=sns.BackoffFunction.EXPONENTIAL
            ),
            throttle_policy=sns.ThrottlePolicy(
                max_receives_per_second=10
            ),
            request_policy=sns.RequestPolicy(
                header_content_type="application/json"
            )
        )
    ))
```

### Amazon SQS

Subscribe a queue to your topic:

```python
my_queue = sqs.Queue(self, "MyQueue")
my_topic = sns.Topic(self, "MyTopic")

my_topic.add_subscription(subscriptions.SqsSubscription(my_queue))
```

KMS key permissions will automatically be granted to SNS when a subscription is made to
an encrypted queue.

Note that subscriptions of queues in different accounts need to be manually confirmed by
reading the initial message from the queue and visiting the link found in it.

### AWS Lambda

Subscribe an AWS Lambda function to your topic:

```python
import aws_cdk.aws_lambda as lambda_
# my_function: lambda.Function


my_topic = sns.Topic(self, "myTopic")
my_topic.add_subscription(subscriptions.LambdaSubscription(my_function))
```

### Email

Subscribe an email address to your topic:

```python
my_topic = sns.Topic(self, "MyTopic")
my_topic.add_subscription(subscriptions.EmailSubscription("foo@bar.com"))
```

The email being subscribed can also be [tokens](https://docs.aws.amazon.com/cdk/latest/guide/tokens.html), that resolve
to an email address during deployment. A typical use case is when the email address is passed in as a [CloudFormation
parameter](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html). The
following code defines a CloudFormation parameter and uses it in an email subscription.

```python
my_topic = sns.Topic(self, "Topic")
email_address = CfnParameter(self, "email-param")

my_topic.add_subscription(subscriptions.EmailSubscription(email_address.value_as_string))
```

Note that email subscriptions require confirmation by visiting the link sent to the
email address.

### SMS

Subscribe an sms number to your topic:

```python
my_topic = sns.Topic(self, "Topic")

my_topic.add_subscription(subscriptions.SmsSubscription("+15551231234"))
```

The number being subscribed can also be [tokens](https://docs.aws.amazon.com/cdk/latest/guide/tokens.html), that resolve
to a number during deployment. A typical use case is when the number is passed in as a [CloudFormation
parameter](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html). The
following code defines a CloudFormation parameter and uses it in an sms subscription.

```python
my_topic = sns.Topic(self, "Topic")
sms_number = CfnParameter(self, "sms-param")

my_topic.add_subscription(subscriptions.SmsSubscription(sms_number.value_as_string))
```

### Amazon Data Firehose

Subscribe an Amazon Data Firehose delivery stream to your topic:

```python
import aws_cdk.aws_kinesisfirehose as firehose
# stream: firehose.DeliveryStream


my_topic = sns.Topic(self, "Topic")

my_topic.add_subscription(subscriptions.FirehoseSubscription(stream))
```

To remove any Amazon SNS metadata from published messages, specify `rawMessageDelivery` to true.

```python
import aws_cdk.aws_kinesisfirehose as firehose
# stream: firehose.DeliveryStream


my_topic = sns.Topic(self, "Topic")

my_topic.add_subscription(subscriptions.FirehoseSubscription(stream,
    raw_message_delivery=True
))
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

from ..aws_iam import IRole as _IRole_235f5d8e
from ..aws_kinesisfirehose import IDeliveryStream as _IDeliveryStream_8f118861
from ..aws_lambda import IFunction as _IFunction_6adb0ab8
from ..aws_sns import (
    DeliveryPolicy as _DeliveryPolicy_76b14b4e,
    FilterOrPolicy as _FilterOrPolicy_ad79be59,
    ITopic as _ITopic_9eca4852,
    ITopicSubscription as _ITopicSubscription_363a9426,
    SubscriptionFilter as _SubscriptionFilter_8e774360,
    SubscriptionProtocol as _SubscriptionProtocol_0df4af69,
    TopicSubscriptionConfig as _TopicSubscriptionConfig_3a01016e,
)
from ..aws_sqs import IQueue as _IQueue_7ed6f679


@jsii.implements(_ITopicSubscription_363a9426)
class EmailSubscription(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sns_subscriptions.EmailSubscription",
):
    '''Use an email address as a subscription target.

    Email subscriptions require confirmation.

    :exampleMetadata: infused

    Example::

        my_topic = sns.Topic(self, "Topic")
        email_address = CfnParameter(self, "email-param")
        
        my_topic.add_subscription(subscriptions.EmailSubscription(email_address.value_as_string))
    '''

    def __init__(
        self,
        email_address: builtins.str,
        *,
        json: typing.Optional[builtins.bool] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
    ) -> None:
        '''
        :param email_address: -
        :param json: Indicates if the full notification JSON should be sent to the email address or just the message text. Default: false (Message text)
        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a82616a80e8cb255f10c290c6973dc00aa57e3134cc5dc533357bb5f9a90695)
            check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
        props = EmailSubscriptionProps(
            json=json,
            dead_letter_queue=dead_letter_queue,
            filter_policy=filter_policy,
            filter_policy_with_message_body=filter_policy_with_message_body,
        )

        jsii.create(self.__class__, self, [email_address, props])

    @jsii.member(jsii_name="bind")
    def bind(self, _topic: _ITopic_9eca4852) -> _TopicSubscriptionConfig_3a01016e:
        '''Returns a configuration for an email address to subscribe to an SNS topic.

        :param _topic: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8196047448e43839102a9b8698847e0dced23efba9bc4c3183517832ea7a337e)
            check_type(argname="argument _topic", value=_topic, expected_type=type_hints["_topic"])
        return typing.cast(_TopicSubscriptionConfig_3a01016e, jsii.invoke(self, "bind", [_topic]))


@jsii.implements(_ITopicSubscription_363a9426)
class FirehoseSubscription(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sns_subscriptions.FirehoseSubscription",
):
    '''Use an Amazon Data Firehose delivery stream as a subscription target.

    :see: https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_kinesisfirehose as firehose
        # stream: firehose.DeliveryStream
        
        
        my_topic = sns.Topic(self, "Topic")
        
        my_topic.add_subscription(subscriptions.FirehoseSubscription(stream))
    '''

    def __init__(
        self,
        delivery_stream: _IDeliveryStream_8f118861,
        *,
        raw_message_delivery: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
    ) -> None:
        '''
        :param delivery_stream: -
        :param raw_message_delivery: Whether to remove any Amazon SNS metadata from published messages. Default: false
        :param role: The role to assume to write messages to the Amazon Data Firehose delivery stream. Default: - A new Role is created
        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb284a753df4f96d68b5336d14cffbd9183054fb6ebd06d8ae9d19e34dadca66)
            check_type(argname="argument delivery_stream", value=delivery_stream, expected_type=type_hints["delivery_stream"])
        props = FirehoseSubscriptionProps(
            raw_message_delivery=raw_message_delivery,
            role=role,
            dead_letter_queue=dead_letter_queue,
            filter_policy=filter_policy,
            filter_policy_with_message_body=filter_policy_with_message_body,
        )

        jsii.create(self.__class__, self, [delivery_stream, props])

    @jsii.member(jsii_name="bind")
    def bind(self, topic: _ITopic_9eca4852) -> _TopicSubscriptionConfig_3a01016e:
        '''Returns a configuration for a Lambda function to subscribe to an SNS topic.

        :param topic: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4451ffe60ee55af18e7cd4f32871e3dcb229ecdc56cfab772a77a55ca36a43d2)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        return typing.cast(_TopicSubscriptionConfig_3a01016e, jsii.invoke(self, "bind", [topic]))


@jsii.implements(_ITopicSubscription_363a9426)
class LambdaSubscription(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sns_subscriptions.LambdaSubscription",
):
    '''Use a Lambda function as a subscription target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_lambda as lambda_
        # fn: lambda.Function
        
        
        my_topic = sns.Topic(self, "MyTopic")
        
        # Lambda should receive only message matching the following conditions on message body:
        # color: 'red' or 'orange'
        my_topic.add_subscription(subscriptions.LambdaSubscription(fn,
            filter_policy_with_message_body={
                "background": sns.FilterOrPolicy.policy({
                    "color": sns.FilterOrPolicy.filter(sns.SubscriptionFilter.string_filter(
                        allowlist=["red", "orange"]
                    ))
                })
            }
        ))
    '''

    def __init__(
        self,
        fn: _IFunction_6adb0ab8,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
    ) -> None:
        '''
        :param fn: -
        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6c58b72bfa1ffbf274b6dab576c34931fb67721a57d2059607f1e3269d774cc)
            check_type(argname="argument fn", value=fn, expected_type=type_hints["fn"])
        props = LambdaSubscriptionProps(
            dead_letter_queue=dead_letter_queue,
            filter_policy=filter_policy,
            filter_policy_with_message_body=filter_policy_with_message_body,
        )

        jsii.create(self.__class__, self, [fn, props])

    @jsii.member(jsii_name="bind")
    def bind(self, topic: _ITopic_9eca4852) -> _TopicSubscriptionConfig_3a01016e:
        '''Returns a configuration for a Lambda function to subscribe to an SNS topic.

        :param topic: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c74a4a7ee6c789de81819b10c186707565592423ffbfce90f325ecb42ea9660b)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        return typing.cast(_TopicSubscriptionConfig_3a01016e, jsii.invoke(self, "bind", [topic]))


@jsii.implements(_ITopicSubscription_363a9426)
class SmsSubscription(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sns_subscriptions.SmsSubscription",
):
    '''Use an sms address as a subscription target.

    :exampleMetadata: infused

    Example::

        my_topic = sns.Topic(self, "Topic")
        
        my_topic.add_subscription(subscriptions.SmsSubscription("+15551231234"))
    '''

    def __init__(
        self,
        phone_number: builtins.str,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
    ) -> None:
        '''
        :param phone_number: -
        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2d2d80745672ed8fea4be3ee0528d1fafd95d1295c1ccaae0a9ac0121e052b9)
            check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
        props = SmsSubscriptionProps(
            dead_letter_queue=dead_letter_queue,
            filter_policy=filter_policy,
            filter_policy_with_message_body=filter_policy_with_message_body,
        )

        jsii.create(self.__class__, self, [phone_number, props])

    @jsii.member(jsii_name="bind")
    def bind(self, _topic: _ITopic_9eca4852) -> _TopicSubscriptionConfig_3a01016e:
        '''Returns a configuration used to subscribe to an SNS topic.

        :param _topic: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad95062c26a9e1173f59db80d43004d3cd582677e7e6211595db1ac44940aeeb)
            check_type(argname="argument _topic", value=_topic, expected_type=type_hints["_topic"])
        return typing.cast(_TopicSubscriptionConfig_3a01016e, jsii.invoke(self, "bind", [_topic]))


@jsii.implements(_ITopicSubscription_363a9426)
class SqsSubscription(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sns_subscriptions.SqsSubscription",
):
    '''Use an SQS queue as a subscription target.

    :exampleMetadata: infused

    Example::

        # queue: sqs.Queue
        
        my_topic = sns.Topic(self, "MyTopic")
        
        my_topic.add_subscription(subscriptions.SqsSubscription(queue))
    '''

    def __init__(
        self,
        queue: _IQueue_7ed6f679,
        *,
        raw_message_delivery: typing.Optional[builtins.bool] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
    ) -> None:
        '''
        :param queue: -
        :param raw_message_delivery: The message to the queue is the same as it was sent to the topic. If false, the message will be wrapped in an SNS envelope. Default: false
        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1fb1d07b2466c785eb4d613099f84cb5aec8abe3ab3ef6953872286f6b6b6eb)
            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
        props = SqsSubscriptionProps(
            raw_message_delivery=raw_message_delivery,
            dead_letter_queue=dead_letter_queue,
            filter_policy=filter_policy,
            filter_policy_with_message_body=filter_policy_with_message_body,
        )

        jsii.create(self.__class__, self, [queue, props])

    @jsii.member(jsii_name="bind")
    def bind(self, topic: _ITopic_9eca4852) -> _TopicSubscriptionConfig_3a01016e:
        '''Returns a configuration for an SQS queue to subscribe to an SNS topic.

        :param topic: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d393bcd5e0b8910200d6e6371a5a3f981e7c1e2160cc3e7fc5ab75cdca89c99c)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        return typing.cast(_TopicSubscriptionConfig_3a01016e, jsii.invoke(self, "bind", [topic]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns_subscriptions.SubscriptionProps",
    jsii_struct_bases=[],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "filter_policy": "filterPolicy",
        "filter_policy_with_message_body": "filterPolicyWithMessageBody",
    },
)
class SubscriptionProps:
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
    ) -> None:
        '''Options to subscribing to an SNS topic.

        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sns as sns
            from aws_cdk import aws_sns_subscriptions as sns_subscriptions
            from aws_cdk import aws_sqs as sqs
            
            # filter_or_policy: sns.FilterOrPolicy
            # queue: sqs.Queue
            # subscription_filter: sns.SubscriptionFilter
            
            subscription_props = sns_subscriptions.SubscriptionProps(
                dead_letter_queue=queue,
                filter_policy={
                    "filter_policy_key": subscription_filter
                },
                filter_policy_with_message_body={
                    "filter_policy_with_message_body_key": filter_or_policy
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cd177765ba71e4e5ee7174b2edc60b767a4303c5d9db2cdd1e6a1925a5ba213)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument filter_policy", value=filter_policy, expected_type=type_hints["filter_policy"])
            check_type(argname="argument filter_policy_with_message_body", value=filter_policy_with_message_body, expected_type=type_hints["filter_policy_with_message_body"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if filter_policy is not None:
            self._values["filter_policy"] = filter_policy
        if filter_policy_with_message_body is not None:
            self._values["filter_policy_with_message_body"] = filter_policy_with_message_body

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''Queue to be used as dead letter queue.

        If not passed no dead letter queue is enabled.

        :default: - No dead letter queue enabled.
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def filter_policy(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]]:
        '''The filter policy.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]], result)

    @builtins.property
    def filter_policy_with_message_body(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]]:
        '''The filter policy that is applied on the message body.

        To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy_with_message_body")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_ITopicSubscription_363a9426)
class UrlSubscription(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sns_subscriptions.UrlSubscription",
):
    '''Use a URL as a subscription target.

    The message will be POSTed to the given URL.

    :see: https://docs.aws.amazon.com/sns/latest/dg/sns-http-https-endpoint-as-subscriber.html
    :exampleMetadata: infused

    Example::

        my_topic = sns.Topic(self, "MyTopic")
        url = CfnParameter(self, "url-param")
        
        my_topic.add_subscription(subscriptions.UrlSubscription(url.value_as_string))
    '''

    def __init__(
        self,
        url: builtins.str,
        *,
        delivery_policy: typing.Optional[typing.Union[_DeliveryPolicy_76b14b4e, typing.Dict[builtins.str, typing.Any]]] = None,
        protocol: typing.Optional[_SubscriptionProtocol_0df4af69] = None,
        raw_message_delivery: typing.Optional[builtins.bool] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
    ) -> None:
        '''
        :param url: -
        :param delivery_policy: The delivery policy. Default: - if the initial delivery of the message fails, three retries with a delay between failed attempts set at 20 seconds
        :param protocol: The subscription's protocol. Default: - Protocol is derived from url
        :param raw_message_delivery: The message to the queue is the same as it was sent to the topic. If false, the message will be wrapped in an SNS envelope. Default: false
        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb20fb5ebe87494e3bac5aa1faafa0ee8b89a54b69e6bd2c759c374b193a6dfc)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        props = UrlSubscriptionProps(
            delivery_policy=delivery_policy,
            protocol=protocol,
            raw_message_delivery=raw_message_delivery,
            dead_letter_queue=dead_letter_queue,
            filter_policy=filter_policy,
            filter_policy_with_message_body=filter_policy_with_message_body,
        )

        jsii.create(self.__class__, self, [url, props])

    @jsii.member(jsii_name="bind")
    def bind(self, _topic: _ITopic_9eca4852) -> _TopicSubscriptionConfig_3a01016e:
        '''Returns a configuration for a URL to subscribe to an SNS topic.

        :param _topic: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd92aadeb4993c9c89443044ed067b13c5ba8d3e6272fafd3efb9a1d01d49d45)
            check_type(argname="argument _topic", value=_topic, expected_type=type_hints["_topic"])
        return typing.cast(_TopicSubscriptionConfig_3a01016e, jsii.invoke(self, "bind", [_topic]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns_subscriptions.UrlSubscriptionProps",
    jsii_struct_bases=[SubscriptionProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "filter_policy": "filterPolicy",
        "filter_policy_with_message_body": "filterPolicyWithMessageBody",
        "delivery_policy": "deliveryPolicy",
        "protocol": "protocol",
        "raw_message_delivery": "rawMessageDelivery",
    },
)
class UrlSubscriptionProps(SubscriptionProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
        delivery_policy: typing.Optional[typing.Union[_DeliveryPolicy_76b14b4e, typing.Dict[builtins.str, typing.Any]]] = None,
        protocol: typing.Optional[_SubscriptionProtocol_0df4af69] = None,
        raw_message_delivery: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for URL subscriptions.

        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered
        :param delivery_policy: The delivery policy. Default: - if the initial delivery of the message fails, three retries with a delay between failed attempts set at 20 seconds
        :param protocol: The subscription's protocol. Default: - Protocol is derived from url
        :param raw_message_delivery: The message to the queue is the same as it was sent to the topic. If false, the message will be wrapped in an SNS envelope. Default: false

        :exampleMetadata: infused

        Example::

            my_topic = sns.Topic(self, "MyTopic")
            
            my_topic.add_subscription(
                subscriptions.UrlSubscription("https://foobar.com/",
                    delivery_policy=sns.DeliveryPolicy(
                        healthy_retry_policy=sns.HealthyRetryPolicy(
                            min_delay_target=Duration.seconds(5),
                            max_delay_target=Duration.seconds(10),
                            num_retries=6,
                            backoff_function=sns.BackoffFunction.EXPONENTIAL
                        ),
                        throttle_policy=sns.ThrottlePolicy(
                            max_receives_per_second=10
                        ),
                        request_policy=sns.RequestPolicy(
                            header_content_type="application/json"
                        )
                    )
                ))
        '''
        if isinstance(delivery_policy, dict):
            delivery_policy = _DeliveryPolicy_76b14b4e(**delivery_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abe65add18291230d30a8771d08cd51f9f4eb89c5f1844a384570386c2c534ed)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument filter_policy", value=filter_policy, expected_type=type_hints["filter_policy"])
            check_type(argname="argument filter_policy_with_message_body", value=filter_policy_with_message_body, expected_type=type_hints["filter_policy_with_message_body"])
            check_type(argname="argument delivery_policy", value=delivery_policy, expected_type=type_hints["delivery_policy"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument raw_message_delivery", value=raw_message_delivery, expected_type=type_hints["raw_message_delivery"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if filter_policy is not None:
            self._values["filter_policy"] = filter_policy
        if filter_policy_with_message_body is not None:
            self._values["filter_policy_with_message_body"] = filter_policy_with_message_body
        if delivery_policy is not None:
            self._values["delivery_policy"] = delivery_policy
        if protocol is not None:
            self._values["protocol"] = protocol
        if raw_message_delivery is not None:
            self._values["raw_message_delivery"] = raw_message_delivery

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''Queue to be used as dead letter queue.

        If not passed no dead letter queue is enabled.

        :default: - No dead letter queue enabled.
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def filter_policy(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]]:
        '''The filter policy.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]], result)

    @builtins.property
    def filter_policy_with_message_body(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]]:
        '''The filter policy that is applied on the message body.

        To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy_with_message_body")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]], result)

    @builtins.property
    def delivery_policy(self) -> typing.Optional[_DeliveryPolicy_76b14b4e]:
        '''The delivery policy.

        :default: - if the initial delivery of the message fails, three retries with a delay between failed attempts set at 20 seconds
        '''
        result = self._values.get("delivery_policy")
        return typing.cast(typing.Optional[_DeliveryPolicy_76b14b4e], result)

    @builtins.property
    def protocol(self) -> typing.Optional[_SubscriptionProtocol_0df4af69]:
        '''The subscription's protocol.

        :default: - Protocol is derived from url
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[_SubscriptionProtocol_0df4af69], result)

    @builtins.property
    def raw_message_delivery(self) -> typing.Optional[builtins.bool]:
        '''The message to the queue is the same as it was sent to the topic.

        If false, the message will be wrapped in an SNS envelope.

        :default: false
        '''
        result = self._values.get("raw_message_delivery")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UrlSubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns_subscriptions.EmailSubscriptionProps",
    jsii_struct_bases=[SubscriptionProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "filter_policy": "filterPolicy",
        "filter_policy_with_message_body": "filterPolicyWithMessageBody",
        "json": "json",
    },
)
class EmailSubscriptionProps(SubscriptionProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
        json: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for email subscriptions.

        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered
        :param json: Indicates if the full notification JSON should be sent to the email address or just the message text. Default: false (Message text)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sns as sns
            from aws_cdk import aws_sns_subscriptions as sns_subscriptions
            from aws_cdk import aws_sqs as sqs
            
            # filter_or_policy: sns.FilterOrPolicy
            # queue: sqs.Queue
            # subscription_filter: sns.SubscriptionFilter
            
            email_subscription_props = sns_subscriptions.EmailSubscriptionProps(
                dead_letter_queue=queue,
                filter_policy={
                    "filter_policy_key": subscription_filter
                },
                filter_policy_with_message_body={
                    "filter_policy_with_message_body_key": filter_or_policy
                },
                json=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a78d2c696d1babec6ccfebac17827b1b6ba6f90d62674866fc5b2df7b5df3d9)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument filter_policy", value=filter_policy, expected_type=type_hints["filter_policy"])
            check_type(argname="argument filter_policy_with_message_body", value=filter_policy_with_message_body, expected_type=type_hints["filter_policy_with_message_body"])
            check_type(argname="argument json", value=json, expected_type=type_hints["json"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if filter_policy is not None:
            self._values["filter_policy"] = filter_policy
        if filter_policy_with_message_body is not None:
            self._values["filter_policy_with_message_body"] = filter_policy_with_message_body
        if json is not None:
            self._values["json"] = json

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''Queue to be used as dead letter queue.

        If not passed no dead letter queue is enabled.

        :default: - No dead letter queue enabled.
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def filter_policy(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]]:
        '''The filter policy.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]], result)

    @builtins.property
    def filter_policy_with_message_body(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]]:
        '''The filter policy that is applied on the message body.

        To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy_with_message_body")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]], result)

    @builtins.property
    def json(self) -> typing.Optional[builtins.bool]:
        '''Indicates if the full notification JSON should be sent to the email address or just the message text.

        :default: false (Message text)
        '''
        result = self._values.get("json")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmailSubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns_subscriptions.FirehoseSubscriptionProps",
    jsii_struct_bases=[SubscriptionProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "filter_policy": "filterPolicy",
        "filter_policy_with_message_body": "filterPolicyWithMessageBody",
        "raw_message_delivery": "rawMessageDelivery",
        "role": "role",
    },
)
class FirehoseSubscriptionProps(SubscriptionProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
        raw_message_delivery: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Properties for an Amazon Data Firehose subscription.

        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered
        :param raw_message_delivery: Whether to remove any Amazon SNS metadata from published messages. Default: false
        :param role: The role to assume to write messages to the Amazon Data Firehose delivery stream. Default: - A new Role is created

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_kinesisfirehose as firehose
            # stream: firehose.DeliveryStream
            
            
            my_topic = sns.Topic(self, "Topic")
            
            my_topic.add_subscription(subscriptions.FirehoseSubscription(stream,
                raw_message_delivery=True
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__985141d3216aa767af7319f266fa3eda68db2fc5132677f99b8aeb05d240609c)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument filter_policy", value=filter_policy, expected_type=type_hints["filter_policy"])
            check_type(argname="argument filter_policy_with_message_body", value=filter_policy_with_message_body, expected_type=type_hints["filter_policy_with_message_body"])
            check_type(argname="argument raw_message_delivery", value=raw_message_delivery, expected_type=type_hints["raw_message_delivery"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if filter_policy is not None:
            self._values["filter_policy"] = filter_policy
        if filter_policy_with_message_body is not None:
            self._values["filter_policy_with_message_body"] = filter_policy_with_message_body
        if raw_message_delivery is not None:
            self._values["raw_message_delivery"] = raw_message_delivery
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''Queue to be used as dead letter queue.

        If not passed no dead letter queue is enabled.

        :default: - No dead letter queue enabled.
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def filter_policy(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]]:
        '''The filter policy.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]], result)

    @builtins.property
    def filter_policy_with_message_body(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]]:
        '''The filter policy that is applied on the message body.

        To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy_with_message_body")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]], result)

    @builtins.property
    def raw_message_delivery(self) -> typing.Optional[builtins.bool]:
        '''Whether to remove any Amazon SNS metadata from published messages.

        :default: false

        :see: https://docs.aws.amazon.com/sns/latest/dg/sns-large-payload-raw-message-delivery.html
        '''
        result = self._values.get("raw_message_delivery")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The role to assume to write messages to the Amazon Data Firehose delivery stream.

        :default: - A new Role is created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirehoseSubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns_subscriptions.LambdaSubscriptionProps",
    jsii_struct_bases=[SubscriptionProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "filter_policy": "filterPolicy",
        "filter_policy_with_message_body": "filterPolicyWithMessageBody",
    },
)
class LambdaSubscriptionProps(SubscriptionProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
    ) -> None:
        '''Properties for a Lambda subscription.

        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_lambda as lambda_
            # fn: lambda.Function
            
            
            my_topic = sns.Topic(self, "MyTopic")
            
            # Lambda should receive only message matching the following conditions on attributes:
            # color: 'red' or 'orange' or begins with 'bl'
            # size: anything but 'small' or 'medium'
            # price: between 100 and 200 or greater than 300
            # store: attribute must be present
            my_topic.add_subscription(subscriptions.LambdaSubscription(fn,
                filter_policy={
                    "color": sns.SubscriptionFilter.string_filter(
                        allowlist=["red", "orange"],
                        match_prefixes=["bl"],
                        match_suffixes=["ue"]
                    ),
                    "size": sns.SubscriptionFilter.string_filter(
                        denylist=["small", "medium"]
                    ),
                    "price": sns.SubscriptionFilter.numeric_filter(
                        between=sns.BetweenCondition(start=100, stop=200),
                        greater_than=300
                    ),
                    "store": sns.SubscriptionFilter.exists_filter()
                }
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38ecc690db1f9c84ad1bee66614e7fd336ee231d47fb11fd9782c269149d5b19)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument filter_policy", value=filter_policy, expected_type=type_hints["filter_policy"])
            check_type(argname="argument filter_policy_with_message_body", value=filter_policy_with_message_body, expected_type=type_hints["filter_policy_with_message_body"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if filter_policy is not None:
            self._values["filter_policy"] = filter_policy
        if filter_policy_with_message_body is not None:
            self._values["filter_policy_with_message_body"] = filter_policy_with_message_body

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''Queue to be used as dead letter queue.

        If not passed no dead letter queue is enabled.

        :default: - No dead letter queue enabled.
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def filter_policy(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]]:
        '''The filter policy.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]], result)

    @builtins.property
    def filter_policy_with_message_body(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]]:
        '''The filter policy that is applied on the message body.

        To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy_with_message_body")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaSubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns_subscriptions.SmsSubscriptionProps",
    jsii_struct_bases=[SubscriptionProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "filter_policy": "filterPolicy",
        "filter_policy_with_message_body": "filterPolicyWithMessageBody",
    },
)
class SmsSubscriptionProps(SubscriptionProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
    ) -> None:
        '''Options for SMS subscriptions.

        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sns as sns
            from aws_cdk import aws_sns_subscriptions as sns_subscriptions
            from aws_cdk import aws_sqs as sqs
            
            # filter_or_policy: sns.FilterOrPolicy
            # queue: sqs.Queue
            # subscription_filter: sns.SubscriptionFilter
            
            sms_subscription_props = sns_subscriptions.SmsSubscriptionProps(
                dead_letter_queue=queue,
                filter_policy={
                    "filter_policy_key": subscription_filter
                },
                filter_policy_with_message_body={
                    "filter_policy_with_message_body_key": filter_or_policy
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99bb02fbcdff56a4213aeeaebfee0a11c1aaf31e49426e34489a56274562df35)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument filter_policy", value=filter_policy, expected_type=type_hints["filter_policy"])
            check_type(argname="argument filter_policy_with_message_body", value=filter_policy_with_message_body, expected_type=type_hints["filter_policy_with_message_body"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if filter_policy is not None:
            self._values["filter_policy"] = filter_policy
        if filter_policy_with_message_body is not None:
            self._values["filter_policy_with_message_body"] = filter_policy_with_message_body

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''Queue to be used as dead letter queue.

        If not passed no dead letter queue is enabled.

        :default: - No dead letter queue enabled.
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def filter_policy(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]]:
        '''The filter policy.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]], result)

    @builtins.property
    def filter_policy_with_message_body(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]]:
        '''The filter policy that is applied on the message body.

        To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy_with_message_body")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SmsSubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns_subscriptions.SqsSubscriptionProps",
    jsii_struct_bases=[SubscriptionProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "filter_policy": "filterPolicy",
        "filter_policy_with_message_body": "filterPolicyWithMessageBody",
        "raw_message_delivery": "rawMessageDelivery",
    },
)
class SqsSubscriptionProps(SubscriptionProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
        raw_message_delivery: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for an SQS subscription.

        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered
        :param raw_message_delivery: The message to the queue is the same as it was sent to the topic. If false, the message will be wrapped in an SNS envelope. Default: false

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sns as sns
            from aws_cdk import aws_sns_subscriptions as sns_subscriptions
            from aws_cdk import aws_sqs as sqs
            
            # filter_or_policy: sns.FilterOrPolicy
            # queue: sqs.Queue
            # subscription_filter: sns.SubscriptionFilter
            
            sqs_subscription_props = sns_subscriptions.SqsSubscriptionProps(
                dead_letter_queue=queue,
                filter_policy={
                    "filter_policy_key": subscription_filter
                },
                filter_policy_with_message_body={
                    "filter_policy_with_message_body_key": filter_or_policy
                },
                raw_message_delivery=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98925d4313aced10536cb11cc2fdf78fd27796f3de056153e756a0db06c594c8)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument filter_policy", value=filter_policy, expected_type=type_hints["filter_policy"])
            check_type(argname="argument filter_policy_with_message_body", value=filter_policy_with_message_body, expected_type=type_hints["filter_policy_with_message_body"])
            check_type(argname="argument raw_message_delivery", value=raw_message_delivery, expected_type=type_hints["raw_message_delivery"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if filter_policy is not None:
            self._values["filter_policy"] = filter_policy
        if filter_policy_with_message_body is not None:
            self._values["filter_policy_with_message_body"] = filter_policy_with_message_body
        if raw_message_delivery is not None:
            self._values["raw_message_delivery"] = raw_message_delivery

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''Queue to be used as dead letter queue.

        If not passed no dead letter queue is enabled.

        :default: - No dead letter queue enabled.
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def filter_policy(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]]:
        '''The filter policy.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]], result)

    @builtins.property
    def filter_policy_with_message_body(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]]:
        '''The filter policy that is applied on the message body.

        To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy_with_message_body")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]], result)

    @builtins.property
    def raw_message_delivery(self) -> typing.Optional[builtins.bool]:
        '''The message to the queue is the same as it was sent to the topic.

        If false, the message will be wrapped in an SNS envelope.

        :default: false
        '''
        result = self._values.get("raw_message_delivery")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqsSubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "EmailSubscription",
    "EmailSubscriptionProps",
    "FirehoseSubscription",
    "FirehoseSubscriptionProps",
    "LambdaSubscription",
    "LambdaSubscriptionProps",
    "SmsSubscription",
    "SmsSubscriptionProps",
    "SqsSubscription",
    "SqsSubscriptionProps",
    "SubscriptionProps",
    "UrlSubscription",
    "UrlSubscriptionProps",
]

publication.publish()

def _typecheckingstub__1a82616a80e8cb255f10c290c6973dc00aa57e3134cc5dc533357bb5f9a90695(
    email_address: builtins.str,
    *,
    json: typing.Optional[builtins.bool] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8196047448e43839102a9b8698847e0dced23efba9bc4c3183517832ea7a337e(
    _topic: _ITopic_9eca4852,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb284a753df4f96d68b5336d14cffbd9183054fb6ebd06d8ae9d19e34dadca66(
    delivery_stream: _IDeliveryStream_8f118861,
    *,
    raw_message_delivery: typing.Optional[builtins.bool] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4451ffe60ee55af18e7cd4f32871e3dcb229ecdc56cfab772a77a55ca36a43d2(
    topic: _ITopic_9eca4852,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6c58b72bfa1ffbf274b6dab576c34931fb67721a57d2059607f1e3269d774cc(
    fn: _IFunction_6adb0ab8,
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c74a4a7ee6c789de81819b10c186707565592423ffbfce90f325ecb42ea9660b(
    topic: _ITopic_9eca4852,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2d2d80745672ed8fea4be3ee0528d1fafd95d1295c1ccaae0a9ac0121e052b9(
    phone_number: builtins.str,
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad95062c26a9e1173f59db80d43004d3cd582677e7e6211595db1ac44940aeeb(
    _topic: _ITopic_9eca4852,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1fb1d07b2466c785eb4d613099f84cb5aec8abe3ab3ef6953872286f6b6b6eb(
    queue: _IQueue_7ed6f679,
    *,
    raw_message_delivery: typing.Optional[builtins.bool] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d393bcd5e0b8910200d6e6371a5a3f981e7c1e2160cc3e7fc5ab75cdca89c99c(
    topic: _ITopic_9eca4852,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cd177765ba71e4e5ee7174b2edc60b767a4303c5d9db2cdd1e6a1925a5ba213(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb20fb5ebe87494e3bac5aa1faafa0ee8b89a54b69e6bd2c759c374b193a6dfc(
    url: builtins.str,
    *,
    delivery_policy: typing.Optional[typing.Union[_DeliveryPolicy_76b14b4e, typing.Dict[builtins.str, typing.Any]]] = None,
    protocol: typing.Optional[_SubscriptionProtocol_0df4af69] = None,
    raw_message_delivery: typing.Optional[builtins.bool] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd92aadeb4993c9c89443044ed067b13c5ba8d3e6272fafd3efb9a1d01d49d45(
    _topic: _ITopic_9eca4852,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abe65add18291230d30a8771d08cd51f9f4eb89c5f1844a384570386c2c534ed(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
    delivery_policy: typing.Optional[typing.Union[_DeliveryPolicy_76b14b4e, typing.Dict[builtins.str, typing.Any]]] = None,
    protocol: typing.Optional[_SubscriptionProtocol_0df4af69] = None,
    raw_message_delivery: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a78d2c696d1babec6ccfebac17827b1b6ba6f90d62674866fc5b2df7b5df3d9(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
    json: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__985141d3216aa767af7319f266fa3eda68db2fc5132677f99b8aeb05d240609c(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
    raw_message_delivery: typing.Optional[builtins.bool] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38ecc690db1f9c84ad1bee66614e7fd336ee231d47fb11fd9782c269149d5b19(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99bb02fbcdff56a4213aeeaebfee0a11c1aaf31e49426e34489a56274562df35(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98925d4313aced10536cb11cc2fdf78fd27796f3de056153e756a0db06c594c8(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, _SubscriptionFilter_8e774360]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, _FilterOrPolicy_ad79be59]] = None,
    raw_message_delivery: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass
