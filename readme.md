List Stray Packages
===================
This package lists "stray" packages in your Sublime Text installation, i.e.
packages that aren't known to [Package Control][pkgctrl]. Use it however you
want; I only synchronise the Package Control config file rather than the full
packages between machines, so when I remove a package on one machine, it
doesn't automatically get uninstalled on other machines. I wrote this package
to find these packages.

[pkgctrl]: https://sublime.wbond.net/

## Configuration
Configuration settings are in the default user config file
(`Packages/User/Preferences.sublime-settings`). The following settings are
available:

* `ignored_stray_packages` -- a list of packages that are not listed, even if
  they aren't in the Package Control package list. Note that the `User` and
  `Package Control` packages are always ignored.

## About
Copyright (c) 2014 Felix Krull <f_krull@gmx.de>  
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1) Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.  
2) Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.  
3) The names of its contributors may not be used to endorse or promote products
   derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES'(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
