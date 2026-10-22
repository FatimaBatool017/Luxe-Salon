"""Luxe Salon - a graphic-rich salon app built with Streamlit.
Run locally:  streamlit run Main.py
"""
from datetime import date, timedelta

import streamlit as st

st.set_page_config(page_title="Luxe Salon", page_icon="💅", layout="centered")

# ───────────────────────── DATA ─────────────────────────
SERVICES = [
    ("Haircut", "✂️", 2500, 45), ("Hair Color", "🎨", 6500, 120),
    ("Facial", "🧖‍♀️", 3500, 60), ("Makeup", "💄", 8000, 90),
    ("Nails", "💅", 2000, 50), ("Spa", "🌿", 5000, 75),
    ("Waxing", "✨", 1800, 30), ("Bridal", "👰", 25000, 240),
]
STYLISTS = [
    ("Ayesha", "Hair colour artist", 4.9, "#B76E79"),
    ("Hira", "Bridal makeup", 4.8, "#D4AF37"),
    ("Zara", "Nail designer", 4.7, "#9C6B8E"),
    ("Mehwish", "Skin and facial expert", 4.9, "#C98B76"),
]
OFFERS = [
    ("Bridal Glow Package", "Makeup, hair and facial", "linear-gradient(135deg,#B76E79,#E8B4B8)"),
    ("Keratin Treatment", "New this month, 20% off", "linear-gradient(135deg,#D4AF37,#F7E7CE)"),
    ("Mani + Pedi Duo", "Bring a friend, save Rs 1,000", "linear-gradient(135deg,#9C6B8E,#F8E1E7)"),
]
TRENDS = [
    ("Balayage waves", "🌊", "#E8B4B8", 190), ("Glass nails", "💎", "#F7E7CE", 130),
    ("Soft glam", "🌸", "#D9A5B3", 150), ("Curtain bangs", "✂️", "#EBD3C0", 170),
]
REVIEWS = [
    ("Best balayage I have ever had. The salon feels like a spa.", "Sana R."),
    ("Booked my bridal look here. Everyone asked who did my makeup.", "Maryam K."),
    ("On time, spotless and the staff are so kind.", "Iqra A."),
]
SLOTS = ["10:00", "11:30", "13:00", "14:30", "16:00", "17:30"]
BOOKED = {"11:30", "16:00"}
PROMO = {"LUXE20": 0.20}

# ───────────────────────── STATE ─────────────────────────
st.session_state.setdefault("page", "Home")
st.session_state.setdefault("name", "Sara")
st.session_state.setdefault("points", 1240)
st.session_state.setdefault("appointments", [])

# ───────────────────────── STYLE ─────────────────────────
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Poppins:wght@300;400;500;600&display=swap');
:root{--blush:#F8E1E7;--rose:#B76E79;--champ:#F7E7CE;--ivory:#FFFAF5;--plum:#3D1F2B;--gold:#D4AF37;}
.stApp{background:
 radial-gradient(circle at 92% -4%,rgba(248,225,231,.95),transparent 42%),
 radial-gradient(circle at -8% 45%,rgba(247,231,206,.9),transparent 38%),
 radial-gradient(circle at 100% 96%,rgba(183,110,121,.25),transparent 42%),var(--ivory);}
html,body,[class*="css"],.stMarkdown,p,label{font-family:'Poppins',sans-serif;color:var(--plum);}
h1,h2,h3,.serif{font-family:'Playfair Display',serif!important;color:var(--plum);}
.block-container{max-width:780px;padding-top:1.2rem;padding-bottom:4rem;}
header[data-testid="stHeader"]{background:transparent;}
#MainMenu,footer{visibility:hidden;}
div[role="radiogroup"]{gap:.4rem;justify-content:center;flex-wrap:wrap;}
div[role="radiogroup"] label{background:rgba(255,255,255,.7);border:1px solid var(--rose);border-radius:22px;padding:.25rem .9rem;}
.stButton>button,.stFormSubmitButton>button{background:linear-gradient(135deg,var(--rose),var(--gold));color:#fff;border:0;border-radius:22px;padding:.55rem 1.5rem;font-weight:500;box-shadow:0 8px 18px rgba(183,110,121,.35);}
.stButton>button:hover{color:#fff;filter:brightness(1.06);}
.top{display:flex;align-items:center;gap:12px;margin:.4rem 0 1rem;}
.av{width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,var(--rose),var(--gold));color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:20px;}
.small{font-size:.8rem;opacity:.75;} .nm{font-size:1.5rem;font-weight:700;line-height:1.1;}
.bell{margin-left:auto;font-size:1.5rem;position:relative;} .bell i{position:absolute;right:-1px;top:2px;width:10px;height:10px;border-radius:50%;background:var(--rose);}
.sec{display:flex;justify-content:space-between;align-items:baseline;margin:1.8rem 0 .8rem;}
.sec b{font-family:'Playfair Display',serif;font-size:1.35rem;} .sec span{color:var(--rose);font-size:.8rem;font-weight:600;}
.hero{position:relative;height:215px;border-radius:30px;overflow:hidden;box-shadow:0 14px 30px rgba(183,110,121,.3);}
.slide{position:absolute;inset:0;padding:26px;opacity:0;animation:fade 12s infinite;display:flex;flex-direction:column;justify-content:center;color:#fff;}
.slide:nth-child(2){animation-delay:4s;} .slide:nth-child(3){animation-delay:8s;}
@keyframes fade{0%{opacity:0}6%{opacity:1}30%{opacity:1}36%{opacity:0}100%{opacity:0}}
.slide h2{color:#fff!important;margin:0 0 4px;font-size:1.7rem;} .slide p{color:#fff;margin:0;}
.slide svg{position:absolute;right:10px;top:12px;}
.sp{position:absolute;color:#fff;animation:tw 2.6s ease-in-out infinite;} @keyframes tw{0%,100%{opacity:.2;transform:scale(.6)}50%{opacity:1;transform:scale(1.3)}}
.row{display:flex;gap:14px;overflow-x:auto;padding:6px 2px 14px;} .row::-webkit-scrollbar{display:none;}
.bub{min-width:78px;text-align:center;font-size:.78rem;}
.bub div{width:66px;height:66px;margin:0 auto 7px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:28px;background:linear-gradient(135deg,var(--blush),var(--champ));border:1.4px solid var(--rose);box-shadow:0 8px 16px rgba(183,110,121,.25);}
.card{background:#fff;border-radius:26px;padding:18px;box-shadow:0 10px 24px rgba(183,110,121,.16);position:relative;overflow:hidden;}
.card .vine{position:absolute;right:-6px;top:-4px;opacity:.55;}
.sty{min-width:150px;text-align:center;} .sty .a{width:58px;height:58px;border-radius:50%;margin:0 auto 8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:22px;border:2px solid #fff;}
.sty b{font-size:.95rem;} .sty p{font-size:.75rem;margin:2px 0 6px;opacity:.8;}
.trend{columns:2;column-gap:12px;} .tile{break-inside:avoid;margin-bottom:12px;border-radius:24px;position:relative;display:flex;align-items:center;justify-content:center;font-size:44px;}
.tile em{position:absolute;left:14px;bottom:10px;font-size:.78rem;font-style:normal;font-weight:600;}
.offer{min-width:250px;height:130px;border-radius:26px;padding:18px;color:#fff;display:flex;flex-direction:column;justify-content:center;}
.offer b{font-family:'Playfair Display',serif;font-size:1.2rem;} .offer span{font-size:.8rem;}
.loy{background:linear-gradient(135deg,#3D1F2B,#6B3A4E);color:#F8E1E7;border-radius:28px;padding:20px;}
.loy .bar{height:8px;border-radius:8px;background:rgba(255,255,255,.2);margin:12px 0 8px;overflow:hidden;} .loy .bar i{display:block;height:100%;background:var(--gold);}
.rev{min-width:270px;} .rev q{display:block;font-size:.9rem;margin:6px 0 10px;quotes:none;}
.ba{position:relative;height:170px;border-radius:26px;overflow:hidden;font-size:60px;}
.ba>div{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;} .ba em{position:absolute;left:14px;bottom:10px;font-size:.85rem;font-style:normal;font-weight:600;color:#fff;}
.ba .ln{position:absolute;top:0;bottom:0;width:3px;background:#fff;}
.chip{display:inline-block;background:var(--blush);border-radius:14px;padding:2px 10px;font-size:.8rem;margin:2px 4px 2px 0;}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


def html(s: str) -> None:
    """Render HTML without Markdown turning indented lines into code blocks."""
    st.markdown(" ".join(line.strip() for line in s.strip().splitlines()), unsafe_allow_html=True)


def section(title: str, more: str = "See all") -> None:
    html(f'<div class="sec"><b>{title}</b><span>{more}</span></div>')


def go(page: str) -> None:
    st.session_state.page = page


VINE = ('<svg class="vine" width="90" height="90" viewBox="0 0 90 90"><path d="M0 90 Q10 30 90 0" fill="none" '
        'stroke="#B76E79" stroke-width="2"/><ellipse cx="22" cy="55" rx="13" ry="5" fill="#B76E79" opacity=".4" '
        'transform="rotate(-50 22 55)"/><ellipse cx="42" cy="32" rx="13" ry="5" fill="#B76E79" opacity=".4" '
        'transform="rotate(-30 42 32)"/><ellipse cx="66" cy="14" rx="13" ry="5" fill="#B76E79" opacity=".4" '
        'transform="rotate(-15 66 14)"/></svg>')

MIRROR = ('<svg width="130" height="165" viewBox="0 0 120 150"><ellipse cx="60" cy="55" rx="42" ry="48" '
          'fill="rgba(255,255,255,.28)" stroke="#fff" stroke-width="3.5"/><ellipse cx="60" cy="55" rx="34" ry="40" '
          'fill="none" stroke="#fff" stroke-width="1.2"/><path d="M38 40 Q42 28 54 24" stroke="#fff" '
          'stroke-width="2.5" fill="none" stroke-linecap="round"/><line x1="60" y1="103" x2="60" y2="145" '
          'stroke="#fff" stroke-width="5" stroke-linecap="round"/></svg>')

SPARKS = "".join(
    f'<span class="sp" style="left:{x}%;top:{y}%;font-size:{s}px;animation-delay:{d}s">✦</span>'
    for x, y, s, d in [(8, 15, 16, 0), (55, 10, 12, .8), (78, 70, 18, 1.4), (40, 82, 12, .4), (90, 38, 14, 2)]
)


# ───────────────────────── PAGES ─────────────────────────
def page_home() -> None:
    name = st.session_state.name
    html(f'<div class="top"><div class="av">{name[:1].upper()}</div><div><div class="small">Welcome back</div>'
         f'<div class="serif nm">{name}</div></div><div class="bell">🔔<i></i></div></div>')

    banners = [("Bridal makeup", "20% off this season", "linear-gradient(135deg,#B76E79,#F7E7CE)"),
               ("Keratin treatment", "New at Luxe Salon", "linear-gradient(135deg,#D4AF37,#F8E1E7)"),
               ("Glow facial", "Free skin consultation", "linear-gradient(135deg,#9C6B8E,#F8E1E7)")]
    slides = "".join(f'<div class="slide" style="background:{g}">{MIRROR}<h2>{t}</h2><p>{s}</p></div>'
                     for t, s, g in banners)
    html(f'<div class="hero">{slides}{SPARKS}</div>')
    st.write("")
    st.button("Book now", on_click=go, args=("Book",), key="hero_book")

    section("Our services")
    html('<div class="row">' + "".join(f'<div class="bub"><div>{i}</div>{n}</div>' for n, i, _, _ in SERVICES) + "</div>")

    section("Your next visit", "")
    if st.session_state.appointments:
        a = st.session_state.appointments[-1]
        svc, who, when = ", ".join(a["services"]), a["stylist"], f'{a["date"]:%a %d %b}, {a["slot"]}'
    else:
        svc, who, when = "Balayage and trim", "Ayesha", "Sat, 2:30 PM"
    html(f'<div class="card">{VINE}<b style="font-size:1.05rem">{svc}</b><br><span class="small">with {who}</span>'
         f'<br><br>📅 {when} &nbsp;&nbsp; ⏳ Coming up</div>')

    section("Top stylists")
    html('<div class="row">' + "".join(
        f'<div class="card sty"><div class="a" style="background:{c}">{n[0]}</div><b>{n}</b><p>{r}</p>⭐ {rt}</div>'
        for n, r, rt, c in STYLISTS) + "</div>")

    section("Trending styles")
    html('<div class="trend">' + "".join(
        f'<div class="tile" style="height:{h}px;background:linear-gradient(135deg,{c},#fff8)">{i}<em>{n}</em></div>'
        for n, i, c, h in TRENDS) + "</div>")

    section("See the difference", "")
    pct = st.slider("Drag to compare before and after", 8, 92, 50, label_visibility="collapsed")
    html(f'<div class="ba"><div style="background:linear-gradient(135deg,#B76E79,#F7E7CE)">✨<em>After</em></div>'
         f'<div style="background:linear-gradient(135deg,#8E8A8C,#D8D2D4);clip-path:inset(0 {100 - pct}% 0 0)">🪞<em>Before</em></div>'
         f'<div class="ln" style="left:{pct}%"></div></div>')

    section("Offers and packages")
    html('<div class="row">' + "".join(
        f'<div class="offer" style="background:{g}"><b>{t}</b><span>{s}</span></div>' for t, s, g in OFFERS) + "</div>")

    pts = st.session_state.points
    html(f'<div class="loy">🏅 <b>Gold member</b> <span style="float:right">{pts:,} pts</span>'
         f'<div class="bar"><i style="width:{min(100, pts // 20)}%"></i></div>'
         f'<span class="small" style="color:#F8E1E7">{max(0, 2000 - pts)} points to your next free treatment</span></div>')

    section("Loved by clients", "")
    html('<div class="row">' + "".join(
        f'<div class="card rev">❝<q>{q}</q><b class="small">{who}</b></div>' for q, who in REVIEWS) + "</div>")


def page_services() -> None:
    st.markdown("## Services")
    q = st.text_input("Search services", placeholder="Try: facial, bridal, nails").strip().lower()
    for n, i, p, m in SERVICES:
        if q and q not in n.lower():
            continue
        html(f'<div class="card" style="margin-bottom:12px">{VINE}<span style="font-size:1.6rem">{i}</span> '
             f'<b style="font-size:1.05rem">&nbsp;{n}</b><br><span class="small">{m} min</span>'
             f'<span style="float:right;font-weight:600;color:#B76E79">Rs {p:,}</span></div>')


def page_book() -> None:
    st.markdown("## Book a visit")
    names = [f"{i} {n}  ·  Rs {p:,}" for n, i, p, _ in SERVICES]
    picked = st.multiselect("Choose services", names, placeholder="Pick one or more")
    stylist = st.selectbox("Choose your stylist", [s[0] for s in STYLISTS])
    day = st.date_input("Pick a date", min_value=date.today(), max_value=date.today() + timedelta(days=60))
    free = [s for s in SLOTS if s not in BOOKED]
    st.caption("Booked times (" + ", ".join(sorted(BOOKED)) + ") are hidden.")
    slot = st.radio("Pick a time", free, horizontal=True)
    promo = st.text_input("Promo code", placeholder="Try LUXE20").strip().upper()

    total = sum(SERVICES[names.index(p)][2] for p in picked)
    disc = PROMO.get(promo, 0)
    if promo and not disc:
        st.warning("That code is not valid.")
    final = int(total * (1 - disc))
    if picked:
        st.info(f"Total: Rs {final:,}" + (f"  (20% off applied, you save Rs {total - final:,})" if disc else ""))

    if st.button("Confirm booking", disabled=not picked):
        st.session_state.appointments.append(
            {"services": [p.split("  ·")[0] for p in picked], "stylist": stylist, "date": day, "slot": slot, "total": final})
        st.session_state.points += final // 100
        st.balloons()
        st.success(f"You are booked. {stylist} will see you on {day:%a %d %b} at {slot}.")


def page_offers() -> None:
    st.markdown("## Offers")
    for t, s, g in OFFERS:
        html(f'<div class="offer" style="background:{g};margin-bottom:14px;width:auto"><b>{t}</b><span>{s}</span></div>')
    st.info("Use code LUXE20 on the Book page for 20% off.")


def page_profile() -> None:
    st.markdown("## Profile")
    st.session_state.name = st.text_input("Your name", st.session_state.name) or "Guest"
    st.markdown("### Your appointments")
    if not st.session_state.appointments:
        st.caption("No bookings yet. Head to Book to make your first one.")
    for a in reversed(st.session_state.appointments):
        chips = "".join(f'<span class="chip">{s}</span>' for s in a["services"])
        html(f'<div class="card" style="margin-bottom:12px">{chips}<br><b>{a["stylist"]}</b> · {a["date"]:%a %d %b}, '
             f'{a["slot"]}<span style="float:right">Rs {a["total"]:,}</span></div>')


# ───────────────────────── NAV ─────────────────────────
PAGES = {"Home": page_home, "Services": page_services, "Book": page_book, "Offers": page_offers, "Profile": page_profile}
st.radio("Navigate", list(PAGES), key="page", horizontal=True, label_visibility="collapsed")
PAGES[st.session_state.page]()
