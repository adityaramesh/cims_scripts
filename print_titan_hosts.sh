#! /usr/bin/env bash
# Filters out only the hosts with Titan GPUs from `gpu_usage`.

/home/deigen/bin/gpu_usage 2> /dev/null | grep "GTX TITAN"
