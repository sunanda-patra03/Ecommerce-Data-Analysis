import matplotlib
matplotlib.use('Agg')  # disables popup windows
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======================
# 1. LOAD DATA
# ======================
df = pd.read_csv("data/ecommerce.csv")

print("Columns in dataset:\n", df.columns)
print(df.head())

# ======================
# 2. DATA CLEANING
# ======================
df.drop_duplicates(inplace=True)

# Fill missing values safely
df.fillna(0, inplace=True)

print("Data Shape after cleaning:", df.shape)

# Convert numeric columns safely
numeric_cols = [
    'Membership_Years','Login_Frequency','Session_Duration_Avg',
    'Pages_Per_Session','Cart_Abandonment_Rate','Wishlist_Items',
    'Total_Purchases','Average_Order_Value','Days_Since_Last_Purchase',
    'Discount_Usage_Rate','Returns_Rate','Email_Open_Rate',
    'Customer_Service_Calls','Product_Reviews_Written',
    'Social_Media_Engagement_Score','Mobile_App_Usage',
    'Payment_Method_Diversity','Lifetime_Value','Credit_Balance','Churned'
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# ======================
# 3. BUSINESS METRICS
# ======================
print("\nAverage Order Value:", df['Average_Order_Value'].mean())
print("Estimated Revenue:", (df['Total_Purchases'] * df['Average_Order_Value']).sum())
print("Churn Rate:", df['Churned'].mean()*100, "%")

# ======================
# 4. CUSTOMER BEHAVIOR ANALYSIS
# ======================
plt.figure(figsize=(6,4))
sns.histplot(df['Membership_Years'], bins=10)
plt.title("Membership Duration Distribution")
plt.savefig("membership_distribution.png")
plt.close()

plt.figure(figsize=(6,4))
sns.boxplot(x=df['Churned'], y=df['Login_Frequency'])
plt.title("Login Frequency vs Churn")
plt.savefig("login_vs_churn.png")
plt.close()



# ======================
# 5. HIGH VALUE CUSTOMERS
# ======================
high_value = df[df['Lifetime_Value'] > df['Lifetime_Value'].median()]
print("Number of High Value Customers:", len(high_value))

# ======================
# 6. ENGAGEMENT VS PURCHASES
# ======================
plt.figure(figsize=(6,4))
sns.scatterplot(x=df['Login_Frequency'], y=df['Total_Purchases'])
plt.title("Engagement vs Purchases")
plt.savefig("engagement_vs_purchases.png")
plt.close()


# ======================
# 7. EXPORT FOR DASHBOARD
# ======================
df.to_csv("cleaned_customer_data.csv", index=False)
print("CSV saved")
print("\nAnalysis Completed Successfully!")
