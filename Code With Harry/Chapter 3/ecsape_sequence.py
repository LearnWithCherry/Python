a = "Hello \nMy name is Rajat"
print(a)

# | Escape Sequence | Meaning                                | Example                              | Output               |
# | --------------- | -------------------------------------- | ------------------------------------ | -------------------- |
# | `\n`            | New Line                               | `print("Hello\nWorld")`              | Hello<br>World       |
# | `\t`            | Horizontal Tab                         | `print("Hello\tWorld")`              | Hello World          |
# | `\\`            | Backslash                              | `print("Path: C:\\new\\folder")`     | Path: C:\new\folder  |
# | `\'`            | Single Quote                           | `print('It\'s fine')`                | It's fine            |
# | `\"`            | Double Quote                           | `print("He said \"hi\"")`            | He said "hi"         |
# | `\r`            | Carriage Return (return to line start) | `print("123\rAB")`                   | AB3                  |
# | `\b`            | Backspace (deletes one char)           | `print("abc\b")`                     | ab                   |
# | `\f`            | Form Feed (new page; rarely used)      | `print("Hello\fWorld")`              | HelloWorld          |
# | `\a`            | Bell (alert sound, might beep)         | `print("\a")`                        | (may beep)           |
# | `\v`            | Vertical Tab                           | `print("a\v\v\v\v\v\v\v\v\v\v\v\v")` | a (vertical spacing) |
# | `\ooo`          | Character with octal value             | `print("\141")`                      | a                    |
# | `\xhh`          | Character with hex value               | `print("\x61")`                      | a                    |
# | `\N{name}`      | Unicode character by name              | `print("\N{SMILING FACE}")`          | 🙂                   |
# | `\uXXXX`        | Unicode character (4-digit hex)        | `print("\u2764")`                    | ❤                    |
# | `\UXXXXXXXX`    | Unicode character (8-digit hex)        | `print("\U0001F602")`                | 😂                   |

a = "Hello \nMy name is \"Rajat\" "
print(a)