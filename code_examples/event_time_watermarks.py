from pyflink.common.watermark_strategy import WatermarkStrategy
from datetime import timedelta

def extract_timestamp(event):
    return event["timestamp"]

watermark_strategy = WatermarkStrategy \
    .for_bounded_out_of_orderness(timedelta(seconds=10)) \
    .with_timestamp_assigner(extract_timestamp)
