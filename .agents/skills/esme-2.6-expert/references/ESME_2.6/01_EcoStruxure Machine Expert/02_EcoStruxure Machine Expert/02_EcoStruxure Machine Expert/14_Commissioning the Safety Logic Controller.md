# Commissioning the Safety Logic Controller

Once you have successfully compiled the project, you can begin with the startup of the Safety Logic Controller application.

Perform the following steps in the listed order:

**Further Information:**

Refer to the [referenced topics in the section "Contents of this Help Chapter"](OnlineGeneral.html#OnlineGeneral__ContentOfCommissioningChapter) for detailed information.

1. Specifiy the Ethernet settings on the standard controller in order to allow the connection between Machine Expert – Safety and the Safety Logic Controller via the Sercos bus.

   **Further Information:**

   Refer to the M262 Programming Guide, chapter "Ethernet Services" for information on IP forwarding settings.

   For PacDrive refer to the User Guide "How to Configure the Firewall for PacDrive LMC Controllers".

   The CommonToolbox Library Guide provides information on related application functions.
2. Establish a communication link between Machine Expert – Safety running on your PC and the Safety Logic Controller:

   * Define the necessary [communication settings](dialogcommunicationparameters.html#dialogcommunicationparameters).
   * Establish the physical connection either directly between the configuration PC and the Safety Logic Controller or via the standard controller.
   * Power up the Safety Logic Controller.
3. As soon as the SLC is scanning the Sercos bus, set the Sercos to phase 2. Use the 'Parameter' editor of the Sercos Master in Machine Expert for that purpose (parameter section 'Phase control' for LMC controllers, section 'SercosPhaseChanger' for M262 controllers).

   **NOTE:**

   * After the startup of the standard controller, the communication connection between the standard controller and SLC is not possible until the Sercos bus has entered phase 2 (device verification phase).
   * The phase-up could result in the PhaseError / 11 (after being once in phase 2) if the SLC has not yet received a safety-related application and its communication parameters are not yet defined. However, the IP addresses have been assigned which was the purpose of the phase-up.

   When establishing the communication connection to the SLC, the system verifies whether the PC was previously connected to the same or a different SLC. This is done by means of the SLC serial number. This helps to avoid connection to an unintended controller. See topic ["Downloading a project (step 2)"](downloadingaproject.html#downloadingaproject) for more information.
4. [Download the project to the Safety Logic Controller](downloadingaproject.html#downloadingaproject).
5. Start the program execution.
6. Perform a function test.

   A proper functional testing of the safety-related application is mandatory and must not be omitted.

   | WARNING | |
   | --- | --- |
   |  | **NON-CONFORMANCE TO SAFETY FUNCTION REQUIREMENTS**  Be sure that the functional testing you perform entirely corresponds to your risk analysis and consider each possible operating mode and scenario the safety-related application should cover.  **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

   When testing and commissioning the system, unintentional system states or incorrect responses must be anticipated.

   | WARNING | |
   | --- | --- |
   |  | **UNINTENDED EQUIPMENT OPERATION**  * Make certain that the functional testing cannot result in hazardous situations for persons or material. * Make certain that requesting the safety function during the functional testing cannot result in hazardous situations for persons or material. * Do not enter the zone of operation while the machine is operating. * Ensure that no other persons can access the zone of operation while the machine is operating. * Observe the regulations given by relevant sector standards while the machine is running in any other operating mode than "operational". * Use appropriate safety interlocks where personnel and/or equipment hazards exist. **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

   To support you in functional testing, Machine Expert – Safety provides the safety-related variable status operation mode. In this mode online values are read cyclically from the Safety Logic Controller and displayed in the editor and the variables worksheets.

   Additionally, Machine Expert – Safety offers debug functions that can be used after switching to the non-safety-related debug mode. This allows you to analyze the behavior of the Safety Logic Controller (i.e., of your safety logic) in the event of a safety request.

   **NOTE:**

   The test of the safety-related application in debug mode must not replace the proper function test using safety-related I/O devices/sensors/actuators under any circumstances. The test in debug mode may only be performed in addition to the standard function test.

   If you detect incorrect behavior or an error in the safety logic during the function test, you must make certain that it will not lead to a hazardous situation. Next, remove the error in the safety logic by reediting the project. Following a successful compilation, start commissioning again.

   **Mandatory assignment validation for the SafeModuleOK data item:**

   The verification/validation of the assignment of each process data item to a global I/O variable is mandatory. By means of this verification, it is ensured that the correct I/O terminals are read/written by the safety-related application. This particularly applies to the SafeModuleOK process data item. This process data item is available for each safety-related module. SafeModuleOK indicates the module status. As the SafeModuleOK data item cannot be influenced, e.g., by switching a module input, the module to be verified must be physically removed from the TM5 bus. As a result, SafeModuleOK switches to SAFEFALSE and the assigned global I/O variable must follow. For further information on the steps to remove and reinsert a module refer to the user manual of the module involved.

   | WARNING | |
   | --- | --- |
   |  | **UNINTENDED EQUIPMENT OPERATION**  * Physically remove each safety-related module from the TM5 bus in order to test for SafeModuleOK. * Verify that the global I/O variable assigned to the SafeModuleOK process data item of the removed safety-related module switches to SAFEFALSE. **Failure to follow these instructions can result in death, serious injury, or equipment damage.** |

## Simulation mode: optional addition to the mandatory function test

Machine Expert – Safety provides a function for simulating the Safety Logic Controller which you can use to test the behavior of the safety logic fully independently of the real hardware. Simulation mode offers an option to force variables, too.

**NOTE:**

The simulation of the safety-related application must not replace the proper function test using the Safety Logic Controller and the safety-related I/O devices/sensors/actuators under any circumstances. The test using the EASYSIM simulation may only be performed in addition to the standard function test.

## Content of this help chapter

In this help chapter, you will learn the necessary information for starting up the safety-related application.

* [Defining the communication settings.](dialogcommunicationparameters.html#dialogcommunicationparameters)
* Possible Safety Logic Controller [states](possibleSafePLCstates.html#possibleSafePLCstates).
* [The Safety Logic Controller operating modes](SafePLC_OperatingModes.html#SafePLC_OperatingModes).

  Depending on the mode (safe and debug) in which the Safety Logic Controller runs, different online operations are possible: displaying the variable status, for example, is possible in both modes. Downloading and debugging is only possible in debug mode.
* [Downloading the project to the Safety Logic Controller](downloadingaproject.html#downloadingaproject).
* Monitoring the Safety Logic Controller operation by [displaying the variable status](DisplayVariableStatus.html#DisplayVariableStatus) (while Safety Logic Controller runs in safe mode or debug mode).
* Usage of the [watch window](watchwindow.html#watchwindow) for displaying online values of variables.
* [Debugging the project](debuggingtheproject.html#debuggingtheproject) by forcing and overwriting variables (if Safety Logic Controller runs in debug mode).
* [Dialogs for controlling the Safety Logic Controller](dialogsforcontrollingthesafePLC.html#dialogsforcontrollingthesafePLC).

EIO0000002147.09