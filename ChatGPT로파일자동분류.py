import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\student\Downloads'

# 이동할 폴더 경로
images_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
docs_folder = os.path.join(download_folder, 'docs')
archive_folder = os.path.join(download_folder, 'archive')

# 파일 확장자별로 이동할 폴더 설정
file_mappings = {
    ('.jpg', '.jpeg'): images_folder,
    ('.csv', '.xlsx'): data_folder,
    ('.txt', '.doc', '.pdf'): docs_folder,
    ('.zip',): archive_folder,
}

# 각 폴더가 존재하지 않으면 생성
for folder in [images_folder, data_folder, docs_folder, archive_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# 다운로드 폴더 내 파일들을 스캔하고 확장자별로 분류하여 이동
for filename in os.listdir(download_folder):
    file_path = os.path.join(download_folder, filename)
    
    # 파일인지 확인
    if os.path.isfile(file_path):
        # 파일 확장자를 확인하여 이동
        for extensions, destination_folder in file_mappings.items():
            if filename.lower().endswith(extensions):
                destination_path = os.path.join(destination_folder, filename)
                print(f"Moving {filename} to {destination_folder}")
                shutil.move(file_path, destination_path)
                break
