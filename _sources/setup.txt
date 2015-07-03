.. _setup:

=====
Setup
=====

Abstract
========

Here we show how to set up `PTC Windchill`_ artifacts for Maven_ such that we later can depend on
these artifacts in our projects.

This is not a introduction to maven_, please see the documentation on the maven_ website for more.

.. note:: The instructions below are geared for a a development machine with unix-like tools but should
   work similar on Windows machines.

Prerequisites
=============

You need to have the needed tools installed:

- A JDK for Windchill development
- ant and maven

On a Mac, this is done by::

	$ brew cask install java
	$ brew install ant maven

TL;DR
=====

On a Mac::

	$ cd windchill-maven
	$ virtualenv .
	$ . ./bin/activate
	$ . ./setenv.sh
	$ pip install -r requirements.txt
	$ fab make:version=MAJOR.MINOR.PATCH.FOO

Where `MAJOR.MINOR.PATCH.FOO` is the actual Windchill version, e.g::

	$ fab make:version=10.2.20.00

This currently creates and imports the artifacts.

.. note:: There's much more included in this repo -- most of I don't understand yet.  Below is
   what I understood so far.  If you have any comments or help, please contact me_.


Creating Windchill Artifacts
============================

.. note:: This step is a **one time** setup task.

To depend on `PTC Windchill`_ code in our project, we need to create a *jar file* out of the code base found in
Windchill.  We need to do this *once per Windchill version*.  Which versions we actually want to support is entirely
up to you.  However, we need to use a *pristine* copy of Windchill, i.e. no custom code or extensions installed, or
they'd too end up in the jar file.

To be able to compile, we need to create these artifacts:

- The *codebase* -- using ant to create a jar file from the Windchill code base
- The *annotations* -- this is in `$WT_HOME/srclib/tools/Annotations.jar`
- The *ie3rdpartylibs* -- this is located at `$WT_HOME/codebase/WEB-INF/lib/ie3rdpartylibs.jar`

Windchill Version
------------------

You need to obtain the Windchill version to import the artifacts using the correct Windchill version.  This
is done by issuing `wndchill version` in a windchill shell **on the server**.  A example output is below::

	$ windchill version
	      Timestamp: Juli 03, 2015 - 12:54:14 (GMT: 03.07.2015 10:54:14)

	      Support   Support                                  Installer
	      Datecode  Release Number  Release Id               Sequence   Display Label
	  --  --------  --------------  ---------------          ---------  ---------------------
	      F000      10.2            pdml.10.2.0.00.62        01         PTC Windchill PDMLink 10.2
	      M020      10.2            wsp.10.2.20.00.28        04         PTC Windchill 10.2 Service Pack
	      M020      10.2            whc.10.2.20.00.28        02         PTC Windchill 10.2 Help Center
	      M020      10.2            ie.10.2.20.00.28         01         PTC Windchill 10.2 Info*Engine
	      M020      10.2            commonpdm.10.2.20.00.28  03         PTC Windchill 10.2 Common Base
	      M020      10.2            wlp.10.2.20.00.28        01         PTC Windchill 10.2 MultiLanguage Pack
	      M020      10.2            wnc.10.2.20.00.28        05         PTC Windchill 10.2 Services

	  There are no patches installed.

	  Non-Default Locale Support:
	  Code  Name
	  ----  ----
	  de

The version used below for this example would be **10.2.0.00**.

Preparing artifacts
-------------------

So, to prepare the files for import into the maven_ repository, do::

	$ cd windchill-maven
	$ export WT_HOME=/Volumes/whereever-your-windchill-home-is
	$ ant makeCodebaseJar
	$ cp $WT_HOME/srclib/tools/Annotations.jar .
	$ cp $WT_HOME/codebase/WEB-INF/lib/ie3rdpartylibs.jar .

Import the artifacts to the *local* maven repository
----------------------------------------------------


To import the artifacts, do::

	$ cd windchill-maven
	$ export WTVERSION=10.2.0.00
	$ mvn install:install-file -Dfile=codebase.jar -DgroupId=com.ptc -DartifactId=codebase -Dversion=$WTVERSION -Dpackaging=jar -DgeneratePom=true -DcreateChecksum=true
	$ mvn install:install-file -Dfile=Annotations.jar -DgroupId=com.ptc -DartifactId=Annotations -Dversion=$WTVERSION -Dpackaging=jar -DgeneratePom=true -DcreateChecksum=true
	$ mvn install:install-file -Dfile=ie3rdpartylibs.jar -DgroupId=com.ptc -DartifactId=ie3rdpartylibs -Dversion=$WTVERSION -Dpackaging=jar -DgeneratePom=true -DcreateChecksum=true

.. _maven: 				https://maven.apache.org/
.. _nexiles: 			http://www.nexiles.com
.. _PTC: 				http://www.ptc.com
.. _PTC Windchill: 		http://www.ptc.com/product-lifecycle-management/windchill
.. _me: 				mailto:se@nexiles.de?subject=windchill%20maven%20setup%20comment

.. vim: set ft=rst tw=75 nocin nosi ai spell sw=4 ts=4 expandtab:
