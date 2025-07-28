from app.tool import BaseTool
from datetime import datetime

from app.tool.base import ToolResult


class GetPerformanceBySubDepartmentIdAndMonth(BaseTool):
    name: str = "get_performance_by_sub_department_id_and_month"
    description: str = "通过分公司ID和月份查询分公司业绩, 接口用途 查询分公司业绩"
    parameters: dict = {
        "type": "object",
        "properties": {
            "subdepartmentid": {
                "type": "string",
                "description": "分公司ID",
            },
            "month": {
                "type": "int",
                "description": "月份  e.g 1 , 2 ",
            }
        },
        "required": ["username"],
    }

    async def execute(self, subdepartmentid: str, month: int) -> str:
        print("**********入参**********")
        print(subdepartmentid)
        print(month)
        print("**********入参**********")
        return "厦门分公司" + str(month) + "月份的业绩是 159W/月"
