# Programming a Project

This help chapter contains topics that describe all necessary steps and procedures for programming a project.

You will learn how to:

* [Create a new project](creatinganewprojectusingtheprojectwizard.html#creatinganewprojectusingtheprojectwizard).
* [Open](openinganexistingproject.html#openinganexistingproject) and [import/export](ImportExportProject_SE.html#ImportExportProject_SE) safety-related projects.
* [Parameterize used devices](DeviceParamEditor.html#DeviceParamEditor) using the Device Parameterization Editor and what are [Advanced and Commissioning Parameters](AdvancedAndCommissioningParameters.html#AdvancedAndCommissioningParameters).
* Define the project structure in the project tree by [managing logical POUs](subtree_logicalpous_intheprojecttree.html#subtree_logicalpous_intheprojecttree) and [libraries](subtree_library_intheprojecttree.html#subtree_library_intheprojecttree).
* Program the [Enable Principle](ProgrammingEnablePrinciple.html#ProgrammingEnablePrinciple).
* Edit code in the [graphical IEC 61131 programming languages FBD and LD](editinginfbd_ldusingthegraphiceditor.html#editinginfbd_ldusingthegraphiceditor).

  **Further Information:**

  Descriptions of the available [code objects](objectsinthegraphiceditor.html#objectsinthegraphiceditor) and the [dialogs used to edit these objects](dialogsforeditingcode.html#dialogsforeditingcode) can be found in the related topics provided in the "User Interface" help chapter.
* Edit code in the [textual IEC 61131 programming language ST](TextEd_Intro.html#TextEd_Intro).
* [Connect/disconnect global I/O variables and process data items](SE_AssignProcessDataItems.html#SE_AssignProcessDataItems).
* [Compare two projects](comparingprojectsources.html#comparingprojectsources).
* [Translate project comments and descriptions](translatingaproject.html#translatingaproject).
* Set the [POU verification flag](POUverification.html#POUverification) after having completed and verified a user POU in order to protect it against unintended modifications and to indicate its state in the project tree.
* [Print a project](printingandpreview.html#printingandpreview).

After having edited the project, continue with

* [compiling the project](compiling.html#compiling) and
* [commissioning the Safety Logic Controller application](OnlineGeneral.html#OnlineGeneral).

**NOTE:**

Term definition: Standard = non-safety-related.

The term "standard" always refers to non-safety-related items/objects. Examples: a standard process data item is only read/written by a non-safety-related I/O device, i.e., a standard device. Standard variables/functions/FBs are non-safety-related data. The term "standard controller" designates the non-safety-related controller.

**NOTE:**

Machine Expert – Safety provides a certification manager for certifying the completed project after successful commissioning. A certified project is protected by password against modifications. (Such modifications would result in a new project acceptance procedure and certification.)

If you can't edit the project although you are logged-on correctly, verify whether the project is already certified. This is indicated in the status bar (rightmost):

![](images/Statusbar_CertificationOn.gif)

Refer to the topic "[Project certification](CertificationManager.html#CertificationManager)" for detailed information.

EIO0000002147.09