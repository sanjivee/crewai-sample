#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from device_info.crew import DeviceInfo

import logging

logging.basicConfig(level=logging.DEBUG)


def run():
    """
    Run the crew.
    """
    queries = [
        { "query": "how much memory?"},
        { "query": "whats the cpu?"},
        {"query": "whats the battery percentage?"}
    ]
    
    try:
        for query in queries:
            result = DeviceInfo().crew().kickoff(inputs=query)
    except Exception as e:
        import traceback
        traceback.print_exc()
