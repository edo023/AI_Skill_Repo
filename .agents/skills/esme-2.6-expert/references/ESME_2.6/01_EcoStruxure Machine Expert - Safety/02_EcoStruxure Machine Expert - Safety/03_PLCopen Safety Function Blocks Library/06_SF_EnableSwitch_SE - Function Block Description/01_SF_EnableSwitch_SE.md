# SF\_EnableSwitch\_SE

The following description is valid for the function block SF\_EnableSwitch\_SE\_V1\_0z, Version 1.0z (where z = 0 to 9).

## Short description

|  |  |
| --- | --- |
| The safety-related SF\_EnableSwitch\_SE function block evaluates the signals of a manually actuated three-stage enable switch (in accordance with EN 60204) in order to identify its switching stage and direction.  The connected enable switch can be used to remove safeguarding, provided that the appropriate operating mode (e.g., limitation of the speed or range of motion) is selected and active.  A restart inhibit can be specified via S\_AutoReset. |  |

The SF\_EnableSwitch\_SE function block supports the Schneider Electric enable switch types "Preventa XY2 XY2AU1" and "Preventa XY2 XY2AU2". The function block evaluates 3 input signals (while the PLCopen SF\_EnableSwitch function block evaluates two input signals). The function block additionally monitors signal equivalence at its inputs S\_EnableSwitchCh1 and S\_EnableSwitchCh3.

**Further Information:**

For details and technical specification of the Preventa enable switches refer to the respective Instruction Sheet.

## Connection and switching diagram

Connect the signals of the enable switch connected to the Safety Logic Controller to the inputs of the safety-related SF\_EnableSwitch\_SE function block as follows:

![](images/EnableSwitch_SE_HowToConnect.png)

|  |  |
| --- | --- |
|  | Pressure point |
|  | Forcibly guided contacts  (The auxiliary contact of the enable switch type "Preventa XY2 XY2AU2" is not considered in the figure.) |

Connect the signal from N/O contact E1 of the enable switch to function block input S\_EnableSwitchCh1. Connect the signal from N/C contact E3 to function block input S\_EnableSwitchCh2 and the signal from N/O contact E2 to input S\_EnableSwitchCh3.

Note that the function block monitors signal equivalence at its inputs S\_EnableSwitchCh1 and S\_EnableSwitchCh3. Therefore the same contact type must be connected to these inputs.

By means of the defined signal sequence of the contacts, the safety-related function block can detect the switching stage and the switching direction of the enable switch (switching stage 0 => switching stage 1/switching stage 2 => switching stage 0).

The switching sequence of the Schneider Electric enable switch types "Preventa XY2 XY2AU1" and "Preventa XY2 XY2AU2" is shown in the figure below. This sequence results in the signals also shown in the graphic at function block inputs S\_EnableSwitchCh1, S\_EnableSwitchCh2 and S\_EnableSwitchCh3.

![](images/Requirements_EnableSwitch_SE.png)

**NOTE:**

The error state of the function block can only be exited if the cause of the error no longer exists. To leave the error state, release the enable switch to move it to switching stage 0. If a restart inhibit has been set with S\_AutoReset = SAFEFALSE, it must then be removed by pressing the reset button.

## Filter times of the input channels

If the parameterized filter time values FilterOn and FilterOff for the three input channels of the safety-related digital input module are too short, the function block may miss switching operations of the enable switch device. The function block then detects a plausibility error and enters the error state C030. (Refer to the topic ["Diagnostic Codes"](codes_EnableSwitch_SE.html#codes_EnableSwitch_SE) for details.)

Proceed as follows to set the FilterOn and FilterOff values:

1. In EcoStruxure Machine Expert - Safety, open the Bus Navigator and select the digital input module involved in the Devices tree on the left. The parameters are visible and can be edited in the grids on the right.
2. Locate the parameter group if each digital input channel involved and set suitable values for the parameters FilterOff and FilterOn.

   A practical value for the supported switch types Preventa XY2 XY2AU1 and XY2 XY2AU2 is 50 ms.

For detailed information, refer to the Safety Modules Parameters guide and open the corresponding chapter of the module used.

The set filter time for the input channels may have an impact on the safety response time of your application.

| WARNING | |
| --- | --- |
|  | **NON-CONFORMANCE TO SAFETY FUNCTION REQUIREMENTS**   * Verify that the time value set at the input channel parameters FilterOn and FilterOff corresponds to your risk analysis. * Be sure that your risk analysis includes an evaluation for incorrectly setting the time value at the FilterOn and FilterOff parameters. * Validate the overall safety-related function with regard to the set FilterOn and FilterOff values and thoroughly test the application.   **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

## Function block inputs

Click the corresponding hyperlinks to obtain detailed information on the items below.

| Name | Short description | Value |
| --- | --- | --- |
| [Activate](act_EnableSwitch_SE.html#act_EnableSwitch_SE) | State-controlled input for activating the function block.  Data type: BOOL  Initial value: FALSE | * **FALSE**: Function block inactive * **TRUE**: Function block activated |
| [S\_SafetyActive](s_act_EnableSwitch_SE.html#s_act_EnableSwitch_SE) | State-controlled signal input for setting the selected operating mode to active (feedback signal, e.g., from safety-related SF\_ModeSelector function block).  Data type: SAFEBOOL  Initial value: SAFEFALSE | * **SAFEFALSE**: The selected operating mode is **not** active. The S\_EnableSwitchOut output remains SAFEFALSE, irrespective of the other inputs. * **SAFETRUE**: The selected operating mode is active. |
| [S\_EnableSwitchCh1](s123_EnableSwitch_SE.html#s123_EnableSwitch_SE) | Input for the signal from N/O contact E1 of the connected enable switch.  Data type: SAFEBOOL  Initial value: SAFEFALSE  The function block monitors equivalence of this input with input S\_EnableSwitchCh3. The allowed discrepancy time is set at input DiscrepancyTimeCh1\_Ch3. | Possible values are: SAFETRUE or SAFEFALSE, depending on the switching stage (see [diagram](sfenableswitch_se.html#sfenableswitch_se__EnableSwitch_Diagrams)). |
| [S\_EnableSwitchCh2](s123_EnableSwitch_SE.html#s123_EnableSwitch_SE) | Input for the signal from N/C contact E3 of the connected enable switch.  Data type: SAFEBOOL  Initial value: SAFEFALSE | Possible values are: SAFETRUE or SAFEFALSE, depending on the switching stage (see [diagram](sfenableswitch_se.html#sfenableswitch_se__EnableSwitch_Diagrams)). |
| [S\_EnableSwitchCh3](s123_EnableSwitch_SE.html#s123_EnableSwitch_SE) | Input for the signal from N/O contact E2 of the connected enable switch.  Data type: SAFEBOOL  Initial value: SAFEFALSE  The function block monitors equivalence of this input with input S\_EnableSwitchCh1. The allowed discrepancy time is set at input DiscrepancyTimeCh1\_Ch3. | Possible values are: SAFETRUE or SAFEFALSE, depending on the switching stage (see [diagram](sfenableswitch_se.html#sfenableswitch_se__EnableSwitch_Diagrams)). |
| [DiscrepancyTimeCh1\_Ch3](DiscrepancyTime_EnableSwitch_SE.html#DiscrepancyTime_EnableSwitch_SE) | Input for specifying the maximum permissible discrepancy time in milliseconds. During this discrepancy time, the signals at S\_EnableSwitchCh1 and S\_EnableSwitchCh3 may be different. However, after the discrepancy time has elapsed, the inputs must be equal to each other or an error is detected (output Error = TRUE, output S\_EnableSwitchOut = SAFEFALSE).  Data type: TIME  Initial value: #0ms | Enter a time value according to your risk analysis.  Refer to the third hazard message below this table. |
| [S\_AutoReset](prog_a_res_EnableSwitch_SE.html#prog_a_res_EnableSwitch_SE) | State-controlled input for specifying the restart inhibit after the connected enable switch has applied a valid signal sequence/combination at inputs S\_EnableSwitchCh1, S\_EnableSwitchCh2 and S\_EnableSwitchCh3.  An active restart inhibit must be removed manually by a positive signal edge at the Reset input. A deactivated restart inhibit causes the S\_EnableSwitchOut output to switch to SAFETRUE automatically when the function block is activated and the safety-related function is no longer requested.  Refer to the first hazard message below this table.  Data type: SAFEBOOL  Initial value: SAFEFALSE | * **SAFEFALSE**: With restart inhibit * **SAFETRUE**: Without restart inhibit |
| [Reset](reset_EnableSwitch_SE.html#reset_EnableSwitch_SE) | Edge-triggered input for the reset signal:  * Resetting error messages when the cause of the error is no longer present. * Manual resetting of an active restart inhibit (specified by S\_AutoReset).  Refer to the second hazard message below this table.  Data type: BOOL  Initial value: FALSE  **NOTE:**  Resetting does not occur with a negative (falling) edge, as specified by the EN ISO 13849-1 standard, but with a positive (rising) edge. | * **FALSE**: Reset is not requested. * Edge **FALSE > TRUE**: Reset is requested. |

| WARNING | |
| --- | --- |
|  | **NON-CONFORMANCE TO SAFETY FUNCTION REQUIREMENTS**   * Be sure that your risk analysis includes an evaluation if the restart inhibit is deactivated (S\_AutoReset = SAFETRUE). * Observe the regulations given by relevant sector standards regarding the restart inhibit. * Verify that a suitable start-up inhibit is in place at another location or using other means if the restart inhibit is deactivated by setting S\_AutoReset = SAFETRUE.   **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

Resetting the function block by means of a positive signal edge at the Reset input can cause the S\_EnableSwitchOut output to switch to SAFETRUE immediately (depending on the status of the other inputs).

| WARNING | |
| --- | --- |
|  | **UNINTENDED START-UP**   * Include in your risk analysis the impact of the reset by means of a positive signal edge at the Reset input. * Make certain that appropriate procedures and measures (according to applicable sector standards) have been established to help avoid hazardous situations when resetting. * Do not enter the zone of operation when resetting. * Ensure that no other persons can access the zone of operation when resetting. * Use appropriate safety interlocks where personnel and/or equipment hazards exist.   **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

| WARNING | |
| --- | --- |
|  | **NON-CONFORMANCE TO SAFETY FUNCTION REQUIREMENTS**   * Verify that the time value set at DiscrepancyTimeCh1\_Ch3 corresponds to your risk analysis. * Be sure that your risk analysis includes an evaluation for incorrectly setting the time value at the DiscrepancyTimeCh1\_Ch3 parameter. * Validate the overall safety-related function with regard to the set DiscrepancyTimeCh1\_Ch3 value and thoroughly test the application.   **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

## Function block outputs

Click the corresponding hyperlinks to obtain detailed information on the items below.

| Name | Short description | Value |
| --- | --- | --- |
| [Ready](ready_EnableSwitch_SE.html#ready_EnableSwitch_SE) | Output for signaling "Function block activated/not activated".  Data type: BOOL | * **TRUE**: Function block is activated (Activate = TRUE) and the output parameters represent the state of the safety-related function. * **FALSE**: Function block is not activated (Activate = FALSE) and all outputs of the function block are switched to FALSE. |
| [S\_EnableSwitchOut](out_EnableSwitch_SE.html#out_EnableSwitch_SE) | Output for enable signal of the function block.  Data type: SAFEBOOL | * **SAFEFALSE**: **No** enable for removing safeguarding.    + The enable switch is not in switching stage 1   + or the function block is not activated   + or an error message is present   + or the operating mode is not active (S\_SafetyActive = SAFEFALSE)   + or a restart inhibit is active. * **SAFETRUE**: Enable for removing safeguarding.    + The enable switch is in switching stage 1   + and the function block is activated   + and no error message is present   + and the operating mode is active (S\_SafetyActive = SAFETRUE)   + and the restart inhibit is not active. |
| [SafetyDemand](s_dem_ENABLESWITCH_SE.html#s_dem_ENABLESWITCH_SE) | Output for signaling "safety-related function requested".  This output displays whether the safety chain is interrupted and as a result, the attention of the operator is required.  Data type: BOOL | * **FALSE**: Safety-related function is not requested.  * **TRUE**: The safety-related function is requested (enable switch is in switching stage 2), or the function block is in one of the following diagnostic states: 8802, 8812, 8822, or 8832.  Refer to the topic ["Diagnostic codes"](codes_EnableSwitch_SE.html#codes_EnableSwitch_SE) for details about these states as well as the FB/environmental conditions. |
| [ResetRequest](r_req_ENABLESWITCH_SE.html#r_req_ENABLESWITCH_SE) | Output for signaling "reset is required".  This output indicates whether a reset by the operator is required.  Data type: BOOL | * **FALSE**: No reset required.  * **TRUE**: A reset is required:    + to remove the active restart inhibit   + **or** to reset an error.  This is the case if the function block is in one of the following diagnostic states: 8422, C420, C440, or C450. |
| [Error](err_EnableSwitch_SE.html#err_EnableSwitch_SE) | Output for error message.  Data type: BOOL  Refer to the hazard message below this table. | * **FALSE**: No error is present. * **TRUE**: The function block has detected an error. The S\_EnableSwitchOut output switches to SAFEFALSE as a result. |
| [DiagCode](diag_EnableSwitch_SE.html#diag_EnableSwitch_SE) | Output for diagnostic message.  Data type: WORD | Diagnostic message of the function block.  The possible values are listed and described in the topic "[Diagnostic codes](codes_EnableSwitch_SE.html#codes_EnableSwitch_SE)". |

If you have not activated a restart inhibit (S\_AutoReset = SAFETRUE), a manual reset does not have to be performed following error removal. In such cases, the error message is confirmed automatically once the error is removed.

| WARNING | |
| --- | --- |
|  | **UNINTENDED START-UP**   * Include in your risk analysis the impact of removing the cause of an error with regard to the automatic reset and restart of the machine if the restart inhibit is deactivated (S\_AutoReset = SAFETRUE). * Make certain that appropriate procedures and measures (according to applicable sector standards) have been established to help avoid hazardous situations when removing the source of an error if the restart inhibit is deactivated. * Do not enter the zone of operation when removing an error under this condition. * Ensure that no other persons can access the zone of operation when removing an error under this condition. * Use appropriate safety interlocks where personnel and/or equipment hazards exist.   **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

## Signal sequence diagram

This diagram shows the signal curve for a typical application with a set restart inhibit after an invalid signal sequence/combination (S\_AutoReset = SAFEFALSE).

**NOTE:**

The signal sequence diagrams in this documentation possibly omit particular diagnostic codes. For example, a diagnostic code is possibly not shown if the related function block state is a temporary transition state and only active for one cycle of the Safety Logic Controller.

Only typical input signal combinations are illustrated. Other signal combinations are possible.

![](images/EnableSwitch_SE_Signal1.png)

|  |  |
| --- | --- |
| 0 | The function block is not yet activated (Activate = FALSE).  As a result, all outputs are FALSE or SAFEFALSE. |
| 1 | The function block is activated (Activate = TRUE). Switching stage 0 (S0 in the figure) is present (input S\_EnableSwitchCh1 and S\_EnableSwitchCh3 = SAFEFALSE, input S\_EnableSwitchCh2 = SAFETRUE). The operating mode is not active (S\_SafetyActive = SAFEFALSE). The S\_EnableSwitchOut output remains in the defined safe state (SAFEFALSE). |
| 2 | The operating mode is signaled via the feedback signal S\_SafetyActive = SAFETRUE. |
| 3 | Change from switching stage 0 to switching stage 1 (S1 in the figure): S\_EnableSwitchCh1 switches to SAFETRUE and S\_EnableSwitchCh2 becomes SAFEFALSE. S\_EnableSwitchCh3 follows S\_EnableSwitchCh1 within the time period set at DiscrepancyTimeCh1\_Ch3. All relevant conditions are fulfilled, S\_EnableSwitchOut output becomes SAFETRUE. |
| 4 | Change from switching stage 1 back to switching stage 0: S\_EnableSwitchCh1 becomes SAFEFALSE, S\_EnableSwitchCh2 becomes SAFETRUE and S\_EnableSwitchCh3 follows S\_EnableSwitchCh1 within the time period set at DiscrepancyTimeCh1\_Ch3.  As a result the S\_EnableSwitchOut output becomes SAFEFALSE. |
| 5 | Change from switching stage 0 to switching stage 1: S\_EnableSwitchCh1 switches to SAFETRUE and S\_EnableSwitchCh2 becomes SAFEFALSE. S\_EnableSwitchCh3 follows S\_EnableSwitchCh1 within the time period set at DiscrepancyTimeCh1\_Ch3. However, as the operating mode is no longer active (S\_SafetyActive = SAFEFALSE), the S\_EnableSwitchOut output remains SAFEFALSE. |
| 6 | The operating mode is now active again and the function block initially expects switching stage 0. However, as switching stage 1 is present at this time (S\_EnableSwitchCh1 and S\_EnableSwitchCh3 = SAFETRUE and S\_EnableSwitchCh2 = SAFEFALSE), the Error output becomes TRUE.  The positive edge at the Reset input is ignored, as the impermissible switching stage 1 is still present (S\_EnableSwitchCh1 and S\_EnableSwitchCh3 = SAFETRUE and S\_EnableSwitchCh2 = SAFEFALSE). |
| 7 | Change to valid switching stage 0. However, the function block detects a static TRUE signal at the Reset input, so the Error output remains TRUE. |
| 8 | While the valid switching stage 0 is present (S\_EnableSwitchCh1 and S\_EnableSwitchCh3 = SAFEFALSE and S\_EnableSwitchCh2 = SAFETRUE), the static signal disappears from the Reset input. However, the error state (Error = TRUE) then has to be reset by a positive edge at the Reset input. |
| 9 | The positive edge at the Reset input resets the Error output to FALSE and removes the restart inhibit. |
| 10 | Change from switching stage 0 to switching stage 1 (S\_EnableSwitchCh1 switches to SAFETRUE, S\_EnableSwitchCh2 becomes SAFEFALSE, S\_EnableSwitchCh3 follows S\_EnableSwitchCh1 within DiscrepancyTimeCh1\_Ch3), the S\_EnableSwitchOut output becomes SAFETRUE. |
| 11 | Change from switching stage 1 to switching stage 2 (S\_EnableSwitchCh1, S\_EnableSwitchCh2 and S\_EnableSwitchCh3 = SAFEFALSE), the S\_EnableSwitchOut output is SAFEFALSE. |
| 12 | From stage 2 a transition is only possible to stage 0: By releasing the button of the enable switch device, input S\_EnableSwitchCh1 and S\_EnableSwitchCh3 switch to SAFEFALSE (DiscrepancyTimeCh1\_Ch3 is not exceeded) and input S\_EnableSwitchCh2 becomes SAFETRUE. S\_EnableSwitchOut output remains SAFEFALSE. |

**NOTE:**

The other [signal sequence diagram](signaldiagrams_EnableSwitch_SE.html#signaldiagrams_EnableSwitch_SE) can be taken into account.

## Application example

This example illustrates the typical connection of a three-stage enable switch S1 to the safety-related SF\_EnableSwitch\_SE function block. The three signals from the enable switch are connected to input terminals I0, I1 and I2 of the safety-related input device SDI 1.

* The signal from the N/O contact E1 of the enable switch device (input terminal I0 of the safety-related input device SDI 1) is assigned to the global I/O variable SwitchControl1\_In. This global I/O variable is connected to the S\_EnableSwitchCh1 input of the function block for evaluation.
* The signal from the other N/O contact E2 (input terminal I1 of SDI 1) is assigned to the global I/O variable SwitchControl3\_In. This global I/O variable is connected to the S\_EnableSwitchCh3 input of the function block because the function block monitors the signal equivalence of this input with input S\_EnableSwitchCh1.
* The signal of the N/C contact E3 (input terminal I2 of SDI 1) is assigned to the global I/O variable SwitchControl2\_In. This global I/O variable is connected to the S\_EnableSwitchCh2 input of the function block for evaluation.

The function block is perpetually activated by the TRUE constant at the Activate input.

A restart inhibit is set via S\_AutoReset. This inhibit becomes active after a valid signal combination returns at the function block inputs S\_EnableSwitchCh1, S\_EnableSwitchCh2 and S\_EnableSwitchCh3. The Reset button S2 for removing the restart inhibit is connected to input terminal NI0 of the standard input device DI 1.

**NOTE:**

In the example, the enable signal at the S\_EnableSwitchOut output controls the removal of safeguarding. To this end, the S\_EnableSwitchOut enable output is connected to other safety-related function blocks or functions.

![](images/EnableSwitch_SE_ApplicationExample1.png)

|  |  |
| --- | --- |
| S2 | Reset |
|  | See second note above the illustration. |

**Further Information:**

The [second application example](applicationexample_EnableSwitch_SE.html#applicationexample_EnableSwitch_SE) can be taken into account.

## Detailed information

Additional information is available in the following sections

* [Functional description](EnableSwitch_SE_function.html#EnableSwitch_SE_function)
* [Additional signal sequence diagrams](signaldiagrams_EnableSwitch_SE.html#signaldiagrams_EnableSwitch_SE)
* [Additional application example](applicationexample_EnableSwitch_SE.html#applicationexample_EnableSwitch_SE)
* [Exception avoidance](EnableSwitch_SE_faultavoidance.html#EnableSwitch_SE_faultavoidance)
* [Implementation of safety requirements from applicable standards](safetyrequirements.html#safetyrequirements)

EIO0000002371.03

© 2020

Schneider Electric.

All rights reserved.