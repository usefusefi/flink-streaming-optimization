from pyflink.datastream.connectors.kafka import FlinkKafkaConsumer, FlinkKafkaProducer
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.serialization import SimpleStringSchema

env = StreamExecutionEnvironment.get_execution_environment()

# Kafka Consumer
kafka_consumer = FlinkKafkaConsumer(
    topics='transactions',
    deserialization_schema=SimpleStringSchema(),
    properties={'bootstrap.servers': 'localhost:9092'}
)
stream = env.add_source(kafka_consumer)

# Kafka Producer
kafka_producer = FlinkKafkaProducer(
    topic='processed-transactions',
    serialization_schema=SimpleStringSchema(),
    producer_config={'bootstrap.servers': 'localhost:9092'}
)
stream.add_sink(kafka_producer)

env.execute("Kafka-Flink Streaming Pipeline")
