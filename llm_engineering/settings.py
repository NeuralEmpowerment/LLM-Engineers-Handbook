from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    # MongoDB NoSQL Database
    DATABASE_HOST: str = "mongodb://decodingml:decodingml@llm_engineering_mongo:27017"
    DATABASE_NAME: str = "twin"

    # Selenium Drivers
    SELENIUM_BROWSER_BINARY_PATH: str | None = None
    SELENIUM_BROWSER_DRIVER_PATH: str | None = None

    # LinkedIn Credentials
    LINKEDIN_USERNAME: str | None = None
    LINKEDIN_PASSWORD: str | None = None

    # RAG
    TEXT_EMBEDDING_MODEL_ID: str = "sentence-transformers/all-MiniLM-L6-v2"
    RERANKING_CROSS_ENCODER_MODEL_ID: str = "cross-encoder/ms-marco-MiniLM-L-4-v2"
    RAG_MODEL_DEVICE: str = "cpu"

    # QdrantDB Vector DB
    USE_QDRANT_CLOUD: bool = False

    QDRANT_DATABASE_HOST: str = "localhost"
    QDRANT_DATABASE_PORT: int = 6333
    QDRANT_DATABASE_URL: str = "http://localhost:6333"

    QDRANT_CLOUD_URL: str = "str"
    QDRANT_APIKEY: str | None = None

    # OpenAI API
    OPENAI_MODEL_ID: str = "gpt-3.5-turbo"
    OPENAI_API_KEY: str | None = None

    # CometML config
    COMET_API_KEY: str | None = None
    COMET_WORKSPACE: str | None = None
    COMET_PROJECT: str | None = None

    ARN_ROLE: str | None = None
    HUGGING_FACE_HUB_TOKEN: str

    HF_MODEL_ID: str = "crumb/nano-mistral"
    GPU_INSTANCE_TYPE: str = "ml.g5.xlarge"
    SM_NUM_GPUS: int = 1
    MAX_INPUT_LENGTH: int = 8000
    MAX_TOTAL_TOKENS: int = 12000
    MAX_BATCH_TOTAL_TOKENS: int = 12000
    COPIES: int = 4  # Number of replicas
    GPUS: int = 1  # Number of GPUs
    CPUS: int = 8  # Number of CPU cores  96 // num_replica - more for management
    RETURN_FULL_TEXT: bool = False

    SAGEMAKER_ENDPOINT_CONFIG_INFERENCE: str = "test"
    SAGEMAKER_INFERENCE_COMPONENT_INFERENCE: str = "test"
    SAGEMAKER_ENDPOINT_INFERENCE: str = "test"
    SAGEMAKER_MODEL_INFERENCE: str = "test"
    TEMPERATURE_INFERENCE: float = 0.01
    TOP_P_INFERENCE: float = 0.9
    MAX_NEW_TOKENS_INFERENCE: int = 150

    AWS_ACCESS_KEY: str | None = None
    AWS_SECRET_KEY: str | None = None

    @property
    def OPENAI_MAX_TOKEN_WINDOW(self) -> int:
        official_max_token_window = {"gpt-3.5-turbo": 16385, "gpt-4-turbo": 128000, "gpt-4o": 128000}[
            self.OPENAI_MODEL_ID
        ]

        max_token_window = int(official_max_token_window * 0.90)

        return max_token_window


settings = Settings()
