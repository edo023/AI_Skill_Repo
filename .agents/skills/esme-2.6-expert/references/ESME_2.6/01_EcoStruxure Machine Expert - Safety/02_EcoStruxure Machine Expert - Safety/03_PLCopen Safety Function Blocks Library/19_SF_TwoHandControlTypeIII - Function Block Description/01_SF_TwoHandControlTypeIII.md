# SF\_TwoHandControlTypeIII

The following description is valid for the function block SF\_TwoHandControlTypeIII\_V1\_0z, Version 1.0z (where z = 0 to 9).

## Short description

|  |  |
| --- | --- |
| The safety-related SF\_TwoHandControlTypeIII function block evaluates the switching behavior of a type III two-hand control device connected to the Safety Logic Controller.  This involves evaluating the switching states of both the buttons on the two-hand control device. The S\_TwoHandOut output only becomes SAFETRUE if both inputs switch from SAFEFALSE to SAFETRUE within 500 ms, either simultaneously or consecutively (if both buttons on the two-hand control device are pressed after being not actuated before). |  |

**NOTE:**

The used type III two-hand control device must comply with the requirements set out by EN 574.

**NOTE:**

Unlike the type III two-hand control device described here, evaluation by the type II version takes place without consideration of a specific duration within which both buttons must be actuated.

## Function block inputs

Click the corresponding hyperlinks to obtain detailed information on the items below.

| Name | Short description | Value |
| --- | --- | --- |
| [Activate](act_THC3.html#act_THC3) | State-controlled input for activating the function block.  Data type: BOOL  Initial value: FALSE  **NOTE:**  While function block activation is taking place (with input Activate = TRUE), both inputs must show the SAFEFALSE state. This means that none of the buttons on the two-hand control device must be actuated. Otherwise, the function block detects this as an error (output Error = TRUE). | * **FALSE**: Function block inactive * **TRUE**: Function block activated |
| [S\_Button1](s_12_THC3.html#s_12_THC3) and [S\_Button2](s_12_THC3.html#s_12_THC3) | State-controlled inputs for evaluating the connected two-hand control device.  Data type: SAFEBOOL  Initial value: SAFEFALSE | * **SAFEFALSE**: Button not pressed * **SAFETRUE**: Button is pressed |

## Function block outputs

| Name | Short description | Value |
| --- | --- | --- |
| [Ready](ready_THC3.html#ready_THC3) | Output for signaling "Function block activated/not activated".  Data type: BOOL | * **FALSE**: Function block is not activated (Activate = FALSE) and all outputs of the function block are switched to FALSE/SAFEFALSE. * **TRUE**: Function block is activated (Activate = TRUE) and the output parameters represent the state of the safety-related function. |
| [S\_TwoHandOut](out_THC3.html#out_THC3) | Control signal for stopping (stop request) or starting and maintaining machine operation.  Data type: SAFEBOOL | * **SAFEFALSE**: S\_TwoHandOut switches to SAFEFALSE if  + the function block has not been activated   + **or** the buttons have not been actuated or have been actuated incorrectly (i.e., after 500 ms have elapsed)   + **or** an error has been detected. * **SAFETRUE**: S\_TwoHandOut is SAFETRUE if  + the function block has been activated   + **and** the buttons have been actuated correctly   + **and** no errors have been detected. |
| [Error](err_THC3.html#err_THC3) | Output for error message.  Data type: BOOL | * **FALSE**: No error is present. * **TRUE**: The function block has detected an error:  + During function block activation (with input Activate = TRUE), either one input at least was in the SAFETRUE state   + **or** the time offset when the state of the inputs was switching to SAFETRUE was greater than 500 ms.  The S\_TwoHandOut output switches to SAFEFALSE as a result.  To leave the error state, both inputs S\_Button1 and S\_Button2 must show the SAFEFALSE state. |
| [DiagCode](diag_THC3.html#diag_THC3) | Output for diagnostic message.  Data type: WORD | Diagnostic message of the function block.  The possible values are listed and described in the topic "[Diagnostic codes](codes_THC3.html#codes_THC3)". |

## Signal sequence diagram

This diagram is based on a typical type III two-hand control application.

**NOTE:**

The signal sequence diagrams in this documentation possibly omit particular diagnostic codes. For example, a diagnostic code is possibly not shown if the related function block state is a temporary transition state and only active for one cycle of the Safety Logic Controller.

Only typical input signal combinations are illustrated. Other signal combinations are possible.

![](images/PROG_2HandType3_Signal1.png)

|  |  |
| --- | --- |
| 0 | The function block is not yet activated (Activate = FALSE).  As a result, all outputs are FALSE or SAFEFALSE. |
| 1 | Function block activated by Activate = TRUE. At this point, the two buttons are **not actuated** (S\_Button1 and S\_Button2 = SAFEFALSE). Both inputs must be SAFEFALSE during activation of the function block, so the Error output remains FALSE. |
| 2 | Button 2 (on S\_Button2) is actuated, which starts the monitoring time. Button 1 is also pressed within the required period of 500 ms. When S\_Button1 switches to SAFETRUE, the condition for two-hand control is met and the S\_TwoHandOut output becomes SAFETRUE. |
| 3 | The S\_TwoHandOut output becomes SAFEFALSE, as S\_Button1 and S\_Button2 switch to SAFEFALSE within a short time of each other (buttons are released). |
| 4 | The button on S\_Button1 is now actuated again. The monitoring time begins. |
| 5 | Monitoring time runs without button 2 having been pressed. Therefore, the S\_TwoHandOut output remains in the defined safe state SAFEFALSE and an error is displayed at the Error output as a result of the TRUE status. |
| 6 | Button 1 is released again, which means that the SAFEFALSE state is now present at both inputs. This causes the error message at Error to be reset: Error becomes FALSE. |
| 7 | The function block is deactivated: Activate switches to FALSE.  Button 2 is pressed while the function block is inactive. This change in state does not start the monitoring time, however, as the function block has not been activated. |
| 8 | Function block is activated again (Activate becomes TRUE again). The signal combination at the inputs (S\_Button1 = SAFEFALSE and S\_Button2 = SAFETRUE) at the time when the function block is activated again leads to an error message (Error = TRUE, S\_TwoHandOut = SAFEFALSE). Both inputs must be SAFEFALSE when the function block is being activated. |
| 9 | The error message is "reset", as S\_Button1 and S\_Button2 are now in the SAFEFALSE state (neither button is actuated). |
| 10 | Both buttons are actuated again (within a period of 500 ms), the condition for two-hand control is fulfilled, and S\_TwoHandOut switches to SAFETRUE again. |

## Application example

This example shows the connection of a type III two-hand control device with the safety-related SF\_TwoHandControlTypeIII function block.

Each of the two buttons has both an N/C and an N/O contact and is connected to safety-related input device SDI 1 via a two-channel arrangement.

The two resulting signals monitored for antivalence are each assigned to global I/O variables and connected to the function block inputs S\_Button1 and S\_Button2 for evaluation

**Further Information:**

The [details and notes for this application example](applicationexample_2hand3.html#applicationexample_2hand3) must also be taken into account.

**NOTE:**

The S\_TwoHandOut enable output of the SF\_TwoHandControlTypeIII function block is connected to an output terminal of the application, either directly or via other safety-related functions/function blocks.

Connect the S\_TwoHandOut enable output of the SF\_TwoHandControlTypeIII function block to the S\_OutControl input of the EDM function block, for example, thus implementing a two-channel output connection.

**Further Information:**

For more detailed information, refer to the description of the corresponding safety-related function block.

![](images/PROG_2HandType3_ApplicationExample.png)

|  |  |
| --- | --- |
| S1 | Button 1 |
| S2 | Button 2 |
|  | See note above the illustration. |

## Detailed information

Additional information is available in the following sections:

* [Functional description](function_2hand3.html#function_2hand3)
* [Details of the application example](applicationexample_2hand3.html#applicationexample_2hand3)
* [Exception avoidance](faultavoidance_2hand3.html#faultavoidance_2hand3)
* [Implementation of safety requirements from applicable standards](safetyrequirements_2hand3.html#safetyrequirements_2hand3)

EIO0000002269.01

© 2020

Schneider Electric.

All rights reserved.