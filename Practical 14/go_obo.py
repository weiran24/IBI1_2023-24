Practical 14/go_obo.py
import xml.sax
import xml.dom.minidom
from collections import Counter
import time
import matplotlib.pyplot as plt

# Define the ontologies
ontologies = ['molecular_function', 'biological_process', 'cellular_component']

# Initialize Counters for each ontology
go_term_counts = {ontology: Counter() for ontology in ontologies}

def parse_with_dom(xml_file):
    # Parse the XML file using DOM
    start_time = time.time()
    dom = xml.dom.minidom.parse(xml_file)
    terms = dom.getElementsByTagName('term')

    # Iterate over all terms and count them by namespace
    for term in terms:
        namespace = term.getElementsByTagName('namespace')[0].firstChild.data
        go_term_counts[namespace].update([term.getElementsByTagName('id')[0].firstChild.data])

    # Record the time taken
    dom_time = time.time() - start_time
    return dom_time

def parse_with_sax(xml_file):
    # Define a handler for SAX parsing
    class GOHandler(xml.sax.ContentHandler):
        def __init__(self):
            self.current_tag = None
            self.namespace = None

        def startElement(self, tag, attributes):
            self.current_tag = tag

        def characters(self, content):
            if self.current_tag == 'namespace':
                self.namespace = content
            elif self.current_tag == 'id':
                go_term_counts[self.namespace].update([content])

    # Parse the XML file using SAX
    start_time = time.time()
    parser = xml.sax.make_parser()
    handler = GOHandler()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    
    # Record the time taken
    sax_time = time.time() - start_time
    return sax_time

def plot_results():
    # Plotting the results
    for ontology, count in go_term_counts.items():
        plt.bar(count.keys(), count.values(), label=ontology)

    plt.xlabel('GO Terms')
    plt.ylabel('Frequency')
    plt.title('GO Terms Frequency by Ontology')
    plt.legend()
    plt.show()

def main():
    # The path to the XML file
    xml_file = 'go_obo.xml'

    # Run the DOM parser
    dom_time = parse_with_dom(xml_file)
    
    # Run the SAX parser
    sax_time = parse_with_sax(xml_file)

    # Print the counts
    for ontology in ontologies:
        print(f"{ontology}: {len(go_term_counts[ontology])} terms")

    # Plot the results
    plot_results()

    # Comment on the fastest parser
    if dom_time < sax_time:
        print("### DOM parser was the fastest ###")
    else:
        print("### SAX parser was the fastest ###")

if __name__ == '__main__':
    main()
