# Makefile for source rpm: gtk2
# $Id: Makefile,v 1.1 2004/08/31 10:48:41 cvsdist Exp $
NAME := gtk2
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
