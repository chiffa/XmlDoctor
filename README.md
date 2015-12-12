# rdfDoctor
Snippets of code for rdf document comprehension for human

Here is an example of the file run on the [Reactome.org human BioPax lvl3 .owl](http://www.reactome.org/pages/download-data/) file. Initial row is a class with count of instances, attribuytes are listed with indent and attributes that link to a class within the rdf documented are indented more and rely on sane names for the identifiers of different classes.

For each tag and class pointed to, percentages indicate percentage of classes where a tag was enountered within a class and number of tags per class, whereas the pointer to the classes within a class indicate how frequently a class was encountered knowing that a tag was encountered and how many time it was present when it was encountered.

```
DnaReference                  289
    comment                                 0.35 %      1.00
    xref                                  100.00 %      1.00
		#UnificationXref                     100.00 %      1.00
    organism                              100.00 %      1.00
		#BioSource                           100.00 %      1.00
    name                                  100.00 %      2.10


Dna                           303
    comment                               100.00 %      1.04
    cellularLocation                      100.00 %      1.00
		#CellularLocationVocabulary          100.00 %      1.00
    displayName                           100.00 %      1.00
    name                                   14.19 %      1.30
    feature                                 6.60 %      1.10
		#FragmentFeature                     100.00 %      1.00
		#ModificationFeature                  10.00 %      1.00
    entityReference                        96.04 %      1.00
		#DnaReference                        100.00 %      1.00
    xref                                  100.00 %      2.00
		#UnificationXref                     100.00 %      2.00
    dataSource                            100.00 %      1.00
		#Provenance                          100.00 %      1.00
    memberPhysicalEntity                    3.96 %      3.25
		#Dna                                 100.00 %      3.25


Provenance                    1
    comment                               100.00 %      1.00
    name                                  100.00 %      1.00


SequenceInterval              16534
    sequenceIntervalBegin                 100.00 %      1.00
		#SequenceSite                        100.00 %      1.00
    sequenceIntervalEnd                   100.00 %      1.00
		#SequenceSite                        100.00 %      1.00


Complex                       9098
    comment                               100.00 %      1.06
    cellularLocation                      100.00 %      1.00
		#CellularLocationVocabulary          100.00 %      1.00
    displayName                           100.00 %      1.00
    name                                   16.66 %      1.16
    componentStoichiometry                 94.30 %      2.48
		#Stoichiometry                       100.00 %      2.48
    component                              94.30 %      2.48
		#PhysicalEntity                       11.12 %      1.13
		#Complex                              44.64 %      1.45
		#Protein                              80.28 %      1.85
		#Rna                                   1.25 %      1.44
		#SmallMolecule                        16.03 %      1.16
		#Dna                                   1.76 %      1.00
    xref                                  100.00 %      2.00
		#UnificationXref                     100.00 %      2.00
    dataSource                            100.00 %      1.00
		#Provenance                          100.00 %      1.00
    memberPhysicalEntity                    5.70 %      3.58
		#Complex                             100.00 %      3.58


RelationshipXref              5026
    comment                                63.81 %      1.00
    relationshipType                      100.00 %      1.00
		#RelationshipTypeVocabulary          100.00 %      1.00
    db                                    100.00 %      1.00
    id                                    100.00 %      1.00


Catalysis                     4082
    xref                                  100.00 %      2.00
		#RelationshipXref                    100.00 %      2.00
    controlled                            100.00 %      1.00
		#Degradation                           0.17 %      1.00
		#BiochemicalReaction                  99.83 %      1.00
    controller                             99.90 %      1.00
		#Complex                              55.84 %      1.00
		#Protein                              39.70 %      1.00
		#PhysicalEntity                        4.46 %      1.00
    controlType                           100.00 %      1.00
    dataSource                            100.00 %      1.00
		#Provenance                          100.00 %      1.00


Stoichiometry                 23586
    physicalEntity                        100.00 %      1.00
		#PhysicalEntity                        4.71 %      1.00
		#Complex                              24.29 %      1.00
		#Protein                              55.94 %      1.00
		#Rna                                   0.65 %      1.00
		#SmallMolecule                        13.76 %      1.00
		#Dna                                   0.64 %      1.00
    stoichiometricCoefficient             100.00 %      1.00


Pathway                       1887
    comment                                99.10 %      3.89
    xref                                  100.00 %      6.59
		#PublicationXref                      89.24 %      4.68
		#UnificationXref                     100.00 %      2.00
		#RelationshipXref                     41.23 %      1.00
    displayName                           100.00 %      1.00
    name                                    3.87 %      1.10
    pathwayComponent                       99.89 %      5.88
		#Degradation                           0.48 %      1.89
		#BiochemicalReaction                  80.48 %      5.97
		#Pathway                              34.16 %      3.05
		#TemplateReaction                      0.95 %      2.56
    dataSource                            100.00 %      1.00
		#Provenance                          100.00 %      1.00
    organism                              100.00 %      1.00
		#BioSource                           100.00 %      1.00
    pathwayOrder                           99.89 %      5.88
		#PathwayStep                         100.00 %      5.88


BioSource                     22
    xref                                  100.00 %      1.00
		#UnificationXref                     100.00 %      1.00
    name                                  100.00 %      1.00


Modulation                    23
    xref                                  100.00 %      2.09
		#PublicationXref                       8.70 %      1.00
		#UnificationXref                     100.00 %      2.00
    displayName                           100.00 %      1.00
    controller                            100.00 %      1.00
		#PhysicalEntity                        4.35 %      1.00
		#Complex                              13.04 %      1.00
		#Protein                               8.70 %      1.00
		#SmallMolecule                        73.91 %      1.00
    controlType                           100.00 %      1.00
    dataSource                            100.00 %      1.00
		#Provenance                          100.00 %      1.00
    controlled                            100.00 %      1.00
		#Catalysis                           100.00 %      1.00


TemplateReactionRegulation    51
    xref                                  100.00 %      2.14
		#PublicationXref                       5.88 %      2.33
		#UnificationXref                     100.00 %      2.00
    displayName                           100.00 %      1.00
    controller                            100.00 %      1.00
		#Complex                              25.49 %      1.00
		#Protein                              72.55 %      1.00
		#SmallMolecule                         1.96 %      1.00
    controlType                           100.00 %      1.00
    dataSource                            100.00 %      1.00
		#Provenance                          100.00 %      1.00
    controlled                            100.00 %      1.00
		#TemplateReaction                    100.00 %      1.00


Rna                           155
    comment                               100.00 %      1.14
    cellularLocation                      100.00 %      1.00
		#CellularLocationVocabulary          100.00 %      1.00
    displayName                           100.00 %      1.00
    name                                   21.29 %      1.36
    feature                                21.29 %      1.00
		#FragmentFeature                     100.00 %      1.00
    entityReference                        85.81 %      1.00
		#RnaReference                        100.00 %      1.00
    xref                                  100.00 %      2.00
		#UnificationXref                     100.00 %      2.00
    dataSource                            100.00 %      1.00
		#Provenance                          100.00 %      1.00
    memberPhysicalEntity                   14.19 %      4.45
		#Rna                                 100.00 %      4.45


Degradation                   17
    comment                               100.00 %      3.65
    xref                                  100.00 %      5.88
		#PublicationXref                     100.00 %      3.82
		#UnificationXref                     100.00 %      2.00
		#RelationshipXref                      5.88 %      1.00
    displayName                           100.00 %      1.00
    dataSource                            100.00 %      1.00
		#Provenance                          100.00 %      1.00
    left                                  100.00 %      1.00
		#Complex                              70.59 %      1.00
		#Protein                              17.65 %      1.00
		#PhysicalEntity                       11.76 %      1.00


PhysicalEntity                1303
    comment                               100.00 %      1.34
    cellularLocation                      100.00 %      1.00
		#CellularLocationVocabulary          100.00 %      1.00
    displayName                           100.00 %      1.00
    name                                   20.57 %      1.13
    xref                                  100.00 %      2.00
		#UnificationXref                     100.00 %      2.00
    dataSource                            100.00 %      1.00
		#Provenance                          100.00 %      1.00
    memberPhysicalEntity                   34.31 %      5.11
		#PhysicalEntity                       27.96 %      3.10
		#Complex                              44.07 %      2.40
		#Protein                              64.88 %      4.30
		#SmallMolecule                        10.07 %      3.56
		#Dna                                   0.22 %     19.00


PublicationXref               18945
    title                                 100.00 %      1.00
    url                                     0.08 %      1.00
    author                                100.00 %      5.67
    db                                     99.60 %      1.00
    source                                 99.86 %      1.00
    year                                   99.92 %      1.00
    id                                     99.60 %      1.00


ProteinReference              8711
    comment                                99.87 %      1.00
    xref                                  100.00 %      1.00
		#UnificationXref                     100.00 %      1.00
    organism                              100.00 %      1.00
		#BioSource                           100.00 %      1.00
    name                                  100.00 %      3.25


TemplateReaction              42
    comment                               100.00 %      3.57
    product                               100.00 %      1.00
		#PhysicalEntity                        2.38 %      1.00
		#Protein                              95.24 %      1.00
		#SmallMolecule                         2.38 %      1.00
    xref                                  100.00 %      3.45
		#PublicationXref                      57.14 %      2.54
		#UnificationXref                     100.00 %      2.00
    displayName                           100.00 %      1.00
    dataSource                            100.00 %      1.00
		#Provenance                          100.00 %      1.00


Control                       946
    comment                                19.34 %      1.00
    xref                                  100.00 %      2.96
		#PublicationXref                      55.39 %      1.74
		#UnificationXref                     100.00 %      2.00
    displayName                           100.00 %      1.00
    controller                             99.89 %      1.00
		#PhysicalEntity                        0.85 %      1.00
		#Complex                              51.11 %      1.00
		#Protein                              30.69 %      1.00
		#Rna                                   0.11 %      1.00
		#SmallMolecule                        17.25 %      1.00
    controlType                           100.00 %      1.00
    dataSource                            100.00 %      1.00
		#Provenance                          100.00 %      1.00
    controlled                            100.00 %      1.00
		#Pathway                               0.32 %      1.00
		#BiochemicalReaction                  99.68 %      1.00


SmallMoleculeReference        1503
    xref                                  100.00 %      1.00
		#UnificationXref                     100.00 %      1.00
    name                                  100.00 %      2.79


SmallMolecule                 3146
    comment                               100.00 %      1.11
    cellularLocation                      100.00 %      1.00
		#CellularLocationVocabulary          100.00 %      1.00
    displayName                           100.00 %      1.00
    name                                   83.38 %      2.84
    entityReference                        88.68 %      1.00
		#SmallMoleculeReference              100.00 %      1.00
    xref                                  100.00 %      2.00
		#UnificationXref                     100.00 %      2.00
    dataSource                            100.00 %      1.00
		#Provenance                          100.00 %      1.00
    memberPhysicalEntity                   11.32 %      4.13
		#SmallMolecule                       100.00 %      4.13


RnaReference                  80
    comment                                11.25 %      1.00
    xref                                  100.00 %      1.00
		#UnificationXref                     100.00 %      1.00
    organism                              100.00 %      1.00
		#BioSource                           100.00 %      1.00
    name                                  100.00 %      2.92


SequenceModificationVocabulary125
    term                                  100.00 %      1.00
    xref                                  100.00 %      1.00
		#UnificationXref                     100.00 %      1.00


PathwayStep                   10454
    stepProcess                           100.00 %      1.49
		#Degradation                           0.16 %      1.00
		#BiochemicalReaction                  81.77 %      1.00
		#Pathway                              17.67 %      1.00
		#Catalysis                            38.78 %      1.01
		#TemplateReaction                      0.40 %      1.00
		#Modulation                            0.11 %      2.09
		#Control                               6.53 %      1.38
		#TemplateReactionRegulation            0.35 %      1.38
    nextStep                               50.35 %      1.47
		#PathwayStep                         100.00 %      1.47


BiochemicalReaction           8554
    participantStoichiometry               15.24 %      1.77
		#Stoichiometry                       100.00 %      1.77
    comment                               100.00 %      3.97
    right                                  96.83 %      1.66
		#PhysicalEntity                        4.47 %      1.07
		#Complex                              60.63 %      1.09
		#Protein                              19.17 %      1.37
		#Rna                                   0.29 %      1.08
		#SmallMolecule                        42.28 %      1.62
    displayName                           100.00 %      1.00
    name                                    9.38 %      1.06
    conversionDirection                   100.00 %      1.00
    xref                                  100.00 %      5.05
		#PublicationXref                      95.67 %      3.15
		#UnificationXref                     100.00 %      2.00
		#RelationshipXref                      3.41 %      1.00
    dataSource                            100.00 %      1.00
		#Provenance                          100.00 %      1.00
    eCNumber                               30.06 %      1.05
    left                                   99.91 %      1.96
		#PhysicalEntity                        7.38 %      1.05
		#Complex                              49.49 %      1.19
		#Protein                              36.91 %      1.36
		#Rna                                   0.54 %      1.04
		#SmallMolecule                        46.20 %      1.61
		#Dna                                   4.20 %      1.00


FragmentFeature               16534
    featureLocation                       100.00 %      1.00
		#SequenceInterval                    100.00 %      1.00


ModificationFeature           3861
    featureLocation                        68.01 %      1.00
		#SequenceSite                        100.00 %      1.00
    modificationType                       98.86 %      1.00
		#SequenceModificationVocabulary       100.00 %      1.00
    comment                                 1.14 %      1.00


SequenceSite                  35694
    sequencePosition                      100.00 %      1.00
    positionStatus                        100.00 %      1.00


RelationshipTypeVocabulary    3
    term                                  100.00 %      1.00
    xref                                   66.67 %      1.00
		#UnificationXref                     100.00 %      1.00


CellularLocationVocabulary    107
    term                                  100.00 %      1.00
    xref                                  100.00 %      1.00
		#UnificationXref                     100.00 %      1.00


Protein                       19011
    comment                               100.00 %      1.11
    cellularLocation                      100.00 %      1.00
		#CellularLocationVocabulary          100.00 %      1.00
    displayName                           100.00 %      1.00
    name                                   83.81 %      2.36
    feature                                87.11 %      1.78
		#FragmentFeature                      99.52 %      1.00
		#ModificationFeature                  29.97 %      2.62
    entityReference                        89.13 %      1.00
		#ProteinReference                    100.00 %      1.00
    xref                                  100.00 %      2.00
		#UnificationXref                     100.00 %      2.00
    dataSource                            100.00 %      1.00
		#Provenance                          100.00 %      1.00
    memberPhysicalEntity                   10.87 %      5.65
		#Protein                             100.00 %      5.65


UnificationXref               99901
    comment                                89.15 %      1.00
    idVersion                              44.58 %      1.00
    db                                    100.00 %      1.00
    id                                    100.00 %      1.00
```



