
import streamlit as st
import pandas as pd

# Sample top priority action data
data = {
    "Focus Area": [
        "OHS Leadership", "OHS Responsibilities", "Workplace Inspections",
        "Forklift Safety", "Forklift Safety", "Forklift Safety",
        "Forklift Safety", "Manual Handling", "Plant Safety",
        "Heights", "Falling Objects", "Welding Safety",
        "Safe Systems of Work", "Safe Systems of Work"
    ],
    "Action": [
        "Include OHS in leadership meetings",
        "Educate managers on OHS obligations",
        "Monthly factory safety checks",
        "Replace ride-on forklifts with walkie stackers",
        "Develop traffic management plan",
        "Install forklift exclusion zones",
        "Train all workers in traffic management plan",
        "Eliminate manual pallet wrapping",
        "Test interlocks and guards regularly",
        "Provide safety harness and ensure proper use",
        "Install mesh on pallet racking near assembly area",
        "Install fire extinguisher in welding area",
        "Develop SOPs for key tasks",
        "Train staff in developed SOPs"
    ],
    "Responsible": ["Lee-Anne Stevenson"] * 14,
    "Priority": ["High"] * 14,
    "Target Completion": [
        "Apr 2025", "Apr 2025", "May 2025", "May 2025", "May 2025",
        "May 2025", "May 2025", "May 2025", "Jun 2025", "Apr 2025",
        "Apr 2025", "Apr 2025", "Jun 2025", "Jun 2025"
    ],
    "Status": ["Not Started"] * 14,
    "Notes": ["" for _ in range(14)]
}

# Convert to DataFrame
df = pd.DataFrame(data)

st.title("OHS Action Plan 2025 Dashboard")
st.write("This dashboard shows top priority safety actions and progress tracking.")

# Editable table
st.data_editor(df, num_rows="dynamic", use_container_width=True)

# Filtering by focus area
focus_area = st.selectbox("Filter by Focus Area", ["All"] + sorted(df["Focus Area"].unique()))
if focus_area != "All":
    filtered = df[df["Focus Area"] == focus_area]
    st.write(f"### Actions under: {focus_area}")
    st.dataframe(filtered)
