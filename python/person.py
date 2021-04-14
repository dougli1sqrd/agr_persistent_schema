# Auto generated from person.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-14 16:48
# Schema: person
#
# id: https://github.com/alliance-genome/agr_persistent_schema/src/schema/person
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml.utils.slot import Slot
from linkml.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml.utils.formatutils import camelcase, underscore, sfx
from linkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml.utils.curienamespace import CurieNamespace
from . informationContentEntity import InformationContentEntity
from linkml_model.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'https://www.w3.org/TR/skos-reference/#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ALLIANCE


# Types

# Class references



@dataclass
class Person(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Person
    class_class_curie: ClassVar[str] = "alliance:Person"
    class_name: ClassVar[str] = "person"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Person

    last_name: Optional[Union[dict, InformationContentEntity]] = None
    first_name: Optional[Union[dict, InformationContentEntity]] = None
    orcid: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.last_name is not None and not isinstance(self.last_name, InformationContentEntity):
            self.last_name = InformationContentEntity(**self.last_name)

        if self.first_name is not None and not isinstance(self.first_name, InformationContentEntity):
            self.first_name = InformationContentEntity(**self.first_name)

        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.orcid = Slot(uri=ALLIANCE.orcid, name="orcid", curie=ALLIANCE.curie('orcid'),
                   model_uri=ALLIANCE.orcid, domain=InformationContentEntity, range=Optional[str])
