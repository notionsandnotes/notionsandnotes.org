Title: The long road to building a static blog with pelican
Date: 2015-04-10 
Modified: 2014-04-29
Category: Tech/Web Development
Tags: pelican, python, built-texts, pelican-bootstrap3, render_math, LaTeX, Barry Steyn, Jinja2, LaTeX in pelican index
Slug: pelican-static-blog-setup
Status: published

[TOC]

<!-- PELICAN_BEGIN_SUMMARY -->
In this post it is documented how this blog was constructed as a static site, 
meaning, the webpages are served from storage and not generated dynamically upon
each visit using scripts (written for example in [php](http://php.net)) and
databases (e. g., [MySQL](https://mysql.com)).


-----------------------------

### Why a static site?

--------------------------------------

The obvious and ubiquitous software choice for blogging is [wordpress](http://wordpress.org),
a dynamic engine, which IMHO, is in several ways superior to other dynamic blogging services
such as [Google Blogger](https://www.blogger.com/), [Livejournal](www.livejournal.com/), 
[Tumblr](https://www.tumblr.com/docs/blog_management), etc., if nothing else for control 
of content. 

It would have been natural to stop there and take that route. However in a more insidious
manifestation of technophilia, a static blog was decided upon. There are many reasons,
which all basically comes down to simplicity, control, cost savings, and, 
*because I can do it*.

**The environment issue**

In wordpress, everything is web-based, and the content storage, database and scripts are 
all intermixed. Editing must take place in the wordpress editor or in custom 
[html](www.w3schools.com/html/)/[javascript](www.w3schools.com/js/)/[css](http://www.w3.org/Style/CSS/Overview.en.html)/[php](http://php.net).
This is all too much detail for the writer to be bothered about, if s/he wants
any degree of customization. Once the design is fixed, s/he should be able to focus
on the content without any distractions, and if design is to be changed, it should
be doable without disturbing the content files.
<!-- PELICAN_END_SUMMARY -->

The architectural issue with wordpress etc. here is that they confound the production and 
development environments. These should ideally be separate for a neat workflow. Instead,
the content writer is forced into undesired technical paraphernalia.

In contrast, static blogs compose their content using schema such as 
[Markdown](http://daringfireball.net/projects/markdown/)
or [reStructuredText](http://docutils.sourceforge.net/rst.html), which consist of:
(1), a plain text structured syntax for document markup, and, (2), a tool for
conversion to [HTML](www.w3schools.com/html/) or other web [markup languages](http://www.linfo.org/markup_language.html).
These are much simpler and much easier to control, and less susceptible 
to version changes.

There is no PHP or database setup required.  Deploying is simply copying the files
to a server, and so pre-publication testing is easy and can be done offline. 
Usually a small server script is provided alongside the static blog engine
for testing. Otherwise a low-footprint server such as [nginx](http://wiki.nginx.org/) 
can be run locally for this purpose.

Thus the problem of confounding development and production platforms is solved,
with nice [developer and testing sandboxes](http://www.agiledata.org/essays/sandboxes.html).

Also all this is very well-integrated with Linux, my favorite operating system,
a very important reason. Command line and text editing is my pasture and I
get to live in that habitat.

The hosting resources required for public deployment are very small, allowing
one to use very cheap hosts such as [NearlyFreeSpeech](http://nearlyfreespeech.net).
Outside the domain registration costs, the running costs come to less than $1
per month, which is a great saving!

This migration to static blogs is gaining more traction and it is increasingly
more popular, especially among developers and hackers (the latter not meaning computer
security criminals, but, followers of [hacker news](https://news.ycombinator.com/)). 
There are many static-site engines available by now, for example as described at
[staticgen](https://www.staticgen.com/). 

From among these, I was highly impressed
by [hexo](http://hexo.io/) based on [Node.js](https://nodejs.org). 
Nevertheless [pelican](https://github.com/getpelican/pelican) was chosen
instead, for, although being older, it is based on [Python](https://www.python.org),
a language which is of interest to me for a long time, given its ease of reading,
comparatively easy coding via libraries and above all its popularity for 
scientific and large-scale computing, in adapting to platforms such as 
[SAGE](http://sagemath.org). The other static blog  platforms such as 
[Jekyll](http://jekyllrb.com/) and [Octopress](http://octopress) were
discarded because I do not have time to learn another involved language such 
as [Ruby](https://www.ruby-lang.org/), when I had already been fixated on
Python. For good or bad, one can't vacillate for too long and pelican it 
is for the near future.

Markdown was chosen vs reStructuredText because various math and programming related sites such as 
[Stackoverflow](http://stackoverflow.com), [Math Stack Exchange](http://math.stackexchange.com)
and [Github](https://help.github.com/articles/github-flavored-markdown/) use it, and I am used to 
posting in it for this reason.

-----------------------------

### Setting up pip and virtualenv

--------------------------------------

It is expected that:

- The user is proficient in Linux and the terminal. 
- User is proficient in [bash](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html) and can work with python if necessary.
- User knows utilities such as `git`, `make`, `ssh`, `rsync` etc., and is familiar with web servers and markup.

`pip` is the python package installer. It takes care of all the Pythonic dependency hell. Use:

    :::console
    ~$ sudo apt-get install -y python-pip python-virtualenv virtualenvwrapper

We do not want to do any global python package installations from now onwards. The method is to use 
[virtual environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/) in which the user installs
packages inside a local directory and runs them through wrapper scripts. There can be multiple such environments and the user can switch back and forth between them, with parameters being different each time. This gives much flexibility for development.

Now we create the `virtualenv` named `pelican` for our blogging purposes.

    :::console
    $ mkvirtualenv pelican
    Running virtualenv with interpreter /usr/bin/python2
    New python executable in pelican/bin/python2
    Also creating executable in pelican/bin/python
    Installing setuptools, pip...done.
    (pelican)~$ 

Note the change in the `bash` prompt. Use `workon` and `deactivate` to activate/deactivate the python environment:


    :::console
    ~$ workon pelican
    (pelican)~$ deactivate
    ~$

This sequence will be part of the blogging workflow whenever required.


-----------------------------

### Installing pelican, themes and plugins

--------------------------------------


Install `pelican`:

    :::console
    ~$ mkdir ~/work/blog
    ~$ cd ~/work/blog
    ~/work/blog$ workon pelican
    (pelican)~/work/blog$ pip install pelican


It downloads and install many packages and finishes with:


    :::console
    Successfully installed pelican jinja2 blinker pygments docutils python-dateutil pytz six feedgenerator unidecode markupsafe
    Cleaning up...
    (pelican)~/work/blog$ 

Now we have pelican installed!

[![Pelican]({filename}/images/pelican.png)](https://github.com/getpelican/pelican)

Install additional packages:

    :::console
    (pelican)~/work/blog$ pip install Markdown beautifulsoup4 typogrify Pillow webassets

Create directory `pelican` and run `pelican-quickstart` to set up the pelican blogging platform inside it:

    :::shell-session
    (pelican)~/work/blog$ mkdir pelican
    (pelican)~/work/blog$ pelican-quickstart 
    Welcome to pelican-quickstart v3.5.0.
    
    This script will help you create a new Pelican-based website.
    
    Please answer the following questions so this script can generate the files needed by Pelican.
    
        
    > Where do you want to create your new web site? [.] pelican
    > What will be the title of this web site? Notions and Notes
    > Who will be the author of this web site? George S.
    > What will be the default language of this web site? [en] 
    > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) 
    > What is your URL prefix? (see above example; no trailing slash) http://www.notionsandnotes.org
    > Do you want to enable article pagination? (Y/n) 
    > How many articles per page do you want? [10] 
    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) 
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) 
    > Do you want to upload your website using FTP? (y/N) 
    > Do you want to upload your website using SSH? (y/N) y
    > What is the hostname of your SSH server? [localhost] notionsandnotes
    > What is the port of your SSH server? [22] 
    > What is your username on that server? [root] 
    > Where do you want to put your web site on that server? [/var/www] 
    > Do you want to upload your website using Dropbox? (y/N) 
    > Do you want to upload your website using S3? (y/N) 
    > Do you want to upload your website using Rackspace Cloud Files? (y/N) 
    > Do you want to upload your website using GitHub Pages? (y/N) 
    Done. Your new project is available at /home/george/work/blog/pelican


Note that, here, the full details of the ssh server are not provided. In my case, it is stored instead
in the `~/.ssh/config` file, as per [ssh config](http://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/)
directives. Replace it as necessary.

We do typesetting using Markdown. Under the `~/work/blog` directory, we store the site files 
in various subdirectories of the directory `raw`. The published site is stored under another 
directory `www.notionsandnotes.org`. As mentioned earlier, `pelican` directory stores the files
for pelican. So we have three subdirectories in total for the `blog` directory.

Now set up these two additional directories and also initialize [git](http://git-scm.com/documentation) to enable version control and rollbacks (if required):

    :::console
    (pelican)~/work/blog$ mkdir www.notionsandnotes.org
    (pelican)~/work/blog$ mv pelican/content ./raw
    (pelican)~/work/blog$ git init .
    (pelican)~/work/blog$ git add .
    (pelican)~/work/blog$ git commit -m "Initial commit"

Now to use pelican [themes](https://github.com/getpelican/pelican-themes) and [plugins](https://github.com/getpelican/pelican-plugins), clone these from github as [submodules](http://git-scm.com/book/en/v2/Git-Tools-Submodules):

    :::console
    (pelican)~/work/blog$ cd pelican
    (pelican)~/work/blog$ git submodule add https://github.com/getpelican/pelican-themes.git themes 
    (pelican)~/work/blog$ git submodule add https://github.com/getpelican/pelican-plugins.git plugins
    (pelican)~/work/blog$ cd ..
    (pelican)~/work/blog$ git -commit -m "Themes+Plugins"


-----------------------------

### Configuration file

--------------------------------------

There are two config files, `pelicanconf.py` and `publishconf.py`. We mostly work with the latter. 
Both are python files. Set the following configuration directives:

    :::python
    PLUGIN_PATHS = ['./plugins']
    PLUGINS = ['extract_toc','render_math','disqus_static','better_figures_and_images']
    MD_EXTENSIONS = ['codehilite','extra','smarty', 'toc']

We have included plugins for: [table of contents](https://github.com/getpelican/pelican-plugins/tree/master/extract_toc), [LaTeX rendering of math](https://github.com/barrysteyn/pelican_plugin-render_math), etc., and similar Markdown extensions are added too. The `toc` Markdown extension
is for example required for the `extract_toc` plugin. The "Better Figures and Images" plugin is taken [from Duncan Lock](http://duncanlock.net/blog/2013/05/29/better-figures-images-plugin-for-pelican/), 
whose site was most helpful for this pelican setup. Plugin [assets](https://github.com/getpelican/pelican-plugins/tree/master/assets) is for 
minification of javascript etc..

Now set the directives:

    :::python
    PATH = '../raw'
    OUTPUT_PATH = '../www.notionsandnotes.org/'
    STATIC_PATHS = ['extra', 'images', 'pdfs']
    EXTRA_PATH_METADATA = {
        'extra/robots.txt': {'path': 'robots.txt'},
        'extra/favicon.ico': {'path': 'favicon.ico'},
        'extra/htaccess': {'path': '.htaccess'}
    }

Create a [favicon](http://querbalken.net/add-favicon-to-my-adoption-of-pelican-theme-tuxlite_tbs-en.html) and [robots.txt](https://github.com/getpelican/pelican/wiki/Tips-n-Tricks) as required. A [custom 404 page](http://docs.getpelican.com/en/latest/tips.html) can be embedded via a
.htaccess configuration directive. [This](/404.html) is ours!

We use the `built-texts` theme and the following directives are added as data for it:

    :::python
    THEME = 'themes/built-texts'
    
    COLOPHON = True
    COLOPHON_TITLE = 'About'
    COLOPHON_CONTENT = "Mainly...."

Edit the [Makefile](http://www.gnu.org/software/make/manual/make.html) as follows:

    :::makefile
    INPUTDIR=$(BASEDIR)/../raw
    OUTPUTDIR=$(BASEDIR)/../www.notionsandnotes.org

Add in other parameters, such as the ssh hostname, as required.

-----------------------------

### Workflow

--------------------------------------


First, enable the virtual environment 'pelican' using 'workon' (and remember to 'deactivate' it later.
Posts are created and edited using plain text editors in files with *.md extensions, in Markdown format.
For example, these are the first few lines of the Markdown for this page:

    :::text
    Title: How this blog was set up using Pelican
    Date: 2015-04-10 
    Category: Tech
    Subcategory: Blogging
    Tags: pelican, python
    Slug: pelican-setup
    
    [TOC]
    
    **Table of contents**
    
    [TOC]
    
    In this post it is documented how this blog was constructed using a static 
    site maker, meaning, there is no server-side processing of data.

More details are available at the [Pelican Documentation](http://pelican.readthedocs.org/en/latest/quickstart.html)
website. The whole source of this website is uploaded to [a github repository](https://github.com/notionsandnotes/notionsandnotes.org)
where more examples and details may be found.

After the articles or pages are edited, the compilation and static site generation are done by `make html`.
Running `make devserver` will fire up a local server at `http://localhost:8000`, which can be used for
pre-publication viewing. Note that this will require fixing up of the `pelicanconf.py` file in addition 
to `publishconf.py` which was edited earlier. In particular, relative URLs to be enabled in pre-publication
mode in order for us to be able to follow links in the browser. 

After viewing, `Ctrl + C` will stop the server and return to shell.

For publication, run `make publish`, and later upload via `make rsync_upload`, which uploads only the
necessary files using 
[rsync](https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories-on-a-vps) + ssh.


-----------------------------

### Screenshots

--------------------------------------

Here are the screen captures of a first built of this site with a (slightly modified) built-texts theme, with some 
[css](http://www.w3.org/Style/CSS/Overview.en.html) additions.
The captures were done using a [Google Chrome extension by Peter Cole](http://mrcoles.com/full-page-screen-capture-chrome-extension/).

Index page screenshot:

[![index.html](/images/screenshot-index-bt-thumb.png)](/images/screenshot-index-bt.png) 
Click for expanding the thumbnail to actual size.
 

Below is the next screenshot of how the article on Lebesgue measure and construction via Caratheodory extension theorem,
was rendered. 

[![index.html](/images/screenshot-lebesgue-bt-thumb.png)](/images/screenshot-lebesgue-bt.png)
Click for actual size image.

Once or twice for small customizations I got stuck and two guys in the [pelican IRC chat](https://botbot.me/freenode/pelican/)
helped me out. Thanks, guys (if you are reading this)!

-----------------------------

### Moving to pelican-bootstrap3 theme and other improvements

------------------------------

The site by now looks good and is workable. I was however not satisfied yet.

The reason is that the web technologies are progressing fast and the current trend is responsive and mobile and tablet-ready
pages. The `built-texts` theme, although very good, was not up to date. Therefore it was decided to replace it with a more
modern and responsive theme. Some of the style customized for the PC screen may be lost, but the viewability in mobile and
touch devices and the more modern font and design are positives.

This time the [pelican-bootstrap3](https://github.com/DandyDev/pelican-bootstrap3) theme was chosen. There
were a few more responsive themes available; but this one was the most used and supported. 

Quite a good amount of tinkering was done to finally make this satisfactory. While the comparatively new 
[bootstrap3](http://getbootstrap.com) theme was more up-to-date, I was still influenced by some of the elegance
of the older `built-texts` theme. A few additions were my own ideas, too, on top of existing changes done
by others, among the foremost of which are [Tyler](https://github.com/tylerhartley/beneathdata) [Hartley's](http://beneathdata.com/) and 
[Christine](https://github.com/chdoig/pelican-bootstrap3-lovers) [Doig's](http://chdoig.github.io) sites.

The most important decision was to use the [Bootswatch](https://bootswatch.com/) theme [readable](https://bootswatch.com/readable/).
This site is meant to be for expository and rigorous articles on pure mathematics and it is of foremost
importance to ease the user's eye when staring the screen for a long time.

There were a lot of settings for the `pelican-bootstrap3` scheme and these were pushed into a separate
file `themeconf.py` and called via an `import` directive. So, in that file, the setting was:

    :::python
    BOOTSTRAP_THEME = 'readable'

#### Menus

The menus on the top navbar were added by a small bit of pythonic tinkering in the [Jinja2](http://jinja.pocoo.org) template:

    :::console
    (pelican)~/work/blog/pelican$ vim plugins/pelican-bootstrap3/templates/article_list.html

Write something like:

    :::text
    {% if DISPLAY_CATEGORIES_ON_MENU %}
      {% for cat, cat_articles in categories %}
        <li class="dropdown {% if cat == category %}active{% endif %}">
        <a href="#" class="dropdown-toggle" id="menu-{{ cat }}" data-toggle="dropdown" >
        {{ cat }}
        <span class="caret"></span>
        </a>
         <ul class="dropdown-menu" role="menu">
         {% for cat_article in cat_articles %}
            <li><a href="{{ SITEURL }}/{{ cat_article.url }}">{{ cat_article.title }}</a></li>
         {% endfor %}
         </ul>
        </li>
      {% endfor %}
    {% endif %}

Similarly, make a menu on the right side of navbar for the pages was added. 

#### Other additions

Another thing to be enabled soon was a commenting system via disqus. This is explained on 
the documentation page.

The save pages were modified, and subcategories were added. 
A little change in the code was required for this to enable
a new `subpath' metadata, as in [this github patch](https://github.com/vpiotr/pelican-plugins/commit/1de663785fba8a80bb0f21045c7e7034caddf324).

Some Jinja2 alternations made are: a custom article sidebar and individual sidebar 
for each article in the indexes, different sidebar for pages, some font-awesome and 
glyphicon additions, etc.. This was altogether done in a haphazard manner as this 
is my first encounter with any templating language. 

The `readable` bootswatch theme had a problem, of having black links and so it was impossible to locate the links.
So link colors were modified to a shade of blue using the `custom.css` file, which was included in `pelicanconf.py` 
as `EXTRA_PATH_METADATA`. [Here](/custom.css) is the whole source.

Some color and other style changes in were incorporated into `extra.css`.
For example, the "more ..." button text for article summary ending in 
indexes was highlighted and enlarged. In `templates/article_list.html`:

    :::text
    <br><a class="btn btn-default btn-small" id="readmore" href="{{ SITEURL }}/{{ article.url }}"> Read more ...</a>

and in `extra.css`:

    :::
    #readmore {
      font-size: 17px;
      font-weight: bold;
      color: #003380;
      background-color: #CCFFCC;
    }

A few more things were added to `extra.css`, to change the heading font style to small caps, to 
change some foreground and background colors, to change font sizes for some cases, and to
highlight code differently.

To the Jinja2 templates, a few other additions were made too, like a custom footer
with colophon, background image, a tag cloud, and a tweets widget. Funnily, 
more than an hour was spent trying to fix this widget, only to realize in 
the end that the browser adblock plus extension was blocking it!

The whole source code is available on a [github repository](https://github.com/notionsandnotes/notionsandnotes.org) for 
examination if required. All the customizations so far were all implemented by self,
with one notable exception that required intervention of a professional developer:


-----------------------------

### Barry Steyn updates pelican render_math plugin for index pages

-----------------------------

This is supposed to be a pure mathematics blog, and so display of math is extremely important.

It was implemented using the very helpful [render_math](https://github.com/getpelican/pelican-plugins/tree/master/render_math)
plugin to display math. It made use of [MathJaX](https://www.mathjax.org/) to display mathematics encoded in the
[LaTeX](http://www.latex-project.org/) typesetting markup language.

This had one small glitch however. The article summaries in `index.html` of the base directory, or other indexes for
authors, tags, categories and so on, failed to render math correctly using MathJaX.

That was how I made [my first post in Github](https://github.com/barrysteyn/pelican_plugin-render_math/issues/19). I had originally imagined
that I must have missed something trivial and it was a bold step for me. The author, [Barry Steyn](https://doctrina.org), responded
promptly and offered a solution, which he also said was not completely trivial like I feared before daring to submit an issue. Moral: 
[Don't be so shy!!](http://en.wikipedia.org/wiki/Social_anxiety_disorder)

He kept to his word and [updated the plugin](https://github.com/barrysteyn/pelican_plugin-render_math) which I cloned
and verified to be working.

Thanks a lot, man!! This addition beautifies me (and this site) a lot, considering the future plans to upload many more Math articles.

See also: [Barry Steyn's pelican LaTeX plugin page](http://doctrina.org/Plugin-For-Pelican-To-Enable-Latex.html).


-------
### Final comments
-------

It took altogether longer than expected, but was an intensive and beneficial (hopefully) journey. This page was titled, *Long Road*,
to be reminiscent of [Grothendieck's Long March](http://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/LM/tableLM.pdf),
but of course no claims to such greatness or even mere competence are made here!! And, as for the reference, this is 
certainly meant to be a pure mathematics focus blog and one might go the whole mile and allude to mathematical references
even in tech posts!

This website domain was registered on an impulse on July 11, 2014, but due to intervening turbulent personal life,
it took me up to April 2015 to turn back to finally act upon site building. So, maybe, it was indeed a long march!

Any suggestions for improvement are welcome, from web designers and pelican aficionados in particular. Thank you!

===========
===========
###The end (Or is it?)
===========
===========

