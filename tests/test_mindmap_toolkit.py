import unittest
from Mindmap_tool import MindmapTool
from Mindmap_toolkit import MindmapToolkit

class MindmapToolkitTestCase(unittest.TestCase):
    def setUp(self):
        self.toolkit = MindmapToolkit()

    def test_get_tools_returns_list_of_tools(self):
        tools = self.toolkit.get_tools()
        self.assertIsInstance(tools, list)
        self.assertTrue(all(isinstance(tool, MindmapTool) for tool in tools))

    def test_get_env_keys_returns_list_of_strings(self):
        env_keys = self.toolkit.get_env_keys()
        self.assertIsInstance(env_keys, list)
        self.assertTrue(all(isinstance(key, str) for key in env_keys))

    def test_toolkit_name_and_description(self):
        self.assertEqual(self.toolkit.name, "Mindmap Toolkit")
        self.assertEqual(self.toolkit.description, "A toolkit for generating text-based mindmaps")

if __name__ == '__main__':
    unittest.main()
