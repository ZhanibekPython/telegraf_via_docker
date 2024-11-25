from .common_params import CommonOutputsParams


class Cloudwatch(CommonOutputsParams):
    pass

class CloudwatchLogs(CommonOutputsParams):
    pass

class Kinesis(CommonOutputsParams):
    pass

class Timestream(CommonOutputsParams):
    pass

class Amon(CommonOutputsParams):
    pass

class Amqp(CommonOutputsParams):
    pass

class Kafka(CommonOutputsParams):
    pass

class AzureDataExplorer(CommonOutputsParams):
    pass

class EventHubs(CommonOutputsParams):
    pass

class Bigquery(CommonOutputsParams):
    pass

class CrateDB(CommonOutputsParams):
    pass

class Clarify(CommonOutputsParams):
    pass

class Datalog(CommonOutputsParams):
    pass

class Discard(CommonOutputsParams):
    pass

class Dynatrace(CommonOutputsParams):
    pass

class ElasticSearch(CommonOutputsParams):
    pass

class Exec(CommonOutputsParams):
    pass

class Execd(CommonOutputsParams):
    pass

class File(CommonOutputsParams):
    files: list[str] | None = None
    use_batch_format: bool | None = None
    rotation_interval: str | None = None
    rotation_max_size: str | None = None
    rotation_max_archives: int | None = None
    data_format: str | None = None
    compression_algorithm: str | None = None
    compression_level: str | None = None

class CloudPursub(CommonOutputsParams):
    pass

class Graphite(CommonOutputsParams):
    pass

class Loki(CommonOutputsParams):
    pass

class Graylog(CommonOutputsParams):
    pass

class Groundwork(CommonOutputsParams):
    pass

class HttpOutput(CommonOutputsParams):
    pass

class Health(CommonOutputsParams):
    pass

class InfluxDB(CommonOutputsParams):
    pass

class InfluxDBV2(CommonOutputsParams):
    pass

class Instrumental(CommonOutputsParams):
    pass

class IotDB(CommonOutputsParams):
    pass

class Librato(CommonOutputsParams):
    pass

class Logzio(CommonOutputsParams):
    pass

class ApplicationInsights(CommonOutputsParams):
    pass

class AzureMonitor(CommonOutputsParams):
    pass

class MongoDB(CommonOutputsParams):
    pass

class Mqtt(CommonOutputsParams):
    pass

class Nats(CommonOutputsParams):
    pass

class NebiusCloudMonitoring(CommonOutputsParams):
    pass

class Newrelic(CommonOutputsParams):
    pass

class Nsq(CommonOutputsParams):
    pass

class OpenSearch(CommonOutputsParams):
    urls: list[str] | None = None
    index_name: str | None = None
    timeout: str | None = None
    enable_sniffer: bool | None = None
    enable_gzip: bool | None = None
    health_check_interval: str | None = None
    health_check_timeout: str | None = None
    username: str | None = None
    password: str | None = None
    auth_bearer_token: str | None = None
    tls_enable: bool | None = None
    tls_ca: str | None = None
    tls_cert: str | None = None
    tls_key: str | None = None
    tls_server_name: str | None = None
    insecure_skip_verify: bool | None = None
    manage_template: bool | None = None
    template_name: str | None = None
    overwrite_template: bool | None = None
    force_document_id: bool | None = None
    float_handling: str | None = None
    float_replacement_value: float | None = None
    use_pipeline: str | None = None
    default_pipeline: str | None = None


class Opentelemetry(CommonOutputsParams):
    pass

class OpentsDB(CommonOutputsParams):
    pass

class Parquet(CommonOutputsParams):
    pass

class Postgresql(CommonOutputsParams):
    pass

class PrometheusClient(CommonOutputsParams):
    pass

class RedisTimeSeries(CommonOutputsParams):
    pass

class Remotefile(CommonOutputsParams):
    pass

class Riemann(CommonOutputsParams):
    pass

class Sensu(CommonOutputsParams):
    pass

class Sifnalfx(CommonOutputsParams):
    pass

class SocketWriter(CommonOutputsParams):
    pass

class Stackdriver(CommonOutputsParams):
    pass

class Stomp(CommonOutputsParams):
    pass

class Sql(CommonOutputsParams):
    pass

class Sumologic(CommonOutputsParams):
    pass

class Syslog(CommonOutputsParams):
    pass

class Warp10(CommonOutputsParams):
    pass

class Wavefront(CommonOutputsParams):
    pass

class Websocket(CommonOutputsParams):
    pass

class YandexCloudMonitoring(CommonOutputsParams):
    pass

class Zabbix(CommonOutputsParams):
    pass

