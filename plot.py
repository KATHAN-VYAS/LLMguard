import matplotlib.pyplot as plt
import numpy as np

# Data extracted from Image 1 (Random Forest)
random_forest_data = {
    'name': 'Random Forest',
    'precision_0': 0.93,
    'recall_0': 0.98,
    'f1_0': 0.95,
    'support_0': 3924,
    'precision_1': 0.98,
    'recall_1': 0.92,
    'f1_1': 0.95,
    'support_1': 3923,
    'accuracy': 0.95,
    'macro_precision': 0.95,
    'macro_recall': 0.95,
    'macro_f1': 0.95,
    'weighted_precision': 0.95,
    'weighted_recall': 0.95,
    'weighted_f1': 0.95,
    'total_support': 7847
}

# Data extracted from Image 2 (XGBoost)
xgboost_data = {
    'name': 'XGBoost',
    'precision_0': 0.92,
    'recall_0': 0.98,
    'f1_0': 0.95,
    'support_0': 3924,
    'precision_1': 0.98,
    'recall_1': 0.92,
    'f1_1': 0.95,
    'support_1': 3923,
    'accuracy': 0.95,
    'macro_precision': 0.95,
    'macro_recall': 0.95,
    'macro_f1': 0.95,
    'weighted_precision': 0.95,
    'weighted_recall': 0.95,
    'weighted_f1': 0.95,
    'total_support': 7847
}

# List of classifiers for easier iteration
classifiers = [random_forest_data, xgboost_data]

# Metrics to compare
metrics = {
    'Accuracy': 'accuracy',
    'Precision (Class 0)': 'precision_0',
    'Recall (Class 0)': 'recall_0',
    'F1-Score (Class 0)': 'f1_0',
    'Precision (Class 1)': 'precision_1',
    'Recall (Class 1)': 'recall_1',
    'F1-Score (Class 1)': 'f1_1',
    'Macro Avg Precision': 'macro_precision',
    'Macro Avg Recall': 'macro_recall',
    'Macro Avg F1-Score': 'macro_f1',
    'Weighted Avg Precision': 'weighted_precision',
    'Weighted Avg Recall': 'weighted_recall',
    'Weighted Avg F1-Score': 'weighted_f1',
}

# Create a figure to hold all subplots
fig, axes = plt.subplots(nrows=len(metrics), ncols=1, figsize=(10, 5 * len(metrics)))
fig.suptitle('Classifier Performance Comparison', fontsize=16, y=1.02) # Add a main title

# Ensure axes is an array even if only one subplot
if len(metrics) == 1:
    axes = [axes]

# Bar width
bar_width = 0.35
index = np.arange(len(classifiers))

for i, (metric_name, metric_key) in enumerate(metrics.items()):
    ax = axes[i]
    
    values = [clf[metric_key] for clf in classifiers]
    
    bars1 = ax.bar(index - bar_width/2, values, bar_width, label='Value', color=['skyblue', 'lightcoral'])
    
    ax.set_ylabel('Score')
    ax.set_title(f'{metric_name} Comparison')
    ax.set_xticks(index)
    ax.set_xticklabels([clf['name'] for clf in classifiers])
    ax.set_ylim(0, 1.05) # Scores are probabilities/ratios, so 0-1 range is appropriate
    ax.legend(['Score'], loc='lower right') # Simplified legend as each bar represents a single score

    # Add text labels on top of the bars
    for bar in bars1:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.01, round(yval, 2), ha='center', va='bottom')

plt.tight_layout(rect=[0, 0.03, 1, 0.98]) # Adjust layout to prevent suptitle overlap
plt.show()

# Alternatively, if you want a single graph with all metrics for each classifier:
print("\n--- Alternative: Single graph for each classifier showing all key metrics ---")

# Key metrics to show on a single graph for each classifier
key_metrics_single_plot = {
    'Accuracy': 'accuracy',
    'F1-Score (Macro Avg)': 'macro_f1',
    'Precision (Macro Avg)': 'macro_precision',
    'Recall (Macro Avg)': 'macro_recall'
}

classifier_names = [clf['name'] for clf in classifiers]
metric_labels = list(key_metrics_single_plot.keys())

# Prepare data for grouped bar chart
rf_values = [random_forest_data[key] for key in key_metrics_single_plot.values()]
xgb_values = [xgboost_data[key] for key in key_metrics_single_plot.values()]

x = np.arange(len(metric_labels)) # the label locations
width = 0.35 # the width of the bars

fig2, ax2 = plt.subplots(figsize=(12, 6))
rects1 = ax2.bar(x - width/2, rf_values, width, label='Random Forest', color='skyblue')
rects2 = ax2.bar(x + width/2, xgb_values, width, label='XGBoost', color='lightcoral')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax2.set_ylabel('Scores')
ax2.set_title('Classifier Performance Comparison (Key Metrics)')
ax2.set_xticks(x)
ax2.set_xticklabels(metric_labels, rotation=45, ha="right")
ax2.set_ylim(0.9, 1.0) # Zoom in to see the small differences
ax2.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax2.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig2.tight_layout()
plt.show()