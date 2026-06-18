# SF\_MutingSeq

The following description is valid for the function block SF\_MutingSeq\_V1\_0z, Version 1.0z (where z = 0 to 9).

## Short description

|  |  |
| --- | --- |
| The safety-related SF\_MutingSeq function block evaluates the signals of four muting sensors and an optoelectronic safety-related equipment (a light grid, for example) in an application for sequential muting with four sensors and switches the enable signal at the S\_AOPD\_Out output.  The signal at the S\_AOPD\_Out output is the enable signal for the entire process. A SAFEFALSE signal at the S\_AOPD\_Out output stops the application in the zone of operation.  This function can be used to temporarily deactivate (or "mute") safety-related equipment in the form of a light grid, for example, in order to allow an object which has been identified by the muting sensors as permissible (for the muting operation) to pass through on an assembly conveyor.  In such a case, the interruption of the light grid does not have any effect on the S\_AOPD\_Out output.  By contrast, if the safety-related equipment is engaged by an object which has not been identified by the muting sensors as permissible, the S\_AOPD\_Out output switches to SAFEFALSE.  For example, if the hand of a worker passes through an assembly conveyer interrupting a light grid, the S\_AOPD\_Out output would be used to signal the actions necessary to set the zone of operation to its defined safe state.  The maximum allowable time for the muting operation is monitored using the four muting sensors. Refer to the following representation to view the arrangement of the muting sensors.  A start-up inhibit can be specified at S\_StartReset. |  |

**NOTE:**

Depending on the result of the risk analysis, optical, mechanical or inductive sensors such as reflection light sensors, mechanical or inductive switches can be used as muting sensors. Optical sensors serve as examples in the help information.

**NOTE:**

Only the material flow direction from muting sensors MutingSwitch11![](images/PfeilTransRichtung.gif)MutingSwitch12 to muting sensors MutingSwitch21![](images/PfeilTransRichtung.gif)MutingSwitch22 is described in the following. The function block also supports the opposite material flow direction from muting sensors MutingSwitch22![](images/PfeilTransRichtung.gif)MutingSwitch21 to muting sensors MutingSwitch12![](images/PfeilTransRichtung.gif)MutingSwitch11. The functional sequence remains identical.

The following graphic illustrates an application for the SF\_MutingSeq function block.

**Further Information:**

The entire muting operation is divided into different muting sequences. For more detailed information, see the [functional description](function_MutingSeq.html#function_MutingSeq).

![](images/MutingSeq_Machine.gif)

The material flow direction in the example shown is from left to right.

**MS\_11, MS\_12**: First sequential muting sensor pair, positioned **before** the safety-related equipment connected to the function block inputs MutingSwitch11 and MutingSwitch12 (the "yellow light beams" symbolize the detection area).

**MS\_21, MS\_22**: Second sequential muting sensor pair, positioned **behind** the safety-related equipment, connected to function block inputs MutingSwitch21 and MutingSwitch22.

**S, R**: Transmitter and receiver of the light grid (safety-related equipment)

**T**: Goods to be transported on an assembly conveyor

**!**: Zone of operation

## Function block inputs

Click the corresponding hyperlinks to obtain detailed information on the items below.

| Name | Short description | Value |
| --- | --- | --- |
| [Activate](act_MutingSeq.html#act_MutingSeq) | State-controlled input for activating the function block.  Data type: BOOL  Initial value: FALSE | * **FALSE**: Function block inactive * **TRUE**: Function block activated |
| [S\_AOPD\_In](a_in_MutingSeq.html#a_in_MutingSeq) | State-controlled input for the status of the safety-related equipment (e.g., light grid).  Data type: SAFEBOOL  Initial value: SAFEFALSE | * **SAFEFALSE**: Light beam of the optoelectronic safety-related equipment (e.g., light barrier) interrupted.  **NOTE:**  The S\_AOPD\_Out output becomes SAFEFALSE when the muting operation is not active (S\_MutingActive = SAFEFALSE).  * **SAFETRUE**: Light beam of the optoelectronic safety-related equipment (e.g., light barrier) not interrupted. |
| [MutingSwitch11](ms_1112_MutingSeq.html#ms_1112_MutingSeq) and [MutingSwitch12](ms_1112_MutingSeq.html#ms_1112_MutingSeq) | State-controlled inputs for the muting sensors of the first sequential sensor pair.  Data type: BOOL  Initial value: FALSE  For the material flow direction  * from **left to right**, both of these sensors are positioned **before** the safety-related equipment. * from **right to left**, both of these sensors are positioned **behind** the safety-related equipment. | * **FALSE**: Light beam of the muting sensor not interrupted * **TRUE**: Light beam of the muting sensor interrupted |
| [MutingSwitch21](ms_2122_MutingSeq.html#ms_2122_MutingSeq) and [MutingSwitch22](ms_2122_MutingSeq.html#ms_2122_MutingSeq) | State-controlled inputs for the muting sensors of the second sequential sensor pair.  Data type: BOOL  Initial value: FALSE  For the material flow direction  * from **left to right**, both of these sensors are positioned **behind** the safety-related equipment. * from **right to left**, both of these sensors are positioned **before** the safety-related equipment. | * **FALSE**: Light beam of the muting sensor not interrupted * **TRUE**: Light beam of the muting sensor interrupted |
| [S\_MutingLamp](mlamp_MutingSeq.html#mlamp_MutingSeq) | State-controlled input for the feedback signal from the muting lamp.  Data type: SAFEBOOL  Initial value: SAFEFALSE | * **SAFEFALSE**: Muting lamp non-functional * **SAFETRUE**: Muting lamp in working order |
| [MaxMutingTime](prog_mmt_MutingSeq.html#prog_mmt_MutingSeq) | Specification of the maximum permissible time for the entire [muting operation](function_MutingSeq.html#function_MutingSeq__MutingSeqVorgang).  Data type: TIME  Initial value: #0ms  If the muting operation is not completed within this time, the S\_AOPD\_Out output is switched to the defined safe state SAFEFALSE (e.g., "switch off machine").  The following is valid for a **material flow direction from left to right**:  * This timer starts when the first muting sensor **before** the safety-related equipment (at input MutingSwitch11) provides a TRUE signal (i.e., there is an object inside the detection area of the sensor). * The muting operation is complete when the first muting sensor **behind** the safety-related equipment (at the MutingSwitch21 input) provides FALSE again.  The following is valid for a **material flow direction from right to left**:  * This timer starts when the first muting sensor **before** the safety-related equipment (at input MutingSwitch22) provides a TRUE signal (i.e., there is an object inside the detection area of the sensor). * The muting operation is complete when the first muting sensor **behind** the safety-related equipment (at the MutingSwitch12 input) provides FALSE again. | **Minimum value:** 0 s  **Maximum value:** 600 s  Enter a time value according to your risk analysis.  Refer to the first hazard message below this table. |
| [MutingEnable](enab_MutingSeq.html#enab_MutingSeq) | State-controlled input for enabling the muting operation.  Data type: BOOL  Initial value: FALSE | * **FALSE**: No enable for the muting operation * **TRUE**: Enable for the muting operation |
| [S\_StartReset](prog_s_res_MutingSeq.html#prog_s_res_MutingSeq) | Specification of the start-up inhibit after the Safety Logic Controller has been started up or after the function block has been activated.  Data type: SAFEBOOL  Initial value: SAFEFALSE  An active start-up inhibit must be removed manually by a positive signal edge at the Reset input. A deactivated start-up inhibit causes the S\_AOPD\_Out output to switch to SAFETRUE automatically when the function block is activated and the safety-related function is not requested.  Refer to the second hazard message below this table. | * **SAFEFALSE**: With start-up inhibit * **SAFETRUE**: Without start-up inhibit |
| [Reset](reset_MutingSeq.html#reset_MutingSeq) | Edge-triggered input for the reset signal:  * Resetting error messages when the cause of the error is no longer present. * Manual resetting of an active start-up inhibit (specified by S\_StartReset).  Refer to the third hazard message below this table.  Data type: BOOL  Initial value: FALSE  **NOTE:**  Resetting does not occur with a negative (falling) edge, as specified by standard EN ISO 13849-1, but with a positive (rising) edge. | * **FALSE**: Reset is not requested * Edge **FALSE > TRUE**: Reset is requested |

| WARNING | |
| --- | --- |
|  | **NON-CONFORMANCE TO SAFETY FUNCTION REQUIREMENTS**   * Verify that the time value set at the time input corresponds to your risk analysis. * Be sure that your risk analysis includes an evaluation for incorrectly setting the time value at the time input. * Validate the overall safety-related function with regard to the set time value and thoroughly test the application.   **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

| WARNING | |
| --- | --- |
|  | **NON-CONFORMANCE TO SAFETY FUNCTION REQUIREMENTS**   * Be sure that your risk analysis includes an evaluation if the start-up inhibit is deactivated (S\_StartReset = SAFETRUE). * Observe the regulations given by relevant sector standards regarding the start-up inhibit. * Verify that a suitable start-up inhibit is in place at another location or using other means if the start-up inhibit is deactivated by setting S\_StartReset = SAFETRUE.   **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

Resetting the function block by means of a positive signal edge at the Reset input can cause the S\_AOPD\_Out output to switch to SAFETRUE immediately (depending on the status of the other inputs).

| WARNING | |
| --- | --- |
|  | **UNINTENDED START-UP**   * Include in your risk analysis the impact of the reset by means of a positive signal edge at the Reset input. * Make certain that appropriate procedures and measures (according to applicable sector standards) have been established to help avoid hazardous situations when resetting. * Do not enter the zone of operation when resetting. * Ensure that no other persons can access the zone of operation when resetting. * Use appropriate safety interlocks where personnel and/or equipment hazards exist.   **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

## Function block outputs

| Name | Short description | Value |
| --- | --- | --- |
| [Ready](ready_MutingSeq.html#ready_MutingSeq) | Output for signaling "Function block activated / not activated".  Data type: BOOL | * **FALSE**: Function block is not activated (Activate = FALSE) and all outputs of the function block are switched to FALSE/SAFEFALSE. * **TRUE**: Function block is activated (Activate = TRUE) and the output parameters represent the state of the safety-related function. |
| [S\_AOPD\_Out](out_MutingSeq.html#out_MutingSeq) | Output for enable signal of the function block.  Data type: SAFEBOOL | * **SAFEFALSE**:  + The [muting operation](function_MutingSeq.html#function_MutingSeq__MutingSeqVorgang) is not active and the light grid detects an object   + **or** the muting operation is active and the function block detects an error   + **or** the function block is not activated   + **or** the start-up inhibit is active. * **SAFETRUE**:    + The muting operation is not active and the light grid does not detect an object   + **or** the muting operation is active and the function block does not detect an error. |
| [S\_MutingActive](m_act_MutingSeq.html#m_act_MutingSeq) | Output for the status of the muting operation.  Data type: SAFEBOOL | * **SAFEFALSE**:    + The muting operation is not active   + **or** the function block is not activated   + **or** the start-up inhibit is active   + **or** an error message is present. * **SAFETRUE**:    + The muting operation is active   + **and** the function block is activated   + **and** the start-up inhibit is not active   + **and** no error message is present. |
| [Error](err_MutingSeq.html#err_MutingSeq) | Output for error message.  Data type: BOOL | * **FALSE**: No error is present. * **TRUE**: The function block has detected an error. The S\_AOPD\_Out output switches to SAFEFALSE as a result. |
| [DiagCode](diag_MutingSeq.html#diag_MutingSeq) | Output for diagnostic message.  Data type: WORD | Diagnostic message of the function block.  The possible values are listed and described in the topic "[Diagnostic codes](codes_MutingSeq.html#codes_MutingSeq)". |

## Signal sequence diagram

The signal sequence diagram shown below illustrates a muting operation (sequential muting with four sensors), using the example of an assembly conveyor that open into a zone of operation with a running machine (as represented in the graphic at the beginning of this topic).

The material flow direction of the conveyor is from left to right, i.e., both of the muting sensors connected to the function block inputs MutingSwitch11 and MutingSwitch12 are positioned one after another and on the same conveyor side **before** the safety-related equipment. The sensors connected to the function block inputs MutingSwitch21 and MutingSwitch22 are positioned **behind** the safety-related equipment (also sequential on the same side of the conveyor). This is represented in the graphic at the beginning of this topic.

Additional assumptions:

* **S\_StartReset = SAFEFALSE:** Start-up inhibit after the function block has been activated and the Safety Logic Controller has started up.
* **MutingEnable = TRUE (constant):** No separate enable signal required for the muting operation.

**NOTE:**

The other [signal sequence diagram](signaldiagrams_MutingSeq.html#signaldiagrams_MutingSeq) can be taken into account.

**NOTE:**

The signal sequence diagrams in this documentation possibly omit particular diagnostic codes. For example, a diagnostic code is possibly not shown if the related function block state is a temporary transition state and only active for one cycle of the Safety Logic Controller.

Only typical input signal combinations are illustrated. Other signal combinations are possible.

![](images/PROG_MutingSeq_Signal.png)

|  |  |
| --- | --- |
| 0 | The function block is not yet activated (Activate = FALSE).  As a result, all outputs are FALSE or SAFEFALSE. |
| 1 | After the function block has been activated by Activate = TRUE, the start-up inhibit is active at first. The S\_AOPD\_Out output therefore first remains SAFEFALSE. |
| 2 | A positive signal edge at the Reset input resets the start-up inhibit.  The S\_AOPD\_Out output switches to SAFETRUE immediately (normal operation) because  1. the muting lamp reports its operational readiness through a SAFETRUE signal at the S\_MutingLamp input and 2. the light grid does not detect an object either (input S\_AOPD\_In = SAFETRUE). |
| 3 | The first muting sensor of the first sequential sensor pair (**before** the safety-related equipment) at input MutingSwitch11 detects an object and switches to TRUE.  The time measurement for the overall muting duration starts after this state change at MutingSwitch11. The maximum permissible period is specified at MaxMutingTime. |
| 4 | The second muting sensor of the first sequential sensor pair also detects the object (the MutingSwitch12 input switches to TRUE).  This meets the requirements for a valid muting sequence. The object is identified as permissible and the S\_MutingActive output switches to SAFETRUE as a result: **Muting is active**. |
| 5 | The object reaches the light grid: the S\_AOPD\_In input switches to SAFEFALSE ("light grid interrupted").  As muting is active (MutingSwitch11 and MutingSwitch12 are still TRUE), the machine may continue to run in the zone of operation: The S\_AOPD\_Out output remains SAFETRUE. |
| 6 | The object reaches the first muting sensor of the second sequential sensor pair (**behind** the safety-related equipment): the MutingSwitch21 input switches to TRUE.  The muting sequence is valid because both muting sensors of the first sensor pair are still TRUE. As a result, outputs S\_AOPD\_Out and S\_MutingActive both remain SAFETRUE. The time measurement for the overall muting duration (timer MaxMutingTime) continues to run. |
| 7 | The second muting sensor of the second sequential sensor pair also detects the object (the MutingSwitch22 input switches to TRUE).  As TRUE signals are still also present at MutingSwitch11 and MutingSwitch12 and MutingSwitch21, the requirements for a valid muting sequence are met and muting remains active: S\_AOPD\_Out and S\_MutingActive both remain SAFETRUE and timer MaxMutingTime continues to run. |
| 8 | The object leaves the detection area of the first muting sensor **before** the safety-related equipment: The MutingSwitch11 input switches from TRUE to FALSE.  This meets the requirements of a valid muting sequence, i.e., muting remains active. As a result, outputs S\_AOPD\_Out and S\_MutingActive both remain SAFETRUE. The time measurement for the overall muting duration (timer MaxMutingTime) continues to run. |
| 9 | The object leaves the detection area of the second muting sensor **before** the safety-related equipment: The MutingSwitch12 input switches from TRUE to FALSE.  This meets the requirements of a valid muting sequence, i.e., muting remains active. As a result, outputs S\_AOPD\_Out and S\_MutingActive both remain SAFETRUE. The time measurement for the overall muting duration (timer MaxMutingTime) continues to run. |
| 10 | The object has passed the light grid (S\_AOPD\_In switches back to SAFETRUE). MutingSwitch21 and MutingSwitch22 are still TRUE.  This meets the requirements of a valid muting sequence, i.e., muting remains active. As a result, outputs S\_AOPD\_Out and S\_MutingActive both remain SAFETRUE. The time measurement for the overall muting duration (timer MaxMutingTime) continues to run. |
| 11 | The object moves out of the detection area of the first muting sensor **behind** the safety-related equipment and toward the zone of operation: The MutingSwitch21 input switches to FALSE.  If MutingSwitch21 switches to FALSE within the time set at MaxMutingTime, the muting operation has been completed successfully. S\_MutingActive becomes SAFEFALSE and output S\_AOPD\_Out remains SAFETRUE.  As the safety-related equipment has not detected an object **and** the muting operation has been completed within the specified time set at MaxMutingTime **and** the state change at MutingSwitch21 meets the requirements of a valid muting sequence, no error is reported (Error remains FALSE) and the S\_AOPD\_Out output remains SAFETRUE ("machine continues to run"). |
| 12 | The MutingSwitch22 input also switches to FALSE and the safety-related equipment does not detect an object. The S\_AOPD\_Out output remains SAFETRUE as this conforms to a valid muting sequence. The muting operation is, therefore, completed successfully. |

## Application example

The graphic below illustrates the connection of four muting sensors (B2, B3, B4, and B5) to the SF\_MutingSeq function block. The muting sensors are arranged as two sequential sensor pairs with all sensors aligned identically and installed on the same side of the conveyor.

The material flow direction of the conveyor is from left to right, i.e., the muting sensor pair MutingSwitch11/MutingSwitch12 is positioned **before** the safety-related equipment and MutingSwitch21/MutingSwitch22 is **behind** the safety-related equipment (as represented in the graphic at the beginning of this topic).

**Further Information:**

The [description and notes for this application example](applicationexample_MutingSeq.html#applicationexample_MutingSeq) can be taken into account.

**NOTE:**

The S\_AOPD\_Out enable output of the SF\_MutingSeq function block is connected to an output terminal of the application via a global I/O variable or via other safety-related functions/function blocks.

![](images/PROG_MutingSeq_ApplicationExample.p.png)

|  |  |
| --- | --- |
| B1 | Two-channel light grid (B1S = optoelectronic transmitter, B1E = optoelectronic receiver) |
| B2, B3 | Optoelectronic muting sensors (first sequential sensor pair), each single-channel, positioned **before** the light grid |
| B4, B5 | Optoelectronic muting sensors (second sequential sensor pair), each single-channel, positioned **behind** the light grid |
| P1 | Muting lamp with single-channel feedback signal, monitored by safety logic |
| S1 | Reset button (single-channel) to reset function block errors and to remove the start-up inhibit |
|  | See note above the illustration. |

## Detailed information

Additional information is available in the following sections:

* [Functional description](function_MutingSeq.html#function_MutingSeq)
* [Additional signal sequence diagram](signaldiagrams_MutingSeq.html#signaldiagrams_MutingSeq)
* [Further details of the application example](applicationexample_MutingSeq.html#applicationexample_MutingSeq)
* [Exception avoidance](faultavoidance_MutingSeq.html#faultavoidance_MutingSeq)
* [Implementation of safety requirements from applicable standards](safetyrequirements_MutingSeq.html#safetyrequirements_MutingSeq)

EIO0000002269.01

© 2020

Schneider Electric.

All rights reserved.