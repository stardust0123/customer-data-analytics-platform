import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(
    page_title="The Gioi Di Dong | Analytics",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

PBI = {
    "overview":  "",
    "customers": "",
    "orders":    "",
    "products":  "",
    "regional":  "",
    "reports":   "",
}

# ─── CSS — Full Dark Mode ─────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap');

:root {
    --yellow:   #FFD400;
    --orange:   #FF6B00;
    --gold:     #F59E0B;
    --bg:       #0D0D0F;
    --surface:  #161618;
    --card:     #1C1C1F;
    --border:   #2A2A2E;
    --text:     #F0F0F0;
    --muted:    #888;
    --green:    #22c55e;
    --red:      #ef4444;
    --radius:   12px;
}

.tgdd-header {
    background: var(--yellow);
    height: 14vh;
    min-height: 90px;
    padding: 0 18px;
    display: flex;
    align-items: center;
    border-bottom: 3px solid var(--orange);
    box-shadow: 0 2px 20px rgba(255,212,0,.25);
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1300;
}

.tgdd-top-nav {
    position: fixed;
    top: 8vh;
    left: 0;
    right: 0;
    z-index: 1250;
    background: rgba(15, 15, 18, .98);
    border-bottom: 1px solid rgba(255,255,255,.08);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 8vh;
    min-height: 52px;
    gap: 12px;
    padding: 0 16px;
    overflow-x: auto;
}

.stApp                  { background: var(--bg) !important; }
.main .block-container  { padding: calc(14vh + 8vh + 32px) 18px 18px !important; max-width: 100% !important; }
html { scroll-behavior: smooth; }
/* ── Remove Streamlit chrome ── */
#MainMenu, footer, header,
.stAppHeader, .stToolbar { display: none !important; }

/* Keep navigator open/close button available */
[data-testid="collapsedControl"] { display: block !important; }

/* Hide default sidebar and use top fixed nav instead */
section[data-testid="stSidebar"] { display: none !important; }
.tgdd-top-nav a {
    color: #FFF;
    text-decoration: none;
    font-size: 13px;
    font-weight: 700;
    padding: 6px 10px;
    border-radius: 8px;
    white-space: nowrap;
}
.tgdd-top-nav a:hover {
    background: rgba(255, 212, 0, .2);
    color: #FFD400;
}

.stApp                  { background: var(--bg) !important; }
.main .block-container  { padding: 132px 18px 18px !important; max-width: 100% !important; }
html, body, [class*="css"] {
    font-family: 'Be Vietnam Pro', sans-serif !important;
    background: var(--bg);
    color: var(--text);
}

/* ── HEADER — stays yellow (brand requirement) ── */
.tgdd-header {
    background: var(--yellow);
    height: 62px;
    padding: 0 32px;
    display: flex;
    align-items: center;
    gap: 13px;
    border-bottom: 3px solid var(--orange);
    box-shadow: 0 2px 20px rgba(255,212,0,.25);
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1300;
}
.logo-ring     { width: 42px; height: 42px; border-radius: 50%; background: #fff; display: flex; align-items: center; justify-content: center; overflow: hidden; flex-shrink: 0; box-shadow: 0 2px 8px rgba(0,0,0,.2); }
.logo-ring img { width: 36px; height: 36px; object-fit: contain; }
.brand-name    { font-size: 18px; font-weight: 800; color: #1A1A2E; letter-spacing: -.5px; line-height: 1; }
.brand-name em { color: var(--orange); font-style: normal; }
.brand-tag     { font-size: 9px; font-weight: 700; color: #1A1A2E; background: rgba(0,0,0,.12); padding: 2px 8px; border-radius: 20px; letter-spacing: 1px; text-transform: uppercase; margin-top: 3px; display: inline-block; }

/* ── SECTION TITLE ── */
.sec-title {
    display: flex; align-items: center; gap: 8px;
    font-size: 15px; font-weight: 800; color: var(--text);
    margin: 0 0 12px;
}
.sec-title::after {
    content: ''; flex: 1; height: 1px;
    background: linear-gradient(90deg, var(--yellow), transparent);
    margin-left: 6px;
}

/* ── KPI CARDS via st.metric override ── */
[data-testid="stMetric"] {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 18px 20px !important;
    box-shadow: 0 4px 20px rgba(0,0,0,.4) !important;
    position: relative;
    overflow: hidden;
    transition: transform .2s, box-shadow .2s;
}
[data-testid="stMetric"]:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 30px rgba(0,0,0,.5) !important;
}
[data-testid="stMetric"]::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, var(--yellow), var(--orange));
}
[data-testid="stMetricLabel"] > div {
    font-size: 10px !important; font-weight: 700 !important;
    text-transform: uppercase; letter-spacing: .6px;
    color: var(--muted) !important;
}
[data-testid="stMetricValue"] {
    font-size: 28px !important; font-weight: 800 !important;
    color: var(--yellow) !important;
}
[data-testid="stMetricDelta"] { font-size: 11px !important; }

/* ── POWER BI ── */
.pbi-wrap {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,.4);
}
.pbi-wrap iframe { width: 100%; border: none; display: block; }
.pbi-empty {
    background: var(--card);
    border: 1px dashed var(--border);
    border-radius: var(--radius);
    padding: 52px 20px; text-align: center;
}
.pbi-empty .ei { font-size: 44px; margin-bottom: 12px; filter: grayscale(.3); }
.pbi-empty h3  { font-size: 15px; font-weight: 700; color: var(--text); margin: 0 0 8px; }
.pbi-empty p   { font-size: 12px; color: var(--muted); margin: 0 auto 12px; max-width: 400px; line-height: 1.65; }
.pbi-empty code { background: #2A2A2E; color: var(--yellow); padding: 3px 10px; border-radius: 6px; font-size: 11px; font-family: monospace; }

/* ── ACTIVITY TABLE ── */
.tbl { width: 100%; border-collapse: collapse; font-size: 12px; }
.tbl th { background: var(--surface); padding: 10px 14px; text-align: left; font-weight: 700; font-size: 10px; text-transform: uppercase; letter-spacing: .5px; color: var(--muted); border-bottom: 1px solid var(--border); }
.tbl td { padding: 11px 14px; border-bottom: 1px solid var(--border); color: var(--text); }
.tbl tr:last-child td { border-bottom: none; }
.tbl tr:hover td { background: rgba(255,212,0,.04); }
.badge { display: inline-block; padding: 2px 9px; border-radius: 20px; font-size: 10px; font-weight: 700; }
.bg { background: rgba(34,197,94,.15);  color: #4ade80; }
.bo { background: rgba(249,115,22,.15); color: #fb923c; }
.bb { background: rgba(59,130,246,.15); color: #60a5fa; }
.br { background: rgba(239,68,68,.15);  color: #f87171; }

/* ── SIDEBAR — dark ── */
section[data-testid="stSidebar"] > div {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
    padding-top: 0 !important;
}
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span { color: rgba(255,255,255,.75) !important; font-size: 12px; }
section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
    background: rgba(255,255,255,.04);
    border-radius: 8px; padding: 8px 12px;
    margin-bottom: 3px; display: block;
    transition: background .15s; cursor: pointer;
    border: 1px solid transparent;
}
section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
    background: rgba(255,212,0,.08);
    border-color: rgba(255,212,0,.2);
}
/* Selectbox dark */
section[data-testid="stSidebar"] .stSelectbox > div > div {
    background: var(--card) !important;
    border-color: var(--border) !important;
    color: var(--text) !important;
}

/* ── DIVIDER ── */
hr { border-color: var(--border) !important; }

/* ── FOOTER ── */
.tgdd-footer {
    display: flex; justify-content: space-between;
    font-size: 11px; color: var(--muted);
    padding-top: 12px; border-top: 1px solid var(--border);
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)


# ─── HELPERS ─────────────────────────────────────────────────────────────────
def sec_title(icon: str, text: str):
    st.markdown(f"""
    <div class="sec-title"><span>{icon}</span> {text}</div>
    """, unsafe_allow_html=True)


def spacer(px: int = 16):
    st.markdown(f"<div style='height:{px}px'></div>", unsafe_allow_html=True)


def embed_powerbi(key: str, height: int = 620):
    url = PBI.get(key, "")
    if url.startswith("http"):
        st.markdown(f"""
        <div class="pbi-wrap">
            <iframe src="{url}" height="{height}" allowfullscreen></iframe>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="pbi-empty">
            <iframe title="test" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiOGYzNTYxZmUtNmFhMC00ZmI0LTg2NTctMmQ4MzIwYjJhMTZlIiwidCI6ImRmN2Y3NTc5LTNlOWMtNGE3ZS1iODQ0LTQyMDI4MGY1Mzg1OSIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>
        </div>""", unsafe_allow_html=True)


# ─── SIDEBAR ─────────────────────────────────────────────────────────────────
with st.sidebar:
    # Yellow brand header strip
    st.markdown("""
    <div style="background:#FFD400;margin:-1rem -1rem 1rem;padding:15px 18px;
                display:flex;align-items:center;gap:10px;">
        <img src="app/static/logo.png"
             style="width:36px;height:36px;border-radius:50%;background:#fff;
                    object-fit:contain;padding:2px;"
             onerror="this.style.display='none'"/>
        <div>
            <div style="font-size:13px;font-weight:800;color:#1A1A2E;line-height:1.1;">
                the<span style="color:#FF6B00;">gioi</span>didong
            </div>
            <div style="font-size:9px;color:#333;font-weight:700;letter-spacing:.5px;margin-top:1px;">
                ANALYTICS PLATFORM
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-size:9px;font-weight:700;letter-spacing:1.2px;"
                "color:rgba(255,255,255,.3) !important;padding:0 4px;margin-bottom:6px;'>"
                "NAVIGATION</p>", unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        ["🏠  Home", "📊  Dashboard", "👥  Customers",
         "🛒  Orders", "📦  Products", "📍  Regional",
         "📈  Reports", "⚙️  Settings"],
        label_visibility="hidden",
    )

    st.markdown("<hr style='border-color:rgba(255,255,255,.08);margin:14px 0;'/>",
                unsafe_allow_html=True)
    st.markdown("<p style='font-size:9px;font-weight:700;letter-spacing:1.2px;"
                "color:rgba(255,255,255,.3) !important;padding:0 4px;margin-bottom:6px;'>"
                "FILTERS</p>", unsafe_allow_html=True)

    year    = st.selectbox("Year",    ["2024", "2023", "2022"])
    quarter = st.selectbox("Quarter", ["Full Year", "Q1", "Q2", "Q3", "Q4"])
    region  = st.selectbox("Region",  ["All Regions", "Ho Chi Minh City",
                                       "Hanoi", "Central", "South"])
    st.markdown("<hr style='border-color:rgba(255,255,255,.08);margin:14px 0;'/>",
                unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;font-size:10px;"
                "color:rgba(255,255,255,.2);'>v1.0.0 · © 2024 The Gioi Di Dong</div>",
                unsafe_allow_html=True)


# Fixed sidebar toggle button (always visible)
components.html("""
<style>
#sidebar-toggle { position: fixed !important; top: 10px !important; right: 10px !important; z-index: 1300 !important; background: #FFD400 !important; color: #000 !important; border: none !important; padding: 8px !important; border-radius: 4px !important; font-size: 16px !important; cursor: pointer !important; font-weight: bold !important; box-shadow: 0 4px 12px rgba(0,0,0,.25) !important; }
</style>
<button id="sidebar-toggle" title="Toggle sidebar">☰</button>
<script>
const getSidebarToggle = () => {
    return window.parent.document.querySelector('[data-testid="collapsedControl"]') ||
           window.parent.document.querySelector('button[aria-label="collapse sidebar"]') ||
           window.parent.document.querySelector('button[aria-label="Collapse sidebar"]') ||
           window.parent.document.querySelector('button[aria-label="expand sidebar"]') ||
           window.parent.document.querySelector('button[aria-label="Expand sidebar"]') ||
           window.parent.document.querySelector('button[data-testid="collapsedControl"]');
};

const ensureRootToggle = () => {
    const button = getSidebarToggle();
    if (!button) return null;
    if (!button.classList.contains('copilot-root-toggle')) {
        button.classList.add('copilot-root-toggle');
        button.style.position = 'fixed';
        button.style.top = '10px';
        button.style.left = '10px';
        button.style.zIndex = '1200';
        button.style.opacity = '1';
        button.style.visibility = 'visible';
        button.style.display = 'block';
        if (button.parentElement && button.parentElement !== window.parent.document.body) {
            window.parent.document.body.appendChild(button);
        }
    }
    return button;
};

const refreshNativeToggleStyle = () => {
    const t = ensureRootToggle();
    if (!t) return;
    t.style.display = 'block';
    t.style.position = 'fixed';
    t.style.top = '10px';
    t.style.left = '10px';
    t.style.zIndex = '1200';
    t.style.opacity = '1';
    t.style.visibility = 'visible';
};

const isSidebarHidden = (sidebar) => {
    if (!sidebar) return true;
    const style = window.getComputedStyle(sidebar);
    if (style.display === 'none' || style.visibility === 'hidden' || style.opacity === '0') return true;
    const width = parseFloat(style.width);
    return isNaN(width) || width < 80;
};

const updateButtonIcon = () => {
    const sidebar = window.parent.document.querySelector('section[data-testid="stSidebar"]');
    const hidden = isSidebarHidden(sidebar);
    document.getElementById('sidebar-toggle').textContent = hidden ? '☰' : '✕';
};

const ensureSidebarVisible = () => {
    const sidebar = window.parent.document.querySelector('section[data-testid="stSidebar"]');
    const hidden = isSidebarHidden(sidebar);
    if (hidden) {
        const toggle = getSidebarToggle();
        if (toggle) toggle.click();
    }
};

setInterval(() => { refreshNativeToggleStyle(); updateButtonIcon(); }, 250);

[100, 350, 800, 1400].forEach(delay => setTimeout(() => {
    ensureSidebarVisible();
    refreshNativeToggleStyle();
    updateButtonIcon();
}, delay));

const btn = document.getElementById('sidebar-toggle');
btn.addEventListener('click', () => {
    try {
        const toggle = getSidebarToggle();
        if (toggle) toggle.click();
    } catch (e) {
        console.warn('Sidebar toggle failed:', e);
    } finally {
        setTimeout(() => { refreshNativeToggleStyle(); updateButtonIcon(); }, 200);
    }
});

updateButtonIcon();
""", height=0)

# ─── HEADER — yellow brand bar ────────────────────────────────────────────────
st.markdown("""
<div class="tgdd-header">
    <div class="logo-ring">
        <img src="app/static/logo.png" alt="TGDD"
             onerror="this.outerHTML='<span style=font-size:20px>📱</span>'"/>
    </div>
    <div>
        <div class="brand-name">the<em>gioi</em>didong</div>
        <div class="brand-tag">Customer Data Analytics Platform</div>
    </div>
</div>

<div class="tgdd-top-nav">
    <a href="#section-overview">Overview</a>
    <a href="#section-customers">Customers</a>
    <a href="#section-orders">Orders</a>
    <a href="#section-products">Products</a>
    <a href="#section-regional">Regional</a>
    <a href="#section-reports">Reports</a>
    <a href="#section-settings">Settings</a>
</div>
""", unsafe_allow_html=True)


# ─── PAGES ───────────────────────────────────────────────────────────────────
def page_home():
    with st.container():
        spacer(20)

        # ── Hero — dark gradient, yellow accents, JS button via components ────
        components.html("""
<!DOCTYPE html><html><head>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@700;800&display=swap');
  *, *::before, *::after { box-sizing:border-box; margin:0; padding:0; }
  body { background:transparent; font-family:'Be Vietnam Pro',sans-serif; }

  .hero {
    background: linear-gradient(135deg, #0D0D0F 0%, #111116 40%, #1a1208 100%);
    border: 1px solid #2A2A2E;
    border-radius: 16px;
    padding: 40px 44px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 8px 40px rgba(0,0,0,.6);
  }
  /* Gold glow top-right */
  .hero::before {
    content:''; position:absolute; top:-80px; right:-80px;
    width:340px; height:340px;
    background: radial-gradient(circle, rgba(255,212,0,.12) 0%, transparent 65%);
    border-radius:50%; pointer-events:none;
  }
  /* Subtle grid pattern */
  .hero::after {
    content:''; position:absolute; inset:0;
    background-image:
      linear-gradient(rgba(255,212,0,.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,212,0,.03) 1px, transparent 1px);
    background-size: 32px 32px;
    pointer-events:none;
  }

  .chip {
    display:inline-flex; align-items:center; gap:6px;
    background:rgba(255,212,0,.1); border:1px solid rgba(255,212,0,.25);
    color:#FFD400; font-size:10px; font-weight:700;
    letter-spacing:1.5px; text-transform:uppercase;
    padding:4px 14px; border-radius:20px; margin-bottom:18px;
    position:relative; z-index:1;
  }
  .dot { width:6px;height:6px;background:#FFD400;border-radius:50%;
         animation:pulse 1.5s ease-in-out infinite; }
  @keyframes pulse {
    0%,100%{ opacity:1; transform:scale(1); }
    50%    { opacity:.4; transform:scale(.7); }
  }

  h1 {
    font-size:38px; font-weight:800; color:#F0F0F0;
    line-height:1.12; letter-spacing:-1px; margin-bottom:14px;
    position:relative; z-index:1;
  }
  h1 .hl { color:#FFD400; }

  p {
    font-size:14px; color:rgba(240,240,240,.58);
    max-width:500px; line-height:1.75; margin-bottom:28px;
    position:relative; z-index:1;
  }

  .btn {
    background: linear-gradient(135deg, #FFD400, #FF9500);
    color: #0D0D0F;
    padding: 12px 28px; border-radius: 9px;
    font-weight: 800; font-size: 14px;
    font-family:'Be Vietnam Pro',sans-serif;
    border: none; cursor: pointer;
    display: inline-flex; align-items: center; gap: 8px;
    box-shadow: 0 4px 20px rgba(255,212,0,.35);
    transition: transform .17s, box-shadow .17s;
    position: relative; z-index: 1;
    letter-spacing: -.2px;
  }
  .btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(255,212,0,.5);
  }
  .btn:active { transform: translateY(-1px); }

  /* Stats row inside hero */
  .stats {
    display: flex; gap: 32px; margin-top: 32px;
    padding-top: 28px;
    border-top: 1px solid rgba(255,255,255,.07);
    position: relative; z-index: 1;
  }
  .stat-val { font-size: 22px; font-weight: 800; color: #FFD400; line-height:1; }
  .stat-lbl { font-size: 11px; color: rgba(240,240,240,.45); margin-top: 3px; font-weight:500; }

  /* Stars */
  .star-wrap { position:fixed; top:0; left:0; width:100%; height:100%;
               pointer-events:none; z-index:9999; display:none; }
  .star { position:absolute; font-size:22px; animation:fly 1.4s ease-out forwards; }
  @keyframes fly {
    0%   { transform:translateY(0) scale(1) rotate(0deg); opacity:1; }
    60%  { transform:translateY(-120px) scale(1.5) rotate(210deg); opacity:1; }
    100% { transform:translateY(-220px) scale(.2) rotate(420deg); opacity:0; }
  }
</style></head><body>

<div class="hero">
  <div class="chip"><span class="dot"></span> Live Analytics Dashboard</div>
  <h1>
    The Gioi Di Dong<br>
    <span class="hl">Customer Data Analytics</span><br>
    Platform
  </h1>
  <p>
    Explore customer behavior, track business performance, and make
    data-driven decisions — all in one intelligent platform built for
    The Gioi Di Dong.
  </p>
  <button class="btn" id="viewBtn">📊 View Dashboard →</button>

  <div class="stats">
    <div>
      <div class="stat-val">12.4M+</div>
      <div class="stat-lbl">Customers</div>
    </div>
    <div>
      <div class="stat-val">34.5B ₫</div>
      <div class="stat-lbl">Revenue 2024</div>
    </div>
    <div>
      <div class="stat-val">2,300+</div>
      <div class="stat-lbl">Stores</div>
    </div>
    <div>
      <div class="stat-val">8.7M+</div>s
      <div class="stat-lbl">Orders</div>
    </div>
  </div>
</div>

<div class="star-wrap" id="stars"></div>

<script>
var EM = ['⭐','🌟','✨','💫','🌠','⭐','✨','🌟','💫','⭐','🌟','✨','🌟','⭐'];
document.getElementById('viewBtn').addEventListener('click', function() {
  var w = document.getElementById('stars');
  w.innerHTML = ''; w.style.display = 'block';
  EM.forEach(function(e, i) {
    var s = document.createElement('span');
    s.className = 'star'; s.textContent = e;
    s.style.left = (3 + Math.random() * 92) + '%';
    s.style.top  = (15 + Math.random() * 65) + '%';
    s.style.animationDelay = (i * 0.06) + 's';
    s.style.fontSize = (16 + Math.random() * 14) + 'px';
    w.appendChild(s);
  });
  setTimeout(function() { w.style.display = 'none'; w.innerHTML = ''; }, 1600);
  setTimeout(function() {
    var el = window.parent.document.getElementById('section-overview');
    if (el) el.scrollIntoView({ behavior:'smooth', block:'start' });
  }, 220);
});
</script>
</body></html>
""", height=370, scrolling=False)

        spacer(28)

        # ── KPI Cards — st.columns + st.metric, styled dark via CSS override ──
        sec_title("📈", "Key Performance Indicators")
        spacer(8)
        k1, k2, k3, k4 = st.columns(4, gap="medium")
        k1.metric("👥 Total Customers",   "12.4M+",  "↑ +8.2% vs last year")
        k2.metric("🛒 Total Orders 2024", "8.7M+",   "↑ +12.1% vs last year")
        k3.metric("💰 Revenue 2024",      "34.5B ₫", "↑ +12.4% growth")
        k4.metric("🏪 Stores Nationwide", "2,300+",  "↑ +120 new stores")

        spacer(32)

        # ── Power BI sections — anchor tags for scroll ────────────────────────
        st.markdown('<a id="section-overview" style="padding-top: calc(14vh + 8vh + 32px); margin-top: -calc(14vh + 8vh + 32px);"></a>', unsafe_allow_html=True)
        sec_title("📊", "Overview Dashboard")
        spacer(6)
        embed_powerbi("overview", height=620)

        spacer(24)

        st.markdown('<a id="section-customers" style="padding-top: calc(14vh + 8vh + 32px); margin-top: -calc(14vh + 8vh + 32px);"></a>', unsafe_allow_html=True)
        sec_title("👥", "Customer Analytics — RFM & CLV")
        spacer(6)
        embed_powerbi("customers", height=620)

        spacer(24)

        st.markdown('<a id="section-orders" style="padding-top: calc(14vh + 8vh + 32px); margin-top: -calc(14vh + 8vh + 32px);"></a>', unsafe_allow_html=True)
        sec_title("🛒", "Order Analytics — Revenue & Trends")
        spacer(6)
        embed_powerbi("orders", height=620)

        spacer(24)

        st.markdown('<a id="section-products" style="padding-top: calc(14vh + 8vh + 32px); margin-top: -calc(14vh + 8vh + 32px);"></a>', unsafe_allow_html=True)
        sec_title("📦", "Product Analytics — Best Sellers")
        spacer(6)
        embed_powerbi("products", height=620)

        spacer(24)

        st.markdown('<a id="section-regional" style="padding-top: calc(14vh + 8vh + 32px); margin-top: -calc(14vh + 8vh + 32px);"></a>', unsafe_allow_html=True)
        sec_title("📍", "Regional Analytics")
        spacer(6)
        embed_powerbi("regional", height=620)

        spacer(28)

        # ── Recent Activity ───────────────────────────────────────────────────
        sec_title("🕒", "Recent Activity")
        spacer(6)
        st.markdown("""
        <div style="background:#1C1C1F;border-radius:12px;border:1px solid #2A2A2E;
                    overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.4);">
        <table class="tbl">
            <thead><tr><th>Event</th><th>Time</th><th>Status</th></tr></thead>
            <tbody>
                <tr><td>📥 Q4 Data Import</td><td>2 minutes ago</td>
                    <td><span class="badge bg">Completed</span></td></tr>
                <tr><td>📊 December Report</td><td>1 hour ago</td>
                    <td><span class="badge bg">Completed</span></td></tr>
                <tr><td>🔄 CRM Sync</td><td>3 hours ago</td>
                    <td><span class="badge bo">Processing</span></td></tr>
                <tr><td>👥 RFM Analysis</td><td>Yesterday</td>
                    <td><span class="badge bb">Scheduled</span></td></tr>
                <tr><td>📦 Inventory Check</td><td>Yesterday</td>
                    <td><span class="badge bg">Completed</span></td></tr>
                <tr><td>⚠️ API Connection Error</td><td>2 days ago</td>
                    <td><span class="badge br">Error</span></td></tr>
            </tbody>
        </table>
        </div>""", unsafe_allow_html=True)

        spacer(28)
        st.markdown("""
        <div class="tgdd-footer">
            <span>© 2024 The Gioi Di Dong — Internal Analytics Platform</span>
            <span>Built with ❤️ · Streamlit · Power BI · Azure</span>
        </div>""", unsafe_allow_html=True)
        spacer(32)


def page_analytics(key: str, icon: str, title: str, desc: str):
    with st.container():
        spacer(20)
        st.markdown(f"""
        <div style="background:#1C1C1F;border:1px solid #2A2A2E;border-left:4px solid #FFD400;
                    border-radius:12px;padding:14px 18px;display:flex;align-items:center;
                    gap:13px;margin-bottom:18px;box-shadow:0 4px 16px rgba(0,0,0,.3);">
            <span style="font-size:26px;flex-shrink:0;">{icon}</span>
            <div>
                <div style="font-size:14px;font-weight:700;color:#F0F0F0;margin-bottom:2px;">{title}</div>
                <div style="font-size:12px;color:#888;">{desc}</div>
            </div>
        </div>""", unsafe_allow_html=True)
        sec_title(icon, title)
        spacer(6)
        embed_powerbi(key, height=720)
        spacer(32)


def page_settings():
    with st.container():
        spacer(20)
        st.markdown("""
        <div style="background:#1C1C1F;border:1px solid #2A2A2E;border-left:4px solid #FFD400;
                    border-radius:12px;padding:14px 18px;display:flex;align-items:center;
                    gap:13px;margin-bottom:18px;box-shadow:0 4px 16px rgba(0,0,0,.3);">
            <span style="font-size:26px;">⚙️</span>
            <div>
                <div style="font-size:14px;font-weight:700;color:#F0F0F0;margin-bottom:2px;">Settings & Data Upload</div>
                <div style="font-size:12px;color:#888;">Configure Power BI URLs and upload data files.</div>
            </div>
        </div>""", unsafe_allow_html=True)

        sec_title("🔗", "Power BI Embed URLs")
        spacer(6)
        st.info("💡 Power BI Service → **File → Embed report → Publish to web** → copy the `src` URL.")
        with st.expander("Configure Report URLs", expanded=True):
            c1, c2 = st.columns(2)
            with c1:
                st.text_input("Overview Dashboard", value=PBI["overview"],  placeholder="https://app.powerbi.com/view?r=...")
                st.text_input("Customer Analytics", value=PBI["customers"], placeholder="https://app.powerbi.com/view?r=...")
                st.text_input("Order Analytics",    value=PBI["orders"],    placeholder="https://app.powerbi.com/view?r=...")
            with c2:
                st.text_input("Product Analytics",  value=PBI["products"],  placeholder="https://app.powerbi.com/view?r=...")
                st.text_input("Regional Analytics", value=PBI["regional"],  placeholder="https://app.powerbi.com/view?r=...")
                st.text_input("Summary Reports",    value=PBI["reports"],   placeholder="https://app.powerbi.com/view?r=...")

        spacer(18)
        sec_title("📁", "Data File Upload")
        spacer(6)
        uploaded = st.file_uploader("Drag & drop a CSV or Excel file", type=["csv", "xlsx", "xls"])
        if uploaded:
            st.success(f"✅ **{uploaded.name}** ({uploaded.size / 1024:.1f} KB)")
            try:
                df = (pd.read_csv(uploaded) if uploaded.name.endswith(".csv")
                      else pd.read_excel(uploaded))
                st.dataframe(df.head(20), use_container_width=True, hide_index=True)
            except Exception as e:
                st.error(str(e))
        spacer(32)


# ─── ROUTER ──────────────────────────────────────────────────────────────────
ROUTES = {
    "🏠  Home":      page_home,
    "📊  Dashboard": page_home,
    "👥  Customers": lambda: page_analytics("customers", "👥",
        "Customer Analytics — RFM & CLV",
        "Segmentation, lifetime value and churn prediction."),
    "🛒  Orders":    lambda: page_analytics("orders", "🛒",
        "Order Analytics — Revenue & Trends",
        "Monthly revenue, AOV and order volume patterns."),
    "📦  Products":  lambda: page_analytics("products", "📦",
        "Product Analytics — Best Sellers",
        "Category performance, return rates and cross-sell."),
    "📍  Regional":  lambda: page_analytics("regional", "📍",
        "Regional Analytics",
        "Revenue distribution and store KPIs across Vietnam."),
    "📈  Reports":   lambda: page_analytics("reports", "📈",
        "Summary Reports",
        "Executive KPI summaries and automated periodic reporting."),
    "⚙️  Settings":  page_settings,
}

ROUTES.get(page, page_home)()