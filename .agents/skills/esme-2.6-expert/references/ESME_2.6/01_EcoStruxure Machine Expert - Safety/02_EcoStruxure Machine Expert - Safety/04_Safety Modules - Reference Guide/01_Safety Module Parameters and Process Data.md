# Safety Module Parameters and Process Data Items

The parameters of the safety-related modules can be set in the safety-related Device Parameterization Editor. This editor is part of the Machine Expert – Safety 'Devices' window.

To edit the parameters of a safety-related module, left-click the respective tree node in the 'Devices' window. Its parameters are then visible in the grid tabs on the right.

**Further Information:**

For further information refer to the "Device Parameterization" topic of the Machine Expert – Safety documentation.

The process data items are listed under the module node in the device tree. These signals can either be read or written by the application (depending on the signal type). When dragging a process data item from the 'Devices' window into the safety-related code, a global variable is created.

**Further Information:**

Also refer to the topic "Connecting/Disconnecting Process Data Items and Global I/O Variables" in the Machine Expert – Safety online help.

**Further Information:**

Refer to the respective device manual for further safety-related information and parameter-/module-specific hazard messages.

**Safety-Related Products of the Safety Logic Controller system**

The Safety Logic Controller system is comprised of the following safety-related products:

**NOTE:**

The safety-related modules can be present for two safety-related system generations: For SLCv1 (SLC types TM5CSLC100FS and TM5CSLC200FS) and for SLCv2 (TM5CSLC300FS and TM5CSLC400FS). The parameters of the device generations differ and are therefore described in separate chapters.

Only the corresponding safety-related modules of the same (firmware) generation can be used with the respective SLC types (since, among other things, the device parameters relevant for the safety response time differ).

| Module Type | Reference |
| --- | --- |
| Safety Logic Controller, SLC 100 Sercos III, 24 VDC | [TM5CSLC100FS(SLCv1)](SoSafeHWModuleParameters_TM5CSLCx00FS.html#SoSafeHWModuleParameters_TM5CSLCx00FS) |
| Safety Logic Controller, SLC 200 Sercos III, 24 VDC | [TM5CSLC200FS(SLCv1)](SoSafeHWModuleParameters_TM5CSLCx00FS.html#SoSafeHWModuleParameters_TM5CSLCx00FS) |
| Safety Logic Controller, SLC 300 Sercos III, 24 VDC | [TM5CSLC300FS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5CSLCx00FS.html#SLCv2_SoSafeHWModuleParameters_TM5CSLCx00FS) |
| Safety Logic Controller, SLC 400 Sercos III, 24 VDC | [TM5CSLC400FS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5CSLCx00FS.html#SLCv2_SoSafeHWModuleParameters_TM5CSLCx00FS) |
| Safety-related Module 2DI 24 VDC | [TM5SDI2DFS (SLCv1)](SoSafeHWModuleParameters_TM5SDI2DFS.html#SoSafeHWModuleParameters_TM5SDI2DFS)  [TM5SDI2DFS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5SDI2DFS.html#SLCv2_SoSafeHWModuleParameters_TM5SDI2DFS) |
| Safety-related Module 4DI 24 VDC | [TM5SDI4DFS (SLCv1)](SoSafeHWModuleParameters_TM5SDI4DFS.html#SoSafeHWModuleParameters_TM5SDI4DFS)  [TM5SDI4DFS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5SDI4DFS.html#SLCv2_SoSafeHWModuleParameters_TM5SDI4DFS) |
| Safety-related Module 20DI 24 VDC | [TM5SDI20DFS (SLCv1)](SoSafeHWModuleParameters_TM5SDI20DFS.html#SoSafeHWModuleParameters_TM5SDI20DFS)  [TM5SDI20DFS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5SDI20DFS.html#SLCv2_SoSafeHWModuleParameters_TM5SDI20DFS) |
| Safety-related Module 2DO 24 VDC, 0.5 A | [TM5SDO2TFS (SLCv1)](SoSafeHWModuleParameters_TM5SDO2TFS.html#SoSafeHWModuleParameters_TM5SDO2TFS)  [TM5SDO2TFS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5SDO2TFS.html#SLCv2_SoSafeHWModuleParameters_TM5SDO2TFS) |
| Safety-related Module 2DO 24 VDC, 2 A | [TM5SDO2TAFS (SLCv1)](SoSafeHWModuleParameters_TM5SDO2TAFS.html#SoSafeHWModuleParameters_TM5SDO2TAFS)  [TM5SDO2TAFS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5SDO2TAFS.html#SLCv2_SoSafeHWModuleParameters_TM5SDO2TAFS) |
| Safety-related Module 2 relay outputs 24 VDC, 6 A | [TM5SDO2DTRFS (SLCv1)](SoSafeHWModuleParameters_TM5SDO2TAFS.html#SoSafeHWModuleParameters_TM5SDO2TAFS)  [TM5SDO2DTRFS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5SDO2TAFS.html#SLCv2_SoSafeHWModuleParameters_TM5SDO2TAFS) |
| Safety-related Module 4DO 24 VDC, 0.5 A | [TM5SDO4TFS (SLCv1)](SoSafeHWModuleParameters_TM5SDO4TFS.html#SoSafeHWModuleParameters_TM5SDO4TFS)  [TM5SDO4TFS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5SDO4TFS.html#SLCv2_SoSafeHWModuleParameters_TM5SDO4TFS) |
| Safety-related Module 4DO 24 VDC, 2 A | [TM5SDO4TAFS (SLCv1)](SoSafeHWModuleParameters_TM5SDO4TAFS.html#SoSafeHWModuleParameters_TM5SDO4TAFS)  [TM5SDO4TAFS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5SDO4TAFS.html#SLCv2_SoSafeHWModuleParameters_TM5SDO4TAFS) |
| Safety-related Module 6DO 24 VDC, 0.2 A | [TM5SDO6TBFS (SLCv1)](SoSafeHWModuleParameters_TM5SDO6TBFS.html#SoSafeHWModuleParameters_TM5SDO6TBFS)  [TM5SDO6TBFS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5SDO6TBFS.html#SLCv2_SoSafeHWModuleParameters_TM5SDO6TBFS) |
| Safety-related Module 2DI (2 pulse output), 2DO 24 VDC, 6 A | [TM5SDM4DTRFS (SLCv1)](SoSafeHWModuleParameters_TM5SDM4DTRFS.html#SoSafeHWModuleParameters_TM5SDM4DTRFS)  [TM5SDM4DTRFS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5SDM4DTRFS.html#SLCv2_SoSafeHWModuleParameters_TM5SDM4DTRFS) |
| Safety-related Module 6DI (6 pulse output), 6DO 24 VDC, 0.5 A | [TM5SDM8TBFS (SLCv1)](SoSafeHWModuleParameters_TM5SDM8DTFS.html#SoSafeHWModuleParameters_TM5SDM8DTFS)  [TM5SDM8TBFS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5SDM8DTFS.html#SLCv2_SoSafeHWModuleParameters_TM5SDM8DTFS) |
| IP67 Block, 8DI, 4DO, 2 A | [TM7SDM12DTFS (SLCv1)](SoSafeHWModuleParameters_TM7SDM12DTFS.html#SoSafeHWModuleParameters_TM7SDM12DTFS)  [TM7SDM12DTFS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM7SDM12DTFS.html#SLCv2_SoSafeHWModuleParameters_TM7SDM12DTFS) |
| Safety-related Module 8DI (2 standard DI, 2 pulse output), 2 standard DO 24 VDC, 12 A, M12 device interface | [TM7SDI8DFS (SLCv1)](SoSafeHWModuleParameters_TM7SDM16DTRFS.html#SoSafeHWModuleParameters_TM7SDM16DTRFS)  [TM7SDI8DFS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM7SDM16DTRFS.html#SLCv2_SoSafeHWModuleParameters_TM7SDM16DTRFS) |
| Safety-related Module 4AI (2x2 current input, 4 to 20 mA, 24 bit converter resolution) | [TM5SAI4AFS (SLCv1)](SoSafeHWModuleParameters_TM5SAI4AFS.html#SoSafeHWModuleParameters_TM5SAI4AFS)  [TM5SAI4AFS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5SAI4AFS.html#SLCv2_SoSafeHWModuleParameters_TM5SAI4AFS) |
| Safety-related Temperature Module (2x2 analog thermocouple inputs for thermoelements of the types J, K, N, S, R, C, T and 1x2 safety-related analog PT100/PT1000 input, 24 bit converter resolution) | [TM5STI4ATCFS (SLCv1)](SoSafeHWModuleParameters_TM5SAI4ATCFS.html#SoSafeHWModuleParameters_TM5SAI4ATCFS)  [TM5STI4ATCFS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5SAI4ATCFS.html#SLCv2_SoSafeHWModuleParameters_TM5SAI4ATCFS) |
| Safety-related Digital Counter Module (1 safety-related digital counter channel, max. input frequency 7 kHz, 24 VDC) | [TM5SDC1FS (SLCv1)](SoSafeHWModuleParameters_TM5SCI1FS.html#SoSafeHWModuleParameters_TM5SCI1FS)  [TM5SDC1FS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5SCI1FS.html#SLCv2_SoSafeHWModuleParameters_TM5SCI1FS) |
| Safety-related Power Supply Module (24 VDC, 10 A) | [TM5SPS10FS (SLCv1)](SoSafeHWModuleParameters_TM5SPS10F.html#SoSafeHWModuleParameters_TM5SPS10F)  [TM5SPS10FS(SLCv2)](SLCv2_SoSafeHWModuleParameters_TM5SPS10F.html#SLCv2_SoSafeHWModuleParameters_TM5SPS10F) |
| Safety Module for LXM62 Drives | [LXM62FS (SLCv1)](SoSafeHWModuleParameters_LXM62.html#SoSafeHWModuleParameters_LXM62)  [LXM62FS(SLCv2)](SLCv2_SoSafeHWModuleParameters_LXM62.html#SLCv2_SoSafeHWModuleParameters_LXM62) |
| Safety Module for ILM62 Drives | [ILM62FS (SLCv1)](SoSafeHWModuleParameters_ILM62.html#SoSafeHWModuleParameters_ILM62)  [ILM62FS(SLCv2)](SLCv2_SoSafeHWModuleParameters_ILM62.html#SLCv2_SoSafeHWModuleParameters_ILM62) |
| TM5 Bus Base for safety-related Electronic modules, safety coded, internal I/O supply interconnected | TM5ACBM3FS |
| Safety-related Terminal Block, 12-pin, safety coded | TM5ACTB52FS |
| Memory Key 2 MB1 | TM5ACSLCM2FS |
| Memory Key 8 MB1 | TM5ACSLCM8FS |

|  |  |
| --- | --- |
| 1 | A memory key is required for operation of the Safety Logic Controller. For more information concerning the role of the memory key in the Safety Logic Controller system, refer to the Safety Logic Controller \* FS - Hardware Guide, which is available for the SLC100/200 and SLC300/400 |

Only modules designated as safety-related modules are allowed to perform safety-related functions. Make certain that neither inputs nor outputs of non-interfering modules are used for safety-related inputs or outputs.

| DANGER | |
| --- | --- |
|  | **IMPROPERLY CONFIGURED SAFETY-RELATED SYSTEM**   * Use only products designated as functional safety devices for use in a safety-related system. * Use only Schneider Electric authorized products in a Safety Logic Controller system.   **Failure to follow these instructions will result in death or serious injury.** |

**NOTE:**

The Sercos III Bus Interface, required for communication with safety-related TM5 modules, is considered a non-interfering module and does not contribute nor detract from the safety-related function of the controller. The safety support layer riding on the Sercos III communication is managed inside the safety-related modules and not in the Sercos III Bus Interface.

EIO0000002265.07