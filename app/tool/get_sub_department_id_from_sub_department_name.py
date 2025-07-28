from app.tool import BaseTool
from datetime import datetime

from app.tool.base import ToolResult


class GetSubDepartmentIdBySubDepartmentName(BaseTool):
    name: str = "get_sub_department_id_from_sub_department_name"
    description: str = "通过分公司的名字获取分公司的ID. 接口用途 查询分公司业绩"
    parameters: dict = {
        "type": "object",
        "properties": {
            "subdepartmentname": {
                "type": "string",
                "description": "分公司名称",
            }
        },
        "required": ["subdepartmentname"],
    }

    async def execute(self, subdepartmentname: str) -> str:
        print("通过分司名称获取分司ID,分公司名称:"+subdepartmentname)
        return str({
            "分公司名称": "厦门分公司",
            "分公司ID": "147"
        })
