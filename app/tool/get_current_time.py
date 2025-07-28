from app.tool import BaseTool
from datetime import datetime


class GetCurrentTime(BaseTool):
    name: str = "get_current_time"
    description: str = "获取当前时间/get current time from system"

    async def execute(self) -> str:
        now = datetime.now()
        datestr = now.strftime("%Y-%m-%d %H:%M:%S")
        return "当前时间:" + datestr
