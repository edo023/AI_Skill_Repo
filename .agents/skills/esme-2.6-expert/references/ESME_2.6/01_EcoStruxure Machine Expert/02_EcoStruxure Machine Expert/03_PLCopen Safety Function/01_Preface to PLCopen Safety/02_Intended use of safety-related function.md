# Intended use of safety-related function blocks

The safety-related function blocks/functions described here are solely intended for use in the EcoStruxure Machine Expert - Safety software for creating safety-related code for suitable Safety Logic Controllers. You can only meet your safety-relevant tasks within the safety-related control system if they were integrated into the execution process in a correct and functionally safe manner.

| WARNING | |
| --- | --- |
|  | **NON-CONFORMANCE TO SAFETY FUNCTION REQUIREMENTS**   * Verify that the safety-related function blocks are only used in accordance with the instructions given in this documentation. * Validate the overall safety-related function and thoroughly test the application.   **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

You must observe all the information in this document as well as in the documentation listed in the 'Related documents' section.

Basic application examples can be found in the description for the relevant function block in the section titled "Application examples".

The safety-related function blocks are integrated into the graphical programming interface of the EcoStruxure Machine Expert - Safety software. Each function block supports a specific safety-related function for creating a safety logic.

The area of responsibility of the function block manufacturer in terms of the function of a safety-related function block ends at the user interface of the function block, which is represented by its inputs and outputs (formal parameters).

In order to fully execute a safety-related function, it is your responsibility to connect the inputs and outputs of the safety-related function blocks in the safety-related EcoStruxure Machine Expert - Safety software

* with your safety logic and
* with the single-channel or two-channel sensors and actuators connected within your safety logic.

| WARNING | |
| --- | --- |
|  | **NON-CONFORMANCE TO SAFETY FUNCTION REQUIREMENTS**   * In order to define the safety integrity level (SIL) or performance level for the complete safety-related function, you must take into consideration all the components involved in the execution of this safety-related function (sensors, actuators, wiring, etc.). * In order to use a safety-related function block/function according to the required safety integrity level as defined by IEC 61508, EN ISO 13849-1, or EN 62061, you must take into consideration the entire path of the safety-related function (all components that are interconnected, as well as all defining logical, configuration and parameter components, to form the safety-related function, such as Safety Logic Controller, I/O modules, device parameterization, wiring, sensors, actuators, single-channel or two-channel operation, etc.), starting from the function block formal parameters. * Validate the entire safety-related function before placing the equipment into operation.   **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

EIO0000002269.01

© 2020

Schneider Electric.

All rights reserved.