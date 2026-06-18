# Password Protection for Projects and Safety Logic Controller

This topic contains information on the following:

* [Overview: Password protection](PasswordProtection.html#PasswordProtection__Passwords_Overview)
* [Which operations require which password?](PasswordProtection.html#PasswordProtection__Passwords_WhichOperations)
* [How to change the project level](PasswordProtection.html#PasswordProtection__Passwords_LoginProject)
* [How to log on to/off from the Safety Logic Controller](PasswordProtection.html#PasswordProtection__Passwords_LoginSafeControl)
* [Automatic "logoff" due to inactivity](PasswordProtection.html#PasswordProtection__Passwords_AutomLogoff)
* [How to define project passwords on project creation](PasswordProtection.html#PasswordProtection__Passwords_How2Define_Project)
* [How to modify/reset project passwords](PasswordProtection.html#PasswordProtection__Passwords_How2Change_Project)
* [How to define a Safety Logic Controller password](PasswordProtection.html#PasswordProtection__Passwords_How2Define_SafeControl)

## Overview

Two passwords provide dual protection in Machine Expert – Safety:

* The **project password** protects the project against unauthorized modifications.

  The following hierarchical project levels are available:

  + Development
  + Commissioning
  + Maintenance

  **NOTE:**

  No password is required for accessing the 'Maintenance' level.

  Safety-related modifications in the safety logic and the project information are logged in the event log together with the name of the logged-on Windows user and the Machine Expert – Safety project level.
* The **Safety Logic Controller password** protects the configuration on the Safety Logic Controller against unauthorized access and the Safety Logic Controller itself against unauthorized switching of the operating mode.

  Online values can be read from the Safety Logic Controller and displayed in Machine Expert – Safety even without logging on to the Safety Logic Controller.

## Which Operations Require which Password?

The following table shows which project password level is required for particular operations and which operation requires the Safety Logic Controller password.

| Action | Project password level | | | Safety Logic Controller password required? |
| --- | --- | --- | --- | --- |
| Development | Commissioning | Maintenance |
| Modifying project passwords | Yes | - | - | - |
| Resetting the event log | Yes | - | - | - |
| Opening worksheets (and object properties dialogs) | Yes | Yes | Yes | - |
| Editing the project tree (POUs and libraries) | Yes | - | - | - |
| Editing code worksheets | Yes | - | - | - |
| Editing variable declarations | Yes | - | - | - |
| Modifying device parameterization | Yes | Yes | - | - |
| Compiling a project | Yes | Yes | Yes | - |
| Downloading a project | Yes | Yes | Yes | Yes |
| Creating an application image | Yes | Yes | Yes | 1) |
| Controlling the Safety Logic Controller (start, stop, reset, ...) | Yes | Yes | Yes | Yes |
| Switching to online mode and displaying the variable status | Yes | Yes | Yes | - |
| Switching to debug mode,forcing and overwriting | Yes | Yes | Yes | Yes |
| Editing project documentation (project info) | Yes | Yes | - | - |
| Printing the project | Yes | Yes | Yes | - |
| Certifying a project  Removing project certification | Yes | - | - | - |
| Set/withdraw POU verification (flag) | Yes | - | - | - |

|  |  |
| --- | --- |
| 1) | The Safety Logic Controller password is not required to create the binary application image (container file) in Machine Expert – Safety. However, the Safety Logic Controller password must be applied to an input of the FB\_ApplicationDownload function block in the standard application (programmed in Machine Expert) for downloading the application image to the Safety Logic Controller. |

## How to log on to the project or change the log on level

1. Select 'Project > Project Log On'.
2. Select a project level and enter the appropriate project password in the 'Project Log On' dialog.

   **NOTE:**

   No password is required for accessing the 'Maintenance' level.
3. Click 'OK'.

Following a successful logon, the status bar at the bottom edge of the screen shows your project level.

Example:  ![](images/ProjectPwd_statusbar_Admin.gif)

## How to log on to/off from the Safety Logic Controller

**NOTE:**

The menu items relating to the Safety Logic Controller password are only visible if a communication connection is established between the computer and the Safety Logic Controller. This is the case, if either the [control dialog](dialogSafePLC.html#dialogSafePLC) is open or the [variable status is displayed (online mode)](DisplayVariableStatus.html#DisplayVariableStatus). Otherwise, these items are hidden.

* **Logging on to the Safety Logic Controller**:

  1. If not already done, first establish a communication connection to the Safety Logic Controller, e.g., by clicking the 'SafePLC' icon on the toolbar.
  2. Select the 'Online > SafePLC Log On' menu item.
  3. In the logon dialog, enter the Safety Logic Controller password and click 'OK'.

  The status bar now displays your logon status on the right:   ![](images/Statusbar_PLCLoggedIn.GIF)

  Now you have full access to the Safety Logic Controller. You can download a project, control the Safety Logic Controller and debug the safety-related application.
* **Logging off from the Safety Logic Controller**: Select the 'Online > SafePLC Log Off' menu item and confirm the appearing prompt with 'Yes'.

  When logging off from the Safety Logic Controller, it remains in its state. If, for example, variables are forced in debug mode, neither the operating mode nor the Safety Logic Controller state or the forced values are influenced by the logoff.

## Automatic logoff due to inactivity

If no user activity is detected within the [access timeout](customizingtheuserinterface_dialog_options.html#customizingtheuserinterface_dialog_options) period specified in the 'General' settings tab in the 'Options' dialog, Machine Expert – Safety is automatically locked. In this case, you have to confirm the appearing dialog and reenter the project password for the project level you need.

This also applies to the Safety Logic Controller. After an hour of inactivity you must reenter the Safety Logic Controller password in order to have access to the Safety Logic Controller.

## How to define project passwords on project creation

If a [new project is created when launching Machine Expert – Safety](creatinganewprojectusingtheprojectwizard.html#creatinganewprojectusingtheprojectwizard), you are asked to define a password for the project levels 'Development' and 'Commissioning'. For the 'Maintenance' level, no password is required.

In the 'Set New Project Password' dialog, define the 'Development' and 'Commissioning' level password by entering it twice into both text fields.

**NOTE:**

A secure password is one that has not been shared or distributed to any unauthorized personnel and does not contain any personal or otherwise obvious information. Further, a mix of upper and lower case letters, numbers and special characters offer the best security possible. You should choose a password length of at least 6 characters. The password is case-sensitive and can be a mix of up to 10 characters.

## How to modify/reset project passwords

When [logged-on at 'Development' level](PasswordProtection.html#PasswordProtection__Passwords_LoginProject), you can modify a defined password at each access level. This corresponds to resetting it.

1. Select 'Project > Change Project Password'.
2. In the 'Change Project Password' dialog, first select the project level for which you want to change the project password.

   Then, enter the new password twice.

   Finally, click 'OK' to apply the new password and close the dialog.

   **NOTE:**

   A secure password is one that has not been shared or distributed to any unauthorized personnel and does not contain any personal or otherwise obvious information. Further, a mix of upper and lower case letters, numbers and special characters offer the best security possible. You should choose a password length of at least 6 characters. The password is case-sensitive and can be a mix of up to 10 characters.

## How to modify a Safety Logic Controller password

**NOTE:**

When you connect to a Safety Logic Controller for the first time which is still unconfigured, you will be automatically asked to define a Safety Logic Controller password. This password is saved in the Safety Logic Controller.

1. Select 'Online > SafePLC Change Password'.
2. In the 'New SafePLC password' dialog, enter the old and the new password and confirm the new password.

   Finally, click 'OK' to apply the new password and close the dialog.

   **NOTE:**

   A secure password is one that has not been shared or distributed to any unauthorized personnel and does not contain any personal or otherwise obvious information. Further, a mix of upper and lower case letters, numbers and special characters offer the best security possible. You should choose a password length of at least 6 characters. The password is case-sensitive and can be a mix of up to 10 characters.

EIO0000002147.09