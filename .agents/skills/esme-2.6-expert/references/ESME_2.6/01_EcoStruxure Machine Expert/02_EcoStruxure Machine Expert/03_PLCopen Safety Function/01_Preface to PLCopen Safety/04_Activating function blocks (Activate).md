# Activating function blocks (Activate)

Each safety-related function block can be activated and deactivated via the Activate input.

This means the Activate input can be used to connect/disconnect one or more items of safety equipment and implement modular safety equipment.

If a function block is deactivated (Activate input = FALSE), any state changes and detected edges at its other inputs have no effect on the states of the function block outputs.

**NOTE:**

In order to activate a function block perpetually, you can connect its Activate input to the TRUE constant.

The topic is explained in terms of the following categories:

* [Individual activation of safety equipment](IndividDeactivation.html#IndividDeactivation): Manual connection/disconnection (activation/deactivation) of individual, mutually independent safety-related functions.
* [Group activation of safety equipment](GroupDeactivation.html#GroupDeactivation): Manual connection/disconnection (activation/deactivation) of combined, mutually independent safety-related functions via a common signal.
* [Modular machines/systems with safety equipment](ModularDeact.html#ModularDeact): Process-related connection/disconnection (activation/deactivation) of individual system modules with safety equipment.

EIO0000002269.01

© 2020

Schneider Electric.

All rights reserved.