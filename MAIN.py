from getFileFromWeb import download_csv_files

if __name__ == "__main__":
  base_url = "http://10.192.12.62/"
  folder_path = "nbulkload/"
  prefix = "dump_tpt_cellsector_"
  save_path = "import/nbulkload"  # Change this to your desired save path
  download_csv_files(base_url, folder_path, prefix, save_path)

  





