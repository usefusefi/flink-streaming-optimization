from pyflink.datastream import StreamExecutionEnvironment, CheckpointingMode
from pyflink.datastream.state_backend import RocksDBStateBackend

env = StreamExecutionEnvironment.get_execution_environment()
env.enable_checkpointing(10000, CheckpointingMode.EXACTLY_ONCE)
env.set_state_backend(RocksDBStateBackend("file:///flink-checkpoints"))

print("RocksDB State Backend Configured")
