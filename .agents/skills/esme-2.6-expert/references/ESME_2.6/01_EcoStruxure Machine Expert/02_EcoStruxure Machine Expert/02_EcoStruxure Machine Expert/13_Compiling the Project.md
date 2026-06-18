# Compiling the Project

After you have finished the development of the project, you have to compile it.

Compiling means translating and transforming the contents of the worksheets into specific machine code which can be executed by the Safety Logic Controller.

**NOTE:**

If a POU is marked with an asterisk (\*) in the project tree, the POU has not yet been compiled after editing variables or code. After the project has been compiled successfully, the asterisk is removed. Due to this marking you can easily see whether modifications have been made since the last compilation.

How to compile the project

Press <F9> or click the 'Compile' icon on the toolbar:

![](images/iconCompile.gif)

What happens while compiling?

The compilation process is performed in several steps:

1. A syntax check of variables declarations and code worksheets is carried out.
2. Compiled worksheets are linked together and intermediate code is generated.
3. Safety Logic Controller-specific machine code is generated which has to be downloaded to the target.

In case of an error in one of these steps, the compile process may be aborted (depending on the kind of error). Re-compile the project after correcting errors (see below).

How to correct errors and alerts

While compiling, the message window displays the compilation process. Any detected errors and alerts (e.g., syntax errors, memory, or file problems) and additional information are displayed in the appropriate message window sheet.

You can use the message window to jump to the suspected code worksheet by double-clicking on the corresponding error message.

How to stop the compiler

Select 'Build > Stop Compile' to abort the compilation process.

**Further Information:**

After compiling, you have to download the project to the Safety Logic Controller. Refer to the chapter ["Commissioning the Safety Logic Controller"](OnlineGeneral.html#OnlineGeneral) for detailed information on downloading, monitoring, and debugging the safety-related application.

**NOTE:**

Switching between the Safety Logic Controller and the EASYSIM simulation in Machine Expert – Safety (by pressing the 'Simulate' icon on the toolbar) automatically compiles the project.

EIO0000002147.09