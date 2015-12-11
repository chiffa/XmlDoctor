"""
A small tool to figure what is really going on within a sanely formatted RDF/owl file.
In my case, was to parse a BioPax lvl3 owl file containing the data from Reactome.org database
"""
import xml.etree.ElementTree as ET

# Updating the readability Dict with what is required for expected functionning if the application
required_readability_mapping = {'{http://www.w3.org/1999/02/22-rdf-syntax-ns#}': 'rdf:',
                                '{http://www.w3.org/2002/07/owl#}': 'owl:'}


def run_xml_doctor(path_to_file, readability_dict=None):
    """
    the main routine of the rdf/owl doctor

    :param path_to_file: path top the
    :param readability_dict: dictionary performing string transformation to make final result
    more readable (usually maps owl url to '' or to a short-name)
    :return:
    """
    # Parse Reactome BioPax
    tree = ET.parse(path_to_file)
    root = tree.getroot()

    if readability_dict:
        readability_dict_full = dict(Reactome_ReadabilityDict.items() +
                                     required_readability_mapping.items())

    else:
        readability_dict_full = required_readability_mapping

    # TODO: [improvement] add a correlation between tags presence.

    def make_readable(sub_tree):
        """
        Increases readability of a sample output for the final user

        :param sub_tree:
        :return: sub_tree where all the tags were replaced by their more readable elements
        """
        for key in readability_dict_full.keys():
            if key in sub_tree:
                return sub_tree.replace(key, readability_dict_full[key])
        return sub_tree

    def update_counter_subdict(counter_subdict, lvl_0_dict):
        """
        Adds a lvl_0_dict information to the global counter information

        :param counter_subdict:
        :param lvl_0_dict:
        :return:
        """
        counter_subdict['TotalCount'] += 1
        lvl_0_keys = lvl_0_dict.keys()
        lvl_0_keys.remove('objType')
        for key_ in lvl_0_keys:
            if key_ not in counter_subdict.keys():
                counter_subdict[key_] = {'appearances': 0, 'count': 0}
            counter_subdict[key_]['appearances'] += 1
            counter_subdict[key_]['count'] += lvl_0_container[key_]['count']
            lvl1keys = lvl_0_dict[key_].keys()
            lvl1keys.remove('count')
            for pointer in lvl1keys:
                if pointer not in counter_subdict[key_].keys():
                    counter_subdict[key_][pointer] = {'appearances': 0, 'count': 0}
                counter_subdict[key_][pointer]['appearances'] += 1
                counter_subdict[key_][pointer]['count'] += lvl_0_container[key_][pointer]

    counter = {}

    for child in root:
        lvl_0_container = {'objType': make_readable(child.tag)}
        for sub_child in child:
            lvl_1_container = [make_readable(sub_child.tag),
                               make_readable(sub_child.attrib.keys()[0])]
            if 'resource' in sub_child.attrib.keys()[0]:
                # pointing to a node, a non-terminal node we are no more interested in a type (
                # resource in the xml from owl), but rather the exact type (Protein, RNA,
                # Small molecule, ...) we have to parse the name to which it points,
                # while getting rid of the identifier number
                referenced = ''
                for letter in sub_child.attrib.values()[0]:
                    if not letter.isdigit():
                        referenced += letter
                lvl_1_container[1] = referenced
            if not lvl_1_container[0] in lvl_0_container.keys():
                lvl_0_container[lvl_1_container[0]] = {'count': 0}
            lvl_0_container[lvl_1_container[0]]['count'] += 1
            if not lvl_1_container[1] in lvl_0_container[lvl_1_container[0]].keys():
                lvl_0_container[lvl_1_container[0]][lvl_1_container[1]] = 0
            lvl_0_container[lvl_1_container[0]][lvl_1_container[1]] += 1
        if 'Ontology' not in lvl_0_container['objType']:
            if lvl_0_container['objType'] not in counter.keys():
                counter[lvl_0_container['objType']] = {'TotalCount': 0}
            update_counter_subdict(counter[lvl_0_container['objType']], lvl_0_container)

    for entry in counter.keys():
        print("%-30s%s" % (entry, counter[entry]['TotalCount']))
        keys_lvl_1 = counter[entry].keys()
        keys_lvl_1.remove('TotalCount')
        for key_lvl1 in keys_lvl_1:
            lvl1_appearance_percentage = "{:>10}".format(
                "{0:.2f}".format(float(counter[entry][key_lvl1]['appearances']) /
                                 float(counter[entry]['TotalCount']) * 100))
            lvl1_count_per_appearance = "{:>10}".format(
                "{0:.2f}".format(float(counter[entry][key_lvl1]['count']) /
                                 float(counter[entry][key_lvl1]['appearances'])))
            print("    %-34s%-10s%s"%
                 (key_lvl1,
                  lvl1_appearance_percentage + ' %',
                  lvl1_count_per_appearance))
            keys_lvl_2 = counter[entry][key_lvl1].keys()
            keys_lvl_2.remove('appearances')
            keys_lvl_2.remove('count')
            if 'rdf:datatype' in keys_lvl_2:
                keys_lvl_2.remove('rdf:datatype')
            for key_lvl2 in keys_lvl_2:
                lvl2_apperance_percentage = "{:>10}".format(
                    "{0:.2f}".format(float(counter[entry][key_lvl1][key_lvl2]['appearances']) /
                                     float(counter[entry][key_lvl1]['appearances']) * 100))
                lvl2_count_per_appearance = "{:>10}".format(
                    "{0:.2f}".format(float(counter[entry][key_lvl1][key_lvl2]['count']) /
                                     float(counter[entry][key_lvl1][key_lvl2]['appearances'])))
                print("\t\t%-30s%-8s%s" %
                      (key_lvl2,
                       '   ' + lvl2_apperance_percentage + ' %',
                       lvl2_count_per_appearance))
        print("\n")


if __name__ == "__main__":
    ReactomeBioPax = "/home/andrei/PycharmProjects/BioFlow/unittests/UT_examples/Homo_sapiens.owl"
    Reactome_ReadabilityDict = {'{http://www.biopax.org/release/biopax-level3.owl#}': ''}
    run_xml_doctor(ReactomeBioPax, Reactome_ReadabilityDict)
