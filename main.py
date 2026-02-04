# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
filepath_pairs = {
    1: ("/var/log/system/auth.log",
        "/var/log/system/аuth.log"),  # HOMOGRAPH (Cyrillic 'а' instead of Latin 'a')

    2: ("/usr/local/bin/cleanup.sh",
        "/usr/local/bin/cleаnup.sh"),  # HOMOGRAPH (Cyrillic 'а')

    3: ("/home/user/docs/summary.pdf",
        "/home/user/docs/summаry.pdf"),  # HOMOGRAPH (Cyrillic 'а')

    4: ("/tmp/cache/session01.dat",
        "/tmp/cache/sessiоn01.dat"),  # HOMOGRAPH (Cyrillic 'о' instead of Latin 'o')

    5: ("/opt/app/config/settings.json",
        "/opt/app/config/settіngs.json"),  # HOMOGRAPH (Cyrillic 'і' instead of Latin 'i')

    6: ("/srv/www/public/index.html",
        "/srv/www/public/indеx.html"),  # HOMOGRAPH (Cyrillic 'е' instead of Latin 'e')

    # ---- Non-homograph pairs (actually different) ----
    7: ("/home/admin/scripts/deploy.sh",
        "/home/admin/scripts/backup.sh"),  # NOT homograph (different filenames)

    8: ("/data/archive/backup_2025.zip",
        "/data/archive/backup_2024.zip"),  # NOT homograph (different year)

    9: ("/mnt/storage/media/video.mp4",
        "/mnt/storage/media/audio.mp3"),  # NOT homograph (different file types)

    10: ("/etc/nginx/nginx.conf",
         "/etc/apache2/httpd.conf"),  # NOT homograph (different services)
}

def get_filepath_pair():
    pass


def determine_homograph():
    pass


def main():
    # Use a breakpoint in the code line below to debug your script.
    pass




      # Press ⌘F8 to toggle the breakpoint.






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
