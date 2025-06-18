
import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title and configuration
st.set_page_config(page_title="CSV Dashboard", layout="wide")

# Add title and description
st.title("Interactive CSV Data Dashboard")
st.markdown("Upload your CSV file to generate interactive visualizations.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# If a file is uploaded, read it and display the dashboard
if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display basic information
    st.subheader("Data Overview")
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Number of rows:** {df.shape[0]}")
        st.write(f"**Number of columns:** {df.shape[1]}")

    with col2:
        st.write("**Column types:**")
        st.write(df.dtypes)

    # Display data sample
    st.subheader("Data Sample")
    st.dataframe(df.head(10))

    # Select columns for visualization
    st.subheader("Create Visualizations")

    # Get numeric columns
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    # If there are numeric columns, create charts
    if len(numeric_cols) > 0:
        # Create two columns for chart options
        col1, col2 = st.columns(2)

        with col1:
            # Bar chart
            st.subheader("Bar Chart")
            bar_x = st.selectbox("Select X-axis for Bar Chart", df.columns)
            if bar_x in numeric_cols:
                bar_color = st.selectbox("Select Color (Group) for Bar Chart", [None] + df.columns.tolist())

                if bar_color == None:
                    fig_bar = px.bar(df, x=bar_x)
                else:
                    fig_bar = px.bar(df, x=bar_x, color=bar_color)

                st.plotly_chart(fig_bar, use_container_width=True)
            else:
                bar_y = st.selectbox("Select Y-axis for Bar Chart", numeric_cols)
                bar_color = st.selectbox("Select Color (Group) for Bar Chart", [None] + df.columns.tolist())

                if bar_color == None:
                    fig_bar = px.bar(df, x=bar_x, y=bar_y)
                else:
                    fig_bar = px.bar(df, x=bar_x, y=bar_y, color=bar_color)

                st.plotly_chart(fig_bar, use_container_width=True)

        with col2:
            # Scatter plot
            st.subheader("Scatter Plot")
            scatter_x = st.selectbox("Select X-axis for Scatter Plot", numeric_cols)
            scatter_y = st.selectbox("Select Y-axis for Scatter Plot", [col for col in numeric_cols if col != scatter_x])
            scatter_color = st.selectbox("Select Color (Group) for Scatter Plot", [None] + df.columns.tolist())

            if scatter_color == None:
                fig_scatter = px.scatter(df, x=scatter_x, y=scatter_y)
            else:
                fig_scatter = px.scatter(df, x=scatter_x, y=scatter_y, color=scatter_color)

            st.plotly_chart(fig_scatter, use_container_width=True)

        # Line chart
        st.subheader("Line Chart")
        line_x = st.selectbox("Select X-axis for Line Chart", df.columns)
        line_y = st.selectbox("Select Y-axis for Line Chart", numeric_cols)
        line_color = st.selectbox("Select Color (Group) for Line Chart", [None] + df.columns.tolist())

        if line_color == None:
            fig_line = px.line(df, x=line_x, y=line_y)
        else:
            fig_line = px.line(df, x=line_x, y=line_y, color=line_color)

        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.warning("No numeric columns found in the CSV. Cannot create visualizations.")

else:
    # If no file is uploaded, show instructions
    st.info("Please upload a CSV file to get started.")

    # Sample CSV format
    st.subheader("Sample CSV Format")
    sample_df = pd.DataFrame({
        'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05'],
        'Category': ['A', 'B', 'A', 'C', 'B'],
        'Sales': [100, 120, 90, 140, 110],
        'Quantity': [5, 6, 4, 7, 5],
        'Profit': [20, 24, 18, 28, 22]
    })

    st.dataframe(sample_df)

    # Requirements info
    st.subheader("Requirements for This Dashboard")
    st.code('''
    # requirements.txt
    streamlit
    pandas
    plotly
    ''')

# Add footer
st.markdown("---")
st.markdown("Created with Streamlit • Simple CSV Dashboard")
