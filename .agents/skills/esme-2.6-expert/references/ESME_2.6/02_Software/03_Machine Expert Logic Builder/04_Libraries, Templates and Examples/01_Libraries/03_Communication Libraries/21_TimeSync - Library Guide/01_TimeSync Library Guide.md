# TimeSync Library Guide

![](images/logo.png)

TimeSync Library Guide

TimeSync Library Guide

This document describes the library TimeSync.

The TimeSync library implements the [SNTP](../glossary/glossary.htm#XREF_D_SE_0024697_818) (Simple Network Time Protocol) client feature. It allows your controller to connect to an NTP (Network Time Protocol) or SNTP time server in order to synchronize the internal [RTC](../glossary/glossary.htm#XREF_D_SE_0024697_729) (Real-Time Clock) of the controller in accordance with the primary time standard [UTC](../glossary/glossary.htm#XREF_D_SE_0024697_483) (Universal Time Coordinated) that is globally unique.

The TimeSync library uses system functions and resources which are supported on specific controller platforms:

EIO0000002791.00

© 2019 Schneider Electric. All rights reserved.