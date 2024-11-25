from pydantic import BaseModel
from .inputs import *
from .outputs import *
from .processors import *
from .aggregators import *
from .stores import *


class GlobalTags(BaseModel):
    tags: dict[str, str | list[str]] | None = None

class SecretStores(BaseModel):
    docker: DockerSecretStore | None = None
    http: HttpSecretStore | None = None
    jose: JoseSecretStore | None = None
    os: OSSecretStore | None = None
    
class AgentParams(BaseModel):
    interval: str | None = None
    round_interval: bool | None = None
    metric_batch_size: int | None = None
    metric_buffer_limit: int | None = None
    collection_jitter: str | None = None
    collection_offset: str | None = None
    flush_interval: str | None = None
    flush_jitter: str | None = None
    precision: str | None = None
    debug: bool | None = None
    quiet: bool | None = None
    logformat: str | None = None
    logfile: str | None = None
    logfile_rotation_interval: str | None = None
    logfile_rotation_max_size: int | None = None
    logfile_rotation_max_archives: int | None = None
    log_with_timezone: str | None = None
    hostname: str | None = None
    omit_hostname: bool | None = None
    snmp_translator: str | None = None
    statefile: str | None = None
    always_include_local_tags: bool | None = None
    always_include_global_tags: bool | None = None
    skip_processors_after_aggregators: bool | None = None
    buffer_strategy: str | None = None
    buffer_directory: str | None = None

class InputsPlugins(BaseModel):
    amqp_consumer: list[AmqpConsumer] | None = None
    activemq: list[Activemq] | None = None
    aliyuncms: list[Aliyuncms] | None = None
    awsalarms: list[Awsalarms] | None = None
    cloudwatch: list[Cloudwatch] | None = None
    kinesis_consumer: list[KinesisConsumer] | None = None
    aurora: list[Aurora] | None = None
    apache: list[Apache] | None = None
    mesos: list[Mesos] | None = None
    solr: list[Solr] | None = None
    tomcat: list[Tomcat] | None = None
    zipkin: list[Zipkin] | None = None
    zookeeper: list[Zookeeper] | None = None
    azure_monitor: list[AzureMonitor] | None = None
    beat: list[Beat] | None = None
    bond: list[Bond] | None = None
    ceph: list[Ceph] | None = None
    chrony: list[Chrony] | None = None
    cisco_telemetry_mdt: list[CiscoTelemetryMdt] | None = None
    clickhouse: list[Clickhouse] | None = None
    cpu: list[Cpu] | None = None
    disk: list[Disk] | None = None
    dns_query: list[DnsQuery] | None = None
    docker: list[Docker] | None = None
    elasticsearch: list[ElasticSearch] | None = None
    elasticsearch_query: list[ElasticSearchQuery] | None = None
    ethtool: list[Ethtool] | None = None
    execd: list[Execd] | None = None
    file: list[File] | None = None
    fireboard: list[Fireboard] | None = None
    fluentd: list[Fluentd] | None = None
    github: list[Github] | None = None
    cloud_pubsub: list[CloudPubsub] | None = None
    graylog: list[Graylog] | None = None
    haproxy: list[Haproxy] | None = None
    http: list[HttpInput] | None = None
    http_listener_v2: list[HttpListenerV2] | None = None
    huebridge: list[Huebridge] | None = None
    influxdb: list[Influxdb] | None = None
    intel_baseband: list[IntelBaseband] | None = None
    internet_speed: list[InternetSpeed] | None = None
    ipvs: list[Ipvs] | None = None
    jenkins: list[Jenkins] | None = None
    kapacitor: list[Kapacitor] | None = None
    kibana: list[Kibana] | None = None
    kubernetes: list[Kubernetes] | None = None
    logparser: list[Logparser] | None = None
    mem: list[Mem] | None = None
    sqlserver: list[Sqlserver] | None = None
    mongodb: list[Mongodb] | None = None
    mysql: list[mMsql] | None = None
    net: list[Net] | None = None
    netstat: list[Netstat] | None = None
    nginx: list[Nginx] | None = None
    nsdp: list[Nsdp] | None = None
    opensearch_query: list[OpensearchQuery] | None = None
    opentelemetry: list[Opentelemetry] | None = None
    oracle: list[Oracle] | None = None
    postgresql: list[Postgresql] | None = None
    prometheus: list[Prometheus] | None = None
    rabbitmq: list[Rabbitmq] | None = None
    redis: list[Redis] | None = None
    snmp: list[Snmp] = None
    snmp_trap: list[SnmpTrap] | None = None
    sql: list[Sql] | None = None
    statsd: list[Statsd] | None = None
    syslog: list[Syslog] | None = None
    system: list[System] | None = None
    temp: list[Temp] | None = None
    win_services: list[WinServices] | None = None


class ProcessorsPlugins(BaseModel):
    aws_ec2: list[AwsEc2] | None = None
    converter: list[Converter] | None = None 
    clone: list[Clone] | None = None 
    date: list[Date] | None = None 
    dedup: list[Dedup] | None = None 
    defaults: list[Defaults] | None = None
    enum: list[Enum] | None = None 
    execd: list[Execd] | None = None 
    filter: list[Filter] | None = None 
    geoip: list[Geoip] | None = None 
    lookup: list[Lookup] | None = None 
    ifname: list[Ifname] | None = None 
    noise: list[Noise] | None = None 
    override: list[Override] | None = None 
    parser: list[Parser] | None = None 
    pivot: list[Pivot] | None = None 
    port_name: list[PortName] | None = None  
    printer: list[Printer] | None = None 
    regex: list[Regex] | None = None 
    rename: list[Rename] | None = None 
    reverse_dns: list[ReverseDns] | None = None 
    s2geo: list[S2geo] | None = None 
    scale: list[Scale] | None = None 
    snmp_lookup: list[SnmpLookup] | None = None 
    split: list[Split] | None = None 
    starlark: list[Starlark] | None = None 
    strings: list[Strings] | None = None 
    tag_limit: list[TagLimit] | None = None 
    template: list[Template] | None = None 
    timestamp: list[Timestamp] | None = None 
    topk: list[Topk] | None = None 
    unpivot: list[Unpivot] | None = None 

class AggregatorsPlugins(BaseModel):
    basicstats: list[Basicstats] | None = None 
    derivative: list[Derivative] | None = None 
    final: list[Final] | None = None 
    histogram: list[Histogram] | None = None 
    merge: list[Merge] | None = None 
    minmax: list[Minmax] | None = None 
    quantile: list[Quantile] | None = None 
    starlark: list[Starlark] | None = None 
    valuecounter: list[ValueCounter] | None = None 


class OutputsPlugins(BaseModel):
    cloudwatch: list[Cloudwatch] | None = None
    cloudwatch_logs: list[CloudwatchLogs] | None = None
    kinesis: list[Kinesis] | None = None
    timestream: list[Timestream] | None = None
    amon: list[Amon] | None = None
    amqp: list[Amqp] | None = None
    kafka: list[Kafka] | None = None
    azure_data_explorer: list[AzureDataExplorer] | None = None
    event_hubs: list[EventHubs] | None = None
    bigquery: list[Bigquery] | None = None
    cratedb: list[CrateDB] | None = None
    clarify: list[Clarify] | None = None
    datalog: list[Datalog] | None = None
    discard: list[Discard] | None = None
    dynatrace: list[Dynatrace] | None = None
    elasticsearch: list[ElasticSearch] | None = None
    exec: list[Exec] | None = None
    execd: list[Execd] | None = None
    file: list[File] | None = None
    cloud_pubsub: list[CloudPubsub] | None = None
    graphite: list[Graphite] | None = None
    loki: list[Loki] | None = None
    graylog: list[Graylog] | None = None
    groundwork: list[Groundwork] | None = None
    httpoutput: list[HttpOutput] | None = None
    health: list[Health] | None = None
    influxdb: list[InfluxDB] | None = None
    influxdb_v2: list[InfluxDBV2] | None = None
    instrumental: list[Instrumental] | None = None
    iotdb: list[IotDB] | None = None
    librato: list[Librato] | None = None
    logzio: list[Logzio] | None = None
    application_insights: list[ApplicationInsights] | None = None
    azure_monitor: list[AzureMonitor] | None = None
    mongodb: list[MongoDB] | None = None
    mqtt: list[Mqtt] | None = None
    nats: list[Nats] | None = None
    nebius_cloud_monitoring: list[NebiusCloudMonitoring] | None = None
    newrelic: list[Newrelic] | None = None
    nsq: list[Nsq] | None = None
    opensearch: list[OpenSearch] | None = None
    opentelemetry: list[Opentelemetry] | None = None
    opentsdb: list[OpentsDB] | None = None
    parquet: list[Parquet] | None = None
    postgresql: list[Postgresql] | None = None
    prometheus_client: list[PrometheusClient] | None = None
    redistimeseries: list[RedisTimeSeries] | None = None
    remotefile: list[Remotefile] | None = None
    riemann: list[Riemann] | None = None
    sensu: list[Sensu] | None = None
    socket_writer: list[SocketWriter] | None = None
    stackdriver: list[Stackdriver] | None = None
    stomp: list[Stomp] | None = None
    sql: list[Sql] | None = None
    sumologic: list[Sumologic] | None = None
    syslog: list[Syslog] | None = None
    warp10: list[Warp10] | None = None
    wavefront: list[Wavefront] | None = None
    websocket: list[Websocket] | None = None
    yandex_cloud_monitoring: list[YandexCloudMonitoring] | None = None
    zabbix: list[Zabbix] | None = None


class ConfigurationFile(BaseModel):
    global_tags: GlobalTags | None = None
    secretstores: SecretStores | None = None
    agent: AgentParams | None = None
    inputs: InputsPlugins | None = None
    processors: ProcessorsPlugins | None = None
    aggregators: AggregatorsPlugins | None = None
    outputs: OutputsPlugins | None = None


class ConfigSchema(BaseModel):
    container_name: str
    config: ConfigurationFile


class ConfigEdit(BaseModel):
    container_name: str
    new_content: dict