class ElectricityFraudDetection:
    def __init__(self, repository_name):
        self.repository_name = repository_name
        self.models = []

    def add_model(self, model_name):
        self.models.append(model_name)

    def show_repository_contents(self):
        print(f"Repository: {self.repository_name}\n")
        print("ML Models for Electricity Fraud Detection:")
        for model in self.models:
            print(f"- {model}")

# Instantiate an ElectricityFraudDetection object
repo = ElectricityFraudDetection("Electricity-Fraud-Detection")

# Add ML models to the repository
repo.add_model("Random Forest Classifier")
repo.add_model("Logistic Regression")
repo.add_model("Gradient Boosting Classifier")
repo.add_model("Support Vector Machine")

# Show repository contents
repo.show_repository_contents()
