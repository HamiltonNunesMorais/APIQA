#!/bin/bash

timestamp=$(date +%Y%m%d_%H%M%S)

newman run collections/QA-FAST-API.postman_collection.json \
  --env-var "BASE_URL=http://localhost:8000" \
  --reporters cli,html \
  --reporter-html-export results/results_${timestamp}.html

echo "Report saved: results/results_${timestamp}.html"
