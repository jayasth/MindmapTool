from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from mindmap_tool import MindmapTool

class MindmapToolkit(BaseToolkit, ABC):
    name: str = "Mindmap Toolkit"
    description: str = "A toolkit for generating text-based mindmaps"

    def get_tools(self) -> List[BaseTool]:
        return [MindmapTool()]

    def get_env_keys(self) -> List[str]:
        return ["KEYWORD"]
