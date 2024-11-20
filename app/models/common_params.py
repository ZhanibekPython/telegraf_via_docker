from pydantic import BaseModel


class CommonInputsParams(BaseModel):
    alias: str | None = None
    interval: str | None = None
    precision: str | None = None
    time_source: str | None = None
    collection_jitter: str | None = None
    collection_offset: str | None = None
    name_override: str | None = None
    name_prefix: str | None = None
    name_suffix: str | None = None
    tags: dict[str, str | list[str]] | None = None
    log_level: str | None = None

class CommonProcessorsParams(BaseModel):
    alias: str | None = None
    order: int | None = None
    log_level: str | None = None

class CommonAggregatorsParams(BaseModel):
    alias: str | None = None
    period: str | None = None
    delay: str | None = None
    grace: str | None = None
    drop_original: bool | None = None
    name_override: str | None = None
    name_prefix: str | None = None
    name_suffix: str | None = None
    tags: dict[str, str] | None = None
    log_level: str | None = None

class CommonOutputsParams(BaseModel):
    alias: str | None = None
    flush_interval: str | None = None
    flush_jitter: str | None = None
    metric_batch_size: int | None = None
    metric_buffer_limit: int | None = None
    name_override: str | None = None
    name_prefix: str | None = None
    name_suffix: str | None = None
    log_level: str | None = None