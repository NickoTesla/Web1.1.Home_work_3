import os
from multiprocessing.pool import ThreadPool


def sort_files_by_extension(directory):
    file_extensions = {}
    for root, _, files in os.walk(directory):
        for file in files:
            _, extension = os.path.splitext(file)
            if extension:
                # Видаляємо крапку з початку розширення
                extension = extension[1:]
                file_path = os.path.join(root, file)
                if extension not in file_extensions:
                    file_extensions[extension] = []
                file_extensions[extension].append(file_path)
    return file_extensions


def move_file(file_path, destination):
    file_name = os.path.basename(file_path)
    destination_path = os.path.join(destination, file_name)
    os.rename(file_path, destination_path)


def process_files(extension, file_paths, destination):
    for file_path in file_paths:
        move_file(file_path, destination)
        print(f"Moved file '{file_path}' to '{destination}'")


def process_directory(directory, destination):
    file_extensions = sort_files_by_extension(directory)
    pool = ThreadPool()
    for extension, file_paths in file_extensions.items():
        pool.apply_async(process_files, (extension, file_paths, destination))
    pool.close()
    pool.join()


if name == 'main':
    directory = 'Мотлох'  # Задана папка
    destination = 'Сортовані файли'  # Папка для переміщення файлів

    if not os.path.exists(destination):
        os.makedirs(destination)

    process_directory(directory, destination)
