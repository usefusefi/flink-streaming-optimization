# Flink Monitoring & Performance Tuning

## Enabling Checkpoints & Savepoints
Use RocksDB as the state backend and configure periodic checkpoints.
```yaml
state.backend: rocksdb
state.checkpoints.dir: file:///flink-checkpoints/
