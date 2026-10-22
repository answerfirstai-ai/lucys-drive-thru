import json
B="/lucys-drive-thru/"; U="https://answerfirstai-ai.github.io/lucys-drive-thru/"
TEL="tel:+12133840721"; DIR="https://www.google.com/maps/dir/?api=1&destination=Lucy%27s+Drive+Thru%2C+1568+W+Pico+Blvd%2C+Los+Angeles%2C+CA+90015"
GMAP="https://www.google.com/maps/place/?q=place_id:ChIJN43S4pXHwoAR_sz0JYM8-tQ"; YELP="https://www.yelp.com/biz/lucys-drive-thru-los-angeles"; EATER="https://la.eater.com/venue/31256/lucy-s-drive-thru"
TITLE="Lucy's Drive Thru | 24-Hour Tacos & Burritos on Pico Blvd, Los Angeles"
DESC="Open 24 hours, 7 days at 1568 W Pico Blvd. Burritos, tacos, pupusas, menudo, burgers and breakfast any hour. Call (213) 384-0721."
schema={"@context":"https://schema.org","@type":"Restaurant","@id":U+"#restaurant","name":"Lucy's Drive Thru","url":U,"telephone":"+1-213-384-0721",
"address":{"@type":"PostalAddress","streetAddress":"1568 W Pico Blvd","addressLocality":"Los Angeles","addressRegion":"CA","postalCode":"90015","addressCountry":"US"},
"geo":{"@type":"GeoCoordinates","latitude":34.0443442,"longitude":-118.2768267},"hasMap":GMAP,
"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"00:00","closes":"23:59"}],
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
<link rel="preload" href="{B}assets/fonts/big-shoulders-display-latin-900-normal.woff2" as="font" type="font/woff2" crossorigin>{preload}
<link rel="stylesheet" href="{B}assets/site.css">
<script type="application/ld+json">{json.dumps(schema)}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav" id="top"><a class="mark" href="{B}" aria-label="Lucy's Drive Thru, home">LUCY'S<span>·</span>PICO</a>
<nav class="links" id="navlinks" aria-label="Main"><a href="{B}menu/">Menu</a><a href="{B}find-us/">Find us</a><a class="tel" data-call href="{TEL}">(213) 384-0721</a><span class="hrs">Open 24 hrs</span></nav>
<button class="burger" type="button" aria-expanded="false" aria-controls="navlinks"><span class="bl"></span><span class="sr">Menu</span>MENU</button></header>
<main id="main">'''
def foot():
  return f'''</main>
<footer class="foot"><div class="f1"><p class="tc"><span class="rec" aria-hidden="true">REC</span> 06:00 AM · still on</p><p class="fbig">LUCY'S<br>DRIVE THRU</p><p>Lucy's Drive Thru, 1568 W Pico Blvd, Los Angeles 90015. (213) 384-0721. Open 24 hours, 7 days.</p></div>
<div class="f2"><p class="stamp">NAP</p><address>1568 W Pico Blvd<br>Los Angeles, CA 90015<br><a data-call href="{TEL}">(213) 384-0721</a></address><p>Open 24 hours, 7 days.</p></div>
<div class="f3"><p class="stamp">Pages</p><ul><li><a href="{B}">Home</a></li><li><a href="{B}menu/">Menu</a></li><li><a href="{B}find-us/">Find us</a></li></ul></div>
<div class="f4"><p class="stamp">Elsewhere</p><ul><li><a href="{GMAP}" rel="noopener" target="_blank">Google Maps</a></li><li><a href="{YELP}" rel="noopener" target="_blank">Yelp</a></li><li><a href="{EATER}" rel="noopener" target="_blank">Eater LA</a></li></ul></div>
<p class="fine">Images marked “Illustrative” are AI-generated textures and street scenes, not Lucy's, its food or its building. Map data © OpenStreetMap contributors.</p></footer>
<div class="mbar">{CALL}{DIRB}</div>
<script src="{B}assets/js/app.js" defer></script></body></html>'''
BOARD=[("Burritos","Carne asada, breakfast burritos"),("Tacos","Street tacos"),("Pupusas","Salvadoran, off the comal"),("Enchilada plates","Combo plates, nachos, tortas, sopes"),("Mariscos","Shrimp plates, cocteles, tostadas, ceviche"),("Caldos","Camarón, res, pollo, albóndigas"),("Menudo","Ask what days"),("Burgers","Chili cheese fries, fish &amp; chips"),("Desayuno","Breakfast, any hour"),("Para tomar","Horchata, jugos naturales, malts &amp; shakes")]
def board(rows,h="h-board"):
  r="".join(f'<li><span class="it">{a}</span><span class="dots" aria-hidden="true"></span><span class="nt">{b}</span></li>' for a,b in rows)
  return f'''<div class="board" role="group" aria-labelledby="{h}"><div class="board-in"><p class="board-top" aria-hidden="true"><span>LUCY'S</span><span>24 HRS</span></p><p class="board-h" id="{h}">El menú</p><ul class="rows">{r}</ul><p class="board-note">Menu may vary. Call for today's prices.</p></div></div>'''
tc=lambda t:f'<p class="tc"><span class="rec" aria-hidden="true">REC</span> {t}</p>'
ILL='<span class="ill">Illustrative scene</span>'
home=head(TITLE,DESC,"",f'<link rel="preload" as="image" type="image/avif" media="(min-width:761px)" imagesrcset="{B}assets/img/hero-d-1280.avif 1280w, {B}assets/img/hero-d-1920.avif 1920w, {B}assets/img/hero-d-2880.avif 2880w" imagesizes="100vw" fetchpriority="high"><link rel="preload" as="image" type="image/avif" media="(max-width:760px)" imagesrcset="{B}assets/img/hero-m-800.avif 800w, {B}assets/img/hero-m-1200.avif 1200w, {B}assets/img/hero-m-1600.avif 1600w" imagesizes="100vw" fetchpriority="high">')+f'''
<section class="hero" aria-labelledby="h1" data-puddle>
<picture class="hero-bg"><source media="(max-width:760px)" type="image/avif" srcset="{B}assets/img/hero-m-800.avif 800w, {B}assets/img/hero-m-1200.avif 1200w, {B}assets/img/hero-m-1600.avif 1600w" sizes="100vw"><source media="(max-width:760px)" type="image/webp" srcset="{B}assets/img/hero-m-800.webp 800w, {B}assets/img/hero-m-1200.webp 1200w, {B}assets/img/hero-m-1600.webp 1600w" sizes="100vw"><source type="image/avif" srcset="{B}assets/img/hero-d-1280.avif 1280w, {B}assets/img/hero-d-1920.avif 1920w, {B}assets/img/hero-d-2880.avif 2880w" sizes="100vw"><source type="image/webp" srcset="{B}assets/img/hero-d-1280.webp 1280w, {B}assets/img/hero-d-1920.webp 1920w, {B}assets/img/hero-d-2880.webp 2880w" sizes="100vw"><img src="{B}assets/img/hero-d-1920.webp" alt="Illustrative: an empty, rain-wet Los Angeles boulevard at 3 AM, sodium streetlights reflected in a puddle" width="2880" height="1620" fetchpriority="high" decoding="async"></picture>
<div class="pd-txt" aria-hidden="true">STILL ON.</div>
<span class="ill hero-ill">Illustrative scene · 03:07 AM</span>
<div class="hero-txt"><p class="tc live"><span class="rec" aria-hidden="true">REC</span> <span data-clock aria-hidden="true">03:07:12 AM</span> · 1568 W PICO BLVD</p>
<h2 class="kicker">24-hour tacos and burritos on Pico Blvd</h2>
<h1 id="h1" class="mega"><span class="ln">Still</span><span class="ln">on.</span></h1></div>
<div class="hero-cta"><p class="lede">Burritos, tacos, pupusas and menudo at 1568 W Pico Blvd, 24 hours a day.</p><div class="ctas">{CALL}{DIRB}</div></div>
<svg width="0" height="0" aria-hidden="true" style="position:absolute"><filter id="rip"><feTurbulence type="fractalNoise" baseFrequency="0.008 0.06" numOctaves="2" seed="3"/><feDisplacementMap in="SourceGraphic" scale="18" xChannelSelector="R" yChannelSelector="G"/></filter></svg>
</section>
<section class="frame f-board" id="menu" aria-labelledby="h-board-l">
<div class="fb-l"><h2 id="h-board-l" class="xl2">On the board at Lucy's</h2><p class="body">Mexican, American and Salvadoran: burritos, tacos, pupusas, enchilada plates, seafood, caldos, menudo, burgers, fish and chips, breakfast.</p><p class="body">Prices change, so ask at the window.</p><p><a class="txtlink" href="{B}menu/">Full board →</a></p></div>
<div class="fb-r">{board(BOARD[:8])}<div class="ctas">{CALL}</div></div>
<p class="tc stamp-bl"><span class="rec" aria-hidden="true">REC</span> 11:48 PM</p></section>
<section class="frame f-bkf" aria-labelledby="h-bkf">{tc("01:30 AM")}<p class="huge" aria-hidden="true">Breakfast</p>
<div class="bkf-t"><h2 id="h-bkf" class="xl3">Breakfast at 1:30 AM</h2><p class="body">Breakfast is on the menu, and Lucy's is open 24 hours. <span lang="es">Desayuno a cualquier hora.</span></p></div></section>
<section class="frame f-sign" aria-labelledby="h-sign"><p class="tc">DAYTIME · SAME SIGN</p>
<h2 id="h-sign" class="addr">1568 W<br>Pico Blvd</h2>
<figure class="sign-ph">{pic("sign",[640,1200],"(min-width:900px) 50vw, 100vw","Lucy's Drive Thru on Pico Blvd in daylight, with its yellow pole sign",1200,895)}<figcaption class="mapc">Lucy's on Pico. Photo: Menujoys directory, author unknown. <span class="need">[NEED: photo rights, or replace with our own shot]</span></figcaption></figure>
<div class="sign-t"><p class="body">The yellow sign out front says OPEN 24 HOURS, and it means it. Pico-Union, a few minutes west of Downtown LA.</p></div></section>
<section class="frame f-find" id="find" aria-labelledby="h-find">
<figure class="map">{pic("map",[640,1200],"(min-width:900px) 58vw, 100vw","Map of W Pico Blvd in Pico-Union with a marker at 1568 W Pico Blvd",1200,640)}<figcaption class="mapc">Map data © <a href="https://www.openstreetmap.org/copyright" rel="noopener" target="_blank">OpenStreetMap</a> contributors</figcaption></figure>
<div class="find-t">{tc("05:52 AM")}<h2 id="h-find" class="xl">Find Lucy's</h2>
<p class="body">Drive through, or sit on the patio. Listings also mention a dining area and a free lot. <span class="need">[NEED: confirm dining room + patio]</span></p>
<p class="body cash">Reviewers say it's cash only. Bring cash to be safe.</p>
<address class="nap">1568 W Pico Blvd, Los Angeles, CA 90015<br>Open 24 hours, 7 days · <a data-call href="{TEL}">(213) 384-0721</a></address>
<div class="ctas">{DIRB}{CALL}</div></div></section>
'''+foot()
menu=head("Menu | Lucy's Drive Thru, 24 Hours on Pico Blvd","Burritos, tacos, pupusas, caldos, menudo, mariscos, burgers and breakfast at Lucy's Drive Thru, 1568 W Pico Blvd. Open 24 hours. Call (213) 384-0721 for today's prices.","menu/")+f'''
<section class="page-h"><div>{tc("01:30 AM · THE BOARD")}<h1 class="mega2">On the board</h1><p class="lede">Mexican, American and Salvadoran. Prices change, so ask at the window or call.</p><div class="ctas">{CALL}{DIRB}</div></div></section>
<section class="menu-full" aria-label="Menu board">{board(BOARD,"h-board")}
<div class="m-aside"><p class="body">Item names come from public listings, grouped by what's on the board. <span class="need">[NEED: confirm full menu + menudo days with Lucy's]</span></p><p class="body cash">Reviewers say it's cash only. Bring cash to be safe.</p></div></section>
'''+foot()
find=head("Find Us | Lucy's Drive Thru, 1568 W Pico Blvd, Los Angeles","Lucy's Drive Thru is at 1568 W Pico Blvd, Los Angeles, CA 90015 in Pico-Union. Open 24 hours, 7 days. Drive-thru and dining area. Call (213) 384-0721.","find-us/")+f'''
<section class="page-h"><div>{tc("05:52 AM · PICO-UNION")}<h1 class="mega2">Find Lucy's</h1><p class="lede">1568 W Pico Blvd. Open 24 hours, 7 days.</p><div class="ctas">{DIRB}{CALL}</div></div></section>
<section class="find-grid"><div class="fg-l">
<dl class="facts"><dt>Address</dt><dd>1568 W Pico Blvd<br>Los Angeles, CA 90015</dd><dt>Phone</dt><dd><a data-call href="{TEL}">(213) 384-0721</a></dd><dt>Hours</dt><dd>Open 24 hours, 7 days</dd><dt>How</dt><dd>Drive-thru, takeout. Listings mention a dining area, patio and free parking lot. <span class="need">[NEED: confirm dining room + patio]</span></dd><dt>Pay</dt><dd>Reviewers say it's cash only. Bring cash to be safe. <span class="need">[NEED: confirm payment]</span></dd></dl>
<p><a class="txtlink" href="{GMAP}" target="_blank" rel="noopener">Open in Google Maps →</a></p></div>
<figure class="fg-r map">{pic("map",[640,1200],"(min-width:900px) 58vw, 100vw","Map of W Pico Blvd in Pico-Union with a marker at 1568 W Pico Blvd",1200,640)}<figcaption class="mapc">Map data © <a href="https://www.openstreetmap.org/copyright" rel="noopener" target="_blank">OpenStreetMap</a> contributors</figcaption></figure></section>
'''+foot()
nf=head("Not found | Lucy's Drive Thru","This page doesn't exist. Lucy's Drive Thru, 1568 W Pico Blvd, open 24 hours.","404.html").replace('<link rel="canonical"','<meta name="robots" content="noindex"><link rel="x-canonical"')+f'''
<section class="nf">{tc("04:04 AM")}<h1 class="mega2">Wrong turn.</h1><p class="lede">Still open, though.</p><div class="ctas" style="justify-content:center"><a class="btn b1" href="{B}">Home</a><a class="btn b2" href="{B}menu/">Menu</a></div></section>
'''+foot()
for p,h in [("index.html",home),("menu/index.html",menu),("find-us/index.html",find),("404.html",nf)]: open(p,"w").write(h)
open("robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {U}sitemap.xml\n")
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{U}{p}</loc><lastmod>2026-10-22</lastmod></url>\n" for p in ["","menu/","find-us/"])+"</urlset>\n")
open("site.webmanifest","w").write(json.dumps({"name":"Lucy's Drive Thru","short_name":"Lucy's","start_url":B,"display":"browser","background_color":"#0D0E10","theme_color":"#0D0E10","icons":[{"src":B+"assets/icon-512.png","sizes":"512x512","type":"image/png"}]}))
