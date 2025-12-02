#!/bin/bash

timestamp=$(date +%Y%m%d_%H%M%S)

newman run collections/QA-FAST-API.postman_collection.json \
  --reporters cli,html \
  --reporter-html-export results/results_${timestamp}.html

echo "Report saved: results/results_${timestamp}.html"
