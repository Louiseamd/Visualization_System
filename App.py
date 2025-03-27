import streamlit as st
import json
import matplotlib.pyplot as plt
import numpy as np

st.title("Visualization of Indicators by Category and Cluster")

# Load JSON file
uploaded_file = st.file_uploader("Choose a JSON file", type="json")
json_data = {}

if uploaded_file:
    try:
        json_content = json.load(uploaded_file)
        if isinstance(json_content, dict):
            metadata = json_content.get("metadata", {})
            results = json_content.get("results", {})
            if results:
                for cluster_id, cluster_results in results.items():
                    json_data[cluster_id] = cluster_results
    except json.JSONDecodeError:
        st.error("File reading error. Please ensure it is properly formatted.")

# Define categories and chart types
indicators_by_category = {
    "Accuracy": {
        "graphique": ["Precision-k", "Recall-k", "NDCG", "Hit Rate"],
        "chiffres": ["MAE", "RMSE"],
        "type": "bar"
    },
    "Coverage": {
        "graphique": ["Simple Coverage", "Catalog Coverage", "Gini Index", "Long Tail Coverage", "Entropy"],
        "chiffres": [],
        "type": "bar"
    },
    "Personalization and Diversity": {
        "graphique": ["Diversity", "Serendipity", "Personalization"],
        "chiffres": ["User Similarity", "Personalization Precision"],
        "type": "line"
    },
    "Novelty and Discovery": {
        "graphique": ["Novelty", "Serendipity"],
        "chiffres": [],
        "type": "pie"
    },
    "Robustness": {
        "graphique": ["Robustness"],
        "chiffres": ["Stability"],
        "type": "bar"
    }
}

# Function to display graphs
def plot_graph(data, selected_measures, category, col):
    if not data or not selected_measures:
        return

    clusters = list(data.keys())
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

    if category == "Personalization and Diversity":
        fig, ax = plt.subplots(figsize=(8, 5))
        for i, measure in enumerate(selected_measures):
            values = [data[cluster].get(measure, 0) for cluster in clusters]
            ax.plot(clusters, values, marker="o", linestyle="-", label=measure, color=colors[i % len(colors)])
        ax.set_title(f"{category} - Selected Measures")
        ax.set_ylabel("Value")
        ax.legend()
        ax.grid(True, linestyle="--", alpha=0.6)
        col.pyplot(fig)
    else:
        for measure in selected_measures:
            fig, ax = plt.subplots(figsize=(8, 5))
            values = [data[cluster].get(measure, 0) for cluster in clusters]

            if indicators_by_category[category]["type"] == "bar":
                x = np.arange(len(clusters))
                ax.bar(x, values, label=measure, color=colors[:len(clusters)])
                ax.set_xticks(x)
                ax.set_xticklabels(clusters)
            elif indicators_by_category[category]["type"] == "line":
                ax.plot(clusters, values, marker="o", linestyle="-", label=measure, color=colors[0])
            elif indicators_by_category[category]["type"] == "pie":
                ax.pie(values, labels=clusters, autopct="%1.1f%%", colors=colors[:len(clusters)])

            ax.set_title(f"{category} - {measure}")
            ax.set_ylabel("Value")
            ax.legend()
            ax.grid(True, linestyle="--", alpha=0.6)
            col.pyplot(fig)

# User interface
if json_data:
    selected_categories = st.multiselect("Choose one or more categories:", list(indicators_by_category.keys()))

    if selected_categories:
        for category in selected_categories:
            st.subheader(f"{category}")
            available_graph_indicators = indicators_by_category[category]["graphique"]
            available_number_indicators = indicators_by_category[category].get("chiffres", [])

            selected_graph_indicators = st.multiselect(
                f"Indicators to display as charts ({category}):", available_graph_indicators)

            selected_number_indicators = st.multiselect(
                f"Indicators to display as numbers ({category}):", available_number_indicators)

            relevant_data_graph = {}
            relevant_data_numbers = {}

            for cluster, values in json_data.items():
                cluster_graph_data = {}
                cluster_number_data = {}

                for category_key, metrics in values.items():
                    if category in indicators_by_category:
                        for indicator in selected_graph_indicators:
                            if indicator in metrics:
                                cluster_graph_data[indicator] = metrics[indicator]
                        for indicator in selected_number_indicators:
                            if indicator in metrics:
                                cluster_number_data[indicator] = metrics[indicator]

                if cluster_graph_data:
                    relevant_data_graph[cluster] = cluster_graph_data
                if cluster_number_data:
                    relevant_data_numbers[cluster] = cluster_number_data

            col1, col2 = st.columns(2)

            if selected_graph_indicators:
                plot_graph(relevant_data_graph, selected_graph_indicators, category, col1)

            if selected_number_indicators:
                with col2:
                    st.subheader(f" Numeric Indicators ({category})")
                    for cluster, values in relevant_data_numbers.items():
                        st.write(f"**Cluster {cluster}**")
                        for indicator, value in values.items():
                            st.write(f"- **{indicator}**: {value}")

else:
    st.info("Please upload a JSON file.")
