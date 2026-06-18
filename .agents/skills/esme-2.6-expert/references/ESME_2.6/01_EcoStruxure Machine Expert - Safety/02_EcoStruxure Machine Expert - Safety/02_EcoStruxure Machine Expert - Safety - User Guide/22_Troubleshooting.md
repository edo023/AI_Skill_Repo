# Troubleshooting

This topic lists some potential issues which may occur while you are working with Machine Expert – Safety. For each potential issue, the corrective action is described. The descriptions are divided into several categories according to the programming system part reporting the potential issue:

* [General](ProblemsSolutionsFAQs.html#ProblemsSolutionsFAQs__General) (affecting the operation of the whole programming system)
* [FBD/LD code editor and variables editor](ProblemsSolutionsFAQs.html#ProblemsSolutionsFAQs__Editors)
* [Project tree](ProblemsSolutionsFAQs.html#ProblemsSolutionsFAQs__ProjectTree)
* [Device parameterization editor](ProblemsSolutionsFAQs.html#ProblemsSolutionsFAQs__DevParamEditor)
* [Compiler](ProblemsSolutionsFAQs.html#ProblemsSolutionsFAQs__Compiler)
* [Online communication](ProblemsSolutionsFAQs.html#ProblemsSolutionsFAQs__OnlineCommunication) between Machine Expert – Safety and Safety Logic Controller
* [Messages of the Safety Logic Controller](ProblemsSolutionsFAQs.html#ProblemsSolutionsFAQs__MessagesOfSafePLC)

## General

|  |  |
| --- | --- |
| *Issue* | While launching Machine Expert – Safety, the installation check routine detects a corrupt system file. A corresponding message box is displayed. |
| **Solution** | Uninstall Machine Expert – Safety and then start the setup program again to reinstall the software. |

|  |  |
| --- | --- |
| *Issue* | The operating system check routine detects that it is tried to run Machine Expert – Safety under an unsupported operating system. |
| **Solution** | Install an operating system which is supported by Machine Expert – Safety or ask your local Schneider Electric representative whether a later Machine Expert – Safety version is available supporting the operating system you are using. |

|  |  |
| --- | --- |
| *Issue* | An error occurs (accompanied by an appropriate message) which cannot be removed by performing the measures described in this topic. |
| **Solution** | Contact your local Schneider Electric representative. |

|  |  |
| --- | --- |
| *Issue* | Machine Expert – Safety or one of its functions does not react or cannot be operated as described in the user manual or online help. |
| **Solution** | Contact your local Schneider Electric representative. |

[Back to top](ProblemsSolutionsFAQs.html#ProblemsSolutionsFAQs)

## FBD/LD code editor and variables editor

|  |  |
| --- | --- |
| *Issue* | A worksheet could not be loaded due to a checksum error. The editor displays a message box. |
| **Solution** | The affected POU is corrupted and has to be deleted. In case of the 'Main' POU (which cannot be deleted), the entire project can no longer be used. |

|  |  |
| --- | --- |
| *Issue* | The editor shows an unexpected reaction when inserting an object or item. (Example: You have inserted a coil but a contact is visible.) This may result from an incorrect user operation, an intermittent error, or a systematic error. |
| **Solution** | Undo the last operation (by pressing <Ctrl> + <Z>) and then redo the operation.  If the result is still incorrect, contact your local Schneider Electric representative. |

|  |  |
| --- | --- |
| *Issue* | The editor reports a data corruption, an intermittent error, or a systematic error. |
| **Solution** | Contact your local Schneider Electric representative.  The worksheet is closed automatically without giving you the possibility of saving the modifications you have made last. |

|  |  |
| --- | --- |
| *Issue* | The global variables worksheet could not be opened due to a checksum error. The editor shows a corresponding message box. |
| **Solution** | The project can no longer be used because the variables worksheet for global declarations cannot be deleted. |

[Back to top](ProblemsSolutionsFAQs.html#ProblemsSolutionsFAQs)

## Project tree

|  |  |
| --- | --- |
| *Issue* | After copying a POU in the project tree, the POU does not contain the expected code or variables worksheet. |
| **Solution** | Delete the copy of the erroneous POU and try to copy again.  If the issue still exists, contact your local Schneider Electric representative. |

[Back to top](ProblemsSolutionsFAQs.html#ProblemsSolutionsFAQs)

## Device parameterization editor

|  |  |
| --- | --- |
| *Issue* | Data could not be loaded in the device parameterization editor due to a checksum error. The editor shows a corresponding message box. |
| **Solution** | The project can no longer be used because the device parameterization data cannot be deleted. |

|  |  |
| --- | --- |
| *Issue* | The device parameterization editor shows an unexpected reaction when editing parameter data. (Example: You have entered '3' but '4' is visible.) This may result from an incorrect user operation, an intermittent error, or a systematic error. |
| **Solution** | Undo the last operation (by pressing <Ctrl> + <Z>) and then redo the operation.  If the result is still incorrect, contact your local Schneider Electric representative. |

|  |  |
| --- | --- |
| *Issue* | The editor reports a data corruption, an intermittent error, or a systematic error. |
| **Solution** | The worksheet is closed automatically without giving you the possibility of saving the modifications you have made last. |

[Back to top](ProblemsSolutionsFAQs.html#ProblemsSolutionsFAQs)

## Compiler

|  |  |
| --- | --- |
| *Issue* | A worksheet cannot be read by the compiler due to an unsuccessful CRC check. The message window displays a corresponding error message. |
| **Solution** | The affected POU is corrupted and has to be deleted. In case of the 'Main' POU (which cannot be deleted), the entire project can no longer be used. |

|  |  |
| --- | --- |
| *Issue* | The second compiler detects an error in the project structure and displays a corresponding error message in the message window. |
| **Solution** | Contact your local Schneider Electric representative. |

|  |  |
| --- | --- |
| *Issue* | A compiler detects a syntactic or semantic error in the user program and displays a corresponding error message in the message window. |
| **Solution** | Open the suspected worksheet and correct the error. Worksheets containing an error can directly be accessed from the message window by double-clicking on the error message. The error position (object/item) is automatically marked in the worksheet. |

|  |  |
| --- | --- |
| *Issue* | A compiler writes an error message into the message window the cause of which you cannot remove (for example 'Internal error'). |
| **Solution** | Try to recompile the project.  If the error is reported again, contact your local Schneider Electric representative. |

[Back to top](ProblemsSolutionsFAQs.html#ProblemsSolutionsFAQs)

## Online communication between Machine Expert – Safety and Safety Logic Controller

|  |  |
| --- | --- |
| *Issue* | An error occurred while downloading the project to the Safety Logic Controller or it is not possible to establish a connection to the Safety Logic Controller at all.  In both cases an error message box is displayed. |
| **Solution** | Verify the following settings and correct as necessary:   * [Communication parameters](dialogcommunicationparameters.html#dialogcommunicationparameters) in Machine Expert – Safety  ('Online > TCPIP Communication settings ...') * Configuration of the IP address * Configuration of the Sercos addresses * Configuration of the Ethernet and firewall settings on the standard controller  **Further Information:**  Refer to the M262 Programming Guide, chapter "Ethernet Services" for information on IP forwarding settings.  For PacDrive refer to the User Guide "How to Configure the Firewall for PacDrive LMC Controllers".  The CommonToolbox Library Guide provides information on related application functions. * Correct firmware of the SLC * Correct SLC device/generation selected in the Machine Expert project (parameter 'SafeLogicType'). * Configuration of the safety-related device parameters ('Devices' window in Machine Expert – Safety) * Wiring of the system. If required, replace the LAN cable or use another port of the PC. * System readiness for operation  If the connection is valid, the status bar in Machine Expert – Safety appears green.  If all the above points are correct, but still no connection can be established, please contact your your local Schneider Electric representative. |

|  |  |
| --- | --- |
| *Issue* | After a successful project download, Machine Expert – Safety detects that the checksum of the project stored on the Safety Logic Controller does not match the checksum of the project on the PC. A corresponding message box is displayed. |
| **Solution** |  |

[Back to top](ProblemsSolutionsFAQs.html#ProblemsSolutionsFAQs)

## Messages of the Safety Logic Controller

|  |  |
| --- | --- |
| *Issue* | The Safety Logic Controller reports an error while compiling the program of the 1st compiler (the program of the 2nd compiler has already been compiled fully on the PC). |
| **Solution** | Contact your local Schneider Electric representative. |

|  |  |
| --- | --- |
| *Issue* | The Safety Logic Controller reports an internal error. |
| **Solution** | Contact your local Schneider Electric representative. |

[Back to top](ProblemsSolutionsFAQs.html#ProblemsSolutionsFAQs)

EIO0000002147.09