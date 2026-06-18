# Event and Error Log

While working with Machine Expert – Safety, user actions are logged in event log files. Two different log types exist:

* The project event log records project-related user actions like inserting, deleting, or modifying a POU. Additionally, error messages received from the error stack of the Safety Logic Controller are included in this error log file.
* The system event log records events that are not project-related such as modifications in the user manager.

Every event log entry contains the following information:

* Date and time of the modification.
* Type of modification.
* Name of the logged-on user.

Both the project event log and the system event log can be exported to a file (\*.eve) which can be imported and opened later for inspection purposes. To clear the event logs, a reset function is available. After resetting an event log only one entry remains in the list logging the user who has performed the reset. Additionally, the event log lists can be filtered and sorted by different criterions.

**NOTE:**

Resetting the event log is only possible if you are logged-on at 'Development' level (see topic ["Password protection"](PasswordProtection.html#PasswordProtection)).

To open the event log, select 'File > Event Log...'. The [event log dialog](dialogsEventLog.html#dialogsEventLog) can either display project events or system events (switchable using the 'Project Events'/'System Events' button).

The following events are logged in the project event log/system event log and can be handled using the dialogs 'Project Event Log'/'System Event Log':

| Logged event | Event group |
| --- | --- |
| Event log reset | Event log |
| New user project created | User project |
| CRC of user project modified (after compiling) | User project |
| User project downloaded to Safety Logic Controller | User project |
| Global variable declaration modified | User project |
| User project compiled | User project |
| Library included | User project |
| Library deleted | User project |
| Project certified | User project |
| Local variable declaration of a POU modified | POU |
| Code worksheet edited | POU |
| New POU inserted | POU |
| POU deleted | POU |
| POU renamed | POU |
| POU verification set/withdrawn | POU |
| Device parameter modified | Device parameterization |
| Device added | Device parameterization |
| Device removed | Device parameterization |
| Device type modified | Device parameterization |
| Error from the Safety Logic Controller error catalog | SafePLC |

EIO0000002147.09