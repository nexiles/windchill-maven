.. _introduction:

============
Introduction
============

:Author:    Stefan Eletzhofer, nexiles GmbH
:Date:      |today|

Problem Statement
=================

The approach proposed by PTC to develop customizations for `PTC Windchill`_ is quite involved and
suggests putting class files directly into the code base of the Windchill server.  Moreover, development
is assumed to happen *directly* on the server.

This is suboptimal for obvious reasons:

- No clean separation between the code PTC_ ships
- No versioning of Windchill dependencies, i.e. you've got what you've got installed on the server
- Developing on a server, i.e. each developer would need to have Windchill installed to even *compile* code


Goals
=====

- We want to have a clean way to depend on `PTC Windchill`_ dependencies for multiple versions
- We want to be able to build on our local development machines w/o need to have access to a Windchill
  server
- We want to document how to set up such a system

About nexiles
=============

nexiles_ is a company based in Germany and Norway.  We develop tools and provide solutions for customers
dealing with `PTC Windchill`_.  If you have any questions or comments, contact us_.

.. _nexiles: 			http://www.nexiles.com
.. _PTC: 				http://www.ptc.com
.. _PTC Windchill: 		http://www.ptc.com/product-lifecycle-management/windchill
.. _us: 				mailto:info@nexiles.com?subject=windchill%20maven%20setup%20request%20for%20information&cc=se@nexiles.de

.. vim: set ft=rst tw=75 nocin nosi ai spell sw=4 ts=4 expandtab:
