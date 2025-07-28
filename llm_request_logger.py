from app.logger import logger
import json

class LLMRequestLogger:

    @classmethod
    def log_llm_request(cls, params: dict):
        return
        """统一记录LLM请求日志"""
        logger.info("===== LLM 请求 =====")
        # 安全地序列化请求参数
        safe_params = params.copy()
        # 限制消息内容长度，避免日志过大
        if 'messages' in safe_params:
            for i, msg in enumerate(safe_params['messages']):
                if isinstance(msg, dict) and 'content' in msg:
                    if isinstance(msg['content'], str):
                        # 截断长文本
                        if len(msg['content']) > 1000:
                            msg['content'] = msg['content'][:1000] + "..."
                    elif isinstance(msg['content'], list):
                        # 处理多模态内容
                        for j, item in enumerate(msg['content']):
                            if isinstance(item, dict) and 'text' in item:
                                if len(item['text']) > 500:
                                    item['text'] = item['text'][:500] + "..."

        logger.info(f"请求详情: {json.dumps(safe_params, default=str, indent=2, ensure_ascii=False)}")

    @classmethod
    def log_llm_response(cls, response):
        return
        """统一记录LLM响应日志"""
        logger.info("===== LLM 响应 =====")

        # 转换响应对象为可序列化的字典
        try:
            response_dict = response.model_dump() if hasattr(response, 'model_dump') else vars(response)
        except:
            response_dict = str(response)

        if hasattr(response, "usage"):  # 非流式响应
            logger.info(f"Token使用: {response.usage}")

        if hasattr(response, "choices") and response.choices:
            logger.info(f"结束原因: {response.choices[0].finish_reason}")
            # 打印第一个choice的内容摘要
            if hasattr(response.choices[0].message, 'content'):
                content = response.choices[0].message.content
                if isinstance(content, str) and len(content) > 1000:
                    content = content[:1000] + "..."

        # 安全地序列化完整响应
        safe_response = cls._make_serializable(response_dict)
        logger.info(f"响应详情: {json.dumps(safe_response, default=str, indent=2, ensure_ascii=False)}")

    @classmethod
    def _make_serializable(cls, obj):
        """递归转换对象为可JSON序列化的格式"""
        if isinstance(obj, dict):
            return {k: cls._make_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [cls._make_serializable(item) for item in obj]
        elif hasattr(obj, '__dict__'):
            return cls._make_serializable(vars(obj))
        else:
            try:
                json.dumps(obj)
                return obj
            except:
                return str(obj)
