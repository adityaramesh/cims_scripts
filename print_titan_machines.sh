#! /usr/bin/env bash
# Produces a sorted list of hosts with TITAN GPUs.

/home/deigen/bin/gpu_usage 2> /dev/null | grep "GTX TITAN" | sed -n 's/\([a-z]\+[[:digit:]]*\s\+[[:digit:]]\).*/\1/p' | sort -k 1,1
