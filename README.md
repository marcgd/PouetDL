# PouetDL: Demoscene prods downloader

[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/marcgd/PouetDL/blob/master/LICENSE)

## You have just found PouetDL.

This small web spider will download and track demoscene productions for your favorite platforms, using pouet.net as source.

It just downloads the prods you don't already have, keeping your download history inside a SQLite dbfile.

Please keep in mind that:

- This personal project is not related to pouet.net or scene.org.
- It's limited to process 1 page of results, avoiding too many requests to the servers.

PouetDL is compatible with: __Python 2.7__.


------------------


## Requirements

PouetDL uses the following dependencies:

- bs4

------------------


## Usage

Clone or download the script and install dependencies, give it run permissions and:

```bash
$ ./pouet.py [Platform]
```

Eg:

```bash
$ ./pouet.py "Amiga AGA"
```

Last productions for chosen platform will be downloaded on the default directory [pouetDLdir]/__down/[Platform]/__

You can run it on a cron if you want to download prods as they are released.

------------------


## Supported platforms


*Used as command arguments:*

- Acorn
- Alambik
- Amiga AGA
- Amiga OCS/ECS
- Amiga PPC/RTG
- Amstrad CPC
- Amstrad Plus
- Android
- Apple II
- Apple II GS
- Atari Falcon 030
- Atari Jaguar
- Atari Lynx
- Atari ST
- Atari STe
- Atari TT 030
- Atari VCS
- Atari XL/XE
- BBC Micro
- BeOS
- BK-0010/11M
- C16/116/plus4
- C64 DTV
- Commodore 128
- Commodore 64
- Dreamcast
- Enterprise
- Flash
- FreeBSD
- Gameboy
- Gameboy Advance
- Gameboy Color
- Gamecube
- GamePark GP2X
- GamePark GP32
- Intellivision
- iOS
- Java
- JavaScript
- Linux
- MacOS
- MacOSX
- MacOSX Intel
- mIRC
- Mobile Phone
- MS-Dos
- MS-Dos/gus
- MSX
- MSX 2
- MSX 2 plus
- MSX Turbo-R
- NEC TurboGrafx/PC Engine
- NeoGeo Pocket
- NES/Famicom
- Nintendo 64
- Nintendo DS
- Nintendo Wii
- Oric
- PalmOS
- PHP
- Playstation
- Playstation 2
- Playstation 3
- Playstation Portable
- PocketPC
- Pokemon Mini
- Raspberry Pi
- SAM Coupé
- SEGA Game Gear
- SEGA Genesis/Mega Drive
- SEGA Master System
- SGI/IRIX
- Sharp MZ
- SNES/Super Famicom
- Solaris
- Spectravideo 3x8
- Thomson
- TI-8x
- TRS-80/CoCo
- Vectrex
- VIC 20
- Virtual Boy
- Wild
- Windows
- Wonderswan
- XBOX
- XBOX 360
- ZX Enhanced
- ZX Spectrum 
- ZX-81