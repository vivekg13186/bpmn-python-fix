import unittest
import os

import bpmn_python.bpmn_diagram_rep as diagram
import bpmn_python.bpmn_diagram_visualizer as visualizer


class BPMNEditorTests(unittest.TestCase):
    """
    This class contains test for bpmn-python package functionality using an example BPMN diagram created in BPMNEditor.
    """
    output_directory = "./output/test-bpmneditor/"
    example_directory = "../examples/BPMNEditor-example.xml"
    output_file_with_di = "BPMNEditor-example-output.xml"
    output_file_no_di = "BPMNEditor-example-output-no-di.xml"
    output_dot_file = "BPMNEditor-example"
    output_png_file = "BPMNEditor-example"


    def test_loadBPMNEditorDiagram(self):
        """
        Test for importing a simple BPMNEditor diagram example (as BPMN 2.0 XML) into inner representation
        and later exporting it to XML file
        """
        bpmn_graph = diagram.BPMNDiagramGraph()
        bpmn_graph.load_diagram_from_xml(os.path.abspath(self.example_directory))
        bpmn_graph.export_xml_file(self.output_directory, self.output_file_with_di)
        bpmn_graph.export_xml_file_no_di(self.output_directory, self.output_file_no_di)


    def test_loadBPMNEditorDiagramAndVisualize(self):
        """
        Test for importing a simple BPMNEditor diagram example (as BPMN 2.0 XML) into inner representation
        and later exporting it to XML file. Includes test for visualization functionality.
        """
        bpmn_graph = diagram.BPMNDiagramGraph()
        bpmn_graph.load_diagram_from_xml(os.path.abspath(self.example_directory))
        visualizer.visualize_diagram(bpmn_graph)
        visualizer.bpmn_diagram_to_dot_file(bpmn_graph, self.output_directory + self.output_dot_file)
        visualizer.bpmn_diagram_to_png(bpmn_graph, self.output_directory + self.output_png_file)
        bpmn_graph.export_xml_file(self.output_directory, self.output_file_with_di)
        bpmn_graph.export_xml_file_no_di(self.output_directory, self.output_file_no_di)

if __name__ == '__main__':
    unittest.main()
