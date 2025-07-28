from app.tool import BaseTool
from datetime import datetime

from app.tool.base import ToolResult


class GetUserIdFromUserName(BaseTool):
    name: str = "get_sub_department_id_from_username"
    description: str = "通过分公司总监的名字获取分公司的ID, 接口用途 查询分公司业绩"
    parameters: dict = {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": "分司总监姓名",
            }
        },
        "required": ["username"],
    }

    async def execute(self, username: str) -> str:
        print("通过员工姓名查询分司ID:" + username)
        return str({
            "分公司名称": "厦门分公司",
            "分公司ID": "147"
        })
