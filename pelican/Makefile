PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/../notionsandnotes-text-src
OUTPUTDIR=$(BASEDIR)/../www.notionsandnotes.org/public
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

FTP_HOST=localhost
FTP_USER=anonymous
FTP_TARGET_DIR=/

SSH_HOST=notionsandnotes
SSH_PORT=22
SSH_TARGET_DIR=/home/public

S3_BUCKET=my_s3_bucket

CLOUDFILES_USERNAME=my_rackspace_username
CLOUDFILES_API_KEY=my_rackspace_api_key
CLOUDFILES_CONTAINER=my_cloudfiles_container

DROPBOX_DIR=~/Dropbox/Public/

GITHUB_PAGES_BRANCH=notionsandnotes.org

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

IMGDIR=$(INPUTDIR)/images
COMPRESSEDIMGDIR=$(BASEDIR)/../compressedimgs
PNGS=$(wildcard $(IMGDIR)/*.png)
PNGCS=$(patsubst $(IMGDIR)/%.png, $(COMPRESSEDIMGDIR)/%.png, $(PNGS))
JPGS=$(wildcard $(IMGDIR)/*.jpg)
JPGCS=$(patsubst $(IMGDIR)/%.jpg, $(COMPRESSEDIMGDIR)/%.jpg, $(JPGS))
JPEGS=$(wildcard $(IMGDIR)/*.jpeg)
JPEGCS=$(patsubst $(IMGDIR)/%.jpeg, $(COMPRESSEDIMGDIR)/%.jpeg, $(JPEGS))

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make serve [PORT=8000]           serve site at http://localhost:8000'
	@echo '   make devserver [PORT=8000]       start/restart develop_server.sh    '
	@echo '   make stopserver                  stop local server                  '
	@echo '   make ssh_upload                  upload the web site via SSH        '
	@echo '   make rsync_upload                upload the web site via rsync+ssh  '
	@echo '   make dropbox_upload              upload the web site via Dropbox    '
	@echo '   make ftp_upload                  upload the web site via FTP        '
	@echo '   make s3_upload                   upload the web site via S3         '
	@echo '   make cf_upload                   upload the web site via Cloud Files'
	@echo '   make github                      upload the web site via gh-pages   '
	@echo '                                                                       '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html'
	@echo '                                                                       '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	cd $(OUTPUTDIR) && $(PY) -m pelican.server
endif

devserver:
ifdef PORT
	$(BASEDIR)/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/develop_server.sh restart
endif

stopserver:
	kill -9 `cat pelican.pid`
	kill -9 `cat srv.pid`
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

pre_upload: compressedimgs publish
	mkdir -p $(OUTPUTDIR)/pdfs
	echo 'Copying pdfs...'
	cp -r ../tex/*.pdf $(OUTPUTDIR)/pdfs/
	echo 'Compressing general files...'
	find $(OUTPUTDIR) \( -name '*.js' -o -name '*.css' -o -name '*.html' -o -name '*.txt' -o -name '*.pdf' -o -name '*.ttf' -o -name '*.ico' -o -name '*.eot' -o -name '*.otf' -o -name '*.svg' -o -name '*.xml' \) -exec gzip --best --force {} \;
	find $(OUTPUTDIR) -name "*~" -delete
	echo 'Replacing images with compressed version..'
	cp -f $(COMPRESSEDIMGDIR)/* $(OUTPUTDIR)/images/

ssh_upload: pre_upload
	scp -r $(OUTPUTDIR)/* $(SSH_HOST):$(SSH_TARGET_DIR)

rsync_upload: pre_upload
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

dropbox_upload: publish
	cp -r $(OUTPUTDIR)/* $(DROPBOX_DIR)

ftp_upload: publish
	lftp ftp://$(FTP_USER)@$(FTP_HOST) -e "mirror -R $(OUTPUTDIR) $(FTP_TARGET_DIR) ; quit"

s3_upload: publish
        s3cmd sync $(OUTPUTDIR)/ s3://$(S3_BUCKET) --acl-public --delete-removed --guess-mime-type

cf_upload: publish
	cd $(OUTPUTDIR) && swift -v -A https://auth.api.rackspacecloud.com/v1.0 -U $(CLOUDFILES_USERNAME) -K $(CLOUDFILES_API_KEY) upload -c $(CLOUDFILES_CONTAINER) .

github: publish
	ghp-import -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)

$(COMPRESSEDIMGDIR)/%.png: $(IMGDIR)/%.png
	pngcrush -q -fix -rem allb -reduce -brute -l 9  $< $@
	optipng -quiet -o7 $@
	advpng -q -z4 $@

$(COMPRESSEDIMGDIR)/%.jpeg: $(IMGDIR)/%.jpeg
	jpegtran -copy none -optimize -outfile $@ $<

$(COMPRESSEDIMGDIR)/%.jpg: $(IMGDIR)/%.jpg
	jpegtran -copy none -optimize -outfile $@ $<

compressedimgs: $(PNGCS) $(JPGCS) $(JPEGCS)
	echo 'Compressing images...'

.PHONY: html help clean regenerate serve devserver publish ssh_upload rsync_upload dropbox_upload ftp_upload s3_upload cf_upload github compressedimgs pre_upload
