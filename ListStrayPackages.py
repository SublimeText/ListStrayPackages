import os
import sublime
import sublime_plugin


class ListStrayPackagesCommand(sublime_plugin.WindowCommand):
    IGNORE = ["User", "Package Control"]

    def run(self):
        settings = sublime.load_settings("Preferences.sublime-settings")
        ignore = self.IGNORE[:]
        ignore.extend(settings.get("ignored_stray_packages", []))

        pkgctrl_settings = sublime.load_settings(
            "Package Control.sublime-settings")
        installed_packages = pkgctrl_settings.get("installed_packages", [])
        stray_packages = []
        for pkgfile in os.listdir(sublime.installed_packages_path()):
            pkgname, ext = os.path.splitext(pkgfile)
            if (ext == ".sublime-package"
                    and pkgname not in installed_packages
                    and pkgname not in ignore):
                stray_packages.append((
                    pkgname,
                    "Installed Packages/%s" % pkgfile,
                    os.path.join(
                        sublime.installed_packages_path(),
                        pkgfile)))
        for pkgdir in os.listdir(sublime.packages_path()):
            fullpath = os.path.join(sublime.packages_path(), pkgdir)
            if (os.path.isdir(fullpath)
                    and pkgdir not in installed_packages
                    and pkgdir not in ignore):
                stray_packages.append((
                    pkgdir,
                    "Packages/%s" % pkgdir,
                    fullpath))

        output = self.window.new_file()
        output.set_scratch(True)
        output.set_name("Stray Packages")
        self.window.focus_view(output)
        output.run_command("stray_packages_result",
                           {"stray_packages": stray_packages})


class StrayPackagesResultCommand(sublime_plugin.TextCommand):
    def run(self, edit, stray_packages):
        if len(stray_packages) == 0:
            msg = "No stray packages.\n"
        else:
            msg = "".join("%s (in %s)\n" % (pkg[0], pkg[1])
                          for pkg in stray_packages)
        self.view.insert(edit, 0, msg)
