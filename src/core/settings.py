from pydantic import BaseSettings, Field, RedisDsn


class Settings(BaseSettings):
    # SERVICE
    host: str = Field("0.0.0.0", env="SERVICE_HOST")
    port: int = Field(8000, env="SERVICE_PORT")
    debug: bool = Field(True, env="SERVICE_DEBUG")
    log_level: str = Field("debug", env="SERVICE_LOG_LEVEL")

    # REDIS
    redis_dsn: RedisDsn = Field("redis://localhost", env="REDIS_DSN")

    # POSTGRES
    postgres_user: str = Field("user", env="POSTGRES_USER")
    postgres_password: str = Field("password", env="POSTGRES_PASSWORD")
    postgres_database: str = Field("database", env="POSTGRES_DB")
    postgres_host: str = Field("0.0.0.0", env="POSTGRES_HOST")
    postgres_port: int = Field(5432, env="POSTGRES_PORT")

    class Config:
        env_file = ".env"
