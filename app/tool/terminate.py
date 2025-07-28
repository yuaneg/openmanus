from app.tool.base import BaseTool

_TERMINATE_DESCRIPTION = """Terminate the interaction when the request is met OR if the assistant cannot proceed further with the task.
When you have finished all the tasks, call this tool to end the work."""


class Terminate(BaseTool):
    name: str = "terminate"
    description: str = _TERMINATE_DESCRIPTION
    parameters: dict = {
        "type": "object",
        "properties": {
            "status": {
                "type": "string",
                "description": "The finish status of the interaction.",
                "enum": ["[success]", "failure"],
            },
            "result": {
                "type": "string",
                "description": "最总结果汇总,注意标点和换行",
            }
        },
        "required": ["status", "result"],
    }

    async def execute(self, status: str, result: str) -> str:
        """Finish the current execution"""
        return f"任务执行结束✌️✌️✌️✌️✌️:" + "\n" + result
