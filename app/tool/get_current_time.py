from app.tool import BaseTool
from datetime import datetime

from app.tool.base import ToolResult


class GetCurrentTime(BaseTool):
    name: str = "get_current_time"
    description: str = "获取当前时间/get current time from system"
    parameters: dict = {
        "type": "object",
        "properties": {
            "current_time": {
                "type": "string",
                "description": "当前时间",
            }
        },
        "required": ["status", "result"],
    }

    async def execute(self,current_time:str) -> ToolResult:
        now = datetime.now()
        datestr = now.strftime("%Y-%m-%d %H:%M:%S")
        #return "当前时间:" + datestr
        return ToolResult(output="当前时间:" + datestr)
