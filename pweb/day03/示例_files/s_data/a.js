function checkType(a,b){return!!a&&a.nodeType==b}function isObject(a){return"object"==typeof a}function isWindow(a){return null!=a&&a==a.window}function isPlainObject(a){return isObject(a)&&!isWindow(a)&&"isPrototypeOf"in a&&"[object Object]"===Object.prototype.toString.call(a)}function hasClass(a,b){if(!checkType(a,nodeType)||!a.className||!b)return!1;var c,d=a.className.split(" ");for(c=0;c<d.length;c++)if(d[c]===b)return!0;return!1}function isArray(a){return"[object Array]"===Object.prototype.toString.call(a)}function extend(a,b,c){for(key in b)c&&(isPlainObject(b[key])||isArray(b[key]))?(isPlainObject(b[key])&&!isPlainObject(a[key])&&(a[key]={}),isArray(b[key])&&!isArray(a[key])&&(a[key]=[]),extend(a[key],b[key],c)):void 0!==b[key]&&(a[key]=b[key]);return a}function setAttribute(a,b,c){null==c?a.removeAttribute(b):a.setAttribute(b,c)}function IEContentLoaded(a,b){var c=a.document,d=!1,e=function(){d||(d=!0,b())};!function(){try{c.documentElement.doScroll("left")}catch(a){return void setTimeout(arguments.callee,500)}e()}(),c.onreadystatechange=function(){"complete"==c.readyState&&(c.onreadystatechange=null,e())}}var idExpr=/^(?:\s*(<[\w\W]+>)[^>]*|#([\w-]*))$/,classTagExpr=/^(?:#([\w-]+)|(\w+)|\.([\w-]+))$/,version="2.0.1";$=window._J=function(a,b){return new _J.fn.init(a,b)},_J.fn=_J.prototype={getElementsByClassName:function(a,b,c){var d=[],e=(b||document).getElementsByTagName(c||"*"),f=e.length,g=new RegExp("(\\s+|^)"+a+"(\\s+|$)");for(i=0,j=0;i<f;i++)g.test(e[i].className)&&(this[j]=d[j]=e[i],j++);return d},find:function(a,b){var c=this.getElementsByClassName(a,this[0],b),d=c.length;for(i=0;i<d;i++)this[i]=c[i],this.length=i+1;return this},addClass:function(a){for(var b=this.length,c=0;c<b;c++){var d=this[c];if(!checkType(d,nodeType)||!a)return;if(!d.className)return void(d.className=t);hasClass(d,a)||(d.className+=" "+a)}return this},remove:function(){for(var a=this.length,b=0;b<a;b++){var c=this[b];if(!checkType(c,nodeType))return;c&&c.parentNode&&c.parentNode.removeChild(c)}},removeClass:function(a){for(var b=this.length,c=0;c<b;c++){var d=this[c];if(!checkType(d,nodeType)||!d.className||!a)return;var e=d.className.split(/\s+/g),f=0;for(f=0;f<e.length&&a!==e[f];f++);e.splice(f,1),d.className=e.join(" ")}return this},hasClass:function(a){return this.length>0&&hasClass(this[0],a)},each:function(a){for(var b=0;b<this.length;b++)a(this[b],b);return this},on:function(a,b){for(var c=0;c<this.length;c++){var d=this[c];d.addEventListener?d.addEventListener(a,b,!1):d.attachEvent&&d.attachEvent("on"+a,b)}return this},off:function(a,b){for(var c=0;c<this.length;c++){var d=this[c];d.removeEventListener?d.removeEventListener(a,b,!1):d.detachEvent&&d.detachEvent("on"+a,b)}return this},attr:function(a,b){var c;return"string"!=typeof a||1 in arguments?this.each(function(c){if(1===this.nodeType)if(isObject(a))for(key in a)setAttribute(this,key,a[key]);else setAttribute(this,a,funcArg(this,b,c,this.getAttribute(a)))}):this.length&&1===this[0].nodeType?!(c=this[0].getAttribute(a))&&a in this[0]?this[0][a]:c:void 0},width:function(){if(0!=this.length)return this[0].offsetWidth},style:function(){if(0!=this.length)return this[0].style},html:function(){return 0==this.length?this:arguments&&arguments.length>0?(this[0].innerHTML=arguments[0],this):this[0].innerHTML},animate:function(a,b,c,d,e,f){function g(a,b,c,d){return c*((a=a/d-1)*a*a+1)+b}for(var h=(new Date).getTime(),i=0;i<this.length;i++){var j=this[i];setTimeout(function(){var i=parseInt(((new Date).getTime()+d-h)/d);j.style[a]=Math.floor(g(i,b,c,20))+e,i>=20?(j.style[a]=b+c+e,f&&f()):setTimeout(arguments.callee,d)},d)}return this}},_J.fn.init=function(a,b){b&&(b=b.length>0?b[0]:b);var c=b||window.document;if("string"==typeof a){if("<"===a[0]&&">"===a[a.length-1]&&a.length>=3?match=[null,a,null]:match=idExpr.exec(a),match&&match[1]){var d=document.createElement("div");return d.innerHTML=a,this[0]=d.childNodes[0],this.length=1,this.context=c,this.selector=a,this}if(match&&match[2]){var d=document.getElementById(match[2]);return d&&d.parentNode&&(this.length=1,this[0]=d),this.context=c,this.selector=a,this}match=classTagExpr.exec(a);var e=void 0;match[2]?e=c.getElementsByTagName(match[2]):match[3]&&(e=c.getElementsByClassName?c.getElementsByClassName(match[3]):_J(c).getElementsByClassName(match[3],c));for(var f=0;f<e.length;f++)this[f]=e[f];return this.length=e.length,this.context=c,this.selector=a,this}return a&&a.nodeType?(this[0]=a,this.length=1,this):(this.length=0,this)},_J.fn.init.prototype=_J.prototype,_J.extend=_J.fn.extend=function(a,b,c){return 1===arguments.length&&(b=a,a=this),extend(a,b,c),a},_J.extend({timeStamp:+new Date,getScript:function(a,b){var c=document.createElement("script");c.type="text/javascript",c.src=a,c.onload=c.onreadystatechange=function(){this.readyState&&"loaded"!==this.readyState&&"complete"!==this.readyState||(document.getElementsByTagName("head")[0].removeChild(c),b&&b())},document.getElementsByTagName("head")[0].appendChild(c)},jsonp:function(a,b){b=!!b||"callback";var b=(a.data,"dsp_"+this.timeStamp++);window[b]=function(b){a.callback(b)};var c=a.url.indexOf("?"),d=a.url+(c>-1?"&":"?")+"callback="+b+"&r="+ +new Date;this.getScript(d,function(){window[b]=void 0;try{delete window[b]}catch(a){}})},clone:function(a){return extend({},a,!0)},template:function(a,b){var c=function(a){var b,d=[],e=[];for(b in a)d.push(b),e.push(a[b]);return new Function(d,c.$).apply(a,e)};if(!c.$){c.$='var $=""\n';for(var d=a.replace(/[\r\t\n]/g," ").replace(/\s+/g," ").split("%>"),e=0;e<d.length;){var f=d[e],g=f.indexOf("<%");"="==f.charAt(g+2)?(c.$+="$+='"+f.substr(0,g).replace(/\'/g,"\\'")+"'\n",c.$+="$+="+f.substr(g+3)+"\n"):g>=0?(c.$+="$+='"+f.substr(0,g).replace(/\'/g,"\\'")+"'\n",c.$+=f.substr(g+2)+"\n"):c.$+="$+='"+f.replace(/\'/g,"\\'")+"'\n",e++}c.$+="return $"}return b?c(b):c},GetQueryString:function(a){var b=new RegExp("(^|&)"+a+"=([^&]*)(&|$)","i"),c=window.location.search.substr(1).match(b);return null!=c?c[2]:null},nano:function(a,b){return a.replace(/\{([\w\.]*)\}/g,function(a,c){for(var d=c.split("."),e=b[d.shift()],f=0,g=d.length;f<g;f++)e=e[d[f]];return void 0!==e&&null!==e?e:""})},getProtocol:function(){return"https:"==document.location.protocol?"https:":"http:"},sendExposals:function(a){if(isArray(a))for(var b=0,c=a.length;b<c;b++)this.sendExposals(a[b]);"string"!=typeof a||/^\s*$/g.test(a)||this.createImg(a)},createImg:function(a){var b=new Image;b.onload=b.onerror=function(){b=null},b.src=a}});var nodeType=1;document.ready=function(a){document.addEventListener?document.addEventListener("DOMContentLoaded",function(){document.removeEventListener("DOMContentLoaded",arguments.callee,!1),a()},!1):document.attachEvent&&IEContentLoaded(window,a)};
/*! jdtpl last edit: 2017-12-12|14:54:20 */
$.extend({getNowTime:function(){var a=new Date,b=a.getFullYear(),c=a.getMonth()+1,d=a.getDate(),e=a.getHours(),f=a.getMinutes(),g=a.getSeconds();return b+"-"+c+"-"+d+" "+e+":"+f+":"+g},enabled:function(a){var b=!1;return"string"==typeof this.get(a)?b=!0:b},set:function(a,b,c){var c=c||{};if(c.domain=c.domain||"",c.path=c.path||"/",c.expires=c.expires||31536e6,"number"==typeof c.expires){var d=new Date;d.setTime(d.getTime()+c.expires)}document.cookie=a+"="+b+";expires="+d.toGMTString()+(c.domain?";domain="+c.domain:"")+";path="+c.path},get:function(a){var b,c=encodeURIComponent(a)+"=",d=document.cookie.indexOf(c),e=null;return d>-1&&(b=document.cookie.indexOf(";",d),-1==b&&(b=document.cookie.length),e=decodeURIComponent(document.cookie.substring(d+c.length,b))),e},remove:function(a){this.set(a,"",{expires:-3600})},uuid:function(){return(new Date).getTime()+""+parseInt(2147483647*Math.random())},initjda:function(){var a=this;if(!a.enabled("__jda")){var b,c;c=Date.parse(new Date).toString().substring(0,10),b="."+a.uuid()+"."+c+"."+c+"."+c+".0",a.set("__jda",b,{expires:15552e6,domain:".jd.com"})}}});
/*! jdtpl last edit: 2017-12-12|14:54:20 */
var _Jconf={priceInterface:"//px.3.cn/prices/mgets?skuids={skuids}&type=1",promoload:"//pf.3.cn/flags/mgets?skuids={skuids}&type=1",imagePrefix:"//img1.360buyimg.com/imgb/",picImgPrefix:"//img1.360buyimg.com/pop/",logo:{width:100,height:20,src:"logoCir40.gif"},imageSize:500,width:500,height:500,needNum:0,layoutNeedNum:0,layoutColNum:0,layoutRowNum:0,styleCss:{borderColor:"#c81623",borderWidth:1},data:{},protocol:"http:",exposes:{}};
/*! jdtpl last edit: 2017-12-12|14:54:20 */
!function(a){a.fn.turns=function(a){for(var b=0;b<this.length;b++)this.turns=new c(a,this[b]);return this};var b={interval:3e3,start:0,gsize:1,contName:".item",navigation:{active:!0,effect:"slide"},pagination:{active:!0,effect:"fade",interact:"hover"},effect:{slide:{speed:500},fade:{speed:1e3}}},c=function(c,d){var c=a.extend(b,c,!0);this.conts=a(c.contName,d),this.tags=a(c.tagName,d),this.options=c,this.interval=c.interval,this.gsize=c.gsize,this.pos=0,this.timer=null,this.size=this.conts.length,this.start(c.start),this.eventBind(a(d),this.tags,this.conts),this.eventBindForTouch(a(d),this.tags,this.conts)},d=_Jconf.exposes;c.prototype={start:function(a){this.auto=!0;var b=this;this.play(a,"next"),this.timer=setInterval(function(){b.next()},b.interval)},play:function(a,b,c){"slide"==this.options.navigation.effect?this.slide(a,b):this.fade(a,b)},show:function(b){this.turnsReset(),this.turnsInnerReset(),a(this.conts[b]).addClass("current"),a(this.tags[b]).addClass("select");for(var c=0;c<this.gsize;c++)this.exposal(this.conts[b])},slide:function(b,c){var d=this.tags[b];this.turnsReset(),this.turnsInnerReset();for(var e=this.conts[b],f=this.conts[(b-1+this.size)%this.size],g=this.conts[(b+1)%this.size],h=0;h<this.gsize;h++)this.exposal(this.conts[b]);a(e).addClass("current"),a(g).addClass("current"),a(f).addClass("current"),a(d).addClass("select");var i=this,j=0,k=e.offsetWidth;e.style.opacity=1,g.style.opacity=1,f.style.opacity=1,"prev"==c?(change=k,j=-k,e.style.left=-k+"px",g.style.left=0,f.style.left=-2*k+"px"):(change=-k,j=k,e.style.left=k+"px",g.style.left=2*k+"px",f.style.left=0);var l=this.options.effect.slide.speed/20;a(e).animate("left",j,change,l,"px",function(){e.style.left=j+change+"px"}),a(g).animate("left",j+k,change,l,"px",function(){g.style.left=j+k+change+"px"}),a(f).animate("left",j-k,change,l,"px",function(){f.style.left=j-k+change+"px",a(".jdAdPrevious").off("mousedown",i.levt).on("mousedown",i.levt),a(".jdAdNext").off("mousedown",i.revt).on("mousedown",i.revt)}),a(".page").html(b+1),a(a(".priceItem")[b]).removeClass("disNone")},fade:function(b,c){var d=this.conts[b],e=this.tags[b];this.options.effect.fade.speed;this.turnsReset(),this.turnsInnerReset(),a(e).addClass("select"),a(d).addClass("current").addClass("jdAdShow"),d.style.left=0;for(var f=0;f<this.gsize;f++)this.exposal(this.conts[b])},next:function(){this.pos++,this.pos%=this.size;this.play(this.pos,"next")},prev:function(){this.pos--,this.pos=(this.pos+this.size)%this.size;this.play(this.pos,"prev")},stop:function(){clearInterval(this.timer)},turnsReset:function(){this.conts.removeClass("current").removeClass("jdAdShow"),this.conts.each(function(a){a.style.left=0,a.style.opacity=1}),this.tags.removeClass("select"),a(".priceItem").addClass("disNone")},turnsInnerReset:function(){a(".jdAdInfo",this.conts[this.pos]).removeClass(".jdAdInfoShow")},exposal:function(b){this.skuImgItem=a(".skuImg"),a(b).each(function(b,c){for(var e=a(b).find("skuImg"),f=0,g=e.length;f<g;f++)if(!e[f].getAttribute("data-done")&&(e[f].src=e[f].getAttribute("data-src"),e[f].setAttribute("data-done","1"),!_Jconf.exposal_urls||""==_Jconf.exposal_urls)){var h=e[f].getAttribute("data-exposal");void 0===d[h]&&(a.sendExposals(h),d[h]=1)}})},eventBind:function(b,c,d){var e=this;b.on("mouseover",function(a){e.stop()}),b.on("mouseout",function(a){e.stop(),e.timer=setTimeout(function(){e.start(++e.pos%e.size)},1e3)}),this.levt=function(b){a(".jdAdPrevious").off("mousedown",e.levt);var c=b||window.event;c.preventDefault&&c.preventDefault(),e.stop(),e.prev()},this.revt=function(b){a(".jdAdNext").off("mousedown",e.revt);var c=b||window.event;c.preventDefault&&c.preventDefault(),e.stop(),e.next()},!0===this.options.navigation.active&&(this.auto=!1,a(".jdAdPrevious").on("mousedown",this.levt),a(".jdAdNext").on("mousedown",this.revt));var f=function(a){var b=this.getAttribute("index");return e.pos!=b&&(e.pos=b,e.turnsReset(),e.stop(),"slide"==e.options.pagination.effect?e.slide(b):e.fade(b),!1)},g=function(a){e.stop(),e.turnsReset(),e.pos=this.index,e.fade(this.index)};if(!0===this.options.pagination.active)if("hover"===this.options.pagination.interact)for(var h=0;h<c.length;h++)c[h].index=h,c[h].onmouseover=g;else"click"===this.options.pagination.interact&&c.on("click",f)},eventBindForTouch:function(a,b,c){var d,e=this,f={x:0,y:0},g=null,h=function(a){var b=a.touches[0];f={x:b.pageX,y:b.pageY},e.stop()},i=function(a){if(!(a.touches.length>1||a.scale&&1!==event.scale)){var b=a.touches[0];d={x:b.pageX-f.x,y:b.pageY-f.y}}},j=function(a){e.stop(),d&&(d.x<-10&&Math.abs(d.y/d.x)<1?e.next():d.x>10&&Math.abs(d.y/d.x)<1&&e.prev(),clearTimeout(g),g=setTimeout(function(){e.stop(),e.start((e.pos+1)%e.size)},e.interval),d=null)};a.on("touchstart",h),a.on("touchmove",i),a.on("touchend",j),a.on("touchcancel",j)}}}(_J);
/*! jdtpl last edit: 2017-12-12|14:54:20 */
!function(a,b){function c(){b.width=document.documentElement.clientWidth||t.width,b.height=document.documentElement.clientHeight||t.height,b.imageSize=b.width>b.height?b.height:b.width}function d(){b.data=t.Query[t.adid],b.protocol=a.getProtocol(),b.exposal_urls=t.Query.exposal_urls,b=a.extend(t,b)}function e(){var a=b.width,c=b.height,d=a/c,e=c/a,f=1,g=function(d){if(1==d||c>a){if(a<=200&&(b.logo.src="logoLsmall.jpg"),b.logo.style="height:20px;",b.logo.imgStyle="#logo img{height:100%}",a<200&&(b.logo.imgStyle+="#logo img{margin-left:"+(a-200)/2+"px;}"),b.logo.imgStyle+=".skuName{display:none}",b.logo.imgStyle+=".skuAdContent{display:none}",b.logo.imgStyle+=".skuPriceInner{display:none}",e>1.4&&e<2)b.logo.imgStyle+=".inner .item{ margin-top:22px;}.skuLink{ height:"+(c-22)+"px;}",b.logo.imgStyle+=".skuLink{ height:"+(c-22)+"px;display:block}",b.logo.imgStyle+=".skuAdContent{display:block; height:22px; padding:0 5px; overflow:hidden; text-align:center;color:#e4393c; font-size:14px}",b.logo.imgStyle+=".item .skuInfo{bottom:36px!important}";else if(e>2){var g=Math.ceil(b.data.length/f),h=(a-40)/g,i=(a-30-g*g)/g;b.logo.imgStyle+=".inner .item{ margin-top:22px;}",b.logo.imgStyle+=".left, .right{ display:none}",b.logo.imgStyle+=".skuLink{display:block;position:relative}",b.logo.imgStyle+=".jdPrice{display:none}",b.logo.imgStyle+=".jdAdIndex{display:none}",b.logo.imgStyle+=".skuPriceInner{display:block;text-indent:5px}",b.logo.imgStyle+=".inner .numTag{display:block; position:absolute; bottom:0; left:0}",b.logo.imgStyle+=".inner .numTag li{float:left; width:"+h+"px;height:5px; font-size:0; overflow:hidden; background:#ccc; margin-left:"+i+"px; cursor:pointer}",b.logo.imgStyle+=".item .skuInfo{height:22px!important}",b.logo.imgStyle+=".inner .numTag .select{background:#DF3939}"}}else{b.logo.src="logoSm.jpg",b.logo.style="background-color:#c91521;display:block;height:"+c+"px;";var j=(a-92)/f;b.logo.imgStyle="#logo img{margin-top:"+(c-90)/2+"px} .inner{margin-left:90px;}.skuLink{overflow:hidden;width:"+(j-1)+"px;_width:"+(Math.floor(j)-1)+"px;border-left:1px solid #fff;}#tpl .item .bg-shadow{display:block; position:absolute;height:22px;background-color:#000;filter:alpha(opacity=30); /*IE */-moz-opacity:0.3; /* 老版Mozilla */-khtml-opacity:0.3; /* 老版Safari */opacity: 0.3; /* 支持opacity的浏览器*/} #tpl .item .skuInfo{ z-index:1; height:22px;line-height:22px;text-indent:5px;}#tpl .skuPriceInner{color:#fff}",b.logo.imgStyle+=".jdPrice{display:none}",b.logo.imgStyle+=".jdAdIndex{display:none}",b.logo.imgStyle+=".skuName{display:none}",b.logo.imgStyle+=".skuAdContent{display:none}",b.layoutType="longLine"}};return a>c?(b.showLayoutType="row",f=d>1.9&&d<5?Math.floor((a-92)/c):d>=5?Math.floor((a-92)/c):1):(b.showLayoutType="col",f=e>1.9?Math.floor(e):1),g(f,e),b.colShowSkuNum=f,f}function f(a,b){var c=b.length,d=c,e=b;return a>1&&(mod=c%a,quotients=Math.ceil(c/a),quotients=quotients>1?quotients:quotients+1,0!==mod&&(d=quotients*a,e=g(b,d))),e}function g(a,b){var c=[],d=a.length;if(c=a.slice(0,b),d<b)for(;b-d>0;)for(var e=0;e<d&&!(b-d<=0);e++)c.push(a[e]),b--;return c}function h(c){var d=[],g=[],h=[],i=[],j="",k="",l=b.colShowSkuNum=e();c=f(l,c),template='         <a class="skuLink"  href="{click_url}" target="_blank" title="{ad_title}">                     <img class="skuImg" data-exposal="{exposal_url}" data-src="{protocol}{imagePrefix}s{imageSize}x{imageSize}_{image_url}" src="{protocol}{imagePrefix}s{imageSize}x{imageSize}_jfs/t3559/298/2228558089/4340/981090cd/58451898N1928067c.png" />                     <div class="skuInfo">                         <p class="skuName ">{ad_title}</p>                         <p class="skuAdContent ">{adcontent}</p>                         <p class="skuPrice{sku_id} skuPriceInner">{cpsprice}</p>                     </div>                     <div class="bg-shadow"></div>                </a> ';for(var m=0,n=c.length;m<n;m++){var o={};m%l==0&&(i.push('<li class="subNum">'+(m+1)+"</li>"),0==m?d.push(' <div class="item"  >'):d.push('</div><div class="item"  >')),o=a.extend(c[m],b),d.push(a.nano(template,o)),g.push(o.sku_id),h.push('<p class="priceItem skuPrice'+o.sku_id+' disNone"></p>'),m==n&&d.push(" </div>")}return b.priceSkuIdArr=g,parseInt(g.length/l),j='<div class="jdAdIndex"><span class="index"><span class="page">1</span>/<span>'+g.length+"</span></span></div>",k='<a class="jdAdLogoBot" href="'+t.logoClickUrl+'" target="_blank">京东推广</a>',arrowHtml='<div class="jdAdPrevious left arrow"><span class="lt"></span></div><div class="jdAdNext right arrow"><span class="gt"></span></div>',d='<a id="logo" target="_blank" href="'+t.logoClickUrl+'"><img src="'+t.logoPrefix+b.logo.src+'" alt="京东logo" /></a><div class="inner">'+d.join("")+"</div>"+j+k+'<div class="jdPrice">'+h.join("")+'</div><ul class="numTag jdAdPagination">'+i.join("")+"</ul>"+arrowHtml}function i(c){var d=[],f=[],g=[],h=[],i="",j=b.colShowSkuNum=e();template='                     <a class="skuLink"  href="{click_url}" target="_blank" title="{ad_title}">                                 <img class="skuImg" data-exposal="{exposal_url}" data-src="{protocol}{imagePrefix}s{imageSize}x{imageSize}_{image_url}" src="{protocol}{imagePrefix}s{imageSize}x{imageSize}_jfs/t3559/298/2228558089/4340/981090cd/58451898N1928067c.png" />                                 <div class="skuInfo">                                     <p class="skuName ">{ad_title}</p>                                     <p class="skuAdContent ">{adcontent}</p>                                     <p class="skuPrice{sku_id} skuPriceInner"><i>¥{seckill_price}</i><span>¥{jd_price}</span></p>                                 </div>                                 <div class="bg-shadow"></div>                            </a> ';for(var k=0,l=c.length;k<l;k++){var m={};k%j==0&&(h.push('<li class="subNum">'+(k+1)+"</li>"),0==k?d.push(' <div class="item"  >'):d.push('</div><div class="item"  >')),m=a.extend(c[k],b),d.push(a.nano(template,m)),f.push(m.sku_id),g.push('<a href="'+m.click_url+'" target="_blank" title="'+m.ad_title+'" class="priceItem skuPrice'+m.sku_id+' "><div class="rob"><em>抢</em><p class="secPrice"><i>¥'+m.seckill_price+'</i><span class="througPrice">¥'+m.jd_price+'</span></p><div class="clear"><p class="progress"><span class="progressBar" style="width:'+m.seckill_show_process+'%"></span></p><p class="fontProcess">已售:'+m.seckill_show_process+"%</p></div></div></a>"),k==l&&d.push(" </div>")}return b.priceSkuIdArr=f,b.width>b.height&&j>1?(b.logo.imgStyle+="#logo{width:90px;overflow:hidden; top:0; left:0; height:100%}#logo img{ position:absolute; margin-top:-60px; left:50%; margin-left:-58px; top:50%;}",b.logo.src="seckillLogo.jpg"):b.logo.src="seckillCirLogo.png",parseInt(f.length/j),'<div class="jdAdIndex"><span class="index"><span class="page">1</span>/<span>'+f.length+"</span></span></div>",i='<a class="jdAdLogoBot" href="'+t.logoClickUrl+'" target="_blank">京东推广</a>',arrowHtml='<div class="jdAdPrevious left arrow"><span class="lt"></span></div><div class="jdAdNext right arrow"><span class="gt"></span></div>',d='<a id="logo" target="_blank" href="'+t.logoClickUrl+'"><img src="'+t.logoPrefix+b.logo.src+'" alt="京东logo" /></a><div class="inner">'+d.join("")+"</div>"+i+'<div class="jdPrice">'+g.join("")+'</div><ul class="numTag jdAdPagination">'+h.join("")+"</ul>"+arrowHtml}function j(c){for(var d,e,f,g=[],h='         <div class="item"" >             <a href="{click_url}" target="_blank">                 <img class="skuImg" src="{protocol}{picImgPrefix}{image_url}" style="display:block; width:100%; margin:0 auto" />             </a>             <img class="expose" src="{exposal_url}" >         </div>',i=0,j=c.length;i<j;i++){var k={};k=a.extend(c[i],b),g.push(a.nano(h,k))}if(e=b.cpdLogUrl,"string"==typeof e&&""!=e&&g.push('<img class="expose" src="'+e+'" >'),f=b.impression_monitor_url,isArray(f)&&f.length>0)for(var l=0,m=f.length;l<m;l++){var n=f[l];"string"==typeof n&&""!=n.replace(/(^\s+)|(\s+$)/g,"")&&g.push('<img class="expose" src="'+n+'" >')}return d='<a class="jdAdLogoBot" href="'+b.logoClickUrl+'" target="_blank">京东推广</a>',g='<div class="inner">'+g.join("")+"</div>"+d}function k(c){function d(){for(var a=[["20-300","0.07","5.71"],["120-600","0.20","6.42"],["130-600","0.22","6.42"],["120-500","0.24","6.24"],["160-600","0.27","6.43"],["120-400","0.30","6.03"],["100-300","0.33","5.76"],["110-300","0.37","5.77"],["130-300","0.43","5.79"],["120-270","0.44","5.69"],["160-320","0.50","5.88"],["120-240","0.50","5.59"],["300-600","0.50","6.51"],["138-261","0.53","5.69"],["150-270","0.56","5.73"],["300-530","0.57","6.41"],["170-282","0.60","5.80"],["300-500","0.60","6.37"],["220-350","0.63","6.02"],["270-428","0.63","6.23"],["160-250","0.64","5.69"],["235-360","0.65","6.06"],["200-300","0.67","5.89"],["320-480","0.67","6.36"],["160-236","0.68","5.65"],["220-320","0.69","5.96"],["300-400","0.75","6.21"],["353-458","0.77","6.36"],["200-250","0.80","5.77"],["640-782","0.82","6.92"],["300-350","0.86","6.13"],["200-230","0.87","5.72"],["198-228","0.87","5.71"],["280-320","0.88","6.05"],["195-220","0.89","5.68"],["180-200","0.90","5.59"],["320-350","0.91","6.16"],["210-220","0.95","5.72"],["300-300","1.00","6.05"],["200-200","1.00","5.64"],["310-310","1.00","6.08"],["280-280","1.00","5.98"],["210-210","1.00","5.69"],["250-250","1.00","5.87"],["130-130","1.00","5.21"],["100-100","1.00","4.95"],["300-280","1.07","6.02"],["320-285","1.12","6.06"],["280-250","1.12","5.93"],["310-275","1.13","6.03"],["300-265","1.13","5.99"],["422-370","1.14","6.33"],["320-280","1.14","6.05"],["300-260","1.15","5.98"],["295-250","1.18","5.96"],["336-280","1.20","6.08"],["300-250","1.20","5.97"],["219-180","1.22","5.65"],["300-245","1.22","5.96"],["260-210","1.24","5.81"],["250-200","1.25","5.77"],["170-135","1.26","5.38"],["480-360","1.33","6.40"],["400-300","1.33","6.21"],["200-150","1.33","5.52"],["280-200","1.40","5.84"],["210-150","1.40","5.55"],["555-395","1.41","6.52"],["498-353","1.41","6.41"],["390-270","1.44","6.16"],["580-400","1.45","6.56"],["500-340","1.47","6.40"],["290-195","1.49","5.86"],["300-200","1.50","5.89"],["298-198","1.51","5.88"],["230-150","1.53","5.62"],["336-218","1.54","5.99"],["294-190","1.55","5.86"],["300-189","1.59","5.87"],["350-220","1.59","6.02"],["400-250","1.60","6.16"],["279-166","1.68","5.78"],["760-450","1.69","6.78"],["300-178","1.69","5.85"],["300-175","1.71","5.85"],["415-240","1.73","6.17"],["295-170","1.74","5.83"],["280-160","1.75","5.78"],["300-170","1.76","5.84"],["800-450","1.78","6.82"],["270-150","1.80","5.73"],["670-352","1.90","6.63"],["670-351","1.91","6.63"],["640-330","1.94","6.58"],["335-170","1.97","5.93"],["1000-100","10.00","6.91"],["700-70","10.00","6.56"],["625-60","10.42","6.44"],["940-90","10.44","6.85"],["630-60","10.50","6.45"],["950-90","10.56","6.86"],["960-90","10.67","6.87"],["640-60","10.67","6.47"],["970-90","10.78","6.88"],["980-90","10.89","6.89"],["990-90","11.00","6.90"],["1000-90","11.11","6.91"],["670-60","11.17","6.51"],["998-88","11.34","6.91"],["1028-90","11.42","6.94"],["960-80","12.00","6.87"],["1110-90","12.33","7.02"],["765-60","12.75","6.64"],["1230-90","13.67","7.12"],["990-70","14.14","6.90"],["950-60","15.83","6.86"],["960-60","16.00","6.87"],["980-60","16.33","6.89"],["500-30","16.67","6.22"],["160-80","2.00","5.19"],["300-150","2.00","5.82"],["678-334","2.03","6.63"],["700-330","2.12","6.65"],["400-180","2.22","6.08"],["295-120","2.46","5.76"],["1000-400","2.50","6.98"],["500-200","2.50","6.29"],["280-100","2.80","5.69"],["300-100","3.00","5.76"],["310-100","3.10","5.79"],["280-90","3.11","5.68"],["390-120","3.25","6.01"],["1000-300","3.33","6.95"],["600-180","3.33","6.44"],["300-90","3.33","5.75"],["308-90","3.42","5.77"],["300-80","3.75","5.74"],["270-70","3.86","5.63"],["350-90","3.89","5.89"],["475-120","3.96","6.19"],["320-80","4.00","5.80"],["400-90","4.44","6.02"],["590-130","4.54","6.40"],["300-65","4.62","5.73"],["730-138","5.29","6.61"],["424-80","5.30","6.07"],["640-120","5.33","6.48"],["555-104","5.34","6.34"],["534-94","5.68","6.30"],["580-100","5.80","6.38"],["600-100","6.00","6.41"],["610-100","6.10","6.43"],["620-100","6.20","6.44"],["590-95","6.21","6.39"],["640-100","6.40","6.47"],["580-90","6.44","6.37"],["590-90","6.56","6.39"],["680-100","6.80","6.53"],["480-70","6.86","6.18"],["637-90","7.08","6.47"],["640-90","7.11","6.47"],["644-90","7.16","6.48"],["650-90","7.22","6.49"],["660-90","7.33","6.50"],["960-130","7.38","6.88"],["670-90","7.44","6.52"],["760-100","7.60","6.64"],["468-60","7.80","6.16"],["640-80","8.00","6.47"],["728-90","8.09","6.60"],["730-90","8.11","6.60"],["980-120","8.17","6.89"],["750-90","8.33","6.63"],["760-90","8.44","6.64"],["762-90","8.47","6.64"],["860-100","8.60","6.76"],["690-80","8.63","6.54"],["680-75","9.07","6.53"],["820-90","9.11","6.72"],["690-75","9.20","6.54"],["950-100","9.50","6.86"],["860-90","9.56","6.76"],["980-100","9.80","6.89"]],c=b.width,d=b.height,e="300-250",f=(c/d).toFixed(2),g=Math.log(Math.sqrt(c*c+d*d)).toFixed(2),h=999,i=0;i<a.length;i++){var j=a[i],k=j[0],l=j[1],m=Math.abs(f-l)+Math.abs(g/10-j[2]/10);m<h&&(h=m,e=k)}return e}for(var e,f=[],g='         <div class="item" data-exposal="{exposal_url}" >             <a href="{click_url}" target="_blank">                 <img class="skuImg" src="{protocol}{tdPicPrefix}'+d()+'.jpg" style="display:block; width:{width}px; height:{height}px; margin:0 auto" />             </a>             <img src="{exposal_url}" style="display:none; width:0; height:0" />         </div>',h=0,i=c.length;h<i;h++){var j={};j=a.extend(c[h],b),f.push(a.nano(g,j))}return e='<a class="jdAdLogoBot" href="'+b.logoClickUrl+'" target="_blank">京东推广</a>',f='<div class="inner">'+f.join("")+"</div>"+e}function l(a){var b=document,c=b.createElement("style");if(c.setAttribute("type","text/css"),c.setAttribute("class","random"),c.styleSheet)c.styleSheet.cssText=a;else{var d=b.createTextNode(a);c.appendChild(d)}var e=b.getElementsByTagName("head");e.length?e[0].appendChild(c):b.documentElement.appendChild(c)}function m(a){var b="body,div,em,form,h1,h2,h3,h4,h5,h6,img,input,li,ol,p,pre,textarea,ul{margin:0;padding:0}body{height:100%;font:0px/1.75 Tahoma,Arial;color:#000;background-color:#fff}li,ul{list-style-type:none}img{border:0}.jdAdCred{color:#c91521}a{color:#006a92;text-decoration:none}a:hover{text-decoration:underline}a:focus{outline:0}";return b+=".jdAdLogoBot{display: inline-block; position: absolute; bottom: 1px; right: 1px; width: 36px; height: 15px; overflow: hidden; line-height: 999px; background: url(//static-alias-1.360buyimg.com/jzt/temp/conermark/"+a+".png) top right no-repeat; z-index: 11;} .expose{width:0;height:0;display:none} ",b+="a.wdIcon{width:24px;height:15px;background:url(//static-alias-1.360buyimg.com/jzt/temp/conermark/ad.png) top right no-repeat;}"}function n(){function c(){var a=b.width-2*b.styleCss.borderWidth,c=a;contentHeight=b.height-2*b.styleCss.borderWidth;var d=b.logo.style,e=t.logoPre+b.logo.src,f=b.logo.imgStyle;return"longLine"==b.layoutType&&(c-=90),{borderColor:b.styleCss.borderColor,borderWidth:b.styleCss.borderWidth,contentWidth:a,contentInnerWidth:c,contentHeight:contentHeight,logoStyle:d,logoUrl:e,logoImg:f}}var d='body,div,em,form,h1,h2,h3,h4,h5,h6,img,input,li,ol,p,pre,textarea,ul{margin:0;padding:0}body{font:0px/1.75 "Microsoft YaHei", "Heiti SC", STHeitiSC, Arial, sans-serif;color:#000;background-color:#fff}li,ul{list-style-type:none}img{border:0}.jdAdCred{color:#c91521}a{color:#006a92;text-decoration:none}a:hover{text-decoration:underline}a:focus{outline:0}';return d+="#tpl{ position:relative; border:{borderWidth}px solid {borderColor}; width:{contentWidth}px; height:{contentHeight}px;overflow:hidden}",d+="#logo{{logoStyle} position:absolute; top:0; left:0; z-index:999}{logoImg}",d+=".inner{ width:{contentInnerWidth}px; height:{contentHeight}px;position:relative}.item{display:none; top:0; position:absolute; width:100%}.current{display:block;}",d+=".item .skuImg{ display:block; margin:0 auto}",d+=".disNone{ display:none; } .numTag{display:none}",d+=".item .skuInfo ,.item .bg-shadow{position:absolute;bottom:0; left:0; width:100%;height:26px; }.item .bg-shadow{display:none;} .skuPriceInner{font-size:12px;color:#E23939}",d+='.jdAdIndex {position: absolute;right: 0;bottom: 0;padding-right: 20px;width: 50px;font-family: "Microsoft YaHei", "Heiti SC", STHeitiSC, Arial, sans-serif;}',d+=".jdAdIndex .index{display:inline-block;font-weight:700;float:right;font-size:14px;padding:0 5px;margin:1px 10px;line-height:19px;border:1px solid #e4393c;color:#e4393c}",d+=".jdAdLogoBot{display: inline-block; position: absolute; bottom: 2px; right: 2px; width: 24px; height: 15px; overflow: hidden; line-height: 999px; background: url(//static-alias-1.360buyimg.com/jzt/temp/conermark/ad.png) top right no-repeat; z-index: 11;}.jdIcon { width:18px;height:18px;bottom: 0; right: -1px;background-image:url(//static-alias-1.360buyimg.com/jzt/temp/conermark/jd.png)}",d+='.jdPrice{position: absolute;left: 0;bottom: 0;font-size: 20px;font-weight: 700;line-height: 26px;padding-right: 5px;word-wrap: break-word;word-break: normal;color: #e4393c;text-indent: 5px;font-family: "Microsoft YaHei", "Heiti SC", STHeitiSC, Arial, sans-serif;}',d+='.jdSkuName{position: absolute;left: 94px;bottom: 0;font-size: 14px;line-height: 26px;padding-right: 5px;word-wrap: break-word;word-break: normal;color: ##006a92;text-indent: 5px;font-family: "Microsoft YaHei", "Heiti SC", STHeitiSC, Arial, sans-serif;}.skuNameItem{ width:124px;height:26px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;}',d+='.arrow { cursor: pointer;filter: progid: DXImageTransform.Microsoft.gradient(startColorstr = "#AFFFFFFF", endColorstr = "#AFFFFFFF");position: absolute;width:16px;height:40px;margin-top:-29px;top:50%;user-select:none;-webkit-user-select:none;padding:2px;background:url(//static-alias-1.360buyimg.com/jzt/temp/conermark/dot.png)}.left{left:0;z-index:5;border-top-right-radius:3px;border-bottom-right-radius:3px}.left .lt{margin:9px 2px;display:block;width:13px;height:23px;background:url(//static-alias-1.360buyimg.com/jzt/temp/conermark/arrow.png) no-repeat}.right{right:0;z-index:5;border-top-left-radius:3px;border-bottom-left-radius:3px}.right .gt{margin:9px 2px;display:block;width:13px;height:23px;background:url(//static-alias-1.360buyimg.com/jzt/temp/conermark/arrow.png) -13px 0 no-repeat}',"row"==b.showLayoutType&&b.colShowSkuNum>1&&(d+=".skuLink{float:left;position:relative}"),a.nano(d,c())}function o(){function c(){var a=b.width-2*b.styleCss.borderWidth,c=a;contentHeight=b.height-2*b.styleCss.borderWidth;var d=b.logo.style,e=t.logoPre+b.logo.src,f=b.logo.imgStyle;return"longLine"==b.layoutType&&(c-=90),{borderColor:b.styleCss.borderColor,borderWidth:b.styleCss.borderWidth,contentWidth:a,contentInnerWidth:c,contentHeight:contentHeight,logoStyle:d,logoUrl:e,logoImg:f}}var d='body,div,em,form,h1,h2,h3,h4,h5,h6,img,input,li,ol,p,pre,textarea,ul{margin:0;padding:0}body{font:0px/1.75 "Microsoft YaHei", "Heiti SC", STHeitiSC, Arial, sans-serif;color:#000;background-color:#fff}li,ul{list-style-type:none}img{border:0}.jdAdCred{color:#c91521}a{color:#e4393c;text-decoration:none}a:hover{text-decoration:none}a:focus{outline:0}';return d+="#tpl{ position:relative; border:{borderWidth}px solid {borderColor}; width:{contentWidth}px; height:{contentHeight}px;overflow:hidden}",d+="#logo{{logoStyle} height:auto; position:absolute; top:10px; left:10px; z-index:999}{logoImg}",d+=".inner{ width:{contentInnerWidth}px; height:{contentHeight}px;position:relative}.item{display:none; top:0; position:absolute; width:100%}.current{display:block;}",d+=".item .skuImg{ display:block; margin:0 auto} .rob{height:35px; border:1px solid #fff; border-radius:2px; position:relative; padding-left:38px;padding-right:5px;font-family:Tahoma,Arial; background:#fff} .rob em{position:absolute; display:block; height:35px; top:0; left:0;font-style:normal; font-size:22px; background:#bc1f29; color:#fff;text-indent:0;padding:0 5px;} .rob .secPrice{line-height:26px;} .rob i{font-style:normal; line-height:24px; } .througPrice{padding-left:5px; font-size:18px; color:#999;text-decoration: line-through;}.rob .fontProcess{font-size:12px; color:#666; position:relative; top:-10px; left:5px;} .progress{float:left;width:60%; display:block;background:#ddd; overflow:hidden; font-size:0; height:6px; border-radius:3px;} .progressBar{float:left; height:6px; background:#bc1f29;} .skuPriceInner i{font-style:normal; font-size:16px; color:#fff;} .skuPriceInner span{color:#dadada;text-decoration: line-through; display:inline-block;}",d+=".disNone{ display:none; } .numTag{display:none}",d+=".item .skuInfo ,.item .bg-shadow{position:absolute;bottom:0; left:0; width:100%;height:26px; }.item .bg-shadow{display:none;} .skuPriceInner{color:#E23939}",d+='.jdAdIndex {position: absolute;right: 0;bottom: 0;padding-right: 20px;width: 50px;font-family: "Microsoft YaHei", "Heiti SC", STHeitiSC, Arial, sans-serif;}',d+=".jdAdIndex .index{display:inline-block;font-weight:700;float:right;font-size:14px;padding:0 5px;margin:1px 10px;line-height:19px;border:1px solid #e4393c;color:#e4393c}",d+=".jdAdLogoBot{display: inline-block; position: absolute; bottom: 2px; right: 2px; width: 24px; height: 15px; overflow: hidden; line-height: 999px; background: url(//static-alias-1.360buyimg.com/jzt/temp/conermark/ad.png) top right no-repeat; z-index: 11;}.jdIcon {width:18px;height:18px;bottom: 0; right: 0;background-image:url(//static-alias-1.360buyimg.com/jzt/temp/conermark/jd.png)}",d+=".jdPrice{position: absolute;left:5px; right:5px;bottom:5px;font-size: 20px;padding-right: 5px;word-wrap: break-word;word-break: normal;color: #e4393c;;font-family:Tahoma,Arial;background:rgba(255,255,255,.5)}",d+='.jdSkuName{position: absolute;left: 94px;bottom: 0;font-size: 14px;line-height: 26px;padding-right: 5px;word-wrap: break-word;word-break: normal;color: ##006a92;text-indent: 5px;font-family: "Microsoft YaHei", "Heiti SC", STHeitiSC, Arial, sans-serif;}.skuNameItem{ width:124px;height:26px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;}',d+='.arrow { cursor: pointer;filter: progid: DXImageTransform.Microsoft.gradient(startColorstr = "#AFFFFFFF", endColorstr = "#AFFFFFFF");position: absolute;width:16px;height:40px;margin-top:-29px;top:50%;user-select:none;-webkit-user-select:none;padding:2px;background:url(//static-alias-1.360buyimg.com/jzt/temp/conermark/dot.png)}.left{left:0;z-index:5;border-top-right-radius:3px;border-bottom-right-radius:3px}.left .lt{margin:9px 2px;display:block;width:13px;height:23px;background:url(//static-alias-1.360buyimg.com/jzt/temp/conermark/arrow.png) no-repeat}.right{right:0;z-index:5;border-top-left-radius:3px;border-bottom-left-radius:3px}.right .gt{margin:9px 2px;display:block;width:13px;height:23px;background:url(//static-alias-1.360buyimg.com/jzt/temp/conermark/arrow.png) -13px 0 no-repeat}',"row"==b.showLayoutType&&b.colShowSkuNum>1&&(d+=".skuLink{float:left;position:relative}"),a.nano(d,c())}function p(c){!b.priceObj||b.priceObj.length<c.length?a.jsonp({url:b.priceInterface.replace("{skuids}","J_"+c.join(",J_")),callback:q}):q(b.priceObj)}function q(c){b.priceObj=c;for(var d=0;d<c.length;d++)for(var e=c[d].id.split("_"),f=a(".skuPrice"+e[1]),g=0;g<f.length;g++)c[d].p>0?f[g].innerHTML="￥"+parseFloat(c[d].p).toFixed(2):f[g].innerHTML="已下架"}function r(){var a;a="mainDiv_"+ +new Date,document.write('<div id="'+a+'"></div>'),window.__jdContent__=document.getElementById(a)}function s(){function e(){var c,d;if(b.resize){window.effect&&window.effect.turns&&(window.effect.turns.stop(),window.effect.turns=null),a("style").remove(),a("#tpl").remove();for(var e in _Jconf.exposes)delete _Jconf.exposes[e];c=h(b.data),d=document.createElement("div"),d.id="tpl",d.innerHTML=c,window.__jdContent__.appendChild(d),l(n()),window.effect=a("#tpl").turns({tagName:".subNum"}),1==a.GetQueryString("adflag")&&a(".jdAdLogoBot").addClass("jdIcon")}else r(),c=h(b.data),d=document.createElement("div"),d.id="tpl",d.innerHTML=c,window.__jdContent__.appendChild(d),l(n()),window.effect=a("#tpl").turns({tagName:".subNum"}),a.sendExposals(b.impression_monitor_url),a.sendExposals(new Array(b.exposal_urls)),a(window).on("resize",function(){setTimeout(s,200)});b.resize=!0,p(b.priceSkuIdArr),a.initjda(),1==a.GetQueryString("adflag")&&a(".jdAdLogoBot").addClass("jdIcon")}function f(){a("style").remove(),a("#tpl").remove();var c,d;r(),c=j(b.data),d=document.createElement("div"),d.id="tpl",d.innerHTML=c,window.__jdContent__.appendChild(d),l(m("ad_jd")),a.initjda(),1==a.GetQueryString("adflag")&&a(".jdAdLogoBot").addClass("jdIcon"),b.logoClickUrl&&""!=b.logoClickUrl||(a(".jdAdLogoBot").addClass("wdIcon"),a(".wdIcon").on("click",function(a){return a&&a.preventDefault?a.preventDefault():window.event.returnValue=!1,!1}))}function g(){a("style").remove(),a("#tpl").remove(),r(),tplHtml=k(b.data),tplCont=document.createElement("div"),tplCont.id="tpl",tplCont.innerHTML=tplHtml,window.__jdContent__.appendChild(tplCont),l(m("ad")),a.sendExposals(b.impression_monitor_url),a.initjda(),1==a.GetQueryString("adflag")&&a(".jdAdLogoBot").addClass("jdIcon")}function q(){var c,d;r(),c=i(b.data),d=document.createElement("div"),d.id="tpl",d.innerHTML=c,window.__jdContent__.appendChild(d),l(o()),window.effect=a("#tpl").turns({tagName:".subNum"}),a.sendExposals(b.impression_monitor_url),a.sendExposals(new Array(b.exposal_urls)),a.initjda(),1==a.GetQueryString("adflag")&&a(".jdAdLogoBot").addClass("jdIcon")}b.exposes={},c(),d(),"reco"===b.adShowType?e():"pic"===b.adShowType?f():"seckill"===b.adShowType?q():g()}var t=_renderData;window.stamp=t.adstamp,s()}(_J,_Jconf);
/*! jdtpl last edit: 2017-12-12|14:54:20 */
