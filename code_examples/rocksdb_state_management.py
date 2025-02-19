from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.state_backend import EmbeddedRocksDBStateBackend

env = StreamExecutionEnvironment.get_execution_environment()
env.set_state_backend(EmbeddedRocksDBStateBackend())  # RocksDB for state storage
