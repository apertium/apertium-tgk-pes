AC_PREREQ(2.52)

AC_INIT([Apertium Tajik-Iranian Persian], [0.1.0], [francis.tyers@gmail.com], [apertium-tgk-pes], [https://wiki.apertium.org/wiki/Apertium-tgk-pes])
AM_INIT_AUTOMAKE
AC_PROG_AWK

PKG_CHECK_MODULES(APERTIUM, apertium >= 3.6.1)
PKG_CHECK_MODULES(LTTOOLBOX, lttoolbox >= 3.5.1)



PKG_CHECK_MODULES(CG3, cg3 >= 1.3.1)
PKG_CHECK_MODULES(APERTIUM_LEX_TOOLS, apertium-lex-tools >= 0.2.3)




AC_PATH_PROGS(ZCAT, [gzcat zcat], [false])
AS_IF([test x$ZCAT = xfalse], [AC_MSG_ERROR([You don't have zcat nor gzcat installed])])

m4_ifdef([AP_CHECK_LING],[],[AC_MSG_ERROR([AP_CHECK_LING not defined, is apertium.m4 in ACLOCAL_PATH? See: https://wiki.apertium.org/wiki/Installation_troubleshooting])])


AP_CHECK_LING([1], [apertium-tgk])

AP_CHECK_LING([2], [apertium-pes])

AP_MKINCLUDE

AC_OUTPUT([Makefile])
