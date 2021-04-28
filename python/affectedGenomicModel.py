# Auto generated from affectedGenomicModel.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-28 15:35
# Schema: Alliance-Schema-Prototype-Affected-Genomic-Model
#
# id: https://github.com/alliance-genome/agr_persistent_schema/affectedGenomicModel
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
from . allele import Allele
from . core import DiseaseAssociation, PhenotypeAssociation
from linkml.utils.metamodelcore import URIorCURIE, XSDDate
from linkml_model.types import Date, Integer, String, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/affectedGenomicModel/')


# Types

# Class references
class AffectedGenomicModelCurie(URIorCURIE):
    pass


@dataclass
class AffectedGenomicModel(YAMLRoot):
    """
    Includes inbred strains, stocks, disease models and mutant genotypes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/affectedGenomicModel/AffectedGenomicModel")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AffectedGenomicModel"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/affectedGenomicModel/AffectedGenomicModel")

    curie: Union[str, AffectedGenomicModelCurie] = None
    subtype: Optional[Union[str, "SubtypeValues"]] = None
    taxon_id: Optional[int] = None
    cross_references: Optional[Union[str, List[str]]] = empty_list()
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    components: Optional[Union[Union[dict, "AffectedGenomicModelComponent"], List[Union[dict, "AffectedGenomicModelComponent"]]]] = empty_list()
    sequence_targeting_reagents: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    parental_populations: Optional[Union[str, URIorCURIE]] = None
    data_provider: Optional[Union[str, List[str]]] = empty_list()
    date_produced: Optional[Union[str, XSDDate]] = None
    disease_associations: Optional[Union[dict, DiseaseAssociation]] = None
    phenotype_associations: Optional[Union[dict, PhenotypeAssociation]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.curie is None:
            raise ValueError("curie must be supplied")
        if not isinstance(self.curie, AffectedGenomicModelCurie):
            self.curie = AffectedGenomicModelCurie(self.curie)

        if self.subtype is not None and not isinstance(self.subtype, SubtypeValues):
            self.subtype = SubtypeValues(self.subtype)

        if self.taxon_id is not None and not isinstance(self.taxon_id, int):
            self.taxon_id = int(self.taxon_id)

        if self.cross_references is None:
            self.cross_references = []
        if not isinstance(self.cross_references, list):
            self.cross_references = [self.cross_references]
        self.cross_references = [v if isinstance(v, str) else str(v) for v in self.cross_references]

        if self.synonyms is None:
            self.synonyms = []
        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms]
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if self.components is None:
            self.components = []
        if not isinstance(self.components, list):
            self.components = [self.components]
        self.components = [v if isinstance(v, AffectedGenomicModelComponent) else AffectedGenomicModelComponent(**v) for v in self.components]

        if self.sequence_targeting_reagents is None:
            self.sequence_targeting_reagents = []
        if not isinstance(self.sequence_targeting_reagents, list):
            self.sequence_targeting_reagents = [self.sequence_targeting_reagents]
        self.sequence_targeting_reagents = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.sequence_targeting_reagents]

        if self.parental_populations is not None and not isinstance(self.parental_populations, URIorCURIE):
            self.parental_populations = URIorCURIE(self.parental_populations)

        if self.data_provider is None:
            self.data_provider = []
        if not isinstance(self.data_provider, list):
            self.data_provider = [self.data_provider]
        self.data_provider = [v if isinstance(v, str) else str(v) for v in self.data_provider]

        if self.date_produced is not None and not isinstance(self.date_produced, XSDDate):
            self.date_produced = XSDDate(self.date_produced)

        if self.disease_associations is not None and not isinstance(self.disease_associations, DiseaseAssociation):
            self.disease_associations = DiseaseAssociation()

        if self.phenotype_associations is not None and not isinstance(self.phenotype_associations, PhenotypeAssociation):
            self.phenotype_associations = PhenotypeAssociation()

        super().__post_init__(**kwargs)


@dataclass
class AffectedGenomicModelComponent(YAMLRoot):
    """
    Allele that affects the model and its zygosity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/affectedGenomicModel/AffectedGenomicModelComponent")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AffectedGenomicModelComponent"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/affectedGenomicModel/AffectedGenomicModelComponent")

    allele: Optional[Union[dict, Allele]] = None
    zygosity: Optional[Union[str, "ZygosityValues"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.allele is not None and not isinstance(self.allele, Allele):
            self.allele = Allele(**self.allele)

        if self.zygosity is not None and not isinstance(self.zygosity, ZygosityValues):
            self.zygosity = ZygosityValues(self.zygosity)

        super().__post_init__(**kwargs)


# Enumerations
class SubtypeValues(EnumDefinitionImpl):

    strain = PermissibleValue(text="strain")
    genotype = PermissibleValue(text="genotype")

    _defn = EnumDefinition(
        name="SubtypeValues",
    )

class ZygosityValues(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ZygosityValues",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "GENO:0000602",
                PermissibleValue(text="GENO:0000602") )
        setattr(cls, "GENO:0000603",
                PermissibleValue(text="GENO:0000603") )
        setattr(cls, "GENO:0000604",
                PermissibleValue(text="GENO:0000604") )
        setattr(cls, "GENO:0000605",
                PermissibleValue(text="GENO:0000605") )
        setattr(cls, "GENO:0000606",
                PermissibleValue(text="GENO:0000606") )
        setattr(cls, "GENO:0000135",
                PermissibleValue(text="GENO:0000135") )
        setattr(cls, "GENO:0000136",
                PermissibleValue(text="GENO:0000136") )
        setattr(cls, "GENO:0000137",
                PermissibleValue(text="GENO:0000137") )
        setattr(cls, "GENO:0000134",
                PermissibleValue(text="GENO:0000134") )

# Slots
class slots:
    pass

slots.subtype = Slot(uri=DEFAULT_.subtype, name="subtype", curie=DEFAULT_.curie('subtype'),
                   model_uri=DEFAULT_.subtype, domain=AffectedGenomicModel, range=Optional[Union[str, "SubtypeValues"]])

slots.components = Slot(uri=DEFAULT_.components, name="components", curie=DEFAULT_.curie('components'),
                   model_uri=DEFAULT_.components, domain=AffectedGenomicModel, range=Optional[Union[Union[dict, "AffectedGenomicModelComponent"], List[Union[dict, "AffectedGenomicModelComponent"]]]])

slots.allele = Slot(uri=DEFAULT_.allele, name="allele", curie=DEFAULT_.curie('allele'),
                   model_uri=DEFAULT_.allele, domain=AffectedGenomicModelComponent, range=Optional[Union[dict, Allele]])

slots.zygosity = Slot(uri=DEFAULT_.zygosity, name="zygosity", curie=DEFAULT_.curie('zygosity'),
                   model_uri=DEFAULT_.zygosity, domain=AffectedGenomicModelComponent, range=Optional[Union[str, "ZygosityValues"]])

slots.sequence_targeting_reagents = Slot(uri=DEFAULT_.sequence_targeting_reagents, name="sequence_targeting_reagents", curie=DEFAULT_.curie('sequence_targeting_reagents'),
                   model_uri=DEFAULT_.sequence_targeting_reagents, domain=AffectedGenomicModel, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.parental_populations = Slot(uri=DEFAULT_.parental_populations, name="parental_populations", curie=DEFAULT_.curie('parental_populations'),
                   model_uri=DEFAULT_.parental_populations, domain=AffectedGenomicModel, range=Optional[Union[str, URIorCURIE]])

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=Optional[str])
