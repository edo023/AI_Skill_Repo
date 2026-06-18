# Explanation of terms

The following explanations of terms are listed in alphabetical order.

| Term | Explanation |
| --- | --- |
| Start-up inhibit | When a start-up inhibit is active, all safety-related outputs of the function block are in the defined safe state. This ensures that a machine/system cannot be started up inadvertently.  If a start-up inhibit is active, a reset signal is required to remove this and enable the machine/system to function. |
| Edge-triggered and state-controlled inputs | A function block only evaluates the signals of edge-triggered inputs for changes in levels.  By contrast, a function block processes the signals of state-controlled inputs continuously, not only when there are modifications in signal levels. |
| Line control | See "Cross-circuit detection". |
| Cross-circuit detection | A "cross circuit" is an unintentional, incorrect connection between redundant circuits.  Clock outputs can be used as an aid for detecting such a cross circuit.  For example, if two differently clocked signals are routed back to two inputs of the Safety Logic Controller along two channels via an emergency-stop control device, a cross circuit can definitely be detected in this emergency-stop circuit: In the event of a cross circuit, the same clock signal would be present at both inputs, instead of two different ones.  **NOTE:**  The Safety Logic Controller must support evaluation of the clock signals for the inputs.  **Further Information:**  Also take the corresponding information on implementing cross-circuit detection, which is found in the User Manual, into account. |
| Redundancy | Redundancy refers generally to the presence of additional components/elements/units used to increase operational reliability and functional safety.  Examples:   * Two mutually independent processing units (paths) in the Safety Logic Controller (signal redundancy). * Two mutually independent circuits/power supplies. * Pairs of contacts and signal lines for a safety-related control device or for an actuator. |
| Risk analysis | Statement, based on scientific fact and predefined criteria (e.g., risk graphs, defined in various standards, depending on the field of application), on the probability of possible risks occurring and on the damaging effects they would have during operation of a machine or system which requires protection.  The result of the risk analysis is classified as a category, level or performance level (depending on the relevant standard, i.e., area of application).  The result of the risk analysis can be used to directly derive the architecture of the functional safety system and to make statements as regards error detection and exception avoidance measures. |
| Safety logic | The safety-related code developed in the EcoStruxure Machine Expert - Safety Code Editor is called safety logic.  The Safety Logic Controller evaluates the safety-related sensors/control devices connected to the safety-related input devices in accordance with the programmed safety logic and switches its outputs accordingly, using the connected actuators. |
| Stop category | Stop categories in accordance with **DIN EN 60204**:  * **Stop category 0**: An uncontrolled stop resulting from immediate removal of power to the machine drive units. * **Stop category 1**: A controlled stop with power left available to the machine drive units in order to achieve the stop. The power is only removed when the stop has been achieved. * **Stop category 2**: A controlled stop with power left available to the machine drive units. |
| Restart inhibit | When a restart inhibit is active, all safety-related outputs of the function block are in the defined safe state. This ensures that a machine/system cannot be restarted inadvertently.  If a restart inhibit is active, a reset signal is required to remove this and enable the machine/system to function. |
| State-controlled inputs | See "Edge-triggered inputs". |

EIO0000002269.01

© 2020

Schneider Electric.

All rights reserved.