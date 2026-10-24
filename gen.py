import json
B="/lucys-drive-thru/"; U="https://answerfirstai-ai.github.io/lucys-drive-thru/"
TEL="tel:+12133840721"; DIR="https://www.google.com/maps/dir/?api=1&destination=Lucy%27s+Drive+Thru%2C+1568+W+Pico+Blvd%2C+Los+Angeles%2C+CA+90015"
GMAP="https://www.google.com/maps/place/?q=place_id:ChIJN43S4pXHwoAR_sz0JYM8-tQ"; YELP="https://www.yelp.com/biz/lucys-drive-thru-los-angeles"; EATER="https://la.eater.com/venue/31256/lucy-s-drive-thru"
TITLE="Lucy's Drive Thru | Tacos & Burritos on Pico Blvd, Los Angeles"
DESC="Listed as open 24 hours per Yelp (call to confirm) at 1568 W Pico Blvd. Burritos, tacos, pupusas, menudo, burgers and breakfast any hour. Call (213) 384-0721."
schema={"@context":"https://schema.org","@type":"Restaurant","@id":U+"#restaurant","name":"Lucy's Drive Thru","url":U,"telephone":"+1-213-384-0721",
"address":{"@type":"PostalAddress","streetAddress":"1568 W Pico Blvd","addressLocality":"Los Angeles","addressRegion":"CA","postalCode":"90015","addressCountry":"US"},
"geo":{"@type":"GeoCoordinates","latitude":34.0443442,"longitude":-118.2768267},"hasMap":GMAP,

"servesCuisine":["Mexican","Salvadoran","American"],"hasMenu":U+"menu/","areaServed":"Pico-Union, Los Angeles","image":U+"assets/og.jpg","sameAs":[EATER,YELP]}
def pic(n,ws,sizes,alt,w,h,lazy=True,cls=""):
  a=", ".join(f"{B}assets/img/{n}-{x}.avif {x}w" for x in ws); v=", ".join(f"{B}assets/img/{n}-{x}.webp {x}w" for x in ws)
  l='loading="lazy"' if lazy else 'fetchpriority="high"'
  return f'<picture class="{cls}"><source type="image/avif" srcset="{a}" sizes="{sizes}"><source type="image/webp" srcset="{v}" sizes="{sizes}"><img src="{B}assets/img/{n}-{ws[0]}.webp" alt="{alt}" width="{w}" height="{h}" {l} decoding="async"></picture>'
CALL=f'<a class="btn b1" data-call href="{TEL}">Call</a>'
DIRB=f'<a class="btn b2" data-dir href="{DIR}" target="_blank" rel="noopener">Directions</a>'
def head(title,desc,path,preload=""):
  return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{U}{path}">
<meta name="theme-color" content="#0D0E10"><meta name="color-scheme" content="dark">
<meta property="og:type" content="website"><meta property="og:site_name" content="Lucy's Drive Thru"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{U}{path}"><meta property="og:image" content="{U}assets/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{U}assets/og.jpg">
<link rel="icon" href="{B}favicon.svg" type="image/svg+xml"><link rel="icon" href="{B}favicon.ico" sizes="32x32"><link rel="apple-touch-icon" href="{B}assets/apple-touch-icon.png"><link rel="manifest" href="{B}site.webmanifest">
<link rel="preload" href="{B}assets/fonts/big-shoulders-display-latin-900-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="{B}assets/fonts/big-shoulders-text-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>{preload}
<link rel="stylesheet" href="{B}assets/site.css">
<script type="application/ld+json">{json.dumps(schema)}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav" id="top"><a class="mark" href="{B}" aria-label="Lucy's Drive Thru, home">LUCY'S<span>·</span>PICO</a>
<nav class="links" id="navlinks" aria-label="Main"><a href="{B}menu/">Menu</a><a href="{B}find-us/">Find us</a><a class="tel" data-call href="{TEL}">(213) 384-0721</a><span class="hrs">24 hours per Yelp</span></nav>
<button class="burger" type="button" aria-expanded="false" aria-controls="navlinks"><span class="bl"></span><span class="sr">Menu</span>MENU</button></header>
<main id="main">'''
def foot():
  return f'''</main>
<footer class="foot"><div class="f1"><p class="lbl">Open 24 hours per Yelp</p><p class="fbig">LUCY'S<br>DRIVE THRU</p><p>Lucy's Drive Thru, 1568 W Pico Blvd, Los Angeles 90015. (213) 384-0721. Open 24 hours per Yelp. Call to confirm.</p></div>
<div class="f2"><p class="stamp">NAP</p><address>1568 W Pico Blvd<br>Los Angeles, CA 90015<br><a data-call href="{TEL}">(213) 384-0721</a></address><p>Open 24 hours per Yelp. Call to confirm.</p></div>
<div class="f3"><p class="stamp">Pages</p><ul><li><a href="{B}">Home</a></li><li><a href="{B}menu/">Menu</a></li><li><a href="{B}find-us/">Find us</a></li></ul></div>
<div class="f4"><p class="stamp">Elsewhere</p><ul><li><a href="{GMAP}" rel="noopener" target="_blank">Google Maps</a></li><li><a href="{YELP}" rel="noopener" target="_blank">Yelp</a></li><li><a href="{EATER}" rel="noopener" target="_blank">Eater LA</a></li></ul></div>
<p class="fine">Photos: <a href="https://www.instagram.com/lucyspicounion/" rel="noopener" target="_blank">@lucyspicounion</a>. Map data &copy; OpenStreetMap contributors.</p></footer>
<div class="mbar">{CALL}{DIRB}</div>
<script src="{B}assets/js/app.js" defer></script></body></html>'''
BOARD=[("Burritos","Carne asada, breakfast burritos"),("Tacos","Street tacos"),("Pupusas","Salvadoran, off the comal"),("Enchilada plates","Combo plates, nachos, tortas, sopes"),("Mariscos","Shrimp plates, cocteles, tostadas, ceviche"),("Caldos","Camarón, res, pollo, albóndigas"),("Menudo","Ask what days"),("Burgers","Chili cheese fries, fish &amp; chips"),("Desayuno","Breakfast, any hour"),("Para tomar","Horchata, jugos naturales, malts &amp; shakes")]
def board(rows,h="h-board"):
  r="".join(f'<li><span class="it">{a}</span><span class="dots" aria-hidden="true"></span><span class="nt">{b}</span></li>' for a,b in rows)
  return f'''<div class="board" role="group" aria-labelledby="{h}"><div class="board-in"><p class="board-top" aria-hidden="true"><span>LUCY'S</span><span>24 HRS</span></p><p class="board-h" id="{h}">El menú</p><ul class="rows">{r}</ul><p class="board-note">Menu may vary. Call for today's prices.</p></div></div>'''
tc=lambda t:''
SIGNPIC=f'''<picture class="hero-bg"><source type="image/avif" srcset="{B}assets/img/sign-ig-675.avif 675w, {B}assets/img/sign-ig-1080.avif 1080w, {B}assets/img/sign-ig-1350.avif 1350w" sizes="(min-width:761px) 48vw, 100vw"><source type="image/webp" srcset="{B}assets/img/sign-ig-675.webp 675w, {B}assets/img/sign-ig-1080.webp 1080w, {B}assets/img/sign-ig-1350.webp 1350w" sizes="(min-width:761px) 48vw, 100vw"><img class="sign-ig" src="{B}assets/img/sign-ig-1080.webp" alt="Lucy's Drive Thru sign lit up at night on Pico Blvd: 24 Hours, Lucy's Drive Thru, Mexican and American Food" width="1350" height="1688" fetchpriority="high" decoding="async"></picture>'''
home=head(TITLE,DESC,"",f'<link rel="preload" as="image" type="image/avif" imagesrcset="{B}assets/img/sign-ig-675.avif 675w, {B}assets/img/sign-ig-1080.avif 1080w, {B}assets/img/sign-ig-1350.avif 1350w" imagesizes="(min-width:761px) 48vw, 100vw" fetchpriority="high">')+f'''
<section class="hero" aria-labelledby="h1" data-puddle>
<figure class="hero-ph">{SIGNPIC}<figcaption class="credit">Photos: <a href="https://www.instagram.com/lucyspicounion/" target="_blank" rel="noopener">@lucyspicounion</a></figcaption></figure>
<div class="hero-txt"><h2 class="kicker">Tacos and burritos on Pico Blvd, Pico-Union</h2>
<h1 id="h1" class="mega"><span class="ln">Still</span><span class="ln y">on.</span></h1>
<p class="lede">Burritos, tacos, pupusas and menudo at 1568 W Pico Blvd. Open 24 hours per Yelp. Call to confirm.</p>
<div class="ctas">{CALL}{DIRB}</div></div>
<div class="pd">{pic("asphalt",[800,1440],"100vw","",1440,810,True,"pd-img")}<div class="pd-txt" aria-hidden="true">STILL ON.</div><span class="ill">Illustrative texture</span></div>
<svg width="0" height="0" aria-hidden="true" style="position:absolute"><filter id="rip"><feTurbulence type="fractalNoise" baseFrequency="0.008 0.06" numOctaves="2" seed="3"/><feDisplacementMap in="SourceGraphic" scale="18" xChannelSelector="R" yChannelSelector="G"/></filter></svg>
</section>
<section class="boardwide" id="menu" aria-labelledby="h-board-l">
<div class="bw-head"><h2 id="h-board-l" class="xl">On the board at Lucy's</h2><p class="body">Mexican, American and Salvadoran. <span lang="es">Desayuno, mariscos, caldos</span> and burgers, all on one board. Prices change, so ask at the window.</p></div>
{board(BOARD)}
<div class="bw-foot"><a class="txtlink" href="{B}menu/">Full menu</a>{CALL}</div></section>
<section class="foodstrip" aria-label="Food from Lucy's Instagram"><div class="fs-g"><a class="fs-c" href="https://www.instagram.com/lucyspicounion/p/DPz3QgvD2LM/" target="_blank" rel="noopener">{pic("food-1",[540,1080],"(min-width:900px) 23vw, 46vw","Carnitas plate with rice and beans, from Lucy's Instagram",1080,1350)}</a><a class="fs-c" href="https://www.instagram.com/lucyspicounion/p/DPxmyXijsYt/" target="_blank" rel="noopener">{pic("food-2",[540,1080],"(min-width:900px) 23vw, 46vw","Chicken tamal with rice and beans, from Lucy's Instagram",1080,1350)}</a><a class="fs-c" href="https://www.instagram.com/lucyspicounion/p/DPXcHw4kvs8/" target="_blank" rel="noopener">{pic("food-3",[540,1080],"(min-width:900px) 23vw, 46vw","Chicken fries with pico de gallo and crema, from Lucy's Instagram",1080,1350)}</a><a class="fs-c" href="https://www.instagram.com/lucyspicounion/p/DPXaOckgaKe/" target="_blank" rel="noopener">{pic("food-4",[540,1080],"(min-width:900px) 23vw, 46vw","Asada fries, from Lucy's Instagram",1080,1350)}</a></div><p class="credit fs-cr">Photos: <a href="https://www.instagram.com/lucyspicounion/" target="_blank" rel="noopener">@lucyspicounion</a></p></section>
<section class="frame f-bkf" aria-labelledby="h-bkf"><p class="huge" aria-hidden="true">Breakfast</p>
<div class="bkf-t"><h2 id="h-bkf" class="xl3">Breakfast at 1:30 AM</h2><p class="body">Breakfast is on the menu, and Lucy's is listed as open 24 hours per Yelp. Call to confirm. <span lang="es">Desayuno a cualquier hora.</span></p></div></section>
<section class="frame f-find" id="find" aria-labelledby="h-find">
<figure class="map">{pic("map",[640,1200],"(min-width:900px) 58vw, 100vw","Map of W Pico Blvd in Pico-Union with a marker at 1568 W Pico Blvd",1200,640)}<figcaption class="mapc">Map data &copy; <a href="https://www.openstreetmap.org/copyright" rel="noopener" target="_blank">OpenStreetMap</a> contributors</figcaption></figure>
<div class="find-t"><h2 id="h-find" class="xl">Find Lucy's</h2>
<p class="body">Drive through, or park and eat. Listings mention a patio, a dining area and a free lot. <a href="{TEL}">Call to confirm.</a></p>
<p class="body cash">Reviewers say it's cash only. Bring cash to be safe.</p>
<address class="nap">1568 W Pico Blvd, Los Angeles, CA 90015<br>Open 24 hours per Yelp. Call to confirm. · <a data-call href="{TEL}">(213) 384-0721</a></address>
<div class="ctas">{DIRB}{CALL}</div></div></section>
'''+foot()
menu=head("Menu | Lucy's Drive Thru on Pico Blvd","Burritos, tacos, pupusas, caldos, menudo, mariscos, burgers and breakfast at Lucy's Drive Thru, 1568 W Pico Blvd. Listed as open 24 hours per Yelp. Call (213) 384-0721 to confirm and for today's prices.","menu/")+f'''
<section class="page-h"><div>{tc("Menu")}<h1 class="mega2">On the board</h1><p class="lede">Mexican, American and Salvadoran. Prices change, so ask at the window or call.</p><div class="ctas">{CALL}{DIRB}</div></div></section>
<section class="menu-full" aria-label="Menu board">{board(BOARD,"h-board")}
<div class="m-aside"><p class="body">Item names come from public listings, grouped by what's on the board. <a href="{TEL}">Call to confirm the full menu and menudo days.</a></p><p class="body cash">Reviewers say it's cash only. Bring cash to be safe.</p></div></section>
'''+foot()
find=head("Find Us | Lucy's Drive Thru, 1568 W Pico Blvd, Los Angeles","Lucy's Drive Thru is at 1568 W Pico Blvd, Los Angeles, CA 90015 in Pico-Union. Listed as open 24 hours per Yelp; call to confirm. Drive-thru and dining area. Call (213) 384-0721.","find-us/")+f'''
<section class="page-h"><div>{tc("Pico-Union")}<h1 class="mega2">Find Lucy's</h1><p class="lede">1568 W Pico Blvd. Open 24 hours per Yelp. Call to confirm.</p><div class="ctas">{DIRB}{CALL}</div></div></section>
<section class="find-grid"><div class="fg-l">
<dl class="facts"><dt>Address</dt><dd>1568 W Pico Blvd<br>Los Angeles, CA 90015</dd><dt>Phone</dt><dd><a data-call href="{TEL}">(213) 384-0721</a></dd><dt>Hours</dt><dd>Open 24 hours per Yelp. Call to confirm.</dd><dt>How</dt><dd>Drive-thru and takeout. Listings mention a patio, a dining area and a free lot. <a href="{TEL}">Call to confirm.</a></dd><dt>Pay</dt><dd>Reviewers say it's cash only. Bring cash to be safe.</dd></dl>
<p><a class="txtlink" href="{GMAP}" target="_blank" rel="noopener">Open in Google Maps →</a></p></div>
<figure class="fg-r map">{pic("map",[640,1200],"(min-width:900px) 58vw, 100vw","Map of W Pico Blvd in Pico-Union with a marker at 1568 W Pico Blvd",1200,640)}<figcaption class="mapc">Map data © <a href="https://www.openstreetmap.org/copyright" rel="noopener" target="_blank">OpenStreetMap</a> contributors</figcaption></figure></section>
'''+foot()
nf=head("Not found | Lucy's Drive Thru","This page doesn't exist. Lucy's Drive Thru, 1568 W Pico Blvd, listed as open 24 hours per Yelp; call to confirm.","404.html").replace('<link rel="canonical"','<meta name="robots" content="noindex"><link rel="x-canonical"')+f'''
<section class="nf"><h1 class="mega2">Wrong turn.</h1><p class="lede">Still open, though.</p><div class="ctas" style="justify-content:center"><a class="btn b1" href="{B}">Home</a><a class="btn b2" href="{B}menu/">Menu</a></div></section>
'''+foot()
for p,h in [("index.html",home),("menu/index.html",menu),("find-us/index.html",find),("404.html",nf)]: open(p,"w").write(h)
open("robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {U}sitemap.xml\n")
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{U}{p}</loc><lastmod>2026-10-22</lastmod></url>\n" for p in ["","menu/","find-us/"])+"</urlset>\n")
open("site.webmanifest","w").write(json.dumps({"name":"Lucy's Drive Thru","short_name":"Lucy's","start_url":B,"display":"browser","background_color":"#0D0E10","theme_color":"#0D0E10","icons":[{"src":B+"assets/icon-512.png","sizes":"512x512","type":"image/png"}]}))
