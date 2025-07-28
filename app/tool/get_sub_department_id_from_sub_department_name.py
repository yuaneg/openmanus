from openai.types.chat import ChatCompletionMessage
from pydantic import Field

from app.llm import LLM
from app.schema import Message
from app.tool import BaseTool
from app.tool.get_sub_department_id_from_username import SSSS


class GetSubDepartmentIdBySubDepartmentName(BaseTool):
    llm: LLM = Field(default_factory=lambda: LLM())

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

    async def execute(self, subdepartmentname: str) -> ChatCompletionMessage | None:
        print("通过分司名称获取分司ID,分公司名称:" + subdepartmentname)
        system_message = Message.system_message(SSSS)
        user_message = Message.user_message(
            f"通过sub_name分公司名称获取 sub_id ,分公司名称: {subdepartmentname}"
        )
        return await self.llm.ask_tool(
            messages=[user_message],
            system_msgs=[system_message],
        )
