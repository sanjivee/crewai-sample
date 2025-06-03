from crewai.tools import BaseTool
import json

class SystemInfo(BaseTool):
    name: str = "system_info"
    description: str = (
        "Returns current system information including battery percentage, memory, and CPU details"
    )

    def _run(self) -> str:
        return json.dumps({"battery": "21%", "memory": "16GB", "cpu": "Intel"})