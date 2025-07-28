from app.tool import BaseTool
from datetime import datetime

from app.tool.base import ToolResult
import requests
import aiohttp
from typing import Union, List


class GetPerformanceBySubDepartmentIdAndMonthDetail(BaseTool):
    name: str = "get_performance_by_sub_department_id_and_month_detail"
    description: str = "通过分公司ID和月份查询分公司业绩详情. (接口用途 查询分公司业绩)"
    parameters: dict = {
        "type": "object",
        "properties": {
            "subdepartmentid": {
                "type": "list",
                "description": "分公司ID",
            },
            "yearmonth": {
                "type": "list",
                "description": "年-月份  e.g 2025-04 ",
            }
        },
        "required": ["subdepartmentid", "yearmonth"],
    }

    async def execute(self, subdepartmentid: Union[str, List[str]], yearmonth: Union[str, List[str]]) -> str:
        """
        异步获取业绩数据的方法，兼容单个值和列表参数

        参数:
            subdepartmentid: 子部门ID，可为单个字符串或列表
            yearmonth: 年份月份，可为单个字符串或列表（格式如"2025-05"）

        返回:
            接口响应文本
        """
        # 确保参数为列表类型
        def ensure_list(param: Union[str, List[str]]) -> List[str]:
            if isinstance(param, list):
                return param
            elif isinstance(param, str):
                return [param]
            else:
                raise ValueError("参数必须是字符串或字符串列表")

        # 处理参数
        sub_ids = ensure_list(subdepartmentid)
        business_months = ensure_list(yearmonth)

        print(f"执行接口查询分司ID: {sub_ids}, 查询月份: {business_months}")

        url = "https://scrm-test.ceboss.cn/scrm-web/ai/robot/getyejidetail"

        # 构建查询参数
        params = []
        for month in business_months:
            params.append(("businessMonths", month))
        for sub_id in sub_ids:
            params.append(("subIds", sub_id))

        headers = {
            'Cookie': 'JSESSIONID=246F37F7F4C46610A064AD20596CF2A7'
        }

        try:
            # 使用异步HTTP客户端
            async with aiohttp.ClientSession() as session:
                async with session.get(
                        url=url,
                        headers=headers,
                        params=params
                ) as response:
                    response.raise_for_status()  # 检查HTTP错误状态
                    return await response.text()
        except Exception as e:
            return f"请求发生错误: {str(e)}"

