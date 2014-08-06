VERSION=0.1
LANG1=tgk
LANG2=pes
PREFIX1=$(LANG1)-$(LANG2)
PREFIX2=$(LANG2)-$(LANG1)

BASENAME=apertium-$(PREFIX1)

TARGETS_COMMON =  \
     $(PREFIX1).automorf.bin $(PREFIX1).autobil.bin $(PREFIX1).autogen.bin \
     $(PREFIX2).automorf.bin $(PREFIX2).autobil.bin \
     $(PREFIX2).autogen.bin \
     $(PREFIX1).t1x.bin  \
     $(PREFIX2).t1x.bin $(PREFIX2).alpha.bin modes  $(PREFIX2).mode

# LANG1 → LANG2
     
$(PREFIX1).automorf.bin: $(AP_SRC1)/$(LANG1).automorf.bin $(PREFIX1).autobil.bin
	lt-trim $^ $@

$(PREFIX1).autobil.bin: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $(BASENAME).$(PREFIX1).dix
	lt-comp lr $(BASENAME).$(PREFIX1).dix $@

$(PREFIX1).autogen.bin: $(AP_SRC2)/apertium-$(LANG2).$(LANG2).dix
	apertium-validate-dictionary $< 
	lt-comp rl $< $@

$(PREFIX1).autopgen.bin: $(BASENAME).post-$(LANG2).dix
	apertium-validate-dictionary $(BASENAME).post-$(LANG2).dix
	lt-comp lr $(BASENAME).post-$(LANG2).dix $@

$(PREFIX1).t1x.bin: $(BASENAME).$(PREFIX1).t1x
	apertium-validate-transfer $(BASENAME).$(PREFIX1).t1x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX1).t1x $@

# LANG2 → LANG1

$(PREFIX2).automorf.bin: $(AP_SRC2)/$(LANG2).automorf.bin $(PREFIX2).autobil.bin
	lt-trim $^ $@

$(PREFIX2).autobil.bin: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $(BASENAME).$(PREFIX1).dix
	lt-comp rl $(BASENAME).$(PREFIX1).dix $@

$(PREFIX2).autogen.bin: $(AP_SRC1)/apertium-$(LANG1).$(LANG1).dix
	apertium-validate-dictionary $<
	lt-comp rl $< $@

$(PREFIX2).autopgen.bin: $(BASENAME).post-$(LANG1).dix
	apertium-validate-dictionary $(BASENAME).post-$(LANG1).dix
	lt-comp lr $(BASENAME).post-$(LANG1).dix $@

$(PREFIX2).alpha.bin: $(BASENAME).$(PREFIX1).alpha.dix
	apertium-validate-dictionary $(BASENAME).$(PREFIX1).alpha.dix
	lt-comp rl $(BASENAME).$(PREFIX1).alpha.dix $@

$(PREFIX2).t1x.bin: $(BASENAME).$(PREFIX2).t1x
	apertium-validate-transfer $(BASENAME).$(PREFIX2).t1x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX2).t1x $@


EXTRA_DIST=$(BASENAME).$(LANG1).dix $(BASENAME).$(PREFIX1).dix \
           $(BASENAME).post-$(LANG1).dix $(BASENAME).post-$(LANG2).dix \
           $(BASENAME).$(LANG2).dix $(BASENAME).$(LANG1).tsx \
           $(BASENAME).$(LANG2).tsx  \
           $(PREFIX1).prob $(PREFIX2).prob \
           $(BASENAME).$(PREFIX1).t1x \
           $(BASENAME).$(PREFIX2).t1x \
           modes.xml

#           $(LANG1)-tagger-data/README $(LANG2)-tagger-data/README 

modes: modes.xml
	apertium-gen-modes modes.xml
	cp *.mode modes/

$(PREFIX1).mode: modes.xml 
	apertium-gen-modes modes.xml
	cp *.mode modes/

$(PREFIX2).mode: modes.xml 
	apertium-gen-modes modes.xml
	cp *.mode modes/

apertium_tgk_pesmodesdir=$(prefix)/share/apertium/modes/
apertium_tgk_pesdir=$(prefix)/share/apertium/apertium-$(PREFIX1)/
apertium_tgk_pes_DATA=$(PREFIX1).automorf.bin $(PREFIX2).automorf.bin \
                    $(PREFIX1).autobil.bin $(PREFIX2).autobil.bin \
                    $(PREFIX1).autogen.bin $(PREFIX2).autogen.bin \
                    $(PREFIX1).prob $(PREFIX2).prob \
		    $(PREFIX1).t1x.bin  \
		    $(PREFIX2).alpha.bin \
		    $(PREFIX2).t1x.bin \
	   	    $(PREFIX2).autopgen.bin \
		    $(PREFIX1).mode $(PREFIX2).mode 
		  
# $(PREFIX1).t2x.bin $(PREFIX1).t3x.bin
# $(PREFIX2).t2x.bin $(PREFIX2).t3x.bin 
#                    $(PREFIX1).autopgen.bin 
#                    $(PREFIX2).autopgen.bin 


install-data-local:
	$(prefix)/bin/apertium-gen-modes modes.xml apertium-$(PREFIX1)
	test -d $(DESTDIR)$(apertium_tgk_pesmodesdir) || mkdir $(DESTDIR)$(apertium_tgk_pesmodesdir)
	$(INSTALL_DATA) $(PREFIX1).mode $(DESTDIR)$(apertium_tgk_pesmodesdir)
	$(INSTALL_DATA) $(PREFIX2).mode $(DESTDIR)$(apertium_tgk_pesmodesdir)
	$(INSTALL_DATA) $(BASENAME).$(PREFIX1).t1x $(BASENAME).$(PREFIX2).t1x $(DESTDIR)$(apertium_tgk_pesdir)
	cp *.mode modes/

CLEANFILES = -r $(TARGETS_COMMON) 
