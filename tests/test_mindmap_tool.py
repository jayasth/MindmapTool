import unittest
from Mindmap_tool import MindmapTool, MindmapInput

class MindmapToolTestCase(unittest.TestCase):
    def setUp(self):
        self.tool = MindmapTool()

    def test_tool_name(self):
        self.assertEqual(self.tool.name, "Mindmap Tool")

    def test_tool_args_schema(self):
        self.assertEqual(self.tool.args_schema, MindmapInput)

    def test_tool_description(self):
        self.assertEqual(self.tool.description, "Generates a text-based mindmap from input text")

    def test_execute_method(self):
        input_text = "Artificial Intelligence"
        expected_output = "Mindmap for keyword: " + input_text
        output = self.tool._execute(text=input_text)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
