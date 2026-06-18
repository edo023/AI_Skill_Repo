# About the Book

## Document Scope

The EcoStruxure Machine Expert™ – Safety application software is used to develop a functional safety system with a Safety Logic Controller (SLC).

Machine Expert – Safety and therefore also this manual cover different generations of functional safety systems referred to as SLCv1 and SLCv2. The SLCv1 generation includes the TM5CSLC100FS and TM5CSLC200FS, while SLCv2 includes the TM5CSLC300FS and TM5CSLC400FS.

Only the corresponding safety-related modules of the same (firmware) generation can be used with the respective SLC types (since, among other things, the device parameters relevant for the safety response time differ).

## Validity Note

This document has been updated with the release of Machine Expert – Safety V2.2.

The technical characteristics of the devices described in this document also appear online. To access this information online, go to the Schneider Electric home page [www.se.com](http://www.se.com).

The characteristics that are described in the present document, as well as those described in the documents included in the Related Documents section below, can be found online. To access the information online, go to the Schneider Electric home page [www.se.com/ww/en/download/](http://www.se.com/ww/en/download).

The characteristics that are presented in the present document should be the same as those characteristics that appear online. In line with our policy of constant improvement, we may revise content over time to improve clarity and accuracy. If you see a difference between the document and online information, use the online information as your reference.

| Title of Documentation | Reference Number |
| --- | --- |
| Modicon TM5 Safety Logic Controller SLCx00FS Hardware Guide | EIO0000000889 (Eng)  EIO0000000891 (Ger),  EIO0000000892 (Ita), |
| TM5/TM7 I/O Safety Modules - Hardware Guide | EIO0000000861 (Eng),  EIO0000000862 (Ger), |
| Modicon TM7 Digital I/O Modules Hardware Guide | EIO0000000703 (Eng),  EIO0000000704 (Fre),  EIO0000000705 (Ger),  EIO0000000706 (Spa),  EIO0000000707 (Ita),  EIO0000000704 (Chs) |
| TM5SD••• Instruction Sheet | S1A85744 |
| TM7SDM12DTFS Instruction Sheet | S1A85745 |
| TM5CSLC• /TM5ACSLCM•• Instruction Sheet | S1A85742 |
| TM5CSLC300FS / TM5CSLC400FS / TM5ACSLCM8FS Instruction Sheet | NNZ96445 |
| LMC Pro/Pro2 Hardware Guide | EIO0000001503 (Eng)  EIO0000001504 (Ger) |
| TM5 SERCOS III Interface - Hardware Guide | EIO0000003221 (Eng),  EIO0000003222 (Fre),  EIO0000003223 (Ger),  EIO0000003224 (Spa),  EIO0000003225 (Ita),  EIO0000003226 (Chs) |
| TM5/TM7 Safety Flexible System - System Planning and Installation Guide | EIO0000001064 (Eng),  EIO0000001066 (Ger), |
| XY2AU1 / XY2AU1 Instruction Sheet | 163437801A55 (Eng, Ger, Por, Spa, Ita, Fre) |
| SlcRemoteController library guide | EIO0000002149 (Eng),  EIO0000002150 (Ger),  EIO0000002150 (Ger),  EIO0000002150 (Ger),  EIO0000002150 (Ger),  EIO0000002150 (Ger),  EIO0000002150 (Ger), |
| M262 Logic/Motion Controller - Programming Guide | EIO0000003651 (Eng),  EIO0000003652 (Fre),  EIO0000003653 (Ger),  EIO0000003654 (Spa),  EIO0000003655 (Ita),  EIO0000003656 (Chs)  EIO0000003657 (Por)  EIO0000003658 (Tur) |
| M262 Embedded Safety - Integration Guide | EIO0000003921 (Eng),  EIO0000003923 (Fre),  EIO0000003922 (Ger),  EIO0000003926 (Spa),  EIO0000003924 (Ita),  EIO0000003925 (Chs) |
| CommonToolbox - Library Guide | EIO0000004219 (Eng),  EIO0000004220 (Fre),  EIO0000004221 (Ger),  EIO0000004222 (Spa),  EIO0000004223 (Ita),  EIO0000004224 (Chs) |
| Safety Modules - Reference Guide | EIO0000002265 (Eng),  EIO0000002266 (Ger),  EIO0000004295 (Ita), |
| Safe Logger for Machine Expert Safety - User Guide | EIO0000002596 (Eng),  EIO0000002597 (Ger),  EIO0000004361 (Ita), |
| Sercos for M262 - User Guide | EIO0000003883 (Eng),  EIO0000003885 (Fre),  EIO0000003884 (Ger),  EIO0000003888 (Spa),  EIO0000003886 (Ita),  EIO0000003887 (Chs) |
| How to Configure the Firewall for PacDrive LMC Controllers | EIO0000004198 (Eng)  EIO0000004199 (Ger) |

## Product Related Information

| DANGER | |
| --- | --- |
|  | **HAZARD OF ELECTRIC SHOCK, EXPLOSION OR ARC FLASH**   * Disconnect all power from all equipment including connected devices prior to removing any covers or doors, or installing or removing any accessories, hardware, cables, or wires except under the specific conditions specified in the appropriate hardware guide for this equipment. * Always use a properly rated voltage sensing device to confirm the power is off where and when indicated. * Replace and secure all covers, accessories, hardware, cables, and wires and confirm that a proper ground connection exists before applying power to the unit. * Use only the specified voltage when operating this equipment and any associated products.   **Failure to follow these instructions will result in death or serious injury.** |

| DANGER | |
| --- | --- |
|  | **POTENTIAL FOR EXPLOSION**   * Only use this equipment in non-hazardous locations, or in locations that comply with Class I, Division 2, Groups A, B, C and D. * Do not substitute components which would impair compliance to Class I, Division 2. * Do not connect or disconnect equipment unless power has been removed or the location is known to be non-hazardous. * Do not use the USB port(s), if so equipped, unless the location is known to be non-hazardous.   **Failure to follow these instructions will result in death or serious injury.** |

| WARNING | |
| --- | --- |
|  | **LOSS OF CONTROL**   * Perform a Failure Mode and Effects Analysis (FMEA), or equivalent risk analysis, of your application, and apply preventive and detective controls before implementation. * Provide a fallback state for undesired control events or sequences. * Provide separate or redundant control paths wherever required. * Supply appropriate parameters, particularly for limits. * Review the implications of transmission delays and take actions to mitigate them. * Review the implications of communication link interruptions and take actions to mitigate them. * Provide independent paths for control functions (for example, emergency stop, over-limit conditions, and error conditions) according to your risk assessment, and applicable codes and regulations. * Apply local accident prevention and safety regulations and guidelines.1 * Test each implementation of a system for proper operation before placing it into service.   **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

|  |  |
| --- | --- |
| 1 | For additional information, refer to NEMA ICS 1.1 (latest edition), Safety Guidelines for the Application, Installation, and Maintenance of Solid State Control and to NEMA ICS 7.1 (latest edition), Safety Standards for Construction and Guide for Selection, Installation and Operation of Adjustable-Speed Drive Systems or their equivalent governing your particular location. |

| WARNING | |
| --- | --- |
|  | **UNINTENDED EQUIPMENT OPERATION**   * Only use software approved by Schneider Electric for use with this equipment. * Update your application program every time you change the physical hardware configuration.   **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

Pay particular attention in conforming to any safety information, different electrical requirements, and normative standards that would apply to your adaptation.

| WARNING | |
| --- | --- |
|  | **UNINTENDED EQUIPMENT OPERATION**   * Perform an in-depth risk analysis to determine the appropriate safety integrity level for your specific application, based on all the applicable standards. * Do not exceed SIL 3 ratings in the application of this product.   **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

For reasons of Internet security, for those devices that have a native Ethernet connection, TCP/IP forwarding is disabled by default. Therefore, you must manually enable TCP/IP forwarding. However, doing so may expose your network to possible cyberattacks if you do not take additional measures to protect your enterprise. In addition, you may be subject to laws and regulations concerning cybersecurity.

| WARNING | |
| --- | --- |
|  | **UNAUTHENTICATED ACCESS AND SUBSEQUENT NETWORK INTRUSION**   * Observe and respect any and all pertinent national, regional and local cybersecurity and/or personal data laws and regulations when enabling TCP/IP forwarding on an industrial network. * Isolate your industrial network from other networks inside your company. * Protect any network against unintended access by using firewalls, VPN, or other, proven security measures.   **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

Consult the [Schneider Electric Cybersecurity Best Practices](https://www.se.com/ww/en/download/document/7EN52-0390/) for additional information.

## Terminology Derived from Standards

The technical terms, terminology, symbols and the corresponding descriptions in this manual, or that appear in or on the products themselves, are generally derived from the terms or definitions of international standards.

In the area of functional safety systems, drives and general automation, this may include, but is not limited to, terms such as *safety*, *safety-related function*, *safe-state*, *fault*, *fault reset*, *malfunction*, *failure*, *error*, *error message*, *dangerous*, etc.

Among others, these standards include:

| Standard | Description |
| --- | --- |
| IEC 61131-2:2008 | Programmable controllers, part 2: Equipment requirements and tests. |
| ISO 13849-1:2015 | Safety of machinery: Safety related parts of control systems.  General principles for design. |
| EN 61496-1:2021 | Safety of machinery: Electro-sensitive protective equipment.  Part 1: General requirements and tests. |
| ISO 12100:2010 | Safety of machinery - General principles for design - Risk assessment and risk reduction |
| EN 60204-1:2019 | Safety of machinery - Electrical equipment of machines - Part 1: General requirements |
| ISO 14119:2013 | Safety of machinery - Interlocking devices associated with guards - Principles for design and selection |
| ISO 13850:2015 | Safety of machinery - Emergency stop - Principles for design |
| IEC 62061:2019 | Safety of machinery - Functional safety of safety-related electrical, electronic, and electronic programmable control systems |
| IEC 61508-1:2011 | Functional safety of electrical/electronic/programmable electronic safety-related systems: General requirements. |
| IEC 61508-2:2010 | Functional safety of electrical/electronic/programmable electronic safety-related systems: Requirements for electrical/electronic/programmable electronic safety-related systems. |
| IEC 61508-3:2011 | Functional safety of electrical/electronic/programmable electronic safety-related systems: Software requirements. |
| IEC 61784-3:2022 | Industrial communication networks - Profiles - Part 3: Functional safety fieldbuses - General rules and profile definitions. |
| 2006/42/EC | Machinery Directive |
| 2014/30/EU | Electromagnetic Compatibility Directive |
| 2014/35/EU | Low Voltage Directive |

In addition, terms used in the present document may tangentially be used as they are derived from other standards such as:

| Standard | Description |
| --- | --- |
| IEC 60034 series | Rotating electrical machines |
| IEC 61800 series | Adjustable speed electrical power drive systems |
| IEC 61158 series | Digital data communications for measurement and control – Fieldbus for use in industrial control systems |

Finally, the term *zone of operation* may be used in conjunction with the description of specific hazards, and is defined as it is for a *hazard zone* or *danger zone* in the *EC Machinery Directive (2006/42/EC)* and *ISO 12100:2010*.

**NOTE:**

The aforementioned standards may or may not apply to the specific products cited in the present documentation. For more information concerning the individual standards applicable to the products described herein, see the characteristics tables for those product references.

If not otherwise stated, the respective terms are used in keeping with the IEC 61508 standard.

* "Error" in keeping with the common use in the context of programming systems. Machine Expert – Safety helps to detect invalid code syntax, programmed by the user, qualifies them as errors and outputs accordingly an error message in the Machine Expert – Safety message window.
* "Standard" = non-safety-related (according to IEC 61508 and PLCopen TC5 Safety Specification V1.0). The term "standard" always refers to non-safety-related items. Examples: a standard process data item is only read/written by a non-safety-related I/O device (that is to say, a standard device). Standard variables/functions/function blocks are non-safety-related data. The term "standard PLC" designates the non-safety-related controller.
* "Non-safe" as synonym for "standard" (only in the Machine Expert – Safety Error Catalog, message text as displayed in Machine Expert – Safety), taking the PLCopen TC5 Safety Specification V1.0 into account.

EIO0000002147.09