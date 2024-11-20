from pydantic import BaseModel
from .common_params import CommonInputsParams


class AmqpConsumer(CommonInputsParams):
    pass

class Activemq(CommonInputsParams):
    pass

class Aliyuncms(CommonInputsParams):
    pass

class Awsalarms(CommonInputsParams):
    pass

class Cloudwatch(CommonInputsParams):
    pass

class KinesisConsumer(CommonInputsParams):
    pass

class Aurora(CommonInputsParams):
    pass

class Apache(CommonInputsParams):
    pass

class Mesos(CommonInputsParams):
    pass

class Solr(CommonInputsParams):
    pass

class Tomcat(CommonInputsParams):
    pass

class Zipkin(CommonInputsParams):
    pass

class Zookeeper(CommonInputsParams):
    pass

class AzureMonitor(CommonInputsParams):
    pass

class Beat(CommonInputsParams):
    pass

class Bond(CommonInputsParams):
    pass

class Ceph(CommonInputsParams):
    pass

class Chrony(CommonInputsParams):
    pass

class CiscoTelemetryMdt(CommonInputsParams):
    pass

class Clickhouse(CommonInputsParams):
    pass

class Cpu(CommonInputsParams):
    pass

class Disk(CommonInputsParams):
    pass

class DnsQuery(CommonInputsParams):
    pass

class Docker(CommonInputsParams):
    pass

class ElasticSearch(CommonInputsParams):
    pass

class ElasticSearchQuery(CommonInputsParams):
    pass

class Ethtool(CommonInputsParams):
    pass

class Execd(CommonInputsParams):
    pass

class File(CommonInputsParams):
    pass

class Fireboard(CommonInputsParams):
    pass

class Fluentd(CommonInputsParams):
    pass

class Github(CommonInputsParams):
    pass

class CloudPubsub(CommonInputsParams):
    pass

class Graylog(CommonInputsParams):
    pass

class Haproxy(CommonInputsParams):
    pass

class HttpInput(CommonInputsParams):
    urls: list[str] | None = None
    method: str | None = None
    headers: dict[str, str] | None = None
    body: str | None = None
    content_encoding: str | None = None
    
    token: str | None = None
    token_file: str | None = None
    
    username: str | None = None
    password: str | None = None
    
    client_id: str | None = None
    client_secret: str | None = None
    token_url: str | None = None
    scopes: list[str] | None = None
    
    use_system_proxy: bool | None = None
    http_proxy_url: str | None = None
    
    tls_enable: bool | None = None
    tls_ca: str | None = None
    tls_cert: str | None = None
    tls_key: str | None = None
    tls_key_pwd: str | None = None
    tls_server_name: str | None = None
    tls_min_version: str | None = None 
    tls_cipher_suites: list[str] | None = None
    tls_renegotiation_method: str | None = None
    insecure_skip_verify: bool | None = None
    
    cookie_auth_url: str | None = None
    cookie_auth_method: str | None = None
    cookie_auth_username: str | None = None
    cookie_auth_password: str | None = None
    cookie_auth_headers: dict[str, str] | None = None
    cookie_auth_body: str | None = None
    cookie_auth_renewal: str | None = None
    
    timeout: str | None = None
    success_status_codes: list[int] | None = None
    data_format: str | None = None

class HttpListenerV2(CommonInputsParams):
    pass

class Huebridge(CommonInputsParams):
    pass

class Influxdb(CommonInputsParams):
    pass

class IntelBaseband(CommonInputsParams):
    pass

class InternetSpeed(CommonInputsParams):
    pass

class Ipvs(CommonInputsParams):
    pass

class Jenkins(CommonInputsParams):
    pass

class Kapacitor(CommonInputsParams):
    pass

class Kibana(CommonInputsParams):
    pass

class Kubernetes(CommonInputsParams):
    pass

class Logparser(CommonInputsParams):
    pass

class Mem(CommonInputsParams):
    pass

class Sqlserver(CommonInputsParams):
    pass

class Mongodb(CommonInputsParams):
    pass

class mMsql(CommonInputsParams):
    pass

class Net(CommonInputsParams):
    pass

class Netstat(CommonInputsParams):
    pass

class Nginx(CommonInputsParams):
    pass

class Nsdp(CommonInputsParams):
    pass

class OpensearchQuery(CommonInputsParams):
    pass

class Opentelemetry(CommonInputsParams):
    pass

class Oracle(CommonInputsParams):
    pass

class Postgresql(CommonInputsParams):
    pass

class Prometheus(CommonInputsParams):
    pass

class Rabbitmq(CommonInputsParams):
    pass

class Redis(CommonInputsParams):
    pass

class SNMPField(BaseModel):
    oid: str | None = None
    name: str | None = None
    conversion: str | None = None
    is_tag: bool | None = None
    oid_index_suffix: str | None = None
    oid_index_length: int | None = None
    translate: bool | None = None
    secondary_index_table: bool | None = None
    secondary_index_use: bool | None = None
    secondary_outer_join: bool | None = None

class SNMPTable(BaseModel):
    inherit_tags: list[str] | None = None
    name: str | None = None
    oid: str | None = None
    index_as_tag: bool | None = None
    field: list[SNMPField] | None = None

class Snmp(CommonInputsParams):
    agents: list[str] | None = None
    timeout: str | None = None
    version: int | None = None
    unconnected_udp_socket: bool | None = None
    path: list[str] | None = None
    community: str | None = None
    agent_host_tag: str | None = None
    retries: int | None = None
    max_repetitions: int | None = None
    sec_name: str | None = None
    auth_protocol: str | None = None
    auth_password: str | None = None
    sec_level: str | None = None
    context_name: str | None = None
    priv_protocol: str | None = None
    priv_password: str | None = None

    field: list[SNMPField] | None = None
    table: list[SNMPTable] | None = None

class SnmpTrap(CommonInputsParams):
    pass

class Sql(CommonInputsParams):
    pass

class Statsd(CommonInputsParams):
    pass

class Syslog(CommonInputsParams):
    pass

class System(CommonInputsParams):
    pass

class Temp(CommonInputsParams):
    pass

class Vsphere(CommonInputsParams):
    vcenters: list[str] | None = None
    username: str | None = None
    password: str | None = None

    vm_include: list[str] | None = None
    vm_exclude: list[str] | None = None
    vm_metric_include: list[str] | None = None
    vm_metric_exclude: list[str] | None = None
    vm_instances: int | None = None

    host_include: list[str] | None = None
    host_exclude: list[str] | None = None
    host_metric_include: list[str] | None = None
    host_metric_exclude: list[str] | None = None
    host_instances: bool | None = None

    cluster_include: list[str] | None = None
    cluster_exclude: list[str] | None = None
    cluster_metric_include: list[str] | None = None
    cluster_metric_exclude: list[str] | None = None
    cluster_instances: bool | None = None

    resource_pool_include: list[str] | None = None
    resource_pool_exclude: list[str] | None = None
    resource_pool_metric_include: list[str] | None = None
    resource_pool_metric_exclude: list[str] | None = None
    resource_pool_instances: bool | None = None

    datastore_include: list[str] | None = None
    datastore_exclude: list[str] | None = None
    datastore_metric_include: list[str] | None = None
    datastore_metric_exclude: list[str] | None = None
    datastore_instances: bool | None = None

    datacenter_include: list[str] | None = None
    datacenter_exclude: list[str] | None = None
    datacenter_metric_include: list[str] | None = None
    datacenter_metric_exclude: list[str] | None = None
    datacenter_instances: bool | None = None

    vsan_metric_include: list[str] | None = None
    vsan_metric_exclude: list[str] | None = None
    vsan_metric_skip_verify: bool | None = None
    vsan_interval: str | None = None
    separator: str | None = None
    max_query_objects: int | None = None
    max_query_metrics: int | None = None
    collect_concurrency: int | None = None
    discover_concurrency: int | None = None
    object_discovery_interval: str | None = None
    timeout: str | None = None
    use_int_samples: bool | None = None
    custom_attribute_include: list[str] | None = None
    custom_attribute_exclude: list[str] | None = None
    metric_lookback: int | None = None
    
    ssl_ca: str | None = None
    ssl_cert: str | None = None
    ssl_key: str | None = None
    insecure_skip_verify: bool | None = None
    
    historical_interval: str | None = None
    disconnected_servers_behavior: str | None = None
    http_proxy_url: str | None = None

class WinServices(CommonInputsParams):
    pass

