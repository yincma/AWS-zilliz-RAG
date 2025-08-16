r'''
# AWS::ODB Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_odb as odb
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ODB construct libraries](https://constructs.dev/search?q=odb)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ODB resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ODB.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ODB](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ODB.html).

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
class CfnCloudAutonomousVmCluster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_odb.CfnCloudAutonomousVmCluster",
):
    '''The ``AWS::ODB::CloudAutonomousVmCluster`` resource creates an Autonomous VM cluster.

    An Autonomous VM cluster provides the infrastructure for running Autonomous Databases.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html
    :cloudformationResource: AWS::ODB::CloudAutonomousVmCluster
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_odb as odb
        
        cfn_cloud_autonomous_vm_cluster = odb.CfnCloudAutonomousVmCluster(self, "MyCfnCloudAutonomousVmCluster",
            autonomous_data_storage_size_in_tBs=123,
            cloud_exadata_infrastructure_id="cloudExadataInfrastructureId",
            cpu_core_count_per_node=123,
            db_servers=["dbServers"],
            description="description",
            display_name="displayName",
            is_mtls_enabled_vm_cluster=False,
            license_model="licenseModel",
            maintenance_window=odb.CfnCloudAutonomousVmCluster.MaintenanceWindowProperty(
                days_of_week=["daysOfWeek"],
                hours_of_day=[123],
                lead_time_in_weeks=123,
                months=["months"],
                preference="preference",
                weeks_of_month=[123]
            ),
            memory_per_oracle_compute_unit_in_gBs=123,
            odb_network_id="odbNetworkId",
            scan_listener_port_non_tls=123,
            scan_listener_port_tls=123,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            time_zone="timeZone",
            total_container_databases=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        autonomous_data_storage_size_in_t_bs: typing.Optional[jsii.Number] = None,
        cloud_exadata_infrastructure_id: typing.Optional[builtins.str] = None,
        cpu_core_count_per_node: typing.Optional[jsii.Number] = None,
        db_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        is_mtls_enabled_vm_cluster: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        license_model: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCloudAutonomousVmCluster.MaintenanceWindowProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        memory_per_oracle_compute_unit_in_g_bs: typing.Optional[jsii.Number] = None,
        odb_network_id: typing.Optional[builtins.str] = None,
        scan_listener_port_non_tls: typing.Optional[jsii.Number] = None,
        scan_listener_port_tls: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        time_zone: typing.Optional[builtins.str] = None,
        total_container_databases: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param autonomous_data_storage_size_in_t_bs: The data storage size allocated for Autonomous Databases in the Autonomous VM cluster, in TB. Required when creating an Autonomous VM cluster.
        :param cloud_exadata_infrastructure_id: The unique identifier of the Cloud Exadata Infrastructure containing this Autonomous VM cluster. Required when creating an Autonomous VM cluster.
        :param cpu_core_count_per_node: The number of CPU cores enabled per node in the Autonomous VM cluster. Required when creating an Autonomous VM cluster.
        :param db_servers: The list of database servers associated with the Autonomous VM cluster.
        :param description: The user-provided description of the Autonomous VM cluster.
        :param display_name: The display name of the Autonomous VM cluster. Required when creating an Autonomous VM cluster.
        :param is_mtls_enabled_vm_cluster: Specifies whether mutual TLS (mTLS) authentication is enabled for the Autonomous VM cluster.
        :param license_model: The Oracle license model that applies to the Autonomous VM cluster. Valid values are ``LICENSE_INCLUDED`` or ``BRING_YOUR_OWN_LICENSE`` .
        :param maintenance_window: The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.
        :param memory_per_oracle_compute_unit_in_g_bs: The amount of memory allocated per Oracle Compute Unit, in GB. Required when creating an Autonomous VM cluster.
        :param odb_network_id: The unique identifier of the ODB network associated with this Autonomous VM cluster. Required when creating an Autonomous VM cluster.
        :param scan_listener_port_non_tls: The SCAN listener port for non-TLS (TCP) protocol. The default is 1521.
        :param scan_listener_port_tls: The SCAN listener port for TLS (TCP) protocol. The default is 2484.
        :param tags: Tags to assign to the Autonomous Vm Cluster.
        :param time_zone: The time zone of the Autonomous VM cluster.
        :param total_container_databases: The total number of Autonomous Container Databases that can be created with the allocated local storage. Required when creating an Autonomous VM cluster.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5f3b11bad526801ca3c7c4e0e6c7dadf7c59ded4c26290e2160449d622fe4b7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCloudAutonomousVmClusterProps(
            autonomous_data_storage_size_in_t_bs=autonomous_data_storage_size_in_t_bs,
            cloud_exadata_infrastructure_id=cloud_exadata_infrastructure_id,
            cpu_core_count_per_node=cpu_core_count_per_node,
            db_servers=db_servers,
            description=description,
            display_name=display_name,
            is_mtls_enabled_vm_cluster=is_mtls_enabled_vm_cluster,
            license_model=license_model,
            maintenance_window=maintenance_window,
            memory_per_oracle_compute_unit_in_g_bs=memory_per_oracle_compute_unit_in_g_bs,
            odb_network_id=odb_network_id,
            scan_listener_port_non_tls=scan_listener_port_non_tls,
            scan_listener_port_tls=scan_listener_port_tls,
            tags=tags,
            time_zone=time_zone,
            total_container_databases=total_container_databases,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84a4f6b25bd9fc71f4af4608dc8d871a48a14e3aa106d9234cbf4fe28cb2b58f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1e2eb3cdd94f355c2d04e4e4acfc5c7ab515c2cf6e1291a5cd397e7293bef9dc)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAutonomousDataStoragePercentage")
    def attr_autonomous_data_storage_percentage(self) -> _IResolvable_da3f097b:
        '''The percentage of data storage currently in use for Autonomous Databases in the Autonomous VM cluster.

        :cloudformationAttribute: AutonomousDataStoragePercentage
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrAutonomousDataStoragePercentage"))

    @builtins.property
    @jsii.member(jsii_name="attrAvailableAutonomousDataStorageSizeInTBs")
    def attr_available_autonomous_data_storage_size_in_t_bs(
        self,
    ) -> _IResolvable_da3f097b:
        '''The available data storage space for Autonomous Databases in the Autonomous VM cluster, in TB.

        :cloudformationAttribute: AvailableAutonomousDataStorageSizeInTBs
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrAvailableAutonomousDataStorageSizeInTBs"))

    @builtins.property
    @jsii.member(jsii_name="attrAvailableContainerDatabases")
    def attr_available_container_databases(self) -> jsii.Number:
        '''The number of Autonomous CDBs that you can create with the currently available storage.

        :cloudformationAttribute: AvailableContainerDatabases
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAvailableContainerDatabases"))

    @builtins.property
    @jsii.member(jsii_name="attrAvailableCpus")
    def attr_available_cpus(self) -> _IResolvable_da3f097b:
        '''The number of CPU cores available for allocation to Autonomous Databases.

        :cloudformationAttribute: AvailableCpus
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrAvailableCpus"))

    @builtins.property
    @jsii.member(jsii_name="attrCloudAutonomousVmClusterArn")
    def attr_cloud_autonomous_vm_cluster_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the Autonomous VM cluster.

        :cloudformationAttribute: CloudAutonomousVmClusterArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCloudAutonomousVmClusterArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCloudAutonomousVmClusterId")
    def attr_cloud_autonomous_vm_cluster_id(self) -> builtins.str:
        '''The unique identifier of the Autonomous VM cluster.

        :cloudformationAttribute: CloudAutonomousVmClusterId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCloudAutonomousVmClusterId"))

    @builtins.property
    @jsii.member(jsii_name="attrComputeModel")
    def attr_compute_model(self) -> builtins.str:
        '''The compute model of the Autonomous VM cluster: ECPU or OCPU.

        :cloudformationAttribute: ComputeModel
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrComputeModel"))

    @builtins.property
    @jsii.member(jsii_name="attrCpuCoreCount")
    def attr_cpu_core_count(self) -> jsii.Number:
        '''The total number of CPU cores in the Autonomous VM cluster.

        :cloudformationAttribute: CpuCoreCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCpuCoreCount"))

    @builtins.property
    @jsii.member(jsii_name="attrCpuPercentage")
    def attr_cpu_percentage(self) -> _IResolvable_da3f097b:
        '''The percentage of total CPU cores currently in use in the Autonomous VM cluster.

        :cloudformationAttribute: CpuPercentage
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrCpuPercentage"))

    @builtins.property
    @jsii.member(jsii_name="attrDataStorageSizeInGBs")
    def attr_data_storage_size_in_g_bs(self) -> _IResolvable_da3f097b:
        '''The total data storage allocated to the Autonomous VM cluster, in GB.

        :cloudformationAttribute: DataStorageSizeInGBs
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrDataStorageSizeInGBs"))

    @builtins.property
    @jsii.member(jsii_name="attrDataStorageSizeInTBs")
    def attr_data_storage_size_in_t_bs(self) -> _IResolvable_da3f097b:
        '''The total data storage allocated to the Autonomous VM cluster, in TB.

        :cloudformationAttribute: DataStorageSizeInTBs
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrDataStorageSizeInTBs"))

    @builtins.property
    @jsii.member(jsii_name="attrDbNodeStorageSizeInGBs")
    def attr_db_node_storage_size_in_g_bs(self) -> jsii.Number:
        '''The local node storage allocated to the Autonomous VM cluster, in gigabytes (GB).

        :cloudformationAttribute: DbNodeStorageSizeInGBs
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrDbNodeStorageSizeInGBs"))

    @builtins.property
    @jsii.member(jsii_name="attrDomain")
    def attr_domain(self) -> builtins.str:
        '''The domain name for the Autonomous VM cluster.

        :cloudformationAttribute: Domain
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomain"))

    @builtins.property
    @jsii.member(jsii_name="attrExadataStorageInTBsLowestScaledValue")
    def attr_exadata_storage_in_t_bs_lowest_scaled_value(self) -> _IResolvable_da3f097b:
        '''The minimum value to which you can scale down the Exadata storage, in TB.

        :cloudformationAttribute: ExadataStorageInTBsLowestScaledValue
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrExadataStorageInTBsLowestScaledValue"))

    @builtins.property
    @jsii.member(jsii_name="attrHostname")
    def attr_hostname(self) -> builtins.str:
        '''The hostname for the Autonomous VM cluster.

        :cloudformationAttribute: Hostname
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHostname"))

    @builtins.property
    @jsii.member(jsii_name="attrMaxAcdsLowestScaledValue")
    def attr_max_acds_lowest_scaled_value(self) -> jsii.Number:
        '''The minimum value to which you can scale down the maximum number of Autonomous CDBs.

        :cloudformationAttribute: MaxAcdsLowestScaledValue
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrMaxAcdsLowestScaledValue"))

    @builtins.property
    @jsii.member(jsii_name="attrMemorySizeInGBs")
    def attr_memory_size_in_g_bs(self) -> jsii.Number:
        '''The total amount of memory allocated to the Autonomous VM cluster, in gigabytes (GB).

        :cloudformationAttribute: MemorySizeInGBs
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrMemorySizeInGBs"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCount")
    def attr_node_count(self) -> jsii.Number:
        '''The number of database server nodes in the Autonomous VM cluster.

        :cloudformationAttribute: NodeCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrNodeCount"))

    @builtins.property
    @jsii.member(jsii_name="attrNonProvisionableAutonomousContainerDatabases")
    def attr_non_provisionable_autonomous_container_databases(self) -> jsii.Number:
        '''The number of Autonomous CDBs that can't be provisioned because of resource constraints.

        :cloudformationAttribute: NonProvisionableAutonomousContainerDatabases
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrNonProvisionableAutonomousContainerDatabases"))

    @builtins.property
    @jsii.member(jsii_name="attrOcid")
    def attr_ocid(self) -> builtins.str:
        '''The Oracle Cloud Identifier (OCID) of the Autonomous VM cluster.

        :cloudformationAttribute: Ocid
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOcid"))

    @builtins.property
    @jsii.member(jsii_name="attrOciResourceAnchorName")
    def attr_oci_resource_anchor_name(self) -> builtins.str:
        '''The name of the OCI resource anchor associated with this Autonomous VM cluster.

        :cloudformationAttribute: OciResourceAnchorName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOciResourceAnchorName"))

    @builtins.property
    @jsii.member(jsii_name="attrOciUrl")
    def attr_oci_url(self) -> builtins.str:
        '''The URL for accessing the OCI console page for this Autonomous VM cluster.

        :cloudformationAttribute: OciUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOciUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrProvisionableAutonomousContainerDatabases")
    def attr_provisionable_autonomous_container_databases(self) -> jsii.Number:
        '''The number of Autonomous CDBs that can be provisioned in the Autonomous VM cluster.

        :cloudformationAttribute: ProvisionableAutonomousContainerDatabases
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrProvisionableAutonomousContainerDatabases"))

    @builtins.property
    @jsii.member(jsii_name="attrProvisionedAutonomousContainerDatabases")
    def attr_provisioned_autonomous_container_databases(self) -> jsii.Number:
        '''The number of Autonomous CDBs currently provisioned in the Autonomous VM cluster.

        :cloudformationAttribute: ProvisionedAutonomousContainerDatabases
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrProvisionedAutonomousContainerDatabases"))

    @builtins.property
    @jsii.member(jsii_name="attrProvisionedCpus")
    def attr_provisioned_cpus(self) -> _IResolvable_da3f097b:
        '''The number of CPU cores currently provisioned in the Autonomous VM cluster.

        :cloudformationAttribute: ProvisionedCpus
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrProvisionedCpus"))

    @builtins.property
    @jsii.member(jsii_name="attrReclaimableCpus")
    def attr_reclaimable_cpus(self) -> _IResolvable_da3f097b:
        '''The number of CPU cores that can be reclaimed from terminated or scaled-down Autonomous Databases.

        :cloudformationAttribute: ReclaimableCpus
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrReclaimableCpus"))

    @builtins.property
    @jsii.member(jsii_name="attrReservedCpus")
    def attr_reserved_cpus(self) -> _IResolvable_da3f097b:
        '''The number of CPU cores reserved for system operations and redundancy.

        :cloudformationAttribute: ReservedCpus
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrReservedCpus"))

    @builtins.property
    @jsii.member(jsii_name="attrShape")
    def attr_shape(self) -> builtins.str:
        '''The shape of the Exadata infrastructure for the Autonomous VM cluster.

        :cloudformationAttribute: Shape
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrShape"))

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
    @jsii.member(jsii_name="autonomousDataStorageSizeInTBs")
    def autonomous_data_storage_size_in_t_bs(self) -> typing.Optional[jsii.Number]:
        '''The data storage size allocated for Autonomous Databases in the Autonomous VM cluster, in TB.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autonomousDataStorageSizeInTBs"))

    @autonomous_data_storage_size_in_t_bs.setter
    def autonomous_data_storage_size_in_t_bs(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40074e4af0815e5d10dc283d57884238e94d4495641eabd516fb0756ea7c3470)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autonomousDataStorageSizeInTBs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cloudExadataInfrastructureId")
    def cloud_exadata_infrastructure_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the Cloud Exadata Infrastructure containing this Autonomous VM cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudExadataInfrastructureId"))

    @cloud_exadata_infrastructure_id.setter
    def cloud_exadata_infrastructure_id(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5301a4ddecbbb56f2a61e1dc19ab1b23bbb1871188111de8c469ba85ec8831c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudExadataInfrastructureId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cpuCoreCountPerNode")
    def cpu_core_count_per_node(self) -> typing.Optional[jsii.Number]:
        '''The number of CPU cores enabled per node in the Autonomous VM cluster.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuCoreCountPerNode"))

    @cpu_core_count_per_node.setter
    def cpu_core_count_per_node(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d5db84de12cdb3e5fabc3ed93ef628c9b5d3c1442b857b2ed5613f1ae8ee8d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuCoreCountPerNode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dbServers")
    def db_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of database servers associated with the Autonomous VM cluster.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dbServers"))

    @db_servers.setter
    def db_servers(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3920feef52a9977e900bf54bab82c28ef41365e37516fc5e8e6a08317645e7bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbServers", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The user-provided description of the Autonomous VM cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__376a9ebe12aa174628e81620a3eb8d3f7a5903598d84242a38a6521b11c10c8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the Autonomous VM cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75d262c2ba8661c4d2d20abe159b3efce30fa2a6854ff6d4d27b98c116630ce7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="isMtlsEnabledVmCluster")
    def is_mtls_enabled_vm_cluster(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether mutual TLS (mTLS) authentication is enabled for the Autonomous VM cluster.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "isMtlsEnabledVmCluster"))

    @is_mtls_enabled_vm_cluster.setter
    def is_mtls_enabled_vm_cluster(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b71c28f08596e3a8e06bf9ac61f202a72d06b5f6a93ae96a6cd988fa2c8b3457)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isMtlsEnabledVmCluster", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="licenseModel")
    def license_model(self) -> typing.Optional[builtins.str]:
        '''The Oracle license model that applies to the Autonomous VM cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseModel"))

    @license_model.setter
    def license_model(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__429e238c2071c653da37b075f2da161573e5972cfc94448900389409da574e63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseModel", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCloudAutonomousVmCluster.MaintenanceWindowProperty"]]:
        '''The scheduling details for the maintenance window.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCloudAutonomousVmCluster.MaintenanceWindowProperty"]], jsii.get(self, "maintenanceWindow"))

    @maintenance_window.setter
    def maintenance_window(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCloudAutonomousVmCluster.MaintenanceWindowProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9893af2fa0c239ed09a25053b836f4c53aa964e484761b3656bf3f69ee2f20aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceWindow", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="memoryPerOracleComputeUnitInGBs")
    def memory_per_oracle_compute_unit_in_g_bs(self) -> typing.Optional[jsii.Number]:
        '''The amount of memory allocated per Oracle Compute Unit, in GB.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryPerOracleComputeUnitInGBs"))

    @memory_per_oracle_compute_unit_in_g_bs.setter
    def memory_per_oracle_compute_unit_in_g_bs(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd777a3c3d03d11ff6d441f65051a7d1dcba1c191c5da7776d901c5b9765eb42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryPerOracleComputeUnitInGBs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="odbNetworkId")
    def odb_network_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the ODB network associated with this Autonomous VM cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "odbNetworkId"))

    @odb_network_id.setter
    def odb_network_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d834f35ba34f357c207777de5cc71d5a4ff7f1fc34d7d2258c384cf3f2fe69ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "odbNetworkId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scanListenerPortNonTls")
    def scan_listener_port_non_tls(self) -> typing.Optional[jsii.Number]:
        '''The SCAN listener port for non-TLS (TCP) protocol.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scanListenerPortNonTls"))

    @scan_listener_port_non_tls.setter
    def scan_listener_port_non_tls(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd9cf4eca6ac7c9c9481d6618538bfd5cfd343c9c4dee27e927e579919f0ee93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scanListenerPortNonTls", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scanListenerPortTls")
    def scan_listener_port_tls(self) -> typing.Optional[jsii.Number]:
        '''The SCAN listener port for TLS (TCP) protocol.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scanListenerPortTls"))

    @scan_listener_port_tls.setter
    def scan_listener_port_tls(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a7c3ab9bede20a7946889e0e134a092708444b390ea3a2deaafb7e86de212cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scanListenerPortTls", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags to assign to the Autonomous Vm Cluster.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c0f9eb455c371aedd7a5d89d20d74ae053b5c2fbe1fd8e6614a484ac7e8c9a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''The time zone of the Autonomous VM cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8343f27429e0f5eae088fa7811047979c32cb60a08a24cfaa30bd3ccb47ed883)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="totalContainerDatabases")
    def total_container_databases(self) -> typing.Optional[jsii.Number]:
        '''The total number of Autonomous Container Databases that can be created with the allocated local storage.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "totalContainerDatabases"))

    @total_container_databases.setter
    def total_container_databases(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f4f14ad61521ea763f91422ba382ad5682e9530d8b2883c57ade0003139ff56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "totalContainerDatabases", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_odb.CfnCloudAutonomousVmCluster.MaintenanceWindowProperty",
        jsii_struct_bases=[],
        name_mapping={
            "days_of_week": "daysOfWeek",
            "hours_of_day": "hoursOfDay",
            "lead_time_in_weeks": "leadTimeInWeeks",
            "months": "months",
            "preference": "preference",
            "weeks_of_month": "weeksOfMonth",
        },
    )
    class MaintenanceWindowProperty:
        def __init__(
            self,
            *,
            days_of_week: typing.Optional[typing.Sequence[builtins.str]] = None,
            hours_of_day: typing.Optional[typing.Union[typing.Sequence[jsii.Number], _IResolvable_da3f097b]] = None,
            lead_time_in_weeks: typing.Optional[jsii.Number] = None,
            months: typing.Optional[typing.Sequence[builtins.str]] = None,
            preference: typing.Optional[builtins.str] = None,
            weeks_of_month: typing.Optional[typing.Union[typing.Sequence[jsii.Number], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The scheduling details for the maintenance window.

            Patching and system updates take place during the maintenance window.

            :param days_of_week: The days of the week when maintenance can be performed.
            :param hours_of_day: The hours of the day when maintenance can be performed.
            :param lead_time_in_weeks: The lead time in weeks before the maintenance window.
            :param months: The months when maintenance can be performed.
            :param preference: The preference for the maintenance window scheduling.
            :param weeks_of_month: The weeks of the month when maintenance can be performed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-odb-cloudautonomousvmcluster-maintenancewindow.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_odb as odb
                
                maintenance_window_property = odb.CfnCloudAutonomousVmCluster.MaintenanceWindowProperty(
                    days_of_week=["daysOfWeek"],
                    hours_of_day=[123],
                    lead_time_in_weeks=123,
                    months=["months"],
                    preference="preference",
                    weeks_of_month=[123]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bec420fa64b103170ca1fde88b7f5526381889811659e8a32ae9356eed292838)
                check_type(argname="argument days_of_week", value=days_of_week, expected_type=type_hints["days_of_week"])
                check_type(argname="argument hours_of_day", value=hours_of_day, expected_type=type_hints["hours_of_day"])
                check_type(argname="argument lead_time_in_weeks", value=lead_time_in_weeks, expected_type=type_hints["lead_time_in_weeks"])
                check_type(argname="argument months", value=months, expected_type=type_hints["months"])
                check_type(argname="argument preference", value=preference, expected_type=type_hints["preference"])
                check_type(argname="argument weeks_of_month", value=weeks_of_month, expected_type=type_hints["weeks_of_month"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if days_of_week is not None:
                self._values["days_of_week"] = days_of_week
            if hours_of_day is not None:
                self._values["hours_of_day"] = hours_of_day
            if lead_time_in_weeks is not None:
                self._values["lead_time_in_weeks"] = lead_time_in_weeks
            if months is not None:
                self._values["months"] = months
            if preference is not None:
                self._values["preference"] = preference
            if weeks_of_month is not None:
                self._values["weeks_of_month"] = weeks_of_month

        @builtins.property
        def days_of_week(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The days of the week when maintenance can be performed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-odb-cloudautonomousvmcluster-maintenancewindow.html#cfn-odb-cloudautonomousvmcluster-maintenancewindow-daysofweek
            '''
            result = self._values.get("days_of_week")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def hours_of_day(
            self,
        ) -> typing.Optional[typing.Union[typing.List[jsii.Number], _IResolvable_da3f097b]]:
            '''The hours of the day when maintenance can be performed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-odb-cloudautonomousvmcluster-maintenancewindow.html#cfn-odb-cloudautonomousvmcluster-maintenancewindow-hoursofday
            '''
            result = self._values.get("hours_of_day")
            return typing.cast(typing.Optional[typing.Union[typing.List[jsii.Number], _IResolvable_da3f097b]], result)

        @builtins.property
        def lead_time_in_weeks(self) -> typing.Optional[jsii.Number]:
            '''The lead time in weeks before the maintenance window.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-odb-cloudautonomousvmcluster-maintenancewindow.html#cfn-odb-cloudautonomousvmcluster-maintenancewindow-leadtimeinweeks
            '''
            result = self._values.get("lead_time_in_weeks")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def months(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The months when maintenance can be performed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-odb-cloudautonomousvmcluster-maintenancewindow.html#cfn-odb-cloudautonomousvmcluster-maintenancewindow-months
            '''
            result = self._values.get("months")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def preference(self) -> typing.Optional[builtins.str]:
            '''The preference for the maintenance window scheduling.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-odb-cloudautonomousvmcluster-maintenancewindow.html#cfn-odb-cloudautonomousvmcluster-maintenancewindow-preference
            '''
            result = self._values.get("preference")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def weeks_of_month(
            self,
        ) -> typing.Optional[typing.Union[typing.List[jsii.Number], _IResolvable_da3f097b]]:
            '''The weeks of the month when maintenance can be performed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-odb-cloudautonomousvmcluster-maintenancewindow.html#cfn-odb-cloudautonomousvmcluster-maintenancewindow-weeksofmonth
            '''
            result = self._values.get("weeks_of_month")
            return typing.cast(typing.Optional[typing.Union[typing.List[jsii.Number], _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceWindowProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_odb.CfnCloudAutonomousVmClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "autonomous_data_storage_size_in_t_bs": "autonomousDataStorageSizeInTBs",
        "cloud_exadata_infrastructure_id": "cloudExadataInfrastructureId",
        "cpu_core_count_per_node": "cpuCoreCountPerNode",
        "db_servers": "dbServers",
        "description": "description",
        "display_name": "displayName",
        "is_mtls_enabled_vm_cluster": "isMtlsEnabledVmCluster",
        "license_model": "licenseModel",
        "maintenance_window": "maintenanceWindow",
        "memory_per_oracle_compute_unit_in_g_bs": "memoryPerOracleComputeUnitInGBs",
        "odb_network_id": "odbNetworkId",
        "scan_listener_port_non_tls": "scanListenerPortNonTls",
        "scan_listener_port_tls": "scanListenerPortTls",
        "tags": "tags",
        "time_zone": "timeZone",
        "total_container_databases": "totalContainerDatabases",
    },
)
class CfnCloudAutonomousVmClusterProps:
    def __init__(
        self,
        *,
        autonomous_data_storage_size_in_t_bs: typing.Optional[jsii.Number] = None,
        cloud_exadata_infrastructure_id: typing.Optional[builtins.str] = None,
        cpu_core_count_per_node: typing.Optional[jsii.Number] = None,
        db_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        is_mtls_enabled_vm_cluster: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        license_model: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCloudAutonomousVmCluster.MaintenanceWindowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        memory_per_oracle_compute_unit_in_g_bs: typing.Optional[jsii.Number] = None,
        odb_network_id: typing.Optional[builtins.str] = None,
        scan_listener_port_non_tls: typing.Optional[jsii.Number] = None,
        scan_listener_port_tls: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        time_zone: typing.Optional[builtins.str] = None,
        total_container_databases: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnCloudAutonomousVmCluster``.

        :param autonomous_data_storage_size_in_t_bs: The data storage size allocated for Autonomous Databases in the Autonomous VM cluster, in TB. Required when creating an Autonomous VM cluster.
        :param cloud_exadata_infrastructure_id: The unique identifier of the Cloud Exadata Infrastructure containing this Autonomous VM cluster. Required when creating an Autonomous VM cluster.
        :param cpu_core_count_per_node: The number of CPU cores enabled per node in the Autonomous VM cluster. Required when creating an Autonomous VM cluster.
        :param db_servers: The list of database servers associated with the Autonomous VM cluster.
        :param description: The user-provided description of the Autonomous VM cluster.
        :param display_name: The display name of the Autonomous VM cluster. Required when creating an Autonomous VM cluster.
        :param is_mtls_enabled_vm_cluster: Specifies whether mutual TLS (mTLS) authentication is enabled for the Autonomous VM cluster.
        :param license_model: The Oracle license model that applies to the Autonomous VM cluster. Valid values are ``LICENSE_INCLUDED`` or ``BRING_YOUR_OWN_LICENSE`` .
        :param maintenance_window: The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.
        :param memory_per_oracle_compute_unit_in_g_bs: The amount of memory allocated per Oracle Compute Unit, in GB. Required when creating an Autonomous VM cluster.
        :param odb_network_id: The unique identifier of the ODB network associated with this Autonomous VM cluster. Required when creating an Autonomous VM cluster.
        :param scan_listener_port_non_tls: The SCAN listener port for non-TLS (TCP) protocol. The default is 1521.
        :param scan_listener_port_tls: The SCAN listener port for TLS (TCP) protocol. The default is 2484.
        :param tags: Tags to assign to the Autonomous Vm Cluster.
        :param time_zone: The time zone of the Autonomous VM cluster.
        :param total_container_databases: The total number of Autonomous Container Databases that can be created with the allocated local storage. Required when creating an Autonomous VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_odb as odb
            
            cfn_cloud_autonomous_vm_cluster_props = odb.CfnCloudAutonomousVmClusterProps(
                autonomous_data_storage_size_in_tBs=123,
                cloud_exadata_infrastructure_id="cloudExadataInfrastructureId",
                cpu_core_count_per_node=123,
                db_servers=["dbServers"],
                description="description",
                display_name="displayName",
                is_mtls_enabled_vm_cluster=False,
                license_model="licenseModel",
                maintenance_window=odb.CfnCloudAutonomousVmCluster.MaintenanceWindowProperty(
                    days_of_week=["daysOfWeek"],
                    hours_of_day=[123],
                    lead_time_in_weeks=123,
                    months=["months"],
                    preference="preference",
                    weeks_of_month=[123]
                ),
                memory_per_oracle_compute_unit_in_gBs=123,
                odb_network_id="odbNetworkId",
                scan_listener_port_non_tls=123,
                scan_listener_port_tls=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                time_zone="timeZone",
                total_container_databases=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__221a7c6782ef0d7603f8cd9a8a17d1bbaad9d65511e49e607ac274b8a007d48b)
            check_type(argname="argument autonomous_data_storage_size_in_t_bs", value=autonomous_data_storage_size_in_t_bs, expected_type=type_hints["autonomous_data_storage_size_in_t_bs"])
            check_type(argname="argument cloud_exadata_infrastructure_id", value=cloud_exadata_infrastructure_id, expected_type=type_hints["cloud_exadata_infrastructure_id"])
            check_type(argname="argument cpu_core_count_per_node", value=cpu_core_count_per_node, expected_type=type_hints["cpu_core_count_per_node"])
            check_type(argname="argument db_servers", value=db_servers, expected_type=type_hints["db_servers"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument is_mtls_enabled_vm_cluster", value=is_mtls_enabled_vm_cluster, expected_type=type_hints["is_mtls_enabled_vm_cluster"])
            check_type(argname="argument license_model", value=license_model, expected_type=type_hints["license_model"])
            check_type(argname="argument maintenance_window", value=maintenance_window, expected_type=type_hints["maintenance_window"])
            check_type(argname="argument memory_per_oracle_compute_unit_in_g_bs", value=memory_per_oracle_compute_unit_in_g_bs, expected_type=type_hints["memory_per_oracle_compute_unit_in_g_bs"])
            check_type(argname="argument odb_network_id", value=odb_network_id, expected_type=type_hints["odb_network_id"])
            check_type(argname="argument scan_listener_port_non_tls", value=scan_listener_port_non_tls, expected_type=type_hints["scan_listener_port_non_tls"])
            check_type(argname="argument scan_listener_port_tls", value=scan_listener_port_tls, expected_type=type_hints["scan_listener_port_tls"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
            check_type(argname="argument total_container_databases", value=total_container_databases, expected_type=type_hints["total_container_databases"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if autonomous_data_storage_size_in_t_bs is not None:
            self._values["autonomous_data_storage_size_in_t_bs"] = autonomous_data_storage_size_in_t_bs
        if cloud_exadata_infrastructure_id is not None:
            self._values["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id
        if cpu_core_count_per_node is not None:
            self._values["cpu_core_count_per_node"] = cpu_core_count_per_node
        if db_servers is not None:
            self._values["db_servers"] = db_servers
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if is_mtls_enabled_vm_cluster is not None:
            self._values["is_mtls_enabled_vm_cluster"] = is_mtls_enabled_vm_cluster
        if license_model is not None:
            self._values["license_model"] = license_model
        if maintenance_window is not None:
            self._values["maintenance_window"] = maintenance_window
        if memory_per_oracle_compute_unit_in_g_bs is not None:
            self._values["memory_per_oracle_compute_unit_in_g_bs"] = memory_per_oracle_compute_unit_in_g_bs
        if odb_network_id is not None:
            self._values["odb_network_id"] = odb_network_id
        if scan_listener_port_non_tls is not None:
            self._values["scan_listener_port_non_tls"] = scan_listener_port_non_tls
        if scan_listener_port_tls is not None:
            self._values["scan_listener_port_tls"] = scan_listener_port_tls
        if tags is not None:
            self._values["tags"] = tags
        if time_zone is not None:
            self._values["time_zone"] = time_zone
        if total_container_databases is not None:
            self._values["total_container_databases"] = total_container_databases

    @builtins.property
    def autonomous_data_storage_size_in_t_bs(self) -> typing.Optional[jsii.Number]:
        '''The data storage size allocated for Autonomous Databases in the Autonomous VM cluster, in TB.

        Required when creating an Autonomous VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html#cfn-odb-cloudautonomousvmcluster-autonomousdatastoragesizeintbs
        '''
        result = self._values.get("autonomous_data_storage_size_in_t_bs")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cloud_exadata_infrastructure_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the Cloud Exadata Infrastructure containing this Autonomous VM cluster.

        Required when creating an Autonomous VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html#cfn-odb-cloudautonomousvmcluster-cloudexadatainfrastructureid
        '''
        result = self._values.get("cloud_exadata_infrastructure_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpu_core_count_per_node(self) -> typing.Optional[jsii.Number]:
        '''The number of CPU cores enabled per node in the Autonomous VM cluster.

        Required when creating an Autonomous VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html#cfn-odb-cloudautonomousvmcluster-cpucorecountpernode
        '''
        result = self._values.get("cpu_core_count_per_node")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def db_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of database servers associated with the Autonomous VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html#cfn-odb-cloudautonomousvmcluster-dbservers
        '''
        result = self._values.get("db_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The user-provided description of the Autonomous VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html#cfn-odb-cloudautonomousvmcluster-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the Autonomous VM cluster.

        Required when creating an Autonomous VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html#cfn-odb-cloudautonomousvmcluster-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_mtls_enabled_vm_cluster(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether mutual TLS (mTLS) authentication is enabled for the Autonomous VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html#cfn-odb-cloudautonomousvmcluster-ismtlsenabledvmcluster
        '''
        result = self._values.get("is_mtls_enabled_vm_cluster")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def license_model(self) -> typing.Optional[builtins.str]:
        '''The Oracle license model that applies to the Autonomous VM cluster.

        Valid values are ``LICENSE_INCLUDED`` or ``BRING_YOUR_OWN_LICENSE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html#cfn-odb-cloudautonomousvmcluster-licensemodel
        '''
        result = self._values.get("license_model")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_window(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCloudAutonomousVmCluster.MaintenanceWindowProperty]]:
        '''The scheduling details for the maintenance window.

        Patching and system updates take place during the maintenance window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html#cfn-odb-cloudautonomousvmcluster-maintenancewindow
        '''
        result = self._values.get("maintenance_window")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCloudAutonomousVmCluster.MaintenanceWindowProperty]], result)

    @builtins.property
    def memory_per_oracle_compute_unit_in_g_bs(self) -> typing.Optional[jsii.Number]:
        '''The amount of memory allocated per Oracle Compute Unit, in GB.

        Required when creating an Autonomous VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html#cfn-odb-cloudautonomousvmcluster-memoryperoraclecomputeunitingbs
        '''
        result = self._values.get("memory_per_oracle_compute_unit_in_g_bs")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def odb_network_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the ODB network associated with this Autonomous VM cluster.

        Required when creating an Autonomous VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html#cfn-odb-cloudautonomousvmcluster-odbnetworkid
        '''
        result = self._values.get("odb_network_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scan_listener_port_non_tls(self) -> typing.Optional[jsii.Number]:
        '''The SCAN listener port for non-TLS (TCP) protocol.

        The default is 1521.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html#cfn-odb-cloudautonomousvmcluster-scanlistenerportnontls
        '''
        result = self._values.get("scan_listener_port_non_tls")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scan_listener_port_tls(self) -> typing.Optional[jsii.Number]:
        '''The SCAN listener port for TLS (TCP) protocol.

        The default is 2484.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html#cfn-odb-cloudautonomousvmcluster-scanlistenerporttls
        '''
        result = self._values.get("scan_listener_port_tls")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags to assign to the Autonomous Vm Cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html#cfn-odb-cloudautonomousvmcluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''The time zone of the Autonomous VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html#cfn-odb-cloudautonomousvmcluster-timezone
        '''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def total_container_databases(self) -> typing.Optional[jsii.Number]:
        '''The total number of Autonomous Container Databases that can be created with the allocated local storage.

        Required when creating an Autonomous VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudautonomousvmcluster.html#cfn-odb-cloudautonomousvmcluster-totalcontainerdatabases
        '''
        result = self._values.get("total_container_databases")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudAutonomousVmClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnCloudExadataInfrastructure(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_odb.CfnCloudExadataInfrastructure",
):
    '''The ``AWS::ODB::CloudExadataInfrastructure`` resource creates an Exadata infrastructure.

    An Exadata infrastructure provides the underlying compute and storage resources for Oracle Database workloads.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudexadatainfrastructure.html
    :cloudformationResource: AWS::ODB::CloudExadataInfrastructure
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_odb as odb
        
        cfn_cloud_exadata_infrastructure = odb.CfnCloudExadataInfrastructure(self, "MyCfnCloudExadataInfrastructure",
            availability_zone="availabilityZone",
            availability_zone_id="availabilityZoneId",
            compute_count=123,
            customer_contacts_to_send_to_oci=[odb.CfnCloudExadataInfrastructure.CustomerContactProperty(
                email="email"
            )],
            database_server_type="databaseServerType",
            display_name="displayName",
            shape="shape",
            storage_count=123,
            storage_server_type="storageServerType",
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
        availability_zone: typing.Optional[builtins.str] = None,
        availability_zone_id: typing.Optional[builtins.str] = None,
        compute_count: typing.Optional[jsii.Number] = None,
        customer_contacts_to_send_to_oci: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCloudExadataInfrastructure.CustomerContactProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        database_server_type: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        shape: typing.Optional[builtins.str] = None,
        storage_count: typing.Optional[jsii.Number] = None,
        storage_server_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param availability_zone: The name of the Availability Zone (AZ) where the Exadata infrastructure is located. Required when creating an Exadata infrastructure. Specify either AvailabilityZone or AvailabilityZoneId to define the location of the infrastructure.
        :param availability_zone_id: The AZ ID of the AZ where the Exadata infrastructure is located. Required when creating an Exadata infrastructure. Specify either AvailabilityZone or AvailabilityZoneId to define the location of the infrastructure.
        :param compute_count: The number of database servers for the Exadata infrastructure. Required when creating an Exadata infrastructure.
        :param customer_contacts_to_send_to_oci: The email addresses of contacts to receive notification from Oracle about maintenance updates for the Exadata infrastructure.
        :param database_server_type: The database server model type of the Exadata infrastructure. For the list of valid model names, use the ``ListDbSystemShapes`` operation.
        :param display_name: The user-friendly name for the Exadata infrastructure. Required when creating an Exadata infrastructure.
        :param shape: The model name of the Exadata infrastructure. Required when creating an Exadata infrastructure.
        :param storage_count: The number of storage servers that are activated for the Exadata infrastructure. Required when creating an Exadata infrastructure.
        :param storage_server_type: The storage server model type of the Exadata infrastructure. For the list of valid model names, use the ``ListDbSystemShapes`` operation.
        :param tags: Tags to assign to the Exadata Infrastructure.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd782f736e7ad827f171e15d160c54071c1fbef5443d136721533cbfdcdb7012)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCloudExadataInfrastructureProps(
            availability_zone=availability_zone,
            availability_zone_id=availability_zone_id,
            compute_count=compute_count,
            customer_contacts_to_send_to_oci=customer_contacts_to_send_to_oci,
            database_server_type=database_server_type,
            display_name=display_name,
            shape=shape,
            storage_count=storage_count,
            storage_server_type=storage_server_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f2b53aab94ecf4f8defcc0e14b676f19557d80b7dd0f9ff46a17b7649889a87)
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
            type_hints = typing.get_type_hints(_typecheckingstub__30c5d730c06a06b60c97eec0e4a7fec63bac2317a2c033784ea9da48cda003b4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrActivatedStorageCount")
    def attr_activated_storage_count(self) -> jsii.Number:
        '''The number of storage servers requested for the Exadata infrastructure.

        :cloudformationAttribute: ActivatedStorageCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrActivatedStorageCount"))

    @builtins.property
    @jsii.member(jsii_name="attrAdditionalStorageCount")
    def attr_additional_storage_count(self) -> jsii.Number:
        '''The number of storage servers requested for the Exadata infrastructure.

        :cloudformationAttribute: AdditionalStorageCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAdditionalStorageCount"))

    @builtins.property
    @jsii.member(jsii_name="attrAvailableStorageSizeInGBs")
    def attr_available_storage_size_in_g_bs(self) -> jsii.Number:
        '''The amount of available storage, in gigabytes (GB), for the Exadata infrastructure.

        :cloudformationAttribute: AvailableStorageSizeInGBs
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAvailableStorageSizeInGBs"))

    @builtins.property
    @jsii.member(jsii_name="attrCloudExadataInfrastructureArn")
    def attr_cloud_exadata_infrastructure_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the Exadata infrastructure.

        :cloudformationAttribute: CloudExadataInfrastructureArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCloudExadataInfrastructureArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCloudExadataInfrastructureId")
    def attr_cloud_exadata_infrastructure_id(self) -> builtins.str:
        '''The unique identifier for the Exadata infrastructure.

        :cloudformationAttribute: CloudExadataInfrastructureId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCloudExadataInfrastructureId"))

    @builtins.property
    @jsii.member(jsii_name="attrComputeModel")
    def attr_compute_model(self) -> builtins.str:
        '''The OCI model compute model used when you create or clone an instance: ECPU or OCPU.

        An ECPU is an abstracted measure of compute resources. ECPUs are based on the number of cores elastically allocated from a pool of compute and storage servers. An OCPU is a legacy physical measure of compute resources. OCPUs are based on the physical core of a processor with hyper-threading enabled.

        :cloudformationAttribute: ComputeModel
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrComputeModel"))

    @builtins.property
    @jsii.member(jsii_name="attrCpuCount")
    def attr_cpu_count(self) -> jsii.Number:
        '''The total number of CPU cores that are allocated to the Exadata infrastructure.

        :cloudformationAttribute: CpuCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCpuCount"))

    @builtins.property
    @jsii.member(jsii_name="attrDataStorageSizeInTBs")
    def attr_data_storage_size_in_t_bs(self) -> _IResolvable_da3f097b:
        '''The size of the Exadata infrastructure's data disk group, in terabytes (TB).

        :cloudformationAttribute: DataStorageSizeInTBs
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrDataStorageSizeInTBs"))

    @builtins.property
    @jsii.member(jsii_name="attrDbNodeStorageSizeInGBs")
    def attr_db_node_storage_size_in_g_bs(self) -> jsii.Number:
        '''The size of the Exadata infrastructure's local node storage, in gigabytes (GB).

        :cloudformationAttribute: DbNodeStorageSizeInGBs
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrDbNodeStorageSizeInGBs"))

    @builtins.property
    @jsii.member(jsii_name="attrDbServerIds")
    def attr_db_server_ids(self) -> typing.List[builtins.str]:
        '''The list of database server identifiers for the Exadata infrastructure.

        :cloudformationAttribute: DbServerIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDbServerIds"))

    @builtins.property
    @jsii.member(jsii_name="attrDbServerVersion")
    def attr_db_server_version(self) -> builtins.str:
        '''The software version of the database servers (dom0) in the Exadata infrastructure.

        :cloudformationAttribute: DbServerVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDbServerVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrMaxCpuCount")
    def attr_max_cpu_count(self) -> jsii.Number:
        '''The total number of CPU cores available on the Exadata infrastructure.

        :cloudformationAttribute: MaxCpuCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrMaxCpuCount"))

    @builtins.property
    @jsii.member(jsii_name="attrMaxDataStorageInTBs")
    def attr_max_data_storage_in_t_bs(self) -> _IResolvable_da3f097b:
        '''The total amount of data disk group storage, in terabytes (TB), that's available on the Exadata infrastructure.

        :cloudformationAttribute: MaxDataStorageInTBs
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrMaxDataStorageInTBs"))

    @builtins.property
    @jsii.member(jsii_name="attrMaxDbNodeStorageSizeInGBs")
    def attr_max_db_node_storage_size_in_g_bs(self) -> jsii.Number:
        '''The total amount of local node storage, in gigabytes (GB), that's available on the Exadata infrastructure.

        :cloudformationAttribute: MaxDbNodeStorageSizeInGBs
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrMaxDbNodeStorageSizeInGBs"))

    @builtins.property
    @jsii.member(jsii_name="attrMaxMemoryInGBs")
    def attr_max_memory_in_g_bs(self) -> jsii.Number:
        '''The total amount of memory, in gigabytes (GB), that's available on the Exadata infrastructure.

        :cloudformationAttribute: MaxMemoryInGBs
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrMaxMemoryInGBs"))

    @builtins.property
    @jsii.member(jsii_name="attrMemorySizeInGBs")
    def attr_memory_size_in_g_bs(self) -> jsii.Number:
        '''The amount of memory, in gigabytes (GB), that's allocated on the Exadata infrastructure.

        :cloudformationAttribute: MemorySizeInGBs
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrMemorySizeInGBs"))

    @builtins.property
    @jsii.member(jsii_name="attrOcid")
    def attr_ocid(self) -> builtins.str:
        '''The OCID of the Exadata infrastructure.

        :cloudformationAttribute: Ocid
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOcid"))

    @builtins.property
    @jsii.member(jsii_name="attrOciResourceAnchorName")
    def attr_oci_resource_anchor_name(self) -> builtins.str:
        '''The name of the OCI resource anchor for the Exadata infrastructure.

        :cloudformationAttribute: OciResourceAnchorName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOciResourceAnchorName"))

    @builtins.property
    @jsii.member(jsii_name="attrOciUrl")
    def attr_oci_url(self) -> builtins.str:
        '''The HTTPS link to the Exadata infrastructure in OCI.

        :cloudformationAttribute: OciUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOciUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrStorageServerVersion")
    def attr_storage_server_version(self) -> builtins.str:
        '''The software version of the storage servers on the Exadata infrastructure.

        :cloudformationAttribute: StorageServerVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStorageServerVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrTotalStorageSizeInGBs")
    def attr_total_storage_size_in_g_bs(self) -> jsii.Number:
        '''The total amount of storage, in gigabytes (GB), on the the Exadata infrastructure.

        :cloudformationAttribute: TotalStorageSizeInGBs
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrTotalStorageSizeInGBs"))

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
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The name of the Availability Zone (AZ) where the Exadata infrastructure is located.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c16313314e3dc88f64b64a6807c0212a1ebb85e656c09cf7edb0f12490e36f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneId")
    def availability_zone_id(self) -> typing.Optional[builtins.str]:
        '''The AZ ID of the AZ where the Exadata infrastructure is located.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneId"))

    @availability_zone_id.setter
    def availability_zone_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2438c10c6661d5ac7195e2cd938683127ead28b38288093164aed692e449d80a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZoneId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="computeCount")
    def compute_count(self) -> typing.Optional[jsii.Number]:
        '''The number of database servers for the Exadata infrastructure.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "computeCount"))

    @compute_count.setter
    def compute_count(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed6c897fe570d07a340273c57b43f97da5d100a17ae8701b161d22cf07674db5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeCount", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="customerContactsToSendToOci")
    def customer_contacts_to_send_to_oci(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCloudExadataInfrastructure.CustomerContactProperty"]]]]:
        '''The email addresses of contacts to receive notification from Oracle about maintenance updates for the Exadata infrastructure.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCloudExadataInfrastructure.CustomerContactProperty"]]]], jsii.get(self, "customerContactsToSendToOci"))

    @customer_contacts_to_send_to_oci.setter
    def customer_contacts_to_send_to_oci(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCloudExadataInfrastructure.CustomerContactProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__564d722d30f571b6b15ec3202d92d33e97da84125c2eabe6a9cebe8d28fed3d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerContactsToSendToOci", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseServerType")
    def database_server_type(self) -> typing.Optional[builtins.str]:
        '''The database server model type of the Exadata infrastructure.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseServerType"))

    @database_server_type.setter
    def database_server_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e15e2bca6e90c311020132fc94b88d4dd573507aadbba5a8fddfbd5970990a3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseServerType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The user-friendly name for the Exadata infrastructure.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d12c1cc442676c06c38458b560f32148a7562dbf983c5df26ac19ffea7c7ee58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="shape")
    def shape(self) -> typing.Optional[builtins.str]:
        '''The model name of the Exadata infrastructure.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shape"))

    @shape.setter
    def shape(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__044d56c3db02ff4cda6e4851e60243f1c99ed89d6880d3e3d3d95a41f20c78c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shape", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="storageCount")
    def storage_count(self) -> typing.Optional[jsii.Number]:
        '''The number of storage servers that are activated for the Exadata infrastructure.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageCount"))

    @storage_count.setter
    def storage_count(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27c4cf52db8d984fcff55e5d69a31d9e228dff810356ee3b15020f688804596f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCount", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="storageServerType")
    def storage_server_type(self) -> typing.Optional[builtins.str]:
        '''The storage server model type of the Exadata infrastructure.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageServerType"))

    @storage_server_type.setter
    def storage_server_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a8454cbe7499d2e89bee927276f8936ca72e6a1ce92f522f2f3a1178753392e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageServerType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags to assign to the Exadata Infrastructure.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9909f2504aae00efa9d8adaf040cb71163078ccb5d88b84ca3af82a80de540b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_odb.CfnCloudExadataInfrastructure.CustomerContactProperty",
        jsii_struct_bases=[],
        name_mapping={"email": "email"},
    )
    class CustomerContactProperty:
        def __init__(self, *, email: typing.Optional[builtins.str] = None) -> None:
            '''A contact to receive notification from Oracle about maintenance updates for a specific Exadata infrastructure.

            :param email: The email address of the contact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-odb-cloudexadatainfrastructure-customercontact.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_odb as odb
                
                customer_contact_property = odb.CfnCloudExadataInfrastructure.CustomerContactProperty(
                    email="email"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__643c0e64847e961d0058c2280408d7c853e987c242dc2bdfb33b5b65dcc6c0f3)
                check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if email is not None:
                self._values["email"] = email

        @builtins.property
        def email(self) -> typing.Optional[builtins.str]:
            '''The email address of the contact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-odb-cloudexadatainfrastructure-customercontact.html#cfn-odb-cloudexadatainfrastructure-customercontact-email
            '''
            result = self._values.get("email")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomerContactProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_odb.CfnCloudExadataInfrastructureProps",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zone": "availabilityZone",
        "availability_zone_id": "availabilityZoneId",
        "compute_count": "computeCount",
        "customer_contacts_to_send_to_oci": "customerContactsToSendToOci",
        "database_server_type": "databaseServerType",
        "display_name": "displayName",
        "shape": "shape",
        "storage_count": "storageCount",
        "storage_server_type": "storageServerType",
        "tags": "tags",
    },
)
class CfnCloudExadataInfrastructureProps:
    def __init__(
        self,
        *,
        availability_zone: typing.Optional[builtins.str] = None,
        availability_zone_id: typing.Optional[builtins.str] = None,
        compute_count: typing.Optional[jsii.Number] = None,
        customer_contacts_to_send_to_oci: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCloudExadataInfrastructure.CustomerContactProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        database_server_type: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        shape: typing.Optional[builtins.str] = None,
        storage_count: typing.Optional[jsii.Number] = None,
        storage_server_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCloudExadataInfrastructure``.

        :param availability_zone: The name of the Availability Zone (AZ) where the Exadata infrastructure is located. Required when creating an Exadata infrastructure. Specify either AvailabilityZone or AvailabilityZoneId to define the location of the infrastructure.
        :param availability_zone_id: The AZ ID of the AZ where the Exadata infrastructure is located. Required when creating an Exadata infrastructure. Specify either AvailabilityZone or AvailabilityZoneId to define the location of the infrastructure.
        :param compute_count: The number of database servers for the Exadata infrastructure. Required when creating an Exadata infrastructure.
        :param customer_contacts_to_send_to_oci: The email addresses of contacts to receive notification from Oracle about maintenance updates for the Exadata infrastructure.
        :param database_server_type: The database server model type of the Exadata infrastructure. For the list of valid model names, use the ``ListDbSystemShapes`` operation.
        :param display_name: The user-friendly name for the Exadata infrastructure. Required when creating an Exadata infrastructure.
        :param shape: The model name of the Exadata infrastructure. Required when creating an Exadata infrastructure.
        :param storage_count: The number of storage servers that are activated for the Exadata infrastructure. Required when creating an Exadata infrastructure.
        :param storage_server_type: The storage server model type of the Exadata infrastructure. For the list of valid model names, use the ``ListDbSystemShapes`` operation.
        :param tags: Tags to assign to the Exadata Infrastructure.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudexadatainfrastructure.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_odb as odb
            
            cfn_cloud_exadata_infrastructure_props = odb.CfnCloudExadataInfrastructureProps(
                availability_zone="availabilityZone",
                availability_zone_id="availabilityZoneId",
                compute_count=123,
                customer_contacts_to_send_to_oci=[odb.CfnCloudExadataInfrastructure.CustomerContactProperty(
                    email="email"
                )],
                database_server_type="databaseServerType",
                display_name="displayName",
                shape="shape",
                storage_count=123,
                storage_server_type="storageServerType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b021189fda911f5f9c01459f93a1cc1991300050c373d976ffb11c43e7ef9081)
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument availability_zone_id", value=availability_zone_id, expected_type=type_hints["availability_zone_id"])
            check_type(argname="argument compute_count", value=compute_count, expected_type=type_hints["compute_count"])
            check_type(argname="argument customer_contacts_to_send_to_oci", value=customer_contacts_to_send_to_oci, expected_type=type_hints["customer_contacts_to_send_to_oci"])
            check_type(argname="argument database_server_type", value=database_server_type, expected_type=type_hints["database_server_type"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument shape", value=shape, expected_type=type_hints["shape"])
            check_type(argname="argument storage_count", value=storage_count, expected_type=type_hints["storage_count"])
            check_type(argname="argument storage_server_type", value=storage_server_type, expected_type=type_hints["storage_server_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if availability_zone_id is not None:
            self._values["availability_zone_id"] = availability_zone_id
        if compute_count is not None:
            self._values["compute_count"] = compute_count
        if customer_contacts_to_send_to_oci is not None:
            self._values["customer_contacts_to_send_to_oci"] = customer_contacts_to_send_to_oci
        if database_server_type is not None:
            self._values["database_server_type"] = database_server_type
        if display_name is not None:
            self._values["display_name"] = display_name
        if shape is not None:
            self._values["shape"] = shape
        if storage_count is not None:
            self._values["storage_count"] = storage_count
        if storage_server_type is not None:
            self._values["storage_server_type"] = storage_server_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The name of the Availability Zone (AZ) where the Exadata infrastructure is located.

        Required when creating an Exadata infrastructure. Specify either AvailabilityZone or AvailabilityZoneId to define the location of the infrastructure.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudexadatainfrastructure.html#cfn-odb-cloudexadatainfrastructure-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def availability_zone_id(self) -> typing.Optional[builtins.str]:
        '''The AZ ID of the AZ where the Exadata infrastructure is located.

        Required when creating an Exadata infrastructure. Specify either AvailabilityZone or AvailabilityZoneId to define the location of the infrastructure.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudexadatainfrastructure.html#cfn-odb-cloudexadatainfrastructure-availabilityzoneid
        '''
        result = self._values.get("availability_zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compute_count(self) -> typing.Optional[jsii.Number]:
        '''The number of database servers for the Exadata infrastructure.

        Required when creating an Exadata infrastructure.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudexadatainfrastructure.html#cfn-odb-cloudexadatainfrastructure-computecount
        '''
        result = self._values.get("compute_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def customer_contacts_to_send_to_oci(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCloudExadataInfrastructure.CustomerContactProperty]]]]:
        '''The email addresses of contacts to receive notification from Oracle about maintenance updates for the Exadata infrastructure.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudexadatainfrastructure.html#cfn-odb-cloudexadatainfrastructure-customercontactstosendtooci
        '''
        result = self._values.get("customer_contacts_to_send_to_oci")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCloudExadataInfrastructure.CustomerContactProperty]]]], result)

    @builtins.property
    def database_server_type(self) -> typing.Optional[builtins.str]:
        '''The database server model type of the Exadata infrastructure.

        For the list of valid model names, use the ``ListDbSystemShapes`` operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudexadatainfrastructure.html#cfn-odb-cloudexadatainfrastructure-databaseservertype
        '''
        result = self._values.get("database_server_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The user-friendly name for the Exadata infrastructure.

        Required when creating an Exadata infrastructure.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudexadatainfrastructure.html#cfn-odb-cloudexadatainfrastructure-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shape(self) -> typing.Optional[builtins.str]:
        '''The model name of the Exadata infrastructure.

        Required when creating an Exadata infrastructure.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudexadatainfrastructure.html#cfn-odb-cloudexadatainfrastructure-shape
        '''
        result = self._values.get("shape")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_count(self) -> typing.Optional[jsii.Number]:
        '''The number of storage servers that are activated for the Exadata infrastructure.

        Required when creating an Exadata infrastructure.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudexadatainfrastructure.html#cfn-odb-cloudexadatainfrastructure-storagecount
        '''
        result = self._values.get("storage_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_server_type(self) -> typing.Optional[builtins.str]:
        '''The storage server model type of the Exadata infrastructure.

        For the list of valid model names, use the ``ListDbSystemShapes`` operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudexadatainfrastructure.html#cfn-odb-cloudexadatainfrastructure-storageservertype
        '''
        result = self._values.get("storage_server_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags to assign to the Exadata Infrastructure.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudexadatainfrastructure.html#cfn-odb-cloudexadatainfrastructure-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudExadataInfrastructureProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnCloudVmCluster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_odb.CfnCloudVmCluster",
):
    '''The ``AWS::ODB::CloudVmCluster`` resource creates a VM cluster on the specified Exadata infrastructure in the Oracle Database.

    A VM cluster provides the compute resources for Oracle Database workloads.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html
    :cloudformationResource: AWS::ODB::CloudVmCluster
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_odb as odb
        
        cfn_cloud_vm_cluster = odb.CfnCloudVmCluster(self, "MyCfnCloudVmCluster",
            cloud_exadata_infrastructure_id="cloudExadataInfrastructureId",
            cluster_name="clusterName",
            cpu_core_count=123,
            data_collection_options=odb.CfnCloudVmCluster.DataCollectionOptionsProperty(
                is_diagnostics_events_enabled=False,
                is_health_monitoring_enabled=False,
                is_incident_logs_enabled=False
            ),
            data_storage_size_in_tBs=123,
            db_node_storage_size_in_gBs=123,
            db_servers=["dbServers"],
            display_name="displayName",
            gi_version="giVersion",
            hostname="hostname",
            is_local_backup_enabled=False,
            is_sparse_diskgroup_enabled=False,
            license_model="licenseModel",
            memory_size_in_gBs=123,
            odb_network_id="odbNetworkId",
            scan_listener_port_tcp=123,
            ssh_public_keys=["sshPublicKeys"],
            system_version="systemVersion",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            time_zone="timeZone"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cloud_exadata_infrastructure_id: typing.Optional[builtins.str] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        cpu_core_count: typing.Optional[jsii.Number] = None,
        data_collection_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCloudVmCluster.DataCollectionOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        data_storage_size_in_t_bs: typing.Optional[jsii.Number] = None,
        db_node_storage_size_in_g_bs: typing.Optional[jsii.Number] = None,
        db_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        display_name: typing.Optional[builtins.str] = None,
        gi_version: typing.Optional[builtins.str] = None,
        hostname: typing.Optional[builtins.str] = None,
        is_local_backup_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        is_sparse_diskgroup_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        license_model: typing.Optional[builtins.str] = None,
        memory_size_in_g_bs: typing.Optional[jsii.Number] = None,
        odb_network_id: typing.Optional[builtins.str] = None,
        scan_listener_port_tcp: typing.Optional[jsii.Number] = None,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        system_version: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        time_zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cloud_exadata_infrastructure_id: The unique identifier of the Exadata infrastructure that this VM cluster belongs to. Required when creating a VM cluster.
        :param cluster_name: The name of the Grid Infrastructure (GI) cluster.
        :param cpu_core_count: The number of CPU cores enabled on the VM cluster. Required when creating a VM cluster.
        :param data_collection_options: The set of diagnostic collection options enabled for the VM cluster.
        :param data_storage_size_in_t_bs: The size of the data disk group, in terabytes (TB), that's allocated for the VM cluster.
        :param db_node_storage_size_in_g_bs: The amount of local node storage, in gigabytes (GB), that's allocated for the VM cluster.
        :param db_servers: The list of database servers for the VM cluster.
        :param display_name: The user-friendly name for the VM cluster. Required when creating a VM cluster.
        :param gi_version: The software version of the Oracle Grid Infrastructure (GI) for the VM cluster. Required when creating a VM cluster.
        :param hostname: The host name for the VM cluster. Required when creating a VM cluster.
        :param is_local_backup_enabled: Specifies whether database backups to local Exadata storage are enabled for the VM cluster.
        :param is_sparse_diskgroup_enabled: Specifies whether the VM cluster is configured with a sparse disk group.
        :param license_model: The Oracle license model applied to the VM cluster.
        :param memory_size_in_g_bs: The amount of memory, in gigabytes (GB), that's allocated for the VM cluster.
        :param odb_network_id: The unique identifier of the ODB network for the VM cluster. Required when creating a VM cluster.
        :param scan_listener_port_tcp: The port number for TCP connections to the single client access name (SCAN) listener. Valid values: ``1024–8999`` with the following exceptions: ``2484`` , ``6100`` , ``6200`` , ``7060`` , ``7070`` , ``7085`` , and ``7879`` Default: ``1521``
        :param ssh_public_keys: The public key portion of one or more key pairs used for SSH access to the VM cluster. Required when creating a VM cluster.
        :param system_version: The operating system version of the image chosen for the VM cluster.
        :param tags: Tags to assign to the Vm Cluster.
        :param time_zone: The time zone of the VM cluster.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54a24296108cf4d367a887b0b65dc2c9163c185183c8fde1522a8cb329db03c9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCloudVmClusterProps(
            cloud_exadata_infrastructure_id=cloud_exadata_infrastructure_id,
            cluster_name=cluster_name,
            cpu_core_count=cpu_core_count,
            data_collection_options=data_collection_options,
            data_storage_size_in_t_bs=data_storage_size_in_t_bs,
            db_node_storage_size_in_g_bs=db_node_storage_size_in_g_bs,
            db_servers=db_servers,
            display_name=display_name,
            gi_version=gi_version,
            hostname=hostname,
            is_local_backup_enabled=is_local_backup_enabled,
            is_sparse_diskgroup_enabled=is_sparse_diskgroup_enabled,
            license_model=license_model,
            memory_size_in_g_bs=memory_size_in_g_bs,
            odb_network_id=odb_network_id,
            scan_listener_port_tcp=scan_listener_port_tcp,
            ssh_public_keys=ssh_public_keys,
            system_version=system_version,
            tags=tags,
            time_zone=time_zone,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed59e4637cf9d059e23e91ea16d89733fbc266730217c0eb52cd6e26b74ca7c7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d823fc77af2f98ddeee14344f0e2eb8f2dd78ad96c2039f50849367a0710a3a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCloudVmClusterArn")
    def attr_cloud_vm_cluster_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the VM cluster.

        :cloudformationAttribute: CloudVmClusterArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCloudVmClusterArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCloudVmClusterId")
    def attr_cloud_vm_cluster_id(self) -> builtins.str:
        '''The unique identifier of the VM cluster.

        :cloudformationAttribute: CloudVmClusterId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCloudVmClusterId"))

    @builtins.property
    @jsii.member(jsii_name="attrComputeModel")
    def attr_compute_model(self) -> builtins.str:
        '''The OCI model compute model used when you create or clone an instance: ECPU or OCPU.

        An ECPU is an abstracted measure of compute resources. ECPUs are based on the number of cores elastically allocated from a pool of compute and storage servers. An OCPU is a legacy physical measure of compute resources. OCPUs are based on the physical core of a processor with hyper-threading enabled.

        :cloudformationAttribute: ComputeModel
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrComputeModel"))

    @builtins.property
    @jsii.member(jsii_name="attrDiskRedundancy")
    def attr_disk_redundancy(self) -> builtins.str:
        '''The type of redundancy configured for the VM cluster.

        ``NORMAL`` is 2-way redundancy. ``HIGH`` is 3-way redundancy.

        :cloudformationAttribute: DiskRedundancy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDiskRedundancy"))

    @builtins.property
    @jsii.member(jsii_name="attrDomain")
    def attr_domain(self) -> builtins.str:
        '''The domain of the VM cluster.

        :cloudformationAttribute: Domain
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomain"))

    @builtins.property
    @jsii.member(jsii_name="attrListenerPort")
    def attr_listener_port(self) -> jsii.Number:
        '''The port number configured for the listener on the VM cluster.

        :cloudformationAttribute: ListenerPort
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrListenerPort"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCount")
    def attr_node_count(self) -> jsii.Number:
        '''The number of nodes in the VM cluster.

        :cloudformationAttribute: NodeCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrNodeCount"))

    @builtins.property
    @jsii.member(jsii_name="attrOcid")
    def attr_ocid(self) -> builtins.str:
        '''The OCID of the VM cluster.

        :cloudformationAttribute: Ocid
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOcid"))

    @builtins.property
    @jsii.member(jsii_name="attrOciResourceAnchorName")
    def attr_oci_resource_anchor_name(self) -> builtins.str:
        '''The name of the OCI resource anchor for the VM cluster.

        :cloudformationAttribute: OciResourceAnchorName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOciResourceAnchorName"))

    @builtins.property
    @jsii.member(jsii_name="attrOciUrl")
    def attr_oci_url(self) -> builtins.str:
        '''The HTTPS link to the VM cluster in OCI.

        :cloudformationAttribute: OciUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOciUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrScanDnsName")
    def attr_scan_dns_name(self) -> builtins.str:
        '''The FQDN of the DNS record for the Single Client Access Name (SCAN) IP addresses that are associated with the VM cluster.

        :cloudformationAttribute: ScanDnsName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrScanDnsName"))

    @builtins.property
    @jsii.member(jsii_name="attrScanIpIds")
    def attr_scan_ip_ids(self) -> typing.List[builtins.str]:
        '''The OCID of the SCAN IP addresses that are associated with the VM cluster.

        :cloudformationAttribute: ScanIpIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrScanIpIds"))

    @builtins.property
    @jsii.member(jsii_name="attrShape")
    def attr_shape(self) -> builtins.str:
        '''The hardware model name of the Exadata infrastructure that's running the VM cluster.

        :cloudformationAttribute: Shape
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrShape"))

    @builtins.property
    @jsii.member(jsii_name="attrStorageSizeInGBs")
    def attr_storage_size_in_g_bs(self) -> jsii.Number:
        '''The amount of local node storage, in gigabytes (GB), that's allocated to the VM cluster.

        :cloudformationAttribute: StorageSizeInGBs
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrStorageSizeInGBs"))

    @builtins.property
    @jsii.member(jsii_name="attrVipIds")
    def attr_vip_ids(self) -> typing.List[builtins.str]:
        '''The virtual IP (VIP) addresses that are associated with the VM cluster.

        Oracle's Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the VM cluster to enable failover. If one node fails, the VIP is reassigned to another active node in the cluster.

        :cloudformationAttribute: VipIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrVipIds"))

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
    @jsii.member(jsii_name="cloudExadataInfrastructureId")
    def cloud_exadata_infrastructure_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the Exadata infrastructure that this VM cluster belongs to.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudExadataInfrastructureId"))

    @cloud_exadata_infrastructure_id.setter
    def cloud_exadata_infrastructure_id(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bf5be722e37c84a8be0753f43f6ebea1d0a90a8366126ea1037239c338f1d8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudExadataInfrastructureId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Grid Infrastructure (GI) cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6ff07037dfba0ff0af683d4166a5b861e52d71412e3f43496c4333804c29424)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cpuCoreCount")
    def cpu_core_count(self) -> typing.Optional[jsii.Number]:
        '''The number of CPU cores enabled on the VM cluster.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuCoreCount"))

    @cpu_core_count.setter
    def cpu_core_count(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97dfb24de12ee075095d22107411f090b917260a37c1ad001b48d7a5c67cb754)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuCoreCount", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dataCollectionOptions")
    def data_collection_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCloudVmCluster.DataCollectionOptionsProperty"]]:
        '''The set of diagnostic collection options enabled for the VM cluster.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCloudVmCluster.DataCollectionOptionsProperty"]], jsii.get(self, "dataCollectionOptions"))

    @data_collection_options.setter
    def data_collection_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCloudVmCluster.DataCollectionOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53fa60e8088e8fcfabc4956f1ab3fbbe0607d6039731af37fdbf97088759d7f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataCollectionOptions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dataStorageSizeInTBs")
    def data_storage_size_in_t_bs(self) -> typing.Optional[jsii.Number]:
        '''The size of the data disk group, in terabytes (TB), that's allocated for the VM cluster.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataStorageSizeInTBs"))

    @data_storage_size_in_t_bs.setter
    def data_storage_size_in_t_bs(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10a4a98dd975dea2ac63836158b2dc7afd11f93fa6eef648312be262c3ea26ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataStorageSizeInTBs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dbNodeStorageSizeInGBs")
    def db_node_storage_size_in_g_bs(self) -> typing.Optional[jsii.Number]:
        '''The amount of local node storage, in gigabytes (GB), that's allocated for the VM cluster.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dbNodeStorageSizeInGBs"))

    @db_node_storage_size_in_g_bs.setter
    def db_node_storage_size_in_g_bs(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56b2b388df0abb719bfd805181dfedcccb07a854fdad9846d4422b3c03934e4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbNodeStorageSizeInGBs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dbServers")
    def db_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of database servers for the VM cluster.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dbServers"))

    @db_servers.setter
    def db_servers(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b1dc50ef9ded98095512787e029921d39680bf2148e093981b23da405bf6c6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbServers", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The user-friendly name for the VM cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faa8f862640240013012d7cb9579c5f7537d081345be3b3e24850b27f8726e8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="giVersion")
    def gi_version(self) -> typing.Optional[builtins.str]:
        '''The software version of the Oracle Grid Infrastructure (GI) for the VM cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "giVersion"))

    @gi_version.setter
    def gi_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e526643f4d50a0bc3309ec23106c8cf45132d45372c3b9b66ffc9329c9e1c8f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "giVersion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> typing.Optional[builtins.str]:
        '''The host name for the VM cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fd54015f6c4b31aa2007d549141e71219e140c311d6f9e23a787d6f35024881)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="isLocalBackupEnabled")
    def is_local_backup_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether database backups to local Exadata storage are enabled for the VM cluster.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "isLocalBackupEnabled"))

    @is_local_backup_enabled.setter
    def is_local_backup_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cee2b990c5219e427b51018646f252e8e93f20f5bc21497075e635e6fee21bc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isLocalBackupEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="isSparseDiskgroupEnabled")
    def is_sparse_diskgroup_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the VM cluster is configured with a sparse disk group.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "isSparseDiskgroupEnabled"))

    @is_sparse_diskgroup_enabled.setter
    def is_sparse_diskgroup_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c9800b0f09654567a1b07e3e8f1762764faa4d45ca7c8f2740ead91709fa406)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isSparseDiskgroupEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="licenseModel")
    def license_model(self) -> typing.Optional[builtins.str]:
        '''The Oracle license model applied to the VM cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseModel"))

    @license_model.setter
    def license_model(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__967fcd6461478a7564eb074b4498f432e3de0c5c89704737d521da3f25b82936)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseModel", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="memorySizeInGBs")
    def memory_size_in_g_bs(self) -> typing.Optional[jsii.Number]:
        '''The amount of memory, in gigabytes (GB), that's allocated for the VM cluster.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memorySizeInGBs"))

    @memory_size_in_g_bs.setter
    def memory_size_in_g_bs(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12fb5bc77e272b408d9ce9c7acda5e61ab3441f5399d13b2019847b549593e4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memorySizeInGBs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="odbNetworkId")
    def odb_network_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the ODB network for the VM cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "odbNetworkId"))

    @odb_network_id.setter
    def odb_network_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__350c5336798cdbfad4947370bdc277a67530ed8e6b01d083fca3f79b8830dea6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "odbNetworkId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scanListenerPortTcp")
    def scan_listener_port_tcp(self) -> typing.Optional[jsii.Number]:
        '''The port number for TCP connections to the single client access name (SCAN) listener.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scanListenerPortTcp"))

    @scan_listener_port_tcp.setter
    def scan_listener_port_tcp(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5eb9bc6b7d5257f43d703fc090ba522f231e4a93d03f84a030b4df45e8c072b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scanListenerPortTcp", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeys")
    def ssh_public_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The public key portion of one or more key pairs used for SSH access to the VM cluster.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sshPublicKeys"))

    @ssh_public_keys.setter
    def ssh_public_keys(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b623a41b47f8d29ffe185d4d174da5e8c6c773a014a3ccf0409f011487bc1b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPublicKeys", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="systemVersion")
    def system_version(self) -> typing.Optional[builtins.str]:
        '''The operating system version of the image chosen for the VM cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "systemVersion"))

    @system_version.setter
    def system_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95a2f67985613635273aa653a865d22f373a34cc2cf492bbaecbc97526a00620)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "systemVersion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags to assign to the Vm Cluster.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb35585e2ec32ece572f8bcd0f0a038f35ebbc9d6e29c933404bd886b5900921)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''The time zone of the VM cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbc007d119e94eccae2b52e6822c2ec73b5e10e124879ca88059e3b3b536edfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_odb.CfnCloudVmCluster.DataCollectionOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "is_diagnostics_events_enabled": "isDiagnosticsEventsEnabled",
            "is_health_monitoring_enabled": "isHealthMonitoringEnabled",
            "is_incident_logs_enabled": "isIncidentLogsEnabled",
        },
    )
    class DataCollectionOptionsProperty:
        def __init__(
            self,
            *,
            is_diagnostics_events_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            is_health_monitoring_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            is_incident_logs_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Information about the data collection options enabled for a VM cluster.

            :param is_diagnostics_events_enabled: Specifies whether diagnostic collection is enabled for the VM cluster.
            :param is_health_monitoring_enabled: Specifies whether health monitoring is enabled for the VM cluster.
            :param is_incident_logs_enabled: Specifies whether incident logs are enabled for the VM cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-odb-cloudvmcluster-datacollectionoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_odb as odb
                
                data_collection_options_property = odb.CfnCloudVmCluster.DataCollectionOptionsProperty(
                    is_diagnostics_events_enabled=False,
                    is_health_monitoring_enabled=False,
                    is_incident_logs_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0be5e048213b0ee63e4c9703a3c1b37da85fb4dc37d9458571be7e6789ddbe30)
                check_type(argname="argument is_diagnostics_events_enabled", value=is_diagnostics_events_enabled, expected_type=type_hints["is_diagnostics_events_enabled"])
                check_type(argname="argument is_health_monitoring_enabled", value=is_health_monitoring_enabled, expected_type=type_hints["is_health_monitoring_enabled"])
                check_type(argname="argument is_incident_logs_enabled", value=is_incident_logs_enabled, expected_type=type_hints["is_incident_logs_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if is_diagnostics_events_enabled is not None:
                self._values["is_diagnostics_events_enabled"] = is_diagnostics_events_enabled
            if is_health_monitoring_enabled is not None:
                self._values["is_health_monitoring_enabled"] = is_health_monitoring_enabled
            if is_incident_logs_enabled is not None:
                self._values["is_incident_logs_enabled"] = is_incident_logs_enabled

        @builtins.property
        def is_diagnostics_events_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether diagnostic collection is enabled for the VM cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-odb-cloudvmcluster-datacollectionoptions.html#cfn-odb-cloudvmcluster-datacollectionoptions-isdiagnosticseventsenabled
            '''
            result = self._values.get("is_diagnostics_events_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def is_health_monitoring_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether health monitoring is enabled for the VM cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-odb-cloudvmcluster-datacollectionoptions.html#cfn-odb-cloudvmcluster-datacollectionoptions-ishealthmonitoringenabled
            '''
            result = self._values.get("is_health_monitoring_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def is_incident_logs_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether incident logs are enabled for the VM cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-odb-cloudvmcluster-datacollectionoptions.html#cfn-odb-cloudvmcluster-datacollectionoptions-isincidentlogsenabled
            '''
            result = self._values.get("is_incident_logs_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataCollectionOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_odb.CfnCloudVmClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_exadata_infrastructure_id": "cloudExadataInfrastructureId",
        "cluster_name": "clusterName",
        "cpu_core_count": "cpuCoreCount",
        "data_collection_options": "dataCollectionOptions",
        "data_storage_size_in_t_bs": "dataStorageSizeInTBs",
        "db_node_storage_size_in_g_bs": "dbNodeStorageSizeInGBs",
        "db_servers": "dbServers",
        "display_name": "displayName",
        "gi_version": "giVersion",
        "hostname": "hostname",
        "is_local_backup_enabled": "isLocalBackupEnabled",
        "is_sparse_diskgroup_enabled": "isSparseDiskgroupEnabled",
        "license_model": "licenseModel",
        "memory_size_in_g_bs": "memorySizeInGBs",
        "odb_network_id": "odbNetworkId",
        "scan_listener_port_tcp": "scanListenerPortTcp",
        "ssh_public_keys": "sshPublicKeys",
        "system_version": "systemVersion",
        "tags": "tags",
        "time_zone": "timeZone",
    },
)
class CfnCloudVmClusterProps:
    def __init__(
        self,
        *,
        cloud_exadata_infrastructure_id: typing.Optional[builtins.str] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        cpu_core_count: typing.Optional[jsii.Number] = None,
        data_collection_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCloudVmCluster.DataCollectionOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        data_storage_size_in_t_bs: typing.Optional[jsii.Number] = None,
        db_node_storage_size_in_g_bs: typing.Optional[jsii.Number] = None,
        db_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        display_name: typing.Optional[builtins.str] = None,
        gi_version: typing.Optional[builtins.str] = None,
        hostname: typing.Optional[builtins.str] = None,
        is_local_backup_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        is_sparse_diskgroup_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        license_model: typing.Optional[builtins.str] = None,
        memory_size_in_g_bs: typing.Optional[jsii.Number] = None,
        odb_network_id: typing.Optional[builtins.str] = None,
        scan_listener_port_tcp: typing.Optional[jsii.Number] = None,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        system_version: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        time_zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnCloudVmCluster``.

        :param cloud_exadata_infrastructure_id: The unique identifier of the Exadata infrastructure that this VM cluster belongs to. Required when creating a VM cluster.
        :param cluster_name: The name of the Grid Infrastructure (GI) cluster.
        :param cpu_core_count: The number of CPU cores enabled on the VM cluster. Required when creating a VM cluster.
        :param data_collection_options: The set of diagnostic collection options enabled for the VM cluster.
        :param data_storage_size_in_t_bs: The size of the data disk group, in terabytes (TB), that's allocated for the VM cluster.
        :param db_node_storage_size_in_g_bs: The amount of local node storage, in gigabytes (GB), that's allocated for the VM cluster.
        :param db_servers: The list of database servers for the VM cluster.
        :param display_name: The user-friendly name for the VM cluster. Required when creating a VM cluster.
        :param gi_version: The software version of the Oracle Grid Infrastructure (GI) for the VM cluster. Required when creating a VM cluster.
        :param hostname: The host name for the VM cluster. Required when creating a VM cluster.
        :param is_local_backup_enabled: Specifies whether database backups to local Exadata storage are enabled for the VM cluster.
        :param is_sparse_diskgroup_enabled: Specifies whether the VM cluster is configured with a sparse disk group.
        :param license_model: The Oracle license model applied to the VM cluster.
        :param memory_size_in_g_bs: The amount of memory, in gigabytes (GB), that's allocated for the VM cluster.
        :param odb_network_id: The unique identifier of the ODB network for the VM cluster. Required when creating a VM cluster.
        :param scan_listener_port_tcp: The port number for TCP connections to the single client access name (SCAN) listener. Valid values: ``1024–8999`` with the following exceptions: ``2484`` , ``6100`` , ``6200`` , ``7060`` , ``7070`` , ``7085`` , and ``7879`` Default: ``1521``
        :param ssh_public_keys: The public key portion of one or more key pairs used for SSH access to the VM cluster. Required when creating a VM cluster.
        :param system_version: The operating system version of the image chosen for the VM cluster.
        :param tags: Tags to assign to the Vm Cluster.
        :param time_zone: The time zone of the VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_odb as odb
            
            cfn_cloud_vm_cluster_props = odb.CfnCloudVmClusterProps(
                cloud_exadata_infrastructure_id="cloudExadataInfrastructureId",
                cluster_name="clusterName",
                cpu_core_count=123,
                data_collection_options=odb.CfnCloudVmCluster.DataCollectionOptionsProperty(
                    is_diagnostics_events_enabled=False,
                    is_health_monitoring_enabled=False,
                    is_incident_logs_enabled=False
                ),
                data_storage_size_in_tBs=123,
                db_node_storage_size_in_gBs=123,
                db_servers=["dbServers"],
                display_name="displayName",
                gi_version="giVersion",
                hostname="hostname",
                is_local_backup_enabled=False,
                is_sparse_diskgroup_enabled=False,
                license_model="licenseModel",
                memory_size_in_gBs=123,
                odb_network_id="odbNetworkId",
                scan_listener_port_tcp=123,
                ssh_public_keys=["sshPublicKeys"],
                system_version="systemVersion",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                time_zone="timeZone"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7c1c550550cdc807e34dbb5ced4b50daf930df9156b6a6f0dfaa8e978be765a)
            check_type(argname="argument cloud_exadata_infrastructure_id", value=cloud_exadata_infrastructure_id, expected_type=type_hints["cloud_exadata_infrastructure_id"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument cpu_core_count", value=cpu_core_count, expected_type=type_hints["cpu_core_count"])
            check_type(argname="argument data_collection_options", value=data_collection_options, expected_type=type_hints["data_collection_options"])
            check_type(argname="argument data_storage_size_in_t_bs", value=data_storage_size_in_t_bs, expected_type=type_hints["data_storage_size_in_t_bs"])
            check_type(argname="argument db_node_storage_size_in_g_bs", value=db_node_storage_size_in_g_bs, expected_type=type_hints["db_node_storage_size_in_g_bs"])
            check_type(argname="argument db_servers", value=db_servers, expected_type=type_hints["db_servers"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument gi_version", value=gi_version, expected_type=type_hints["gi_version"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument is_local_backup_enabled", value=is_local_backup_enabled, expected_type=type_hints["is_local_backup_enabled"])
            check_type(argname="argument is_sparse_diskgroup_enabled", value=is_sparse_diskgroup_enabled, expected_type=type_hints["is_sparse_diskgroup_enabled"])
            check_type(argname="argument license_model", value=license_model, expected_type=type_hints["license_model"])
            check_type(argname="argument memory_size_in_g_bs", value=memory_size_in_g_bs, expected_type=type_hints["memory_size_in_g_bs"])
            check_type(argname="argument odb_network_id", value=odb_network_id, expected_type=type_hints["odb_network_id"])
            check_type(argname="argument scan_listener_port_tcp", value=scan_listener_port_tcp, expected_type=type_hints["scan_listener_port_tcp"])
            check_type(argname="argument ssh_public_keys", value=ssh_public_keys, expected_type=type_hints["ssh_public_keys"])
            check_type(argname="argument system_version", value=system_version, expected_type=type_hints["system_version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cloud_exadata_infrastructure_id is not None:
            self._values["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if cpu_core_count is not None:
            self._values["cpu_core_count"] = cpu_core_count
        if data_collection_options is not None:
            self._values["data_collection_options"] = data_collection_options
        if data_storage_size_in_t_bs is not None:
            self._values["data_storage_size_in_t_bs"] = data_storage_size_in_t_bs
        if db_node_storage_size_in_g_bs is not None:
            self._values["db_node_storage_size_in_g_bs"] = db_node_storage_size_in_g_bs
        if db_servers is not None:
            self._values["db_servers"] = db_servers
        if display_name is not None:
            self._values["display_name"] = display_name
        if gi_version is not None:
            self._values["gi_version"] = gi_version
        if hostname is not None:
            self._values["hostname"] = hostname
        if is_local_backup_enabled is not None:
            self._values["is_local_backup_enabled"] = is_local_backup_enabled
        if is_sparse_diskgroup_enabled is not None:
            self._values["is_sparse_diskgroup_enabled"] = is_sparse_diskgroup_enabled
        if license_model is not None:
            self._values["license_model"] = license_model
        if memory_size_in_g_bs is not None:
            self._values["memory_size_in_g_bs"] = memory_size_in_g_bs
        if odb_network_id is not None:
            self._values["odb_network_id"] = odb_network_id
        if scan_listener_port_tcp is not None:
            self._values["scan_listener_port_tcp"] = scan_listener_port_tcp
        if ssh_public_keys is not None:
            self._values["ssh_public_keys"] = ssh_public_keys
        if system_version is not None:
            self._values["system_version"] = system_version
        if tags is not None:
            self._values["tags"] = tags
        if time_zone is not None:
            self._values["time_zone"] = time_zone

    @builtins.property
    def cloud_exadata_infrastructure_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the Exadata infrastructure that this VM cluster belongs to.

        Required when creating a VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-cloudexadatainfrastructureid
        '''
        result = self._values.get("cloud_exadata_infrastructure_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Grid Infrastructure (GI) cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-clustername
        '''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpu_core_count(self) -> typing.Optional[jsii.Number]:
        '''The number of CPU cores enabled on the VM cluster.

        Required when creating a VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-cpucorecount
        '''
        result = self._values.get("cpu_core_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def data_collection_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCloudVmCluster.DataCollectionOptionsProperty]]:
        '''The set of diagnostic collection options enabled for the VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-datacollectionoptions
        '''
        result = self._values.get("data_collection_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCloudVmCluster.DataCollectionOptionsProperty]], result)

    @builtins.property
    def data_storage_size_in_t_bs(self) -> typing.Optional[jsii.Number]:
        '''The size of the data disk group, in terabytes (TB), that's allocated for the VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-datastoragesizeintbs
        '''
        result = self._values.get("data_storage_size_in_t_bs")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def db_node_storage_size_in_g_bs(self) -> typing.Optional[jsii.Number]:
        '''The amount of local node storage, in gigabytes (GB), that's allocated for the VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-dbnodestoragesizeingbs
        '''
        result = self._values.get("db_node_storage_size_in_g_bs")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def db_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of database servers for the VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-dbservers
        '''
        result = self._values.get("db_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The user-friendly name for the VM cluster.

        Required when creating a VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gi_version(self) -> typing.Optional[builtins.str]:
        '''The software version of the Oracle Grid Infrastructure (GI) for the VM cluster.

        Required when creating a VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-giversion
        '''
        result = self._values.get("gi_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''The host name for the VM cluster.

        Required when creating a VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-hostname
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_local_backup_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether database backups to local Exadata storage are enabled for the VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-islocalbackupenabled
        '''
        result = self._values.get("is_local_backup_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def is_sparse_diskgroup_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the VM cluster is configured with a sparse disk group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-issparsediskgroupenabled
        '''
        result = self._values.get("is_sparse_diskgroup_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def license_model(self) -> typing.Optional[builtins.str]:
        '''The Oracle license model applied to the VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-licensemodel
        '''
        result = self._values.get("license_model")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory_size_in_g_bs(self) -> typing.Optional[jsii.Number]:
        '''The amount of memory, in gigabytes (GB), that's allocated for the VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-memorysizeingbs
        '''
        result = self._values.get("memory_size_in_g_bs")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def odb_network_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the ODB network for the VM cluster.

        Required when creating a VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-odbnetworkid
        '''
        result = self._values.get("odb_network_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scan_listener_port_tcp(self) -> typing.Optional[jsii.Number]:
        '''The port number for TCP connections to the single client access name (SCAN) listener.

        Valid values: ``1024–8999`` with the following exceptions: ``2484`` , ``6100`` , ``6200`` , ``7060`` , ``7070`` , ``7085`` , and ``7879``

        Default: ``1521``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-scanlistenerporttcp
        '''
        result = self._values.get("scan_listener_port_tcp")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ssh_public_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The public key portion of one or more key pairs used for SSH access to the VM cluster.

        Required when creating a VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-sshpublickeys
        '''
        result = self._values.get("ssh_public_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def system_version(self) -> typing.Optional[builtins.str]:
        '''The operating system version of the image chosen for the VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-systemversion
        '''
        result = self._values.get("system_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags to assign to the Vm Cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''The time zone of the VM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-cloudvmcluster.html#cfn-odb-cloudvmcluster-timezone
        '''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudVmClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnOdbNetwork(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_odb.CfnOdbNetwork",
):
    '''The ``AWS::ODB::OdbNetwork`` resource creates an ODB network.

    An ODB network provides the networking foundation for Oracle Database resources.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-odbnetwork.html
    :cloudformationResource: AWS::ODB::OdbNetwork
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_odb as odb
        
        cfn_odb_network = odb.CfnOdbNetwork(self, "MyCfnOdbNetwork",
            availability_zone="availabilityZone",
            availability_zone_id="availabilityZoneId",
            backup_subnet_cidr="backupSubnetCidr",
            client_subnet_cidr="clientSubnetCidr",
            default_dns_prefix="defaultDnsPrefix",
            delete_associated_resources=False,
            display_name="displayName",
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
        availability_zone: typing.Optional[builtins.str] = None,
        availability_zone_id: typing.Optional[builtins.str] = None,
        backup_subnet_cidr: typing.Optional[builtins.str] = None,
        client_subnet_cidr: typing.Optional[builtins.str] = None,
        default_dns_prefix: typing.Optional[builtins.str] = None,
        delete_associated_resources: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        display_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param availability_zone: The Availability Zone (AZ) where the ODB network is located. Required when creating an ODB network. Specify either AvailabilityZone or AvailabilityZoneId to define the location of the network.
        :param availability_zone_id: The AZ ID of the AZ where the ODB network is located. Required when creating an ODB network. Specify either AvailabilityZone or AvailabilityZoneId to define the location of the network.
        :param backup_subnet_cidr: The CIDR range of the backup subnet in the ODB network.
        :param client_subnet_cidr: The CIDR range of the client subnet in the ODB network. Required when creating an ODB network.
        :param default_dns_prefix: The DNS prefix to the default DNS domain name. The default DNS domain name is oraclevcn.com.
        :param delete_associated_resources: Specifies whether to delete associated OCI networking resources along with the ODB network. Required when creating an ODB network.
        :param display_name: The user-friendly name of the ODB network. Required when creating an ODB network.
        :param tags: Tags to assign to the Odb Network.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fb7fc690c89d5ce8f5abecb60ad841f57c0a476f500c817c386b57c3cd0f5d6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOdbNetworkProps(
            availability_zone=availability_zone,
            availability_zone_id=availability_zone_id,
            backup_subnet_cidr=backup_subnet_cidr,
            client_subnet_cidr=client_subnet_cidr,
            default_dns_prefix=default_dns_prefix,
            delete_associated_resources=delete_associated_resources,
            display_name=display_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2bd65fc6165cb531de2b171a21a41aaf44e19b81b1e54c00c7b0bb7dbc5feab)
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
            type_hints = typing.get_type_hints(_typecheckingstub__afa78d8af0d52b46b8c4cc90575b6a94e64eb6cb32aa68eb759b91d8213e31ac)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrOciNetworkAnchorId")
    def attr_oci_network_anchor_id(self) -> builtins.str:
        '''The unique identifier of the OCI network anchor for the ODB network.

        :cloudformationAttribute: OciNetworkAnchorId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOciNetworkAnchorId"))

    @builtins.property
    @jsii.member(jsii_name="attrOciResourceAnchorName")
    def attr_oci_resource_anchor_name(self) -> builtins.str:
        '''The name of the OCI resource anchor that's associated with the ODB network.

        :cloudformationAttribute: OciResourceAnchorName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOciResourceAnchorName"))

    @builtins.property
    @jsii.member(jsii_name="attrOciVcnUrl")
    def attr_oci_vcn_url(self) -> builtins.str:
        '''The URL for the VCN that's associated with the ODB network.

        :cloudformationAttribute: OciVcnUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOciVcnUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrOdbNetworkArn")
    def attr_odb_network_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the ODB network.

        :cloudformationAttribute: OdbNetworkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOdbNetworkArn"))

    @builtins.property
    @jsii.member(jsii_name="attrOdbNetworkId")
    def attr_odb_network_id(self) -> builtins.str:
        '''The unique identifier of the ODB network.

        :cloudformationAttribute: OdbNetworkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOdbNetworkId"))

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
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone (AZ) where the ODB network is located.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87621d2b03c5469d26954de7e37dfd0d3e012b5b4644ec0232e59bfecfb758e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneId")
    def availability_zone_id(self) -> typing.Optional[builtins.str]:
        '''The AZ ID of the AZ where the ODB network is located.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneId"))

    @availability_zone_id.setter
    def availability_zone_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__328deed1718c1266e8446a386f2cfe2272763b64c3f37b5bd93a7c2f77ab2d5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZoneId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="backupSubnetCidr")
    def backup_subnet_cidr(self) -> typing.Optional[builtins.str]:
        '''The CIDR range of the backup subnet in the ODB network.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupSubnetCidr"))

    @backup_subnet_cidr.setter
    def backup_subnet_cidr(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eee98a4fbff2c83a839881f8a102d4b7813c50e6fdb9be0997144c385e71c305)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupSubnetCidr", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="clientSubnetCidr")
    def client_subnet_cidr(self) -> typing.Optional[builtins.str]:
        '''The CIDR range of the client subnet in the ODB network.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSubnetCidr"))

    @client_subnet_cidr.setter
    def client_subnet_cidr(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__964e75c8af7e656feecdf2af9cc1f3709e5857d22d004e58037f1a4d97df301d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSubnetCidr", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultDnsPrefix")
    def default_dns_prefix(self) -> typing.Optional[builtins.str]:
        '''The DNS prefix to the default DNS domain name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultDnsPrefix"))

    @default_dns_prefix.setter
    def default_dns_prefix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccee4738061946ef5f75dacb78a62f5c60382f3bd85cd506ee1454b932d8374a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultDnsPrefix", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deleteAssociatedResources")
    def delete_associated_resources(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to delete associated OCI networking resources along with the ODB network.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "deleteAssociatedResources"))

    @delete_associated_resources.setter
    def delete_associated_resources(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc86642a834ad1214ad781ba4b6b7516ddb5e4df5219e6f1572c3707c253846a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteAssociatedResources", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The user-friendly name of the ODB network.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f9a4c06370e66400707daa4ab73fb37a67d67c8422f10b57fa0ee6b191128e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags to assign to the Odb Network.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a78f63e76d627d52015eb8e2a0dc2ab1a80a0926480a2a40fc93da33d803ce3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_odb.CfnOdbNetworkProps",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zone": "availabilityZone",
        "availability_zone_id": "availabilityZoneId",
        "backup_subnet_cidr": "backupSubnetCidr",
        "client_subnet_cidr": "clientSubnetCidr",
        "default_dns_prefix": "defaultDnsPrefix",
        "delete_associated_resources": "deleteAssociatedResources",
        "display_name": "displayName",
        "tags": "tags",
    },
)
class CfnOdbNetworkProps:
    def __init__(
        self,
        *,
        availability_zone: typing.Optional[builtins.str] = None,
        availability_zone_id: typing.Optional[builtins.str] = None,
        backup_subnet_cidr: typing.Optional[builtins.str] = None,
        client_subnet_cidr: typing.Optional[builtins.str] = None,
        default_dns_prefix: typing.Optional[builtins.str] = None,
        delete_associated_resources: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        display_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOdbNetwork``.

        :param availability_zone: The Availability Zone (AZ) where the ODB network is located. Required when creating an ODB network. Specify either AvailabilityZone or AvailabilityZoneId to define the location of the network.
        :param availability_zone_id: The AZ ID of the AZ where the ODB network is located. Required when creating an ODB network. Specify either AvailabilityZone or AvailabilityZoneId to define the location of the network.
        :param backup_subnet_cidr: The CIDR range of the backup subnet in the ODB network.
        :param client_subnet_cidr: The CIDR range of the client subnet in the ODB network. Required when creating an ODB network.
        :param default_dns_prefix: The DNS prefix to the default DNS domain name. The default DNS domain name is oraclevcn.com.
        :param delete_associated_resources: Specifies whether to delete associated OCI networking resources along with the ODB network. Required when creating an ODB network.
        :param display_name: The user-friendly name of the ODB network. Required when creating an ODB network.
        :param tags: Tags to assign to the Odb Network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-odbnetwork.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_odb as odb
            
            cfn_odb_network_props = odb.CfnOdbNetworkProps(
                availability_zone="availabilityZone",
                availability_zone_id="availabilityZoneId",
                backup_subnet_cidr="backupSubnetCidr",
                client_subnet_cidr="clientSubnetCidr",
                default_dns_prefix="defaultDnsPrefix",
                delete_associated_resources=False,
                display_name="displayName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41648888050cc85bcebe5a38dc9918a297404cec697643f0d6d43e8c7feb6ea8)
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument availability_zone_id", value=availability_zone_id, expected_type=type_hints["availability_zone_id"])
            check_type(argname="argument backup_subnet_cidr", value=backup_subnet_cidr, expected_type=type_hints["backup_subnet_cidr"])
            check_type(argname="argument client_subnet_cidr", value=client_subnet_cidr, expected_type=type_hints["client_subnet_cidr"])
            check_type(argname="argument default_dns_prefix", value=default_dns_prefix, expected_type=type_hints["default_dns_prefix"])
            check_type(argname="argument delete_associated_resources", value=delete_associated_resources, expected_type=type_hints["delete_associated_resources"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if availability_zone_id is not None:
            self._values["availability_zone_id"] = availability_zone_id
        if backup_subnet_cidr is not None:
            self._values["backup_subnet_cidr"] = backup_subnet_cidr
        if client_subnet_cidr is not None:
            self._values["client_subnet_cidr"] = client_subnet_cidr
        if default_dns_prefix is not None:
            self._values["default_dns_prefix"] = default_dns_prefix
        if delete_associated_resources is not None:
            self._values["delete_associated_resources"] = delete_associated_resources
        if display_name is not None:
            self._values["display_name"] = display_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone (AZ) where the ODB network is located.

        Required when creating an ODB network. Specify either AvailabilityZone or AvailabilityZoneId to define the location of the network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-odbnetwork.html#cfn-odb-odbnetwork-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def availability_zone_id(self) -> typing.Optional[builtins.str]:
        '''The AZ ID of the AZ where the ODB network is located.

        Required when creating an ODB network. Specify either AvailabilityZone or AvailabilityZoneId to define the location of the network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-odbnetwork.html#cfn-odb-odbnetwork-availabilityzoneid
        '''
        result = self._values.get("availability_zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_subnet_cidr(self) -> typing.Optional[builtins.str]:
        '''The CIDR range of the backup subnet in the ODB network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-odbnetwork.html#cfn-odb-odbnetwork-backupsubnetcidr
        '''
        result = self._values.get("backup_subnet_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_subnet_cidr(self) -> typing.Optional[builtins.str]:
        '''The CIDR range of the client subnet in the ODB network.

        Required when creating an ODB network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-odbnetwork.html#cfn-odb-odbnetwork-clientsubnetcidr
        '''
        result = self._values.get("client_subnet_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_dns_prefix(self) -> typing.Optional[builtins.str]:
        '''The DNS prefix to the default DNS domain name.

        The default DNS domain name is oraclevcn.com.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-odbnetwork.html#cfn-odb-odbnetwork-defaultdnsprefix
        '''
        result = self._values.get("default_dns_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_associated_resources(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to delete associated OCI networking resources along with the ODB network.

        Required when creating an ODB network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-odbnetwork.html#cfn-odb-odbnetwork-deleteassociatedresources
        '''
        result = self._values.get("delete_associated_resources")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The user-friendly name of the ODB network.

        Required when creating an ODB network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-odbnetwork.html#cfn-odb-odbnetwork-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags to assign to the Odb Network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-odb-odbnetwork.html#cfn-odb-odbnetwork-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOdbNetworkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCloudAutonomousVmCluster",
    "CfnCloudAutonomousVmClusterProps",
    "CfnCloudExadataInfrastructure",
    "CfnCloudExadataInfrastructureProps",
    "CfnCloudVmCluster",
    "CfnCloudVmClusterProps",
    "CfnOdbNetwork",
    "CfnOdbNetworkProps",
]

publication.publish()

def _typecheckingstub__d5f3b11bad526801ca3c7c4e0e6c7dadf7c59ded4c26290e2160449d622fe4b7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    autonomous_data_storage_size_in_t_bs: typing.Optional[jsii.Number] = None,
    cloud_exadata_infrastructure_id: typing.Optional[builtins.str] = None,
    cpu_core_count_per_node: typing.Optional[jsii.Number] = None,
    db_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    is_mtls_enabled_vm_cluster: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    license_model: typing.Optional[builtins.str] = None,
    maintenance_window: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCloudAutonomousVmCluster.MaintenanceWindowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    memory_per_oracle_compute_unit_in_g_bs: typing.Optional[jsii.Number] = None,
    odb_network_id: typing.Optional[builtins.str] = None,
    scan_listener_port_non_tls: typing.Optional[jsii.Number] = None,
    scan_listener_port_tls: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    time_zone: typing.Optional[builtins.str] = None,
    total_container_databases: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84a4f6b25bd9fc71f4af4608dc8d871a48a14e3aa106d9234cbf4fe28cb2b58f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e2eb3cdd94f355c2d04e4e4acfc5c7ab515c2cf6e1291a5cd397e7293bef9dc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40074e4af0815e5d10dc283d57884238e94d4495641eabd516fb0756ea7c3470(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5301a4ddecbbb56f2a61e1dc19ab1b23bbb1871188111de8c469ba85ec8831c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d5db84de12cdb3e5fabc3ed93ef628c9b5d3c1442b857b2ed5613f1ae8ee8d8(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3920feef52a9977e900bf54bab82c28ef41365e37516fc5e8e6a08317645e7bb(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__376a9ebe12aa174628e81620a3eb8d3f7a5903598d84242a38a6521b11c10c8d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75d262c2ba8661c4d2d20abe159b3efce30fa2a6854ff6d4d27b98c116630ce7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b71c28f08596e3a8e06bf9ac61f202a72d06b5f6a93ae96a6cd988fa2c8b3457(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__429e238c2071c653da37b075f2da161573e5972cfc94448900389409da574e63(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9893af2fa0c239ed09a25053b836f4c53aa964e484761b3656bf3f69ee2f20aa(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCloudAutonomousVmCluster.MaintenanceWindowProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd777a3c3d03d11ff6d441f65051a7d1dcba1c191c5da7776d901c5b9765eb42(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d834f35ba34f357c207777de5cc71d5a4ff7f1fc34d7d2258c384cf3f2fe69ea(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd9cf4eca6ac7c9c9481d6618538bfd5cfd343c9c4dee27e927e579919f0ee93(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a7c3ab9bede20a7946889e0e134a092708444b390ea3a2deaafb7e86de212cb(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c0f9eb455c371aedd7a5d89d20d74ae053b5c2fbe1fd8e6614a484ac7e8c9a1(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8343f27429e0f5eae088fa7811047979c32cb60a08a24cfaa30bd3ccb47ed883(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4f14ad61521ea763f91422ba382ad5682e9530d8b2883c57ade0003139ff56(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bec420fa64b103170ca1fde88b7f5526381889811659e8a32ae9356eed292838(
    *,
    days_of_week: typing.Optional[typing.Sequence[builtins.str]] = None,
    hours_of_day: typing.Optional[typing.Union[typing.Sequence[jsii.Number], _IResolvable_da3f097b]] = None,
    lead_time_in_weeks: typing.Optional[jsii.Number] = None,
    months: typing.Optional[typing.Sequence[builtins.str]] = None,
    preference: typing.Optional[builtins.str] = None,
    weeks_of_month: typing.Optional[typing.Union[typing.Sequence[jsii.Number], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__221a7c6782ef0d7603f8cd9a8a17d1bbaad9d65511e49e607ac274b8a007d48b(
    *,
    autonomous_data_storage_size_in_t_bs: typing.Optional[jsii.Number] = None,
    cloud_exadata_infrastructure_id: typing.Optional[builtins.str] = None,
    cpu_core_count_per_node: typing.Optional[jsii.Number] = None,
    db_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    is_mtls_enabled_vm_cluster: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    license_model: typing.Optional[builtins.str] = None,
    maintenance_window: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCloudAutonomousVmCluster.MaintenanceWindowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    memory_per_oracle_compute_unit_in_g_bs: typing.Optional[jsii.Number] = None,
    odb_network_id: typing.Optional[builtins.str] = None,
    scan_listener_port_non_tls: typing.Optional[jsii.Number] = None,
    scan_listener_port_tls: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    time_zone: typing.Optional[builtins.str] = None,
    total_container_databases: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd782f736e7ad827f171e15d160c54071c1fbef5443d136721533cbfdcdb7012(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    availability_zone: typing.Optional[builtins.str] = None,
    availability_zone_id: typing.Optional[builtins.str] = None,
    compute_count: typing.Optional[jsii.Number] = None,
    customer_contacts_to_send_to_oci: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCloudExadataInfrastructure.CustomerContactProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    database_server_type: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    shape: typing.Optional[builtins.str] = None,
    storage_count: typing.Optional[jsii.Number] = None,
    storage_server_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f2b53aab94ecf4f8defcc0e14b676f19557d80b7dd0f9ff46a17b7649889a87(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30c5d730c06a06b60c97eec0e4a7fec63bac2317a2c033784ea9da48cda003b4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c16313314e3dc88f64b64a6807c0212a1ebb85e656c09cf7edb0f12490e36f6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2438c10c6661d5ac7195e2cd938683127ead28b38288093164aed692e449d80a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed6c897fe570d07a340273c57b43f97da5d100a17ae8701b161d22cf07674db5(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__564d722d30f571b6b15ec3202d92d33e97da84125c2eabe6a9cebe8d28fed3d6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCloudExadataInfrastructure.CustomerContactProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e15e2bca6e90c311020132fc94b88d4dd573507aadbba5a8fddfbd5970990a3e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d12c1cc442676c06c38458b560f32148a7562dbf983c5df26ac19ffea7c7ee58(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__044d56c3db02ff4cda6e4851e60243f1c99ed89d6880d3e3d3d95a41f20c78c6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27c4cf52db8d984fcff55e5d69a31d9e228dff810356ee3b15020f688804596f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a8454cbe7499d2e89bee927276f8936ca72e6a1ce92f522f2f3a1178753392e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9909f2504aae00efa9d8adaf040cb71163078ccb5d88b84ca3af82a80de540b3(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__643c0e64847e961d0058c2280408d7c853e987c242dc2bdfb33b5b65dcc6c0f3(
    *,
    email: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b021189fda911f5f9c01459f93a1cc1991300050c373d976ffb11c43e7ef9081(
    *,
    availability_zone: typing.Optional[builtins.str] = None,
    availability_zone_id: typing.Optional[builtins.str] = None,
    compute_count: typing.Optional[jsii.Number] = None,
    customer_contacts_to_send_to_oci: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCloudExadataInfrastructure.CustomerContactProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    database_server_type: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    shape: typing.Optional[builtins.str] = None,
    storage_count: typing.Optional[jsii.Number] = None,
    storage_server_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54a24296108cf4d367a887b0b65dc2c9163c185183c8fde1522a8cb329db03c9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cloud_exadata_infrastructure_id: typing.Optional[builtins.str] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    cpu_core_count: typing.Optional[jsii.Number] = None,
    data_collection_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCloudVmCluster.DataCollectionOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data_storage_size_in_t_bs: typing.Optional[jsii.Number] = None,
    db_node_storage_size_in_g_bs: typing.Optional[jsii.Number] = None,
    db_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    display_name: typing.Optional[builtins.str] = None,
    gi_version: typing.Optional[builtins.str] = None,
    hostname: typing.Optional[builtins.str] = None,
    is_local_backup_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    is_sparse_diskgroup_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    license_model: typing.Optional[builtins.str] = None,
    memory_size_in_g_bs: typing.Optional[jsii.Number] = None,
    odb_network_id: typing.Optional[builtins.str] = None,
    scan_listener_port_tcp: typing.Optional[jsii.Number] = None,
    ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    system_version: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    time_zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed59e4637cf9d059e23e91ea16d89733fbc266730217c0eb52cd6e26b74ca7c7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d823fc77af2f98ddeee14344f0e2eb8f2dd78ad96c2039f50849367a0710a3a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bf5be722e37c84a8be0753f43f6ebea1d0a90a8366126ea1037239c338f1d8d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6ff07037dfba0ff0af683d4166a5b861e52d71412e3f43496c4333804c29424(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97dfb24de12ee075095d22107411f090b917260a37c1ad001b48d7a5c67cb754(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53fa60e8088e8fcfabc4956f1ab3fbbe0607d6039731af37fdbf97088759d7f1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCloudVmCluster.DataCollectionOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10a4a98dd975dea2ac63836158b2dc7afd11f93fa6eef648312be262c3ea26ec(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56b2b388df0abb719bfd805181dfedcccb07a854fdad9846d4422b3c03934e4f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b1dc50ef9ded98095512787e029921d39680bf2148e093981b23da405bf6c6f(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faa8f862640240013012d7cb9579c5f7537d081345be3b3e24850b27f8726e8e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e526643f4d50a0bc3309ec23106c8cf45132d45372c3b9b66ffc9329c9e1c8f1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fd54015f6c4b31aa2007d549141e71219e140c311d6f9e23a787d6f35024881(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cee2b990c5219e427b51018646f252e8e93f20f5bc21497075e635e6fee21bc6(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c9800b0f09654567a1b07e3e8f1762764faa4d45ca7c8f2740ead91709fa406(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__967fcd6461478a7564eb074b4498f432e3de0c5c89704737d521da3f25b82936(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12fb5bc77e272b408d9ce9c7acda5e61ab3441f5399d13b2019847b549593e4b(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__350c5336798cdbfad4947370bdc277a67530ed8e6b01d083fca3f79b8830dea6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eb9bc6b7d5257f43d703fc090ba522f231e4a93d03f84a030b4df45e8c072b2(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b623a41b47f8d29ffe185d4d174da5e8c6c773a014a3ccf0409f011487bc1b1(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95a2f67985613635273aa653a865d22f373a34cc2cf492bbaecbc97526a00620(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb35585e2ec32ece572f8bcd0f0a038f35ebbc9d6e29c933404bd886b5900921(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbc007d119e94eccae2b52e6822c2ec73b5e10e124879ca88059e3b3b536edfd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0be5e048213b0ee63e4c9703a3c1b37da85fb4dc37d9458571be7e6789ddbe30(
    *,
    is_diagnostics_events_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    is_health_monitoring_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    is_incident_logs_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7c1c550550cdc807e34dbb5ced4b50daf930df9156b6a6f0dfaa8e978be765a(
    *,
    cloud_exadata_infrastructure_id: typing.Optional[builtins.str] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    cpu_core_count: typing.Optional[jsii.Number] = None,
    data_collection_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCloudVmCluster.DataCollectionOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data_storage_size_in_t_bs: typing.Optional[jsii.Number] = None,
    db_node_storage_size_in_g_bs: typing.Optional[jsii.Number] = None,
    db_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    display_name: typing.Optional[builtins.str] = None,
    gi_version: typing.Optional[builtins.str] = None,
    hostname: typing.Optional[builtins.str] = None,
    is_local_backup_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    is_sparse_diskgroup_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    license_model: typing.Optional[builtins.str] = None,
    memory_size_in_g_bs: typing.Optional[jsii.Number] = None,
    odb_network_id: typing.Optional[builtins.str] = None,
    scan_listener_port_tcp: typing.Optional[jsii.Number] = None,
    ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    system_version: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    time_zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fb7fc690c89d5ce8f5abecb60ad841f57c0a476f500c817c386b57c3cd0f5d6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    availability_zone: typing.Optional[builtins.str] = None,
    availability_zone_id: typing.Optional[builtins.str] = None,
    backup_subnet_cidr: typing.Optional[builtins.str] = None,
    client_subnet_cidr: typing.Optional[builtins.str] = None,
    default_dns_prefix: typing.Optional[builtins.str] = None,
    delete_associated_resources: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    display_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2bd65fc6165cb531de2b171a21a41aaf44e19b81b1e54c00c7b0bb7dbc5feab(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afa78d8af0d52b46b8c4cc90575b6a94e64eb6cb32aa68eb759b91d8213e31ac(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87621d2b03c5469d26954de7e37dfd0d3e012b5b4644ec0232e59bfecfb758e9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__328deed1718c1266e8446a386f2cfe2272763b64c3f37b5bd93a7c2f77ab2d5d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eee98a4fbff2c83a839881f8a102d4b7813c50e6fdb9be0997144c385e71c305(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__964e75c8af7e656feecdf2af9cc1f3709e5857d22d004e58037f1a4d97df301d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccee4738061946ef5f75dacb78a62f5c60382f3bd85cd506ee1454b932d8374a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc86642a834ad1214ad781ba4b6b7516ddb5e4df5219e6f1572c3707c253846a(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f9a4c06370e66400707daa4ab73fb37a67d67c8422f10b57fa0ee6b191128e7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a78f63e76d627d52015eb8e2a0dc2ab1a80a0926480a2a40fc93da33d803ce3(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41648888050cc85bcebe5a38dc9918a297404cec697643f0d6d43e8c7feb6ea8(
    *,
    availability_zone: typing.Optional[builtins.str] = None,
    availability_zone_id: typing.Optional[builtins.str] = None,
    backup_subnet_cidr: typing.Optional[builtins.str] = None,
    client_subnet_cidr: typing.Optional[builtins.str] = None,
    default_dns_prefix: typing.Optional[builtins.str] = None,
    delete_associated_resources: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    display_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
