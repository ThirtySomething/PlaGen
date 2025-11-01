# PlaGen

Playlist generator using drag and drop

## Motivation

I've added some CDs to my (large) collection. After ripping them to [flac][wiki_flac] using [DockerRipper][url_dockerripper] (thanks to [RiX][url_rix]) I have to create manually a playlist for the new CDs. So I thought this must be more convenient and the idea was born.

## Details

The program will create playlist in the [m3u][wiki_m3u] format. At the beginning the simple format is used, maybe at a later point the extended format might be implemented.

The playlists will contain only relative paths. This is because folder of the playlists is located inside my [flac][wiki_flac] collection. This enables the playlist used on my PC as well as on my mobile using [PowerAmp][url_poweramp].

## Usage

The usage of the program should be self explaining. Create a new playlist by clicking the correspondig button, then drap'n'drop the files/folders for the playlist to the main window, save the playlist and you're done. Optional you can edit the playlist and change the order of the songs.

## Tools

For the program there are various tools used:

- [MDO][url_mdo] for handling of the config
- [Python][url_python] programming language
- [VSCode][url_vscode] as [IDE][wiki_ide]
- [wxFormBuilder][url_wxformbuilder] for [UI][wiki_ui] design
- [wxPython][url_wxpython] for the [UI][wiki_ui]

## License

The program is using the [MIT license][wiki_mit_license].

```
MIT License

Copyright (c) 2025 Jochen Paul

This file is part of PlaGen.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

[url_dockerripper]: https://github.com/rix1337/docker-ripper
[url_mdo]: https://github.com/ThirtySomething/MDO
[url_poweramp]: https://powerampapp.com/
[url_python]: https://www.python.org/
[url_rix]: https://github.com/rix1337
[url_vscode]: https://code.visualstudio.com/
[url_wxformbuilder]: https://github.com/wxFormBuilder/wxFormBuilder
[url_wxpython]: https://wxpython.org/index.html
[wiki_flac]: https://en.wikipedia.org/wiki/FLAC
[wiki_ide]: https://en.wikipedia.org/wiki/Integrated_development_environment
[wiki_m3u]: https://en.wikipedia.org/wiki/M3U
[wiki_mit_license]: https://en.wikipedia.org/wiki/MIT_License
[wiki_ui]: https://en.wikipedia.org/wiki/User_interface
