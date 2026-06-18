# Overview on Machine Expert – Safety features

Machine Expert – Safety is based on the IEC 61131-3 standard and is designed to meet the safety requirements defined in the IEC 61508 standard.

Machine Expert – Safety is an extended level tool according to the PLCopen Safety Specification.

Machine Expert – Safety includes the required tools for the various development phases of a Safety Logic Controller application:

* Editing the safety-related application
* Compiling the project
* Downloading the project to the Safety Logic Controller
* Controlling the Safety Logic Controller (e.g., starting, stopping, resetting, etc.)
* Performing a function test
* Monitoring and debugging the safety-related application
* Documenting the project
* Printing the project documentation

These tools and functions are:

* Project tree used for:

  Organizing the Safety Logic Controller application program by defining POUs (according to IEC 61131). Refer to topic ["Project Tree - Overview"](projecttree_overview.html#projecttree_overview) for details.

  Including firmware libraries (safety-related function blocks, basic safety-related, and standard functions/function blocks). Refer to the topic ["Libraries: Inserting and deleting"](subtree_library_intheprojecttree.html#subtree_library_intheprojecttree) for details.
* Graphical code editor and Edit Wizard for developing code in the IEC 61131-3 languages [FBD (Function Block Diagram) and LD (Ladder Diagram)](editinginfbd_ldusingthegraphiceditor.html#editinginfbd_ldusingthegraphiceditor). Code elements of both languages can be mixed in graphical code worksheets.
* Textual code editor for developing code in the IEC 61131-3 language [ST (Structured Text)](TextEd_Intro.html#TextEd_Intro).
* Grid-based variables editor for [declaring variables and FB instance names](variablegridworksheets_generaldescription.html#variablegridworksheets_generaldescription).
* ['Devices' window contains the Bus Navigator](BusNavigatorGeneral.html#BusNavigatorGeneral) showing the safety-related bus configuration. The Bus Navigator displays the connected safety-related devices with the relevant information and data such as available I/O terminals, CPU address, etc. It allows to parameterize the connected safety-related devices.

  With the bus configuration, also the device terminals are imported as process data items into the application project. These process data items can simply be dragged from the device tree into the FBD/LD code.
* [Cross references window](crossreferencewindow.html#crossreferencewindow).
* [Message window](messagewindow.html#messagewindow).
* Monitoring and debug functions: [variable status display](DisplayVariableStatus.html#DisplayVariableStatus), [forcing/overwriting variables](debuggingtheproject.html#debuggingtheproject), [single cycle operation](debuggingtheproject.html#debuggingtheproject__SingleCycleMode), [watch window](watchwindow.html#watchwindow).
* [Safety Logic Controller simulation](Simulation.html#Simulation) supports the functions offered by the Safety Logic Controller, thus allowing the safety logic to be simulated without accessing physical I/Os.
* Machine Expert – Safety provides [dual protection](PasswordProtection.html#PasswordProtection) thanks to two passwords: the project password protects from unauthorized project modifications (code and device parameterization). The Safety Logic Controller password protects the configuration on the Safety Logic Controller from unauthorized access, thus preventing unauthorized switching of the operating mode.

EIO0000002147.09