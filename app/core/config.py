class Settings:
    DATABASE_URL: str = "postgresql://postgres:root@localhost:5432/BankingCustomerInfo"
    POOL_SIZE: int = 10
    POOL_PRE_PING: bool = True
    MAX_OVERFLOW = 20

settings = Settings()