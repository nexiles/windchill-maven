import os
import sys

from fabric.api import task, execute, local, lcd
from fabric.colors import red, yellow, green
from fabric.context_managers import settings, hide

WT_HOME = os.environ.get("WT_HOME")
if not os.path.exists(WT_HOME):
    print(red("Can't access WT_HOME: {}".format(WT_HOME)))
    sys.exit(10)


project_root    = os.path.dirname(__file__)
build_dir       = os.path.join(project_root, "build")
docs_dir        = os.path.join(project_root, "docs")

GROUP_ID = "com.ptc"

@task
def make_artifats(version):
    "create windchill artifacts"
    dest = os.path.join(build_dir, version)

    os.environ["WTVERSION"] = version

    print green("Building artifacts for {} version {}".format(GROUP_ID, version))
    with settings(hide("running", "stdout")):
        print green("    Copying jar files ...")
        local("mkdir -p {}".format(dest))
        with lcd(dest):
            local("cp {}/srclib/tool/Annotations.jar .".format(WT_HOME))
            local("cp {}/codebase/WEB-INF/lib/ie3rdpartylibs.jar .".format(WT_HOME))

        print green("    Creating codebase jar file ...")
        local("ant makeCodebaseJar")


@task
def import_artifats(version):
    "import artifacts to maven local repo"
    src = os.path.join(build_dir, version)
    os.environ["WTVERSION"] = version


    if not os.path.exists(src):
        print(red("Please make artifacts for version {} first.".format(version)))
        sys.exit(10)

    print green("Importing artifacts for {} version {}".format(GROUP_ID, version))
    with settings(hide("running", "stdout")):
        with lcd(src):
            for artifact in "codebase Annotations ie3rdpartylibs".split():
                print green("    {} ...".format(artifact))
                cmd = "mvn install:install-file -Dfile={artifact}.jar " \
                      "-DgroupId={group_id} -DartifactId={artifact} " \
                      "-Dversion={version} -Dpackaging=jar -DgeneratePom=true " \
                      "-DcreateChecksum=true".format(artifact=artifact, version=version, group_id=GROUP_ID)
                local(cmd)


@task
def build_docs():
    print green("Building docs ...")
    with settings(hide("running", "stdout")):
        with lcd(docs_dir):
            local("make gh_pages")
            local("make preview")


@task
def push_docs():
    print green("Pushing docs to GitHub ...")
    with settings(hide("running", "stdout")):
        with lcd(docs_dir):
            local("make gh_pages_sync")


@task
def make(version):
    "create and import artifacts to maven local repo"
    execute(make_artifats, version=version)
    execute(import_artifats, version=version)

# EOF
