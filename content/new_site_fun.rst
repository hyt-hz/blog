关于新网站
##########

:date: 2013-10-13 23:05
:tags: life, web
:category: life
:author: Yiting Huang
:summary: 折腾新网站，域名，DISQUS，webmaster，analytics
:slug: 折腾新网站

这几天花了不少时间在这个新网站上，互联网时代，网上廉价和免费的资源不少，但和开源软件一样，都不免会有些折腾，\
还好，折腾新鲜物件也是一种乐趣。

域名
----

首先是域名，域名一直都是白菜价，个人网站，自然应该有一个属于自己的闪闪亮的域名，本着开放，自信，大气，高端的原则，我决定直接\
用自己的名字，但只恨下手晚了，已经被注册了，所以就有了现在这个名前姓后的全拼域名，`yitinghuang.com`_，就当是与国际接轨了。\
说到买域名，自然是大名鼎鼎的godaddy了，虽然国内也有万网之类的服务商，不过看过知乎上的这个\ `提问`_\ ，相信大家都会断了用国内服务的念想。\
其实懂点英文，godaddy上点点并不难，而且人还贴心的提供了支付宝付款；不过因为是国外的，网页打开还是慢了点。

.. _yitinghuang.com: http://yitinghuang.com
.. _提问: http://www.zhihu.com/question/19673386

Github pages支持自定义域名，而且很方便，首先在domain host也就是godaddy上添加一条A record，将\ `blog.yitinghuang.com`_，也就是我\
博客的domain，指向github的服务器的IP：204.232.175.78，接着在相应的github project（即\ `github.com/hyt-hz/blog`_\ ）\
的gh-pages branch中添加一个CNAME文件，填写前面设置的域名，即blog.yitinghuang.com，这样github就知道\ `blog.yitinghuang.com`\
是当前的\ `github project page`_\ 的一个别名。虽然在设置A record的时候godaddy夸张的表示域名配置生效最长需要48小时，但我马上就能访问\
新域名了。

.. _blog.yitinghuang.com: http://blog.yitinghuang.com
.. _github.com/hyt-hz/blog: https://github.com/hyt-hz/blog
.. _github project page: http://hyt-hz.github.io/blog

但我高兴的太早了，真正的折腾还在后面。`blog.yitinghuang.com`_\ 是成功启用了，但www.yitinghuang.com和yitinghuang.com仍然\
是无法解析的，这显然是不能接受的。也许以后我会需要那这两个域名做点别的什么，不过现在我希望它们能指向我的博客，这儿就有两个options，\
一是设置CNAME，将它们都变成\ `blog.yitinghuang.com`_\ 的别名，二是用301/302重定向。github不支持第一个选项，所以只能用重定向。\
godaddy支持域名重定向，但是配置的入口并不那么显而易见，在配置了重定向forwarding后，发现还需要手动添加A record将需要重定向的域名\
指向godaddy指定的IP（应该就是godaddy用来做重定向服务的服务器IP），一切就绪后，我就开始了漫长的等待，但是奇迹没有发生，重定向\
没有发生。不甘心的我又尝试了其他配置，但一直不成功，直到我尝试ping了一下godaddy提供的IP，惨不忍睹阿，一个都ping不通，这是被墙了阿。\
**我又被GFW给耍了**。

godaddy算是被废了，只能换domain host了。DNSPod在国内算是最火的了，于是决定尝试一下，但是又马上就放弃了，因为启用重定向功能需要\
验证我的手机号，no way，就算你国内速度再快，我也没兴趣。又是一阵搜索，发现\ `namecheap`_\ 是个不错的选择，不需要transfer也可以免费\
host其他地方购买的域名，支持重定向，也没被墙，设置还简单。于是在godaddy上把Nameservers全部指向namecheap的服务器，\
同时在namecheap上简单一设，重定向就这么成了。接下来就要祈祷GFW不要把namecheap给墙了。

.. _namecheap: http://namecheap.com

DISQUS
------

DISQUS_\ 是国外一个很火的评论服务，在任何网页中插入DISQUS的JS代码，就能添加一个漂亮的评论框。DISQUS后台是基于Django开发的，所有评论\
也都是由DISQUS负责存放，对于向我这样希望添加评论功能，但又没有后台数据库的静态页面站点来说，无疑是个福音，更何况pelican以及我使用的theme\
都充分考虑了DISQUS的集成，添加起来并不费尽，只需去DISQUS网站注册一下我的博客网站，并设置在pelican中配置一下DISQUS_SITENAME这个变量，\
我的博客就有评论功能了。

虽然DISQUS在国外如日中天，我逛过的不少老外博客，以及一些商业网站都有使用，但是在国内却基本见不到踪影，和其他国外流行的web service一样，\
网速，本地化，还有政策风险阻碍了它在国内的发展，同时也一如既往，DISQUS在国内有好几个山寨版，有兴趣大家可以去搜一搜。

.. _DISQUS: http://disqus.com/

Google Webmaster
----------------

说到google就绕不开GFW，现在GFW对付google的招式非常之下三烂。不像facebook或twitter，GFW并没有直接封杀google，而是抽风的断连接,\
也不管有没有敏感词，google的页面，连几下就会断，想在google上做点事，那是需要极大的耐心和勇气，说不准搞了一半，就被reset了，然后就是\
漫长的等待，直到又能连上。这样的结果，就是baidu的崛起。

吐槽无益，继续正题。`Google Webmasters`_\ 可以帮助站长查看自己网站被google的收录和索引情况，好奇的我自然非常希望了解一下。但是要查看\
这些信息，你必须证明你是站长，验证方法有多个，比如关联domain host，插条特定DNS record等，我选择了插入google analytics服务。\
刚建的网站google自然还没有收录，你可以等google的爬虫什么时候爬到你家，也可以在webmaster上手动提交请求，让google来爬一爬，\
我提交了一下，google已经顺索引了这个博客。

百度也有个对应的服务，叫百度站长，有机会也去捣腾一下。

.. _Google Webmasters: http://www.google.com/webmasters/

Google Analytics
----------------

上面已经提到了\ `Google Analytics`_\ ，这个工具可以提供如网站流量，网站访问来源（如搜索引擎，其他地方的连接等）等的统计信息，以及\
再次基础上的分析，这个工具对商业网站应该是非常重要的。

若是希望google帮你统计这些信息，那就需要在网站的每一个页面植入google提供的JS代码，同样，pelican也考虑到了这个，因此集成也不难，\
需要的是耐心到google页面注册，并获取一个对应自己网站的key，并配置到pelican。Google提供的这些JS据说都是异步获取和载入的，\
虽然国内访问google时断时续，速度也不好，但是我观察下来，加入这些GA服务后，并没有明显影响博客的加载速度。

百度自然也不会拉下，对应的有个叫做百度统计的服务。

.. _Google Analytics: http://www.google.com/analytics/

另外
----

对于一个有些网站来说，以上折腾的这些只能算是些皮毛，但是对于非营利的个人博客网站，应该也就够了，什么SEO之类我就不研究了。接下来\
就是要督促自己勤快一点，多多写博。
