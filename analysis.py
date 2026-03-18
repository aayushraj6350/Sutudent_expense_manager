import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("expenses.csv")

print("📊 Expense Data:")
print(df)

# Convert Amount to numeric
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

# Category-wise total
print("\n💰 Category-wise Total Expense:")
category_total = df.groupby("Category")["Amount"].sum()
print(category_total)

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Create Month column
df["Month"] = df["Date"].dt.to_period("M")

# Monthly total expense
monthly_total = df.groupby("Month")["Amount"].sum()

print("\n📈 Monthly Expense Trend:")
print(monthly_total)

# Create dashboard
fig, ax = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("AI Smart Expense Manager Dashboard", fontsize=16)

# BAR CHART
category_total.plot(kind="bar", ax=ax[0, 0], title="Category-wise Expenses")
ax[0, 0].set_xlabel("Category")
ax[0, 0].set_ylabel("Amount")

# PIE CHART
category_total.plot(
    kind="pie",
    ax=ax[0, 1],
    autopct="%1.1f%%",
    title="Expense Distribution"
)
ax[0, 1].set_ylabel("")

# LINE CHART
monthly_total.plot(
    kind="line",
    marker="o",
    linewidth=2,
    grid=True,
    ax=ax[1, 0],
    title="Monthly Expense Trend"
)

# Remove empty subplot
fig.delaxes(ax[1, 1])

plt.tight_layout()
plt.show()