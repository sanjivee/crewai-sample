#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from device_info.crew import DeviceInfo

# import logging

# logging.basicConfig(level=logging.DEBUG)


def run():
    """
    Run the crew.
    """
    inputs = {
        "query": "what is the battery percent?"
    }
    
    try:
        result = DeviceInfo().crew().kickoff(inputs=inputs)
        print(result, "res")
    except Exception as e:
        import traceback
        traceback.print_exc()
