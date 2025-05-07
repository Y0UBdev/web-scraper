
def compress_folder(folder_path: str):
    import shutil
    return shutil.make_archive(folder_path, 'zip', folder_path)
    print(f"[📦] Dossier compressé en ZIP : {zip_path}")