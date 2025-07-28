from datetime import datetime

import pytz

from app.tool import BaseTool


class TimeConvertToUSA(BaseTool):
    name: str = "time_convert_to_usa"
    description: str = "转换成美国时区的时间"
    parameters: dict = {
        "type": "object",
        "properties": {
            "current_time": {
                "type": "string",
                "description": "当前时间",
            }
        },
        "required": ["current_time"],
    }

    async def execute(self, current_time: str) -> str:
        # 先将字符串转换为datetime对象（假设输入是UTC时间或本地时间）
        # 这里假设输入的是UTC时间，如果是本地时间可去掉utc=True参数
        input_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")

        # 定义美国时区（以纽约为例）
        us_tz = pytz.timezone('America/New_York')

        # 如果输入时间没有时区信息，需要先本地化（这里假设输入为UTC时间）
        utc_tz = pytz.timezone('UTC')
        utc_time = utc_tz.localize(input_time)

        # 转换为美国东部时间
        us_time = utc_time.astimezone(us_tz)

        # 格式化输出
        datestr = us_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")
        return "当前美国时间: " + datestr
