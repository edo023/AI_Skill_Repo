# IEC 61131-3 Basic Functions/Function Blocks

This help file contains descriptions of firmware functions and function blocks.

## How to call help on functions/function blocks?

You can call the table of contents of the complete FU/FB help via the menu by selecting the '? > Help on FB/FU' menu item.

To open the help topic relating to a specific function or function block you can use the Edit Wizard or the dialog 'Function/Function Block'.

* In the **Edit Wizard** selection area, right-click the desired function or function block and select 'Help on FB/FU' from the context menu.

  Or:
* In the **graphical editor**, right-click on the relevant block icon and select 'Help on FB/FU' from the context menu.
* The **'Function/Function Block' dialog** provides the '?' button to call the related FU/FB help topic. To open the dialog, double-click the relevant block icon in the editor or select 'Object Properties...' from its context menu.

## Definition of basic functions/function blocks according to the IEC 61131-3 standard

**Functions** (short: FUs) are POUs which may have several input parameters but always exactly one output parameter. As they do not have any internal memory, a function called with the same input values always returns the same result.

**Function blocks** (short: FBs) are POUs which may have several input and several output parameters. FBs have an internal memory. This means that the value a function block returns depends on the value of its internal memory. Therefore, function blocks have to be instantiated: An instance name has to be declared for each FB to be used, which uniquely identifies the FB instance, and with which the FB can be used (called) in the code. The declaration of the instance name is done automatically using the 'Variable' dialog when inserting an FB from the Edit Wizard into the code.

In addition to the IEC 61131-3 basic functions/function blocks, further libraries can be included in EcoStruxure Machine Expert - Safety (see topic "[How to insert/delete libraries](subtree_library_intheprojecttree.html#subtree_library_intheprojecttree)") providing additional blocks.

EIO0000002267.00

© 2021

Schneider Electric.

All rights reserved.