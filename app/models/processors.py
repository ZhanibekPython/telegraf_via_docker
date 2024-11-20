from pydantic import BaseModel
from .common_params import CommonProcessorsParams



class AwsEc2(CommonProcessorsParams):
    pass

class ConverterTagsParams(BaseModel):
    measurement: list[str] | None = None
    string: list[str] | None = None
    integer: list[str] | None = None
    unsigned: list[str] | None = None
    boolean: list[bool] | None = None
    float: list[str] | None = None
    timestamp: list[str] | None = None
    timestamp_format: str | None = None

class ConverterFieldsParams(ConverterTagsParams):
    tag: list[str] | None = None

class Converter(CommonProcessorsParams):
    tags: ConverterTagsParams | None = None
    fields: ConverterFieldsParams | None = None

class CloneTags(BaseModel):
    additional_tag: str | None = None

class Clone(CommonProcessorsParams):
    name_override: str | None = None
    name_prefix: str | None = None
    name_suffix: str | None = None
    tags: list[CloneTags] | None = None

class Date(CommonProcessorsParams):
    tag_key: str | None = None
    field_key: str | None = None
    date_format: str | None = None
    date_format: str | None = None
    date_offset: str | None = None
    timezone: str | None = None

class Dedup(CommonProcessorsParams):
    dedup_interval: str | None = None

class DefaultsFields(BaseModel):
    field_1: str | None = None
    time_idle: int | None = None
    is_error: bool | None = None

class Defaults(CommonProcessorsParams):
    fields: DefaultsFields | None = None

class EnumValueMapping(BaseModel):
    green: int | None = None
    amber: int | None = None
    red: str | None = None

class EnumMapping(BaseModel):
    field: str | None = None
    tag: str | None = None
    dest: str | None = None
    default: str | None = None
    value_mapping: list[EnumValueMapping] | None = None

class Enum(CommonProcessorsParams):
    mapping: list[EnumMapping] | None = None

class Execd(CommonProcessorsParams):
    command: list[str] | None = None
    environment: list[str] | None = None
    restart_delay: str | None = None
    data_format: str | None = None

class FilterRule(BaseModel):
    name: list[str] | None = None
    tags: dict[str, str] | None = None
    fields: list[str] | None = None
    action: str | None = None

class Filter(CommonProcessorsParams):
    default: str | None = None
    rule: list[FilterRule] | None = None
        
class Geoip(CommonProcessorsParams):
    pass

class Lookup(CommonProcessorsParams):
    pass

class Ifname(CommonProcessorsParams):
    pass

class Noise(CommonProcessorsParams):
    pass

class OverrideTag(BaseModel):
    additional_tag: str | None = None

class Override(CommonProcessorsParams):
    name_override: str | None = None
    name_prefix: str | None = None
    name_suffix: str | None = None

    tags: list[OverrideTag] | None = None

class Parser(CommonProcessorsParams):
    parse_fields: list[str] | None = None
    parse_fields_base64: list[str] | None = None
    parse_tags: list[str] | None = None
    drop_original: bool | None = None
    merge: str | None = None
    data_format: str | None = None

class Pivot(CommonProcessorsParams):
    tag_key: str | None = None
    value_key: str | None = None

class PortName(CommonProcessorsParams):
    pass

class Printer(CommonProcessorsParams):
    pass

class RegexCommonParams(BaseModel):
    pattern: str | None = None
    replacement: str | None = None

class RegexParamsResultKey(RegexCommonParams):
    result_key: str | None = None

class RegexPlusKey(RegexCommonParams):
    key: str | None = None

class Regex(CommonProcessorsParams):
    namepass: list[str] | None = None

    tags: list[RegexPlusKey] | None = None
    fields: list[RegexPlusKey] | None = None
    field_rename: list[RegexParamsResultKey] | None = None
    tag_rename: list[RegexParamsResultKey] | None = None
    metric_rename: list[RegexCommonParams] | None = None

class RenameReplace(BaseModel):
    measurement: str | None = None
    tag: str | None = None
    field: str | None = None 
    dest: str | None = None

class Rename(CommonProcessorsParams):
    replace: list[RenameReplace] | None = None

class Rename(CommonProcessorsParams):
    pass

class ReverseDns(CommonProcessorsParams):
    pass

class S2geo(CommonProcessorsParams):
    pass

class Scale(CommonProcessorsParams):
    pass

class SnmpLookupTags(BaseModel):
    oid: str | None = None
    name: str | None = None
    conversion: str | None = None

class SnmpLookup(CommonProcessorsParams):
    agent_tag: str | None = None
    index_tag: str | None = None
    max_parallel_lookups: int | None = None
    max_cache_entries: int | None = None
    ordered: bool | None = None
    cache_ttl: str | None = None
    min_time_between_updates: str | None = None
    tag: list[SnmpLookupTags] | None = None


class SplitTemplate(BaseModel):
    name: str | None = None
    tags: list[str] | None = None
    fields: list[str] | None = None

class Split(CommonProcessorsParams):
    drop_original: bool | None = None
    template: list[SplitTemplate] | None = None

class StarlarkConstants(BaseModel):
    max_size: int | None = None
    threshold: float | None = None
    default_name: str | None = None
    debug_mode: bool | None = None

class Starlark(CommonProcessorsParams):
    source: str | None = None
    script: str | None = None
    constants: list[StarlarkConstants] | None = None

class Strings(CommonProcessorsParams):
    pass

class TagLimit(CommonProcessorsParams):
    pass

class Template(CommonProcessorsParams):
    pass

class Timestamp(CommonProcessorsParams):
    field: str | None = None
    source_timestamp_format: str | None = None
    source_timestamp_timezone: str | None = None
    destination_timestamp_format: str | None = None
    destination_timestamp_timezone: str | None = None

class Topk(CommonProcessorsParams):
    period: int | None = None
    k: int | None = None
    group_by: list[str] | None = None
    fields: list[str] | None = None
    aggregation: str | None = None
    bottomk: bool | None = None
    add_groupby_tag: str | None = None
    add_rank_fields: list[str] | None = None
    add_aggregate_fields: list[str] | None = None

class Unpivot(CommonProcessorsParams):
    pass

