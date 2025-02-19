from pyflink.datastream import StreamExecutionEnvironment, TimeCharacteristic
from pyflink.datastream.window import TumblingEventTimeWindows
from pyflink.datastream.functions import TimestampAssigner

env = StreamExecutionEnvironment.get_execution_environment()
env.set_stream_time_characteristic(TimeCharacteristic.EventTime)

class CustomTimestampAssigner(TimestampAssigner):
    def extract_timestamp(self, element, record_timestamp):
        return element[1]  # Assuming the second field is the event timestamp

# Define Kafka source with watermarks
data_stream = env.add_source(
    KafkaSource(...).assign_timestamps_and_watermarks(
        WatermarkStrategy.for_monotonous_timestamps()
        .with_timestamp_assigner(CustomTimestampAssigner())
    )
)

# Apply windowed aggregation
windowed_stream = data_stream \
    .key_by(lambda x: x[0]) \
    .window(TumblingEventTimeWindows.of(Time.seconds(10))) \
    .reduce(lambda a, b: (a[0], a[1] + b[1]))

windowed_stream.print()
env.execute("Event Time & Watermarks Example")
