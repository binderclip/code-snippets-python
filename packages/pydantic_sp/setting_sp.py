from pydantic import BaseSettings


class Settings(BaseSettings):
    redis_host = 'localhost'    # set os env APP_REDIS_HOST to overwrite
    redis_port = 6379
    redis_database = 0
    debug = False   # 'true' and '1' are True, 'false' and '0' are False

    class Config:
        env_prefix = 'APP_'


def main():
    settings = Settings()
    print(settings.redis_host)
    print(settings.redis_port, type(settings.redis_port))
    print(settings.debug)


if __name__ == '__main__':
    main()


# https://pydantic-docs.helpmanual.io/#settings
