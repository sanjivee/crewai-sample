import json
import platform
import psutil
from crewai.tools import BaseTool

class SystemInfo(BaseTool):
    name: str = "system_info"
    description: str = (
        "Returns current system information including battery percentage, memory, and CPU details"
    )
    

    def _run(self) -> str:
        return json.dumps({"battery_percent": self.get_battery_percent(), 
                            "memory":self.get_total_memory(), 
                            "cpu": self.get_cpu_info()
                        })

    def get_cpu_info(self):
        cpu = platform.processor()
        if not cpu:
            cpu = platform.uname().processor
        return cpu

    def get_total_memory(self):
        mem = psutil.virtual_memory()
        total_gb = mem.total / (1024 ** 3)
        return f"{total_gb:.2f} GB"
    

    def get_battery_percent(self):
        battery = psutil.sensors_battery()
        return f"{battery.percent}%"
