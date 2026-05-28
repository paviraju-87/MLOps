from huggingface_hub import HfApi
import os

api = HfApi(token="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")
api.upload_folder(
    folder_path="/content/drive/MyDrive/Python/ModelIntepretability/WK2/mlops/deployment",     # the local folder containing your files
    repo_id="PaviRaju/Bank-Customer-Churn",          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
