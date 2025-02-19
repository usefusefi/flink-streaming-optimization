from pyflink.datastream.connectors.kafka import FlinkKafkaConsumer, FlinkKafkaProducer
from pyflink.common.serialization import SimpleStringSchema

# Kafka source
kafka_source = FlinkKafkaConsumer(
    topics="transactions",
    properties={"bootstrap.servers": "kafka-broker:9092", "group.id": "flink-fraud"},
    deserialization_schema=SimpleStringSchema()
)
transactions = env.add_source(kafka_source)

# Fraud Detection Logic
fraud_alerts = transactions.filter(lambda tx: float(tx["amount"]) > 5000)

# Send to Kafka Sink
kafka_sink = FlinkKafkaProducer(
    topic="fraud-alerts",
    producer_config={"bootstrap.servers": "kafka-broker:9092"},
    serialization_schema=SimpleStringSchema()
)
fraud_alerts.add_sink(kafka_sink)
