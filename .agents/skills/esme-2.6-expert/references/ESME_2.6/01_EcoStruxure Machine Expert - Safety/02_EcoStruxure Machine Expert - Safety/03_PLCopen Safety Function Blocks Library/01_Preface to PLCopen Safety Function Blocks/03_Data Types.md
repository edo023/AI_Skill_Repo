# Data Types

In EcoStruxure Machine Expert - Safety, the following IEC 61131-3 defined elementary data types and special safety-related data types are available:

## IEC 61131-3 data types

| **Data type** | **Description** | **Size/Bit** | **Range** | **Default initial value** |
| --- | --- | --- | --- | --- |
| BOOL | Boolean | 1 | 0...1 | BOOL#0 |
| INT | Integer | 16 | -32,768 up to 32,767 | INT#0 |
| DINT | Double Integer | 32 | -2,147,483,648 up to 2,147,483,647 | DINT#0 |
| TIME | Duration | 32 | 0 up to 2,147,483,647ms | TIME#0s |
| BYTE | Bit string of length 8 | 8 | 0...255 (16#00...16#FF) | BYTE#0 |
| WORD | Bit string of length 16 | 16 | 0...65,535 (16#00...16#FFFF) | WORD#0 |
| DWORD | DoubleWord Bit string of length 32 | 32 | 0...4,294,967,295 (16#00....16#FFFFFFFF) | DWORD#0 |

## Safety-related data types

| **Data type** | **Description** | **Size/Bit** | **Range** | **Default initial value** |
| --- | --- | --- | --- | --- |
| SAFEBOOL | Safety-related Boolean | 1 | 0...1 | SAFEBOOL#0 |
| SAFEINT | Safety-related Integer | 16 | -32,768 up to 32,767 | SAFEINT#0 |
| SAFEDINT | Safety-related Double Integer | 32 | -2,147,483,648 up to 2,147,483,647 | SAFEDINT#0 |
| SAFETIME | Safety-related duration | 32 | 0 up to 2,147,483,647ms | SAFETIME#0s |
| SAFEBYTE | Safety-related bit string of length 8 | 8 | 0...255 (16#00...16#FF) | SAFEBYTE#0 |
| SAFEWORD | Safety-related bit string of length 16 | 16 | 0...65,535 (16#00...16#FFFF) | SAFEWORD#0 |
| SAFEDWORD | Safety-related doubleWord Bit string of length 32 | 32 | 0...4,294,967,295 (16#00....16#FFFFFFFF) | SAFEDWORD#0 |

## Generic data types

Generic data types are used to group elementary data types by forming a hierarchical structure. The generic data type ANY\_SAFEBIT, for example, includes the elementary data types SAFEDWORD, SAFEWORD, SAFEBYTE and SAFEBOOL. If a formal paramater can be connected to ANY\_SAFEBIT, this means that variables of the data types SAFEDWORD, SAFEWORD, SAFEBYTE and SAFEBOOL can be applied to it.

In EcoStruxure Machine Expert - Safety, generic data types and safety-related generic data types are structured as follows:

`ANY_(SAFE)ELEMENTARY`

`ANY_(SAFE)NUM`

`ANY_(SAFE)INT`

`(SAFE)INT, (SAFE)DINT`

`ANY_(SAFE)BIT`

`(SAFE)DWORD, (SAFE)WORD, (SAFE)BYTE, (SAFE)BOOL`

`(SAFE)TIME`

**NOTE:**

Data types which cannot be used for functional safety-related purposes, such as REAL or LREAL, etc., are not considered in the listing above.

**NOTE:**

The use of data types depends on your hardware. Refer to your hardware documentation for restrictions concerning generic data types.

EIO0000002269.01

© 2020

Schneider Electric.

All rights reserved.