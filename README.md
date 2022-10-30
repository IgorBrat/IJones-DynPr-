# Indiana Jones and The Last Rectangle Detour

## Description
Indiana Jones must obey these rules:

- after every step he **must be righter** in hall than he was;
- he can always go on one step right;
- he can also jump to any plate with same letter as he is on now.

## Task
For given hall calculate all possible unique paths.

### Input data
File `ijones.in` contains of **H+1** lines:

- First line: numbers ***W and H*** - width and height respectively; 1 <= _**W, H**_ <= 2000.
- Each of next _**H**_ lines contains array of letters with length of **_W_** (a-z).

### Output data
File `ijones.out` contains of one number - count of all unique paths.