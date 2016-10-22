import sys
import xml.etree.ElementTree as ElementTree

def log(msg):
    sys.stderr.write(msg + '\n')

class Project:
    Filename = 'Helpers.UITests.Droid.csproj'
    Schema = '{http://schemas.microsoft.com/developer/msbuild/2003}'
    RootTag = Schema + 'Project'
    Property = Schema + 'PropertyGroup'
    Release = Schema + 'ReleaseVersion'
    Package = Schema + 'Description'

class Manifest:
    Filename = 'Properties/AndroidManifest.xml'
    Declaration = '<?xml version="1.0" encoding="utf-8"?>\n'
    Schema = '{http://schemas.android.com/apk/res/android}'
    RootTag = 'manifest'
    VersionName = Schema + 'versionName'
    VersionCode = Schema + 'versionCode'
    Package = 'package'

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

    ElementTree.register_namespace('android', 'http://schemas.android.com/apk/res/android')
    manifest_tree = ElementTree.parse(Manifest.Filename)
    manifest = manifest_tree.getroot()

    if manifest.tag == Manifest.RootTag:
        if (manifest.attrib[Manifest.VersionName] == version and
            manifest.attrib[Manifest.Package] == package):
            log('Info: no changes.')
        else:
            old_package = manifest.attrib[Manifest.Package]
            old_version = manifest.attrib[Manifest.VersionName]
            old_code = manifest.attrib[Manifest.VersionCode]

            manifest.attrib[Manifest.Package] = package
            manifest.attrib[Manifest.VersionName] = version
            manifest.attrib[Manifest.VersionCode] = str(int(manifest.attrib[Manifest.VersionCode]) + 1)

            log('VersionName: {} -> {}'.format(old_version, manifest.attrib[Manifest.VersionName]))
            log('VersionCode: {} -> {}'.format(old_code, manifest.attrib[Manifest.VersionCode]))
            log('Package: {} -> {}'.format(old_package, manifest.attrib[Manifest.Package]))

            with open(Manifest.Filename, 'w') as output:
                output.write(Manifest.Declaration)
                manifest_tree.write(output, xml_declaration=False, encoding='utf-8')
    else:
        log('Error: version not found!')
        return -1

if __name__ == '__main__':
    sys.exit(main(*sys.argv))
