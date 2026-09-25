import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data_set 2 - Copy.csv")

print("Columns in Dataset:")
print(df.columns.tolist())

print("\nInvestment Information Sources:")
print(df["Source"])

source_counts = df["Source"].value_counts()


print("\n============================================")
print("COMMON INVESTMENT INFORMATION SOURCES")
print("============================================")

print(source_counts)

total_participants = source_counts.sum()

source_percentage = (
    source_counts / total_participants
) * 100


summary = pd.DataFrame({
    "Information Source": source_counts.index,
    "Number of Participants": source_counts.values,
    "Percentage": source_percentage.values.round(2)
})


print("\nSummary of Information Sources:")
print(summary.to_string(index=False))


most_common_source = source_counts.idxmax()

highest_frequency = source_counts.max()


print("\nMost Common Information Source:")
print(most_common_source)

print("\nNumber of Participants:")
print(highest_frequency)


print("\nRanking of Information Sources:")

for index, row in summary.iterrows():

    print(
        f"{index + 1}. "
        f"{row['Information Source']} - "
        f"{row['Number of Participants']} participants "
        f"({row['Percentage']}%)"
    )

plt.figure(figsize=(10, 6))

source_counts.plot(kind="bar")

plt.title("Common Sources of Investment Information")
plt.xlabel("Information Source")
plt.ylabel("Number of Participants")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()