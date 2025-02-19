#!/bin/bash
flink run -m jobmanager:8081 -c com.example.FraudDetectionPipeline /flink-jobs/fraud_detection.jar
