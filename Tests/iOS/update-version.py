import sys
import xml.etree.ElementTree as ElementTree

def log(msg):
    sys.stderr.write(msg + '\n')

class Project:
    Filename = 'Tests.iOS.csproj'
    Schema = '{http://schemas.microsoft.com/developer/msbuild/2003}'
    RootTag = Schema + 'Project'
    Property = Schema + 'PropertyGroup'
    Release = Schema + 'ReleaseVersion'
    Package = Schema + 'Description'

class Info:
    Filename = 'Info.plist'
    Declaration = '<?xml version="1.0" encoding="UTF-8"?>\n'
    DocType = '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n'
    RootTag = 'dict'
    Package = 'CFBundleIdentifier'
    ShortVersion = 'CFBundleShortVersionString'
    Version = 'CFBundleVersion'

def main(*args):
    project_tree = ElementTree.parse(Project.Filename)
    project = project_tree.getroot()

    version = None
    package = None

    for release in project.iter(Project.Release):
        version = release.text
        log('Release: {}'.format(version))
        break
    else:
        log('Error: version not found!')
        return -1

    for name in project.iter(Project.Package):
        package = name.text
        log('Package: {}'.format(package))
        break
    else:
        log('Error: package not found!')
        return -1

    # ElementTree.register_namespace('android', 'http://schemas.android.com/apk/res/android')
    info_tree = ElementTree.parse(Info.Filename)
    info = info_tree.getroot()

    old_package = ''
    old_short_version = ''
    old_version = ''

    last = ''
    for e in info:
        if e.tag == Info.RootTag:
            for value in e:
                if last == Info.Package:
                    old_package = value.text
                    value.text = package
                elif last == Info.ShortVersion:
                    old_short_version = value.text
                    value.text = version
                elif last == Info.Version:
                    old_version = value.text
                    value.text = version
                last = value.text

    if old_version == version and old_package == package:
        log('Info: no changes.')
        return

    log('Version: {} -> {}'.format(old_version, version))
    log('ShortVersion: {} -> {}'.format(old_short_version, version))
    log('Package: {} -> {}'.format(old_package, package))

    with open(Info.Filename, 'w') as output:
        output.write(Info.Declaration)
        output.write(Info.DocType)
        info_tree.write(output, xml_declaration=False, encoding='utf-8')

if __name__ == '__main__':
    sys.exit(main(*sys.argv))
