# ModuleGenerator
Python script that generates clean architecture modules

# How to:
1. Run `python generator.py`
2. Type author full name: This will appear on the top of the swift files (e.g. William Hass)
3. Type project name: This will appear on the top of the swift files (e.g. ACME)
4. Type module name: The name of the module you are creating (e.g. Sign up, Login...)

## Class diagram
![Class diagram](https://raw.githubusercontent.com/hvsw/Clean-Architecture-Module-Generator/master/Class%20diagram.png)

- Yellow boxes represent interfaces/protocols
- Blue boxes represent concrete objects

## Files templates:
- Protocols templates: `./protocols`
- Classes templates: `./concrete_classes`


## Classes and protocols templates examples:

- `$_AUTHOR` will be replaced by what was typed when asked for `Author full name`
- `$_PROJECT_NAME` will be replaced by what was typed when asked for `Project name`
- `__` will be replaced by what was typed when asked for `Module name`.
- `$_DATE` will be internally replaced by the current date in the following format: `%Y-%m-%d`

Examples:
File name: `__UseCaseProtocol.swift`
File content:
```
//
//  __UseCaseProtocol.swift
//  $_PROJECT_NAME
//
//  Created by $_AUTHOR on $_DATE.
//

import Foundation

protocol __UseCaseProtocol {
    
}
```
