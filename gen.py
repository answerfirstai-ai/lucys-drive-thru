import json
B="/lucys-drive-thru"; SITE="https://answerfirstai-ai.github.io/lucys-drive-thru"
DIR="https://www.google.com/maps/dir/?api=1&destination=Lucy%27s+Drive+Thru%2C+1568+W+Pico+Blvd%2C+Los+Angeles%2C+CA+90015"
TEL="tel:+12133840721"
ICO_P='<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
ICO_D='<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M21.7 11.3 12.7 2.3a1 1 0 0 0-1.4 0l-9 9a1 1 0 0 0 0 1.4l9 9a1 1 0 0 0 1.4 0l9-9a1 1 0 0 0 0-1.4zM14 14.5V12h-4v3H8v-4a1 1 0 0 1 1-1h5V7.5l3.5 3.5z"/></svg>'
def dbtn(cls="btn-a",lbl="Get directions"): return f'<a class="btn {cls}" data-dir href="{DIR}" target="_blank" rel="noopener">{ICO_D}<span class="lbl">{lbl}</span></a>'
def cbtn(cls="btn-g",lbl="Call (213) 384-0721"): return f'<a class="btn {cls}" data-call href="{TEL}">{ICO_P}<span class="lbl">{lbl}</span></a>'
SIGN='''<svg class="sign" viewBox="0 0 300 470" role="img" aria-labelledby="sgt"><title id="sgt">Illustration of Lucy's pole sign: Open 24 Hours, Lucy's Drive Thru, Mexican and American Food</title>
<rect class="pole" x="138" y="330" width="24" height="140"/>
<g class="box" data-box><rect x="50" y="8" width="200" height="56" rx="6" fill="#F2D43A" stroke="#C8312B" stroke-width="3"/><text x="150" y="45" text-anchor="middle" font-family="Bowlby One, Impact, sans-serif" font-size="19" fill="#C8312B">OPEN 24 HOURS</text></g>
<g class="box" data-box><rect x="40" y="76" width="220" height="104" rx="8" fill="#fff" stroke="#1F7A3A" stroke-width="4"/><text x="150" y="138" text-anchor="middle" font-family="Yellowtail, cursive" font-size="62" fill="#C8312B">Lucy's</text><text x="150" y="168" text-anchor="middle" font-family="Barlow Condensed, Arial Narrow, sans-serif" font-weight="700" font-size="24" letter-spacing="4" fill="#1F7A3A">DRIVE THRU</text></g>
<g class="box" data-box><rect x="10" y="192" width="280" height="138" rx="8" fill="#F2D43A" stroke="#C8312B" stroke-width="4"/><text text-anchor="middle" font-family="Bowlby One, Impact, sans-serif" fill="#C8312B"><tspan x="150" y="244" font-size="36">MEXICAN</tspan><tspan x="150" y="278" font-size="21">AND AMERICAN</tspan><tspan x="150" y="314" font-size="38">FOOD</tspan></text></g>
</svg>'''
SCHEMA={"@context":"https://schema.org","@type":"Restaurant","@id":SITE+"/#restaurant","name":"Lucy's Drive Thru","url":SITE+"/","telephone":"+1-213-384-0721",
"address":{"@type":"PostalAddress","streetAddress":"1568 W Pico Blvd","addressLocality":"Los Angeles","addressRegion":"CA","postalCode":"90015","addressCountry":"US"},
"geo":{"@type":"GeoCoordinates","latitude":34.0443442,"longitude":-118.2768267},
"hasMap":"https://www.google.com/maps/place/?q=place_id:ChIJN43S4pXHwoAR_sz0JYM8-tQ",
"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"00:00","closes":"23:59"}],
"servesCuisine":["Mexican","American"],"paymentAccepted":"Cash","priceRange":"$","areaServed":"Pico-Union, Los Angeles","image":SITE+"/assets/og.png",
"sameAs":["https://la.eater.com/venue/31256/lucy-s-drive-thru","https://www.yelp.com/biz/lucys-drive-thru-los-angeles"]}
def head(title,desc,path,extra=""):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{SITE}{path}">
<meta name="theme-color" content="#141A33"><meta name="color-scheme" content="dark">
<meta property="og:type" content="restaurant"><meta property="og:site_name" content="Lucy's Drive Thru"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{SITE}{path}"><meta property="og:image" content="{SITE}/assets/og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{SITE}/assets/og.png">
<link rel="icon" href="{B}/favicon.svg" type="image/svg+xml"><link rel="icon" href="{B}/favicon.ico" sizes="32x32"><link rel="apple-touch-icon" href="{B}/assets/apple-touch-icon.png"><link rel="manifest" href="{B}/site.webmanifest">
<link rel="preload" href="{B}/assets/fonts/BowlbyOne-400.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="{B}/assets/fonts/Barlow-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{B}/assets/site.css">
<script>if(!matchMedia('(prefers-reduced-motion: reduce)').matches)document.documentElement.classList.add('js-motion')</script>
<script type="application/ld+json">{json.dumps(SCHEMA)}</script>{extra}</head><body>
<a class="skip" href="#main">Skip to content</a>'''
def nav(cur):
    a=lambda h,t,k:f'<a class="l{" hide-s" if k=="find" else ""}" href="{B}{h}"{" aria-current=\"page\"" if cur==k else ""}>{t}</a>'
    return f'<nav class="nav" aria-label="Main"><a class="logo" href="{B}/" aria-label="Lucy\'s Drive Thru home">Lucy\'s</a>{a("/menu/","Menu","menu")}{a("/find-us/","Find us","find")}{cbtn("btn-g hide-s","Call")}{dbtn("btn-a","Directions")}</nav>'
FOOT=f'''<footer><div class="wrap f-grid">
<div><p class="logo" style="display:inline-block">Lucy's</p><p>Drive-thru on Pico.<br>Mexican and American food.</p></div>
<div><p><strong>Lucy's Drive Thru</strong><br>1568 W Pico Blvd<br>Los Angeles, CA 90015 (Pico-Union)</p><p><a href="{TEL}">(213) 384-0721</a></p></div>
<div><p><span class="open"><i></i>Open 24 hours, every day</span></p><p><span class="need">[NEED: confirm holiday hours]</span></p><p><strong>Cash only.</strong></p></div>
<div><p>Also listed on <a href="https://la.eater.com/venue/31256/lucy-s-drive-thru" rel="noopener" target="_blank">Eater LA</a>.</p><p><a href="{B}/menu/">Menu</a> · <a href="{B}/find-us/">Find us</a></p><p style="opacity:.6;font-size:.85rem">Sign artwork is an illustration based on Lucy's real pole sign.</p></div>
</div></footer>
<div class="mbar" role="group" aria-label="Quick actions">{dbtn("btn-a","Directions")}{cbtn("btn-g","Call")}</div>
<script src="{B}/assets/js/gsap.min.js" defer></script><script src="{B}/assets/js/ScrollTrigger.min.js" defer></script><script src="{B}/assets/js/app.js" defer></script></body></html>'''
ROUTE='''<svg viewBox="0 0 400 220" role="img" aria-label="Simplified line drawing of W Pico Blvd with a pin at 1568 W Pico Blvd"><rect width="400" height="220" rx="12" fill="#141A33"/>
<path d="M0 150 H400" stroke="#2f3866" stroke-width="22"/><path class="pico" d="M0 150 H400" stroke="#FFB238" stroke-width="4" stroke-dasharray="400" stroke-dashoffset="0" fill="none"/>
<text x="16" y="186" fill="#F4F4EE" font-family="Barlow Condensed, sans-serif" font-weight="700" font-size="16" letter-spacing="3">W PICO BLVD</text>
<g class="pin"><path d="M268 140c-14-18-22-30-22-42a22 22 0 0 1 44 0c0 12-8 24-22 42z" fill="#C8312B"/><circle cx="268" cy="98" r="8" fill="#fff"/></g>
<text x="300" y="104" fill="#fff" font-family="Barlow, sans-serif" font-weight="600" font-size="15">1568</text></svg>'''
MAPBOX=f'<div class="mapbox" data-map><button class="btn btn-g" type="button" data-loadmap>Show the map</button></div>'
# ---------- HOME
cards=[("y","24","Hours a day. Every day. Pull up whenever."),("","Cash","Only, at the window. Bring it and you're set."),("g","Drive","Thru. Stay in the car, roll down the window."),("r","Mexican","Food, right on the sign."),("","American","Food too. Says so in yellow."),("y","Pico","1568 W Pico Blvd, Pico-Union."),("","Menu","<span class=\"need\">[NEED: real menu + photos from Lucy's]</span>")]
shelf="".join(f'<article class="card {c}"><p class="big">{b}</p><p>{t}</p></article>' for c,b,t in cards)
home=head("Lucy's Drive Thru | Open 24 Hours on Pico Blvd, Los Angeles","Mexican and American food drive-thru at 1568 W Pico Blvd in Pico-Union, open 24 hours. Cash only. Call (213) 384-0721 or get directions.","/")+nav("home")+f'''
<main id="main">
<section class="hero" aria-labelledby="h1"><div class="lamp" style="left:8%"></div><div class="lamp" style="right:4%"></div><div class="street" aria-hidden="true"></div>
<div class="wrap hero-grid"><div class="hero-copy">
<p class="open" data-hero><i></i>Open now · 24 hours</p>
<h1 id="h1" data-hero><span class="s">Lucy's.</span>Mexican and American food on <span class="y">Pico.</span> Open 24 hours.</h1>
<p class="sub" data-hero>Pull up any time. Bring cash.</p>
<div class="ctas">{dbtn()}{cbtn()}</div></div>
{SIGN}</div>
<div class="lanes" aria-hidden="true"><span class="lane">24 HRS</span><span class="lane">CASH ONLY</span></div></section>

<section class="pull" id="pull" aria-labelledby="pull-h"><div class="beam" aria-hidden="true"></div><div class="beam b2" aria-hidden="true"></div>
<div class="wrap pull-grid"><div><p class="eyebrow">Chapter 1 · Pull in</p><h2 id="pull-h">Headlights on. Window down.</h2><p class="sub" style="max-width:36ch;margin:18px 0 24px">Lucy's is a drive-thru on W Pico Blvd. Order from the car, any hour.</p>{dbtn()}</div>
<div class="board"><div class="board-in" data-board><div class="board-head"><span class="flap" data-flap>THE BOARD</span><span>CASH ONLY</span></div>
<ul class="rows"><li><span>Mexican food</span><span>✓</span></li><li><span>American food</span><span>✓</span></li><li><span>Open 24 hours</span><span>✓</span></li><li><span>Cards</span><span>✗</span></li><li><span class="need">[NEED: menu items + prices from Lucy's]</span></li></ul></div></div></div></section>

<section class="shelf-sec" aria-labelledby="shelf-h"><h2 class="shelf-h" id="shelf-h">The short version. <span>Everything you need before you pull up.</span></h2>
<div class="shelf" tabindex="0" aria-label="Quick facts, scroll sideways" data-shelf>{shelf}</div>
<div class="shelf-ctrl"><button type="button" aria-label="Previous" data-sh="-1">←</button><button type="button" aria-label="Next" data-sh="1">→</button></div></section>

<section class="sky" id="sky" aria-labelledby="sky-h"><h2 id="sky-h" class="skip" style="position:absolute;left:-999px">Open any hour</h2>
<div class="layer l-dusk"></div><div class="layer l-night"></div><div class="stars" aria-hidden="true"></div><div class="layer l-dawn"></div><div class="sun" aria-hidden="true"></div><div class="skyline" aria-hidden="true"></div>
<div class="sky-ui"><div><p class="eyebrow" style="color:#fff">Chapter 3 · Any hour</p><p class="clock" aria-hidden="true" data-clock>6 PM</p><p class="stamp">Open.</p><p class="cap" data-cap>6 PM. Open.</p>
<p class="sr" style="position:absolute;left:-999px">6 PM. Open. 3 AM. Still open. 6 AM. Yep, open.</p></div></div></section>

<section class="cash" aria-labelledby="cash-h"><div class="wrap"><p class="eyebrow" style="color:#C8312B">Bring cash</p><h2 id="cash-h">Cash only at the window.</h2><p>Plan ahead and you're set. <span class="need">[NEED: confirm nearest ATM]</span></p>
<p class="ticker" aria-hidden="true">CASH ONLY · 24 HRS · CASH ONLY · 24 HRS · CASH ONLY · 24 HRS · CASH ONLY · 24 HRS</p></div></section>

<section class="find" id="find" aria-labelledby="find-h"><div class="wrap find-grid"><div><p class="eyebrow">Find us</p><h2 id="find-h">On Pico, in Pico-Union.</h2>
<address class="nap"><strong>Lucy's Drive Thru</strong>1568 W Pico Blvd<br>Los Angeles, CA 90015<br><a href="{TEL}">(213) 384-0721</a></address><div class="ctas">{dbtn()}{cbtn()}</div></div>
<div class="route">{ROUTE}{MAPBOX}</div></div></section>

<section class="final" aria-labelledby="fin-h"><div class="wrap"><h2 id="fin-h">Hungry now? We're up.</h2><p class="sub" style="margin:14px auto 0">Open 24 hours. Cash only.</p><div class="ctas">{dbtn()}{cbtn()}</div></div></section>
</main>'''+FOOT
open("index.html","w").write(home)
# ---------- MENU
cats="".join(f'<article class="card"><p class="big" style="font-size:1.6rem">{t}</p><p><span class="need">[NEED: items + prices from Lucy\'s]</span></p></article>' for t in ["Mexican","American"])
menu=head("Menu | Lucy's Drive Thru, 24 Hours on Pico Blvd","Lucy's Drive Thru serves Mexican and American food 24 hours a day at 1568 W Pico Blvd, Los Angeles. Cash only. Call (213) 384-0721.","/menu/")+nav("menu")+f'''
<main id="main"><section class="page-hero"><div class="wrap"><p class="eyebrow">The board</p><h1>Mexican and American food. <span style="color:var(--primary)">Any hour.</span></h1>
<p class="sub" style="max-width:52ch;margin:18px 0 0">The full menu is coming straight from Lucy's. Until then, call and ask what's good tonight.</p>
<p style="margin-top:16px"><span class="need">[NEED: confirmed menu + prices from owner. Will be labeled "Prices may vary, call to confirm."]</span></p>
<div class="ctas" style="margin-top:24px">{cbtn("btn-a","Call (213) 384-0721")}{dbtn("btn-g")}</div>
<p style="margin-top:18px"><strong>Cash only.</strong> Open 24 hours.</p>
<div class="cats">{cats}</div></div></section></main>'''+FOOT
open("menu/index.html","w").write(menu)
# ---------- FIND
find=head("Find Us | Lucy's Drive Thru, 1568 W Pico Blvd, Los Angeles","Directions to Lucy's Drive Thru at 1568 W Pico Blvd, Los Angeles, CA 90015 in Pico-Union. Open 24 hours, cash only. Call (213) 384-0721.","/find-us/")+nav("find")+f'''
<main id="main"><section class="page-hero"><div class="wrap find-grid"><div><p class="eyebrow">Find us</p><h1>1568 W Pico Blvd.</h1>
<address class="nap"><strong>Lucy's Drive Thru</strong>1568 W Pico Blvd<br>Los Angeles, CA 90015 (Pico-Union)<br><a href="{TEL}">(213) 384-0721</a></address>
<p><span class="open"><i></i>Open 24 hours, every day</span> · <strong>Cash only</strong></p>
<p><span class="need">[NEED: which side is the drive-thru entrance?]</span></p><p><span class="need">[NEED: walk-up window? parking?]</span></p>
<div class="ctas" style="margin-top:20px">{dbtn()}{cbtn()}</div></div><div class="route">{ROUTE}{MAPBOX}</div></div></section></main>'''+FOOT
open("find-us/index.html","w").write(find)
nf=head("Page not found | Lucy's Drive Thru","This page isn't on the board. Lucy's Drive Thru, 1568 W Pico Blvd, open 24 hours.","/404.html",'<meta name="robots" content="noindex">')+nav("")+f'''<main id="main"><section class="page-hero" style="min-height:70vh"><div class="wrap"><p class="eyebrow">404</p><h1>Wrong turn on Pico.</h1><p class="sub" style="margin:18px 0 24px">That page isn't here. Lucy's still is, 24 hours.</p><div class="ctas"><a class="btn btn-a" href="{B}/">Back to Lucy's</a>{dbtn("btn-g")}</div></div></section></main>'''+FOOT
open("404.html","w").write(nf)
open("robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{SITE}{p}</loc><lastmod>2026-10-22</lastmod></url>\n" for p in ["/","/menu/","/find-us/"])+"</urlset>\n")
open("site.webmanifest","w").write(json.dumps({"name":"Lucy's Drive Thru","short_name":"Lucy's","start_url":B+"/","display":"browser","background_color":"#141A33","theme_color":"#141A33","icons":[{"src":B+"/assets/apple-touch-icon.png","sizes":"180x180","type":"image/png"},{"src":B+"/assets/icon-512.png","sizes":"512x512","type":"image/png"}]}))
