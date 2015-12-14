"""
A general parser for the rdf documents, vaguely based off the Reactome Biopax lvl3 owl parser
"""
import xml.etree.ElementTree as ET
from collections import defaultdict


def zip_dicts(dict1, dict2):
    """
    defines a dictionary update rules that are required for a proper dictionary update
    :param dict1: dictionary #1
    :param dict2: dictionary #2
    """
    for key in dict2.keys():
        if key not in dict1.keys():
            dict1[key] = dict2[key]  # never used in production
        else:
            assert isinstance(dict2[key], (list, tuple))
            dict1[key] = dict1[key] + dict2[key]
    return dict1


class RdfParser(object):

    def __init__(self, path_to_rdf_file):

        self.tree = ET.parse(path_to_rdf_file)
        self.root = self.tree.getroot()

        self.parse = defaultdict(dict)

    def _get_all_terms(self, term_name):
        search_pattern = '{http://www.biopax.org/release/biopax-level3.owl#}%s' % term_name
        xml_iterator = self.root.findall(search_pattern)
        return xml_iterator

    def parse(self):
        pass

if __name__ == "__main__":
    source_file = "C:\\Users\\Andrei\Downloads\\Homo_sapiens.owl"
    RP = RdfParser(source_file)
    RP.parse()