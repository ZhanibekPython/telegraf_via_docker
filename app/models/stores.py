from pydantic import BaseModel


class DockerSecretStore(BaseModel):
    id: str | None = None ## in this secret-store via @{<id>:<secret_key>} (mandatory)
    path: str | None = None ## Directory for storing the secrets
    dynamic: bool | None = None ## Allow dynamic secrets that are updated during runtime of telegraf
   
class HttpSecretStore(BaseModel):
    pass

class JoseSecretStore(BaseModel):
    id: str | None = None ## in this secret-store via @{<id>:<secret_key>} (mandatory)
    path: str | None = None ## Directory for storing the secrets
    password: str | None = None

class OSSecretStore(BaseModel):
    id: str | None = None ## in this secret-store via @{<id>:<secret_key>} (mandatory)
    keyring: str | None = None ##`<collection>:<keyring>:<key_name>`
    collection: str | None = None
    password: str | None = None ## macOS Keychain password
    dynamic: str | None = None ## Allow dynamic secrets that are updated during runtime of telegraf