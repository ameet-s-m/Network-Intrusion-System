import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Column names
columns = [
'duration','protocol_type','service','flag','src_bytes','dst_bytes','land',
'wrong_fragment','urgent','hot','num_failed_logins','logged_in',
'num_compromised','root_shell','su_attempted','num_root','num_file_creations',
'num_shells','num_access_files','num_outbound_cmds','is_host_login',
'is_guest_login','count','srv_count','serror_rate','srv_serror_rate',
'rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate',
'srv_diff_host_rate','dst_host_count','dst_host_srv_count',
'dst_host_same_srv_rate','dst_host_diff_srv_rate',
'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate',
'dst_host_serror_rate','dst_host_srv_serror_rate',
'dst_host_rerror_rate','dst_host_srv_rerror_rate','label','difficulty'
]

# Load dataset
df = pd.read_csv("../dataset/KDDTrain+.txt", names=columns)

print("✅ Dataset Loaded")

# Drop difficulty column
df.drop(['difficulty'], axis=1, inplace=True)

# Convert labels to binary
df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)

print("\n✅ Label Distribution:")
print(df['label'].value_counts())

# Encode categorical columns
categorical_cols = ['protocol_type', 'service', 'flag']

le = LabelEncoder()

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

print("\n✅ Encoding Done")

# Split features and target
X = df.drop('label', axis=1)
y = df['label']

print("\n✅ Features shape:", X.shape)
print("✅ Target shape:", y.shape)

# Save processed data (optional for debugging)
X.to_csv("X_processed.csv", index=False)
y.to_csv("y_processed.csv", index=False)

print("\n🔥 Preprocessing Completed Successfully")