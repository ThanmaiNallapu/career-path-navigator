from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load dataset
df = pd.read_excel("careers_dataset.xlsx")

@app.route("/", methods=["GET", "POST"])
def home():
    results = None
    degrees = ["B.Tech","B.E","B.Sc","B.Com","BBA","BA","MBBS","BCA","Diploma","Any Degree"]

    if request.method == "POST":
        degree = request.form.get("degree")
        region = request.form.get("region")
        company = request.form.get("company")
        user_skills = request.form.get("skills")
        career_type = request.form.get("career_type")


        # Step 1: Basic filtering
        filtered_df = df[
            (df["Degree"].str.contains(degree, case=False, na=False)) &
            (df["Region"].str.contains(region, case=False, na=False))
        ]

        if career_type == "Higher Studies":
            filtered_df = filtered_df[filtered_df["Category"] == "Higher Studies"]
        else:
            filtered_df = filtered_df[filtered_df["Category"] != "Higher Studies"]


        if company and company.strip() != "":
            temp_df = filtered_df[
            filtered_df["Companies"].str.lower().str.contains(company.strip().lower(), na=False)
        ]

            if not temp_df.empty:
                filtered_df = temp_df



        if not filtered_df.empty and user_skills:
            # Step 2: ML Matching
            vectorizer = TfidfVectorizer()

            skill_vectors = vectorizer.fit_transform(filtered_df["Required_Skills"])
            user_vector = vectorizer.transform([user_skills])

            similarity_scores = cosine_similarity(user_vector, skill_vectors)

            filtered_df["Similarity"] = similarity_scores[0]

            filtered_df = filtered_df.sort_values(by="Similarity", ascending=False)

            results = filtered_df.head(5).to_dict(orient="records")

            degrees = sorted(df["Degree"].dropna().unique())


    return render_template("index.html", results=results, degrees=degrees)


if __name__ == "__main__":
    app.run(debug=True)
