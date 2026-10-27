import os
from datetime import date

import pandas as pd
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

PROFILE = {
    "name": "Benedict Reynz Matedios",
    "section": "F1",
    "program": "BS Computer Science",
    "year": "3",
    "tagline": "Just a random paserby in your life.",
    "email": "benedictreynz.matedios@cit.edu",
    "github": "https://github.com/Evandle",
    "photo": "assets/pfp.png",
}

BIO = "I am a third-year BS Computer Science student at Cebu Institute of Technology University. I have a strong interest in programming and artificial intelligence, and I am always eager to learn new technologies and improve my skills. In my free time, I enjoy exploring new programming languages, working on personal projects, and reading about the latest developments in the field."

STORY = {
    "Background": "I grew up in a small town and developed an early interest in technology thanks to peso net. I was fascinated by SchizoDev and he inspired me to study and try to make my own Ai models.",
    "Education": "I am currently pursuing a degree in Computer Science at Cebu Institute of Technology University, where I have been able to deepen my knowledge and skills in programming, algorithms, and data structures. I graduated from highschool at Cordova Chatolic Cooperative School in 2021 and I am currently in my third year of college.",
    "Interests": "I am particularly interested in cosplaying, drawing, reading, and exploring new technologies. I enjoy participating in gamejams and watching tech videos, as they provide an opportunity to apply my skills in a practical setting and learn from others in the field.",
}

MILESTONES = [
    (2018, "I dieted and went to the gym, from 87kg I went down to 59kg"),
    (2021, "My fanart was noticed by my favorite V Tuber FallenShadow(Shondo)"),
    (2025, "I started my journey as a cosplayer"),
    (2026, "Developed a horror game with my friends for a horror gamejam"),
]

SKILLS = { 
    "Python": 70,
    "Data analysis": 60,
    "Communication": 90,
    "SQL": 50,
    "Teamwork": 85,
}

HOURS_PER_YEAR = pd.DataFrame(  
    {"Python": [0, 40, 20], "Data analysis": [0, 30, 40], "SQL": [0, 20, 40]},
    index=[2024, 2025, 2026],
)

PROJECTS = [
    {
        "title": "Escape Colon",
        "role": "Designer and Developer",
        "tools": ["Godot", "Blender", "ibisPaint X"],
        "outcome": "We made the game, it was alright, but we learned a lot from it.",
        "link": "", 
    },
    {
        "title": "Aphaty",
        "role": "Developer and Creator",
        "tools": ["C"],
        "outcome": "It was a terminal game I made for fun",
        "link": "",
    },
    {
        "title": "Van Rental Management System",
        "role": "Developer",
        "tools": ["SQL", "C#", "Blazor", "TailwindCSS", "Superbase"],
        "outcome": "Make the entire working website for the Van Rental Management System, it was a fun project to work on.",
        "link": "",
    },
]

FUN_FACTS = ["I cosplay", "Im a Femboy", "I dated a menhera Jirai Kei girl once, didn't end well"]
# Code na itself

st.set_page_config(page_title=f"{PROFILE['name']} | Portfolio", page_icon=">w<", layout="wide")

st.markdown(
    """
    <style>
    [data-testid="stMetric"] {border: 1px solid #C9D6D6; border-radius: 10px; padding: 12px 16px;}
    h1 {letter-spacing: -0.5px;}
    </style>
    """,
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "fact_index" not in st.session_state:
    st.session_state.fact_index = 0


@st.cache_resource
def stand_in_photo():
    img = Image.new("RGB", (400, 400), "#2F5D62")
    try:
        font = ImageFont.load_default(size=36)
    except TypeError:
        font = ImageFont.load_default()
    ImageDraw.Draw(img).text((200, 200), "Photo here", fill="white", anchor="mm", font=font)
    return img


def load_photo():
    if os.path.exists(PROFILE["photo"]):
        return Image.open(PROFILE["photo"])
    return stand_in_photo()


def summary_text():
    lines = [f"{PROFILE['name']} ({PROFILE['section']})", PROFILE["tagline"], "", BIO, "", "Projects:"]
    for p in PROJECTS:
        lines.append(f"- {p['title']} | {p['role']} | {', '.join(p['tools'])} | {p['outcome']}")
    return "\n".join(lines)


all_tools = sorted({t for p in PROJECTS for t in p["tools"]})

# sidebar
with st.sidebar:
    st.image(load_photo(), use_container_width=True)
    st.header(PROFILE["name"])
    st.caption(f"{PROFILE['program']} · {PROFILE['year']}")
    st.caption(f"Section: {PROFILE['section']}")
    st.divider()
    st.subheader("Browse options")
    tool_filter = st.multiselect("Filter projects by tool", all_tools)
    sort_by = st.selectbox("Sort projects by", ["Original order", "Title (A-Z)", "Most tools"])
    show_facts = st.checkbox("Show fun facts", value=True)
    st.divider()
    st.download_button("Download my summary", summary_text(), file_name="summary.txt")
    st.link_button("My GitHub", PROFILE["github"])

# header
st.title(PROFILE["name"])
st.markdown(f"**{PROFILE['tagline']}**")
st.caption(f"{PROFILE['program']} · {PROFILE['year']} · Section {PROFILE['section']}")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Projects", len(PROJECTS))
m2.metric("Tools used", len(all_tools))
m3.metric("Skills tracked", len(SKILLS))
m4.metric("Top skill", max(SKILLS, key=SKILLS.get), f"{max(SKILLS.values())}/100")

tab_about, tab_story, tab_skills, tab_projects, tab_contact = st.tabs(
    ["About", "Autobiography", "Skills", "Projects", "Contact"]
)

# about
with tab_about:
    left, right = st.columns([1, 2], gap="large")
    with left:
        st.image(load_photo(), caption=PROFILE["name"], use_container_width=True)
    with right:
        st.header("About me")
        st.write(BIO)
        if show_facts:
            with st.container(border=True):
                st.subheader("Fun fact")
                st.write(FUN_FACTS[st.session_state.fact_index % len(FUN_FACTS)])
                if st.button("Show another"):
                    st.session_state.fact_index += 1
                    st.rerun()

# autobiography
with tab_story:
    st.header("My story")
    cols = st.columns(len(STORY), gap="medium")
    for col, (heading, text) in zip(cols, STORY.items()):
        with col:
            st.subheader(heading)
            st.write(text)

    st.divider()
    st.subheader("Milestones")
    first, last = MILESTONES[0][0], MILESTONES[-1][0]
    years = st.select_slider("Show milestones between", options=list(range(first, last + 1)), value=(first, last))
    shown = [(y, t) for y, t in MILESTONES if years[0] <= y <= years[1]]
    st.table(pd.DataFrame(shown, columns=["Year", "Milestone"]).set_index("Year"))
    with st.expander("Read the full timeline"):
        for y, t in MILESTONES:
            st.markdown(f"**{y}**: {t}")

# skills
with tab_skills:
    st.header("Skills")
    st.write("My ego has long since been rubbed thought the ground, so I think I'm just decent.")
    min_level = st.slider("Show skills rated at least", 0, 100, 0, step=5)
    view = st.radio("View as", ["Chart", "Table"], horizontal=True)
    skills_df = pd.DataFrame({"Skill": list(SKILLS), "Level": list(SKILLS.values())})
    skills_df = skills_df[skills_df["Level"] >= min_level].set_index("Skill")

    c1, c2 = st.columns(2, gap="large")
    with c1:
        if skills_df.empty:
            st.info("No skills at that level. Lower the slider.")
        elif view == "Chart":
            st.bar_chart(skills_df)
        else:
            st.dataframe(
                skills_df,
                column_config={"Level": st.column_config.ProgressColumn("Level", min_value=0, max_value=100, format="%d")},
                use_container_width=True,
            )
    with c2:
        st.subheader("Practice hours per year")
        st.line_chart(HOURS_PER_YEAR)

# projects
with tab_projects:
    st.header("Projects")
    items = [p for p in PROJECTS if not tool_filter or set(tool_filter) & set(p["tools"])]
    if sort_by == "Title (A-Z)":
        items = sorted(items, key=lambda p: p["title"])
    elif sort_by == "Most tools":
        items = sorted(items, key=lambda p: len(p["tools"]), reverse=True)

    if not items:
        st.warning("No projects use those tools. Clear the filter in the sidebar.")
    for p in items:
        with st.container(border=True):
            a, b = st.columns([3, 1])
            with a:
                st.subheader(p["title"])
                st.markdown(f"**Role:** {p['role']}")
                st.markdown("**Tools:** " + ", ".join(f"`{t}`" for t in p["tools"]))
                st.write(p["outcome"])
            with b:
                if p["link"]:
                    st.link_button("View project", p["link"])
                else:
                    st.caption("No link yet")

# contact
with tab_contact:
    st.header("Contact and feedback")
    form_col, info_col = st.columns([2, 1], gap="large")
    with form_col:
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your name")
            email = st.text_input("Your email")
            topic = st.selectbox("Topic", ["Feedback on this site", "Project question", "Say hello"])
            rating = st.slider("How would you rate this site?", 1, 5, 4)
            reply = st.radio("Preferred reply", ["Email", "No reply needed"], horizontal=True)
            message = st.text_area("Message", height=120)
            agree = st.checkbox("I'm okay with my message being saved for this session")
            sent = st.form_submit_button("Send message")

        if sent:
            if not name.strip() or "@" not in email or not message.strip():
                st.error("Add your name, a valid email, and a message, then send again.")
            elif not agree:
                st.error("Tick the checkbox so the message can be saved.")
            else:
                st.session_state.messages.append(
                    {"From": name, "Topic": topic, "Rating": rating, "Reply": reply, "Message": message}
                )
                st.success(f"Thanks, {name}! Your message was sent.")
                st.balloons()

    with info_col:
        st.metric("Messages sent this session", len(st.session_state.messages))
        st.write(f"Email: {PROFILE['email']}")
        if st.session_state.messages:
            avg = sum(m["Rating"] for m in st.session_state.messages) / len(st.session_state.messages)
            st.metric("Average rating", f"{avg:.1f} / 5")
            if st.button("Clear sent messages"):
                st.session_state.messages = []
                st.rerun()

    if st.session_state.messages:
        with st.expander("See messages sent this session"):
            st.dataframe(pd.DataFrame(st.session_state.messages), use_container_width=True)

st.divider()
st.caption(f"{PROFILE['name']} · {PROFILE['section']} · {date.today().year}")
