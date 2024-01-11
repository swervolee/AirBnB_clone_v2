#!/usr/bin/env bash

timestamp="$(date +%F%T)"
timestamp_without_hyphens=$(echo "$timestamp" | tr -d '-' | tr -d ':')

echo "$timestamp_without_hyphens"
