#!/bin/bash

echo "Running Postman tests..."
newman run collections/QA-FAST-API.postman_collection.json --reporters cli,html --reporter-html-export results.html
echo "Done! Report saved to results.html"
