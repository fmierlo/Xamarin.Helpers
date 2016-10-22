import sys
import xml.etree.ElementTree as ElementTree

def log(msg):
    sys.stderr.write(msg + '\n')

class Project:
    Filename = 'Helpers.csproj'
    Schema = '{http://schemas.microsoft.com/developer/msbuild/2003}'
    RootTag = Schema + 'Project'
    Property = Schema + 'PropertyGroup'
    Release = Schema + 'ReleaseVersion'
    Package = Schema + 'Description'

class Version:
    In = 'Version.cs.in'
    Out = 'Version.cs'

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

    with open(Version.In) as input:
        with open(Version.Out, 'w') as output:
            content = input.read()
            content = content.replace('{VersionName}', version)
            content = content.replace('{PackageName}', package)
            output.write(content)
            log('Writed: {} -> {}.{} -> {}'.format(Version.In, package, version, Version.Out))

if __name__ == '__main__':
    sys.exit(main(*sys.argv))
